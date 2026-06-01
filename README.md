# Proof-By-Induction-RAG

Dataset found here: https://link.springer.com/article/10.1007/s40593-025-00498-2

A specialized AI chatbot web application focused on teaching and assisting with **Proof by Induction**. Built with Llama 3, Flask, and React.

> 🎓 *A self-learning project to explore LLMs, Retrieval-Augmented Generation (RAG), and software engineering fundamentals.*

---

## 🚀 Features

- **LLM-Powered Chatbot** — Uses Llama 3 for natural language interaction
- **Proof by Induction Focus** — Designed to help understand and construct inductive proofs
- *(Future)* **Modular Architecture** — Flask backend + React frontend
- *(Future)* **RAG Pipeline** — Will retrieve context from textbooks, websites, and Excel files to enhance responses

---

## 🧱 Tech Stack

| Layer       | Technology                         |
|-------------|------------------------------------|
| Frontend    | React, CSS                         |
| Backend     | Flask (Python)                     |
| LLM         | Llama 3 (via Ollama or local setup)|
| Future RAG  | Vector DB (Chroma/FAISS), LangChain|

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js (v18+ recommended)
- npm or yarn
- (Optional) [Ollama](https://ollama.com/) for running Llama 3 locally (Or a different model)

---

### To run locally

```powershell
git clone https://github.com/yourusername/Proof-By-Induction-RAG.git
cd Proof-By-Induction-RAG
# create virtual environment in project root
python -m venv .venv
```
```powershell
# install requirements
pip install -r requirements.txt
```
```powershell
python grader.py
```