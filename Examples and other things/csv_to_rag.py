import pandas as pd
import json
import re

df = pd.read_csv('Raw data/Q1_WrittenInduction_v1.csv')

# Remove completely empty or useless answers
df = df[df['Proof'].notna()]
df = df[df['Proof'].str.strip() != '']
df = df[df['Proof'].str.len() > 20]  # Remove very short answers
df = df[~df['Proof'].str.lower().str.contains('idk|no idea|forgot|dont know')]

# Create a clean version without grader notes
df['clean_proof'] = df['Proof'].str.replace(r'\*.*?\*', '', regex=True)
df['clean_proof'] = df['clean_proof'].str.replace(r'\([^)]*grader[^)]*\)', '', regex=True, flags=re.IGNORECASE)


def create_chunk(row):
    # Determine quality label
    if row['Total Score'] >= 12:
        quality = "EXCELLENT"
    elif row['Total Score'] >= 7:
        quality = "GOOD"
    else:
        quality = "POOR"

    # Create a compact representation
    chunk = f"""Quality: {quality} (Score: {row['Total Score']}/14)
Base Case: {row['Identify Base Case']}/2 | Hypothesis: {row['Hypothesis is stated']}/2 | Goal Clear: {row['Goal is Clear']}/2

Student Answer:
{row['clean_proof'][:1500]}  # Truncate if too long
"""
    return chunk


df['chunk'] = df.apply(create_chunk, axis=1)

df['metadata'] = df.apply(lambda row: {
    'total_score': int(row['Total Score']) if pd.notna(row['Total Score']) else 0,
    'quality': 'excellent' if row['Total Score'] >= 12 else 'good' if row['Total Score'] >= 7 else 'poor',
    'has_base': int(row['Identify Base Case'] >= 1),
    'has_hypothesis': int(row['Hypothesis is stated'] >= 1),
    'has_goal': int(row['Goal is Clear'] >= 1),
    'applies_ih': int(row['Inductive Hypothesis is applied'] >= 1),
    'proof_length': len(str(row['Proof'])),
    'score_components': {
        'base': int(row['Identify Base Case']),
        'prove_base': int(row['Prove Base Case']),
        'hypothesis': int(row['Hypothesis is stated']),
        'goal': int(row['Goal is Clear']),
        'decomposes': int(row['Expression of Size k_1 is decomposed into expression of size k']),
        'applies': int(row['Inductive Hypothesis is applied'])
    }
}, axis=1)

import openai
from typing import List

def get_embeddings(texts: List[str], model="text-embedding-3-small"):
    """Use OpenAI's embedding model (cheaper than ada v2)"""
    response = openai.embeddings.create(
        model=model,
        input=texts
    )
    return [item.embedding for item in response.data]

# Generate embeddings for all chunks
embeddings = get_embeddings(df['chunk'].tolist())

import chromadb
from chromadb.utils import embedding_functions

# Create embedding function wrapper
class OpenAIEmbeddingFunction:
    def __call__(self, texts):
        return get_embeddings(texts)

client = chromadb.Client()
collection = client.create_collection(
    name="induction_proofs",
    embedding_function=OpenAIEmbeddingFunction()
)

# Add documents
for idx, row in df.iterrows():
    collection.add(
        documents=[row['chunk']],
        metadatas=[row['metadata']],
        ids=[str(idx)]
    )


def retrieve_relevant_examples(query: str, top_k: int = 3, filter_criteria: dict = None):
    """Retrieve relevant student answers"""

    # Get query embedding
    query_embedding = get_embeddings([query])[0]

    # Search with optional filters
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=filter_criteria  # e.g., {"quality": "excellent"}
    )

    return results['documents'][0], results['metadatas'][0]


def answer_with_rag(query: str):
    """Complete RAG pipeline with GPT-4o mini"""

    # Step 1: Retrieve relevant examples
    examples, metadata = retrieve_relevant_examples(query, top_k=3)

    # Step 2: Build prompt
    prompt = f"""You are an AI teaching assistant for a discrete math course. 
Use the following student answers to help answer the question.

QUESTION: {query}

RETRIEVED EXAMPLES:
{chr(10).join([f"Example {i + 1}: {ex}" for i, ex in enumerate(examples)])}

INSTRUCTIONS:
- If the examples show a pattern, explain it
- If the question asks for a correct example, pick the highest quality one
- If the question asks for common mistakes, focus on low-scoring examples
- Be concise and helpful

ANSWER:"""

    # Step 3: Call GPT-4o mini
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content

