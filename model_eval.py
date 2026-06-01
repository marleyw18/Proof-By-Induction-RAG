import pandas as pd
import os
from sklearn.model_selection import train_test_split
from pylatexenc.latex2text import LatexNodes2Text

"""Model evaluation"""
# data to be split
folder = 'Clean Data'

for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        # Open the file and load JSON
        with open(filepath, 'r') as file:
        # convert to pd df for train_test_split
            df = pd.read_json(file)

        # Convert any latex text to plain text
        def clean_latex(text):
            return LatexNodes2Text().latex_to_text(text)

        df['Proof'] = df['Proof'].apply(clean_latex)

        # preview data and ensure all rows were loaded
        print(f'{filename} successfully loaded.... Preview: {df.head(1), len(df)}')

        train, test = train_test_split(df, train_size=.8, random_state=42)

        os.makedirs("RAG Data", exist_ok=True)
        os.makedirs("Evaluation Data", exist_ok=True)

        # Separate data for validation and RAG
        # save for RAG
        rag_path = os.path.join('RAG Data', 'RAG Ready ' + filename)
        train.to_json(rag_path, orient='records', indent=2)

        # save questions, we will be using to compute metrics
        val_path = os.path.join('Evaluation Data', 'Evaluation ' + filename)
        test.to_json(val_path, orient='records', indent=2)

        print(f"Saved {len(train)} training records to {rag_path}")
        print(f"Saved {len(test)} validation records to {val_path}")

