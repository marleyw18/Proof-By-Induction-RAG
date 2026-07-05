# Proof-By-Induction-RAG
> 🎓 A self-learning project exploring LLMs, Retrieval-Augmented Generation (RAG), and software engineering through building a proof-by-induction assistant.
---
**Current Status:** CLI-based evaluation & RAG data preparation pipeline. Web interface planned.


**The induction proof dataset is derived from:** https://link.springer.com/article/10.1007/s40593-025-00498-2
**Note:** This project prioritizes learning over polish. Code may be experimental, and features evolve as concepts are mastered.


## 📋 Overview

This project aims to build a specialized assistant for teaching and evaluating **Proof by Induction**—a fundamental mathematical technique. The system uses:

- **Llama 3** for natural language understanding and generation
- **RAG architecture** to ground responses in verified textbook content
- **Automated evaluation** against structured rubrics

*Primary goal:* Learn how to build, evaluate, and iterate on RAG systems in practice.

## 🎯 Current Features

| Feature | Status         | Description |
|---------|----------------|-------------|
| Data Processing | ✅ Complete     | Cleaned & structured induction proof dataset |
| RAG Data Preparation | ✅ Complete     | Split data for retrieval & evaluation |
| Model Evaluation | 🚧 In Progress | Script to grade LLM responses against rubrics |
| SQL Querying | ✅ Complete     | Structured proof data storage & retrieval |
| Web Interface | 🚧 Planned     | React frontend + Flask backend |
| Real-time RAG | 🚧 Planned     | Vector DB integration with Chroma/FAISS |

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| LLM | Llama 3 (via Ollama) | Response generation & evaluation |
| Backend | Flask (planned) | API serving & orchestration |
| Frontend | React (planned) | User interface |
| RAG Vector DB | Chroma/FAISS (planned) | Document retrieval |
| Data Processing | Python, Pandas | Dataset cleaning & preparation |
| Evaluation | Custom Python scripts | Rubric-based grading |

## 📁 Project Structure
Proof-By-Induction-RAG/
├── grader.py # Main grading script for LLM responses
├── main.py # Core orchestration logic
├── model_eval.py # Model evaluation utilities
├── rubric_prompt # Prompt template for grading rubric
├── system_prompt # Base system prompt for Llama 3
├── requirements.txt # Python dependencies
├── Clean data/ # Processed induction proof examples
├── Questions/ # Test questions for evaluation
├── RAG Data/ # Source documents for retrieval
├── Raw Data/ # Original dataset (Springer article)
└── SQL Queries/ # SQL scripts for structured queries


## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.ai/) installed locally
- Llama 3 model pulled via Ollama:
  ```bash
  ollama pull llama3
  ```
  
### To run locally

1. Clone repo
```powershell
git clone https://github.com/yourusername/Proof-By-Induction-RAG.git
cd Proof-By-Induction-RAG
```

2. Setup Python environment
```powershell
# create virtual environment in project root
python -m venv .venv

# activate virtual environment (Windows)
.venv/Scripts/Activate.ps1

# install requirements
pip install -r requirements.txt
```
```powershell
# run this script to interact with grader
python grader.py

# run this to see a preview of the evaluation and RAG data
python main.py
```

**Next Steps**
Phase 1: Core RAG (Next)

    Implement vector database (Chroma/FAISS)

    Create document chunking pipeline

    Add retrieval step to main.py

    Test retrieval quality with held-out questions

Phase 2: Web Interface

    Build Flask API endpoints

    Create simple React chat interface

    Add real-time RAG querying

Phase 3: Advanced Features

    Support Excel/PDF document ingestion

    Add user feedback collection

    Implement query routing (RAG vs. direct LLM)

