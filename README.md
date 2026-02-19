# 🕉️ GitaRAG

### Grounded Thematic Retrieval Engine for the Bhagavad Gita

A fully extractive, hallucination-resistant RAG system built using SentenceTransformers + FAISS + Streamlit.

🌐 **Live App:** https://gitarag.streamlit.app  

---

## 🧠 Problem Statement

Most AI systems hallucinate when answering philosophical or religious questions.

This project solves that by building a **fully extractive Retrieval-Augmented Generation (RAG) system** that:

- Retrieves semantically relevant verses
- Applies similarity threshold filtering
- Computes confidence scoring
- Detects doctrinal themes
- Returns grounded responses ONLY from source text

No generative model is used.

Zero hallucinated content.

---

## 🏗 System Architecture

User Query  
↓  
Query Expansion  
↓  
SentenceTransformer Embedding (all-MiniLM-L6-v2)  
↓  
FAISS Vector Search (Inner Product)  
↓  
Similarity Threshold Filtering (0.45)  
↓  
Confidence Score (Mean Similarity)  
↓  
Theme Detection (Chapter + Text Aware Logic)  
↓  
Structured Extractive Response  

---

## ⚙ Tech Stack

- Python
- SentenceTransformers
- FAISS (Vector Search)
- NumPy
- Streamlit (UI + Deployment)
- Streamlit Cloud (Production Hosting)

Embedding Model:
`all-MiniLM-L6-v2`

Vector Index:
FAISS (Inner Product with L2 normalization)

---

## 🛡 Hallucination Resistance

- Fully Extractive Retrieval
- No LLM generation
- Similarity threshold enforcement
- Mean similarity confidence scoring
- Thematic clustering logic
- Query expansion for semantic robustness

This system guarantees responses are grounded strictly in retrieved verses.

---

## 📊 Evaluation Results

Evaluation conducted on 10 doctrinal queries.

# 🕉️ GitaRAG

### Grounded Thematic Retrieval Engine for the Bhagavad Gita

A fully extractive, hallucination-resistant RAG system built using SentenceTransformers + FAISS + Streamlit.

🌐 **Live App:** https://gitarag.streamlit.app  

---

## 🧠 Problem Statement

Most AI systems hallucinate when answering philosophical or religious questions.

This project solves that by building a **fully extractive Retrieval-Augmented Generation (RAG) system** that:

- Retrieves semantically relevant verses
- Applies similarity threshold filtering
- Computes confidence scoring
- Detects doctrinal themes
- Returns grounded responses ONLY from source text

No generative model is used.

Zero hallucinated content.

---

## 🏗 System Architecture

User Query  
↓  
Query Expansion  
↓  
SentenceTransformer Embedding (all-MiniLM-L6-v2)  
↓  
FAISS Vector Search (Inner Product)  
↓  
Similarity Threshold Filtering (0.45)  
↓  
Confidence Score (Mean Similarity)  
↓  
Theme Detection (Chapter + Text Aware Logic)  
↓  
Structured Extractive Response  

---

## ⚙ Tech Stack

- Python
- SentenceTransformers
- FAISS (Vector Search)
- NumPy
- Streamlit (UI + Deployment)
- Streamlit Cloud (Production Hosting)

Embedding Model:
`all-MiniLM-L6-v2`

Vector Index:
FAISS (Inner Product with L2 normalization)

---

## 🛡 Hallucination Resistance

- Fully Extractive Retrieval
- No LLM generation
- Similarity threshold enforcement
- Mean similarity confidence scoring
- Thematic clustering logic
- Query expansion for semantic robustness

This system guarantees responses are grounded strictly in retrieved verses.

---

## 📊 Evaluation Results

Evaluation conducted on 10 doctrinal queries.

Average Confidence: 0.5237
Max Confidence: 0.5985
Min Confidence: 0.4614


Themes correctly identified:
- Bhakti (Devotion)
- Karma Yoga (Action)
- Self-Realization (Atman)
- Meditation & Discipline
- Renunciation & Liberation

---

## 🌐 Live Demo

Try it here:

👉 https://gitarag.streamlit.app

Example Queries:
- Who is dear to Krishna?
- What is Karma Yoga?
- Is the soul eternal?
- What is meditation?
- What is renunciation?

---

## 🧪 Run Locally

Clone the repository:

git clone https://github.com/your-username/GitaRAG.git

cd GitaRAG


Create virtual environment:

python -m venv venv
venv\Scripts\activate (Windows)


Install dependencies:

pip install -r requirements.txt


Run app:

streamlit run app.py


---

## 📁 Project Structure

GitaRAG/
│
├── core/
│ ├── retriever.py
│ ├── formatter.py
│ ├── embedder.py
│ ├── indexer.py
│
├── data/
│ ├── gita.json
│ ├── commentary.json
│ ├── verses.json
│
├── gita_index.faiss
├── metadata.npy
├── evaluation.py
├── app.py
├── requirements.txt
└── README.md

---

## 📌 Future Improvements

- Hybrid Retrieval (BM25 + Dense)
- Larger embedding model
- Automatic theme classification via ML
- Multi-script support (Sanskrit/Hindi/English)
- Doctrinal comparison engine
- Academic citation export

---

## 👩‍💻 Author

Arpita Mishra  
B.Tech CSE | AI/ML Enthusiast  
Building Hallucination-Resistant AI Systems  

---

### 🚀 Built as a production-grade deployable AI system.
