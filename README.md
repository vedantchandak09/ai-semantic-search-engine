# 🔍 AI Semantic Search Engine

## 🚀 Overview
This project is a full-stack AI-powered semantic search engine that retrieves results based on meaning rather than keyword matching.

It uses transformer-based embeddings to understand user queries and return the most relevant results.

---

## 🧠 Features
- 🔹 Semantic search using Sentence Transformers (MiniLM)
- 🔹 Cosine similarity-based ranking
- 🔹 FastAPI backend with REST API
- 🔹 Interactive frontend UI
- 🔹 Real-time search results

---

## 🛠 Tech Stack
- Python
- FastAPI
- Sentence Transformers
- Scikit-learn
- HTML, CSS, JavaScript

---

## ⚙️ How It Works
1. Documents are converted into vector embeddings
2. User query is converted into embedding
3. Cosine similarity is computed
4. Top relevant results are returned

---

## 📸 Demo
![Demo](add-your-screenshot-here)
## 📸 Demo

![UI](assets/ui.png)
![Results](assets/results.png)

---

## ▶️ Run Locally

```bash
git clone https://github.com/vedantchandak09/ai-semantic-search-engine.git
cd ai-semantic-search-engine/backend
pip install -r requirements.txt
python3 -m uvicorn app:app --reload
