# 🕉️ GitaRAG

Grounded Thematic Retrieval Engine for the Bhagavad Gita

GitaRAG is a hallucination-resistant semantic retrieval system built using:

- SentenceTransformers (all-MiniLM-L6-v2)
- FAISS (Cosine Similarity Search)
- Streamlit (Interactive UI)

## 🚀 Features

- Thematic detection based on dominant chapter clustering
- Confidence scoring based on semantic similarity
- Query expansion for improved grounding
- Dark/Light premium UI mode
- Doctrinal insight extraction
- Structured verse cluster output

## 🧠 Architecture

User Query  
→ Query Expansion  
→ Embedding (MiniLM)  
→ FAISS Search  
→ Similarity Filtering  
→ Thematic Detection  
→ Structured Formatter  
→ UI Rendering

## 📂 Project Structure

app.py
core/
retriever.py
formatter.py
gita_index.faiss
metadata.npy


## 📦 Deployment

Deployed using Streamlit Cloud.

---

Built as a Hallucination-Resistant RAG system.
