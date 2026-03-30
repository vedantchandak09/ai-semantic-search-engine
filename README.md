# 🔍 AI Semantic Search Engine

## 🚀 Overview
A full-stack AI-powered search engine that retrieves results based on **semantic meaning** rather than keyword matching.

Built using transformer-based embeddings, this system understands user intent and returns contextually relevant results.

---

## 📸 Demo

### 🔍 User Interface
![UI](assets/ui.png)

### 📊 Search Results
![Results](assets/results.png)

---

## 🧠 Features
- Semantic search using Sentence Transformers (MiniLM)
- Cosine similarity-based ranking
- FastAPI backend with REST API
- Interactive frontend UI
- Real-time results

---

## 🛠 Tech Stack
- Python
- FastAPI
- Sentence Transformers
- Scikit-learn
- HTML, CSS, JavaScript

---

## ⚙️ How It Works
1. Convert documents into vector embeddings
2. Convert query into embedding
3. Compute cosine similarity
4. Return top relevant results

---

## ▶️ Run Locally

```bash
cd backend
pip install -r requirements.txt
python3 -m uvicorn app:app --reload
