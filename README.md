# Proof-By-Induction-RAG

A specialized AI chatbot web application focused on teaching and assisting with **Proof by Induction**. Built with Llama 3, Flask, and React.

> 🎓 *A self-learning project to explore LLMs, Retrieval-Augmented Generation (RAG), and software engineering fundamentals.*

---

## 🚀 Features

- **LLM-Powered Chatbot** — Uses Llama 3 for natural language interaction
- **Proof by Induction Focus** — Designed to help understand and construct inductive proofs
- **Modular Architecture** — Flask backend + React frontend
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

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Proof-By-Induction-RAG.git
cd Proof-By-Induction-RAG
```
### 2. Backend Setup (Flask)
```terminal 
cd aichatbot
python -m venv venv
```
```
# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
```
# Install dependencies
pip install -r requirements.txt
```
```
# Run the Flask server
flask run
# or
python app.py
```

### 3. Frontend Setup (React)
``` bash
cd frontend
npm install
npm start
```