# 🔍 AI Semantic Search Engine

## 🚀 Overview
This project is a full-stack AI-powered semantic search engine that retrieves results based on **meaning** rather than simple keyword matching.

It uses transformer-based embeddings to understand user intent and return contextually relevant results in real time.

---

## 📸 Demo

### 🔍 User Interface
![UI](assets/ui.png)

### 📊 Search Results
![Results](assets/results.png)

---

## 🧠 Features
- 🔹 Semantic search using Sentence Transformers (MiniLM)
- 🔹 Context-aware search results (not keyword-based)
- 🔹 Cosine similarity ranking
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
1. Documents are converted into vector embeddings using a transformer model
2. User query is converted into an embedding
3. Cosine similarity is computed between query and documents
4. Top relevant results are returned

---

## 📁 Project Structure
