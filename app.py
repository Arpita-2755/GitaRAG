import streamlit as st
from core.retriever import GitaRetriever
from core.formatter import ResponseFormatter


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="GitaRAG",
    page_icon="🕉️",
    layout="wide"
)
# ------------------------------
# Sidebar System Info
# ------------------------------
st.sidebar.title("🔬 System Information")

st.sidebar.markdown("""
**Mode:** Extractive RAG  
**Embedding Model:** all-MiniLM-L6-v2  
**Vector Index:** FAISS (Inner Product)  
**Similarity Threshold:** 0.45  
**Hallucination Risk:** Minimal  
""")

st.sidebar.markdown("---")
st.sidebar.success("✅ Fully Extractive Retrieval")
st.sidebar.caption("No generative model used. Responses are grounded strictly in retrieved verses.")



# -------------------------------------------------
# PREMIUM GLOBAL STYLING
# -------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

/* Title Styling */
h1 {
    font-size: 44px;
    text-align: center;
    font-weight: 700;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 30px;
}

/* Input box */
.stTextInput > div > div > input {
    font-size: 18px;
    padding: 14px;
    border-radius: 10px;
}

/* Confidence Box */
.confidence-box {
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 25px;
    font-weight: 600;
}

/* Verse Card */
.verse-card {
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 18px;
    line-height: 1.7;
    transition: 0.3s ease-in-out;
}

.verse-card:hover {
    transform: scale(1.01);
}

.theme-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    opacity: 0.6;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("🕉️ GitaRAG")
st.markdown("<div class='subtitle'>Grounded Thematic Retrieval Engine for the Bhagavad Gita</div>", unsafe_allow_html=True)


# -------------------------------------------------
# DARK MODE TOGGLE
# -------------------------------------------------
dark_mode = st.toggle("🌙 Enable Dark Mode")

if dark_mode:
    bg = "#0f1117"
    card_bg = "#1c2233"
    text_color = "white"
    confidence_bg = "#1f2a44"
else:
    bg = "#f8f5ef"
    card_bg = "white"
    text_color = "black"
    confidence_bg = "#fff3cd"

st.markdown(f"""
<style>
    .main {{
        background-color: {bg};
        color: {text_color};
    }}
    .confidence-box {{
        background-color: {confidence_bg};
    }}
    .verse-card {{
        background-color: {card_bg};
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    }}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# LOAD RETRIEVER
# -------------------------------------------------
@st.cache_resource
def load_retriever():
    return GitaRetriever()

retriever = load_retriever()


# -------------------------------------------------
# QUERY INPUT
# -------------------------------------------------
query = st.text_input("Ask a philosophical question from the Gita:")

if query:

    raw_response = retriever.search(query)

    if raw_response["status"] == "insufficient_context":
        st.warning("Insufficient grounded context found. Try rephrasing your question.")
    else:
        formatted = ResponseFormatter.build_structured_response(raw_response)

        theme = formatted["theme"]
        confidence_score = formatted["confidence_score"]
        confidence_label = formatted["confidence_label"]

        # Confidence color logic
        if confidence_score >= 0.65:
            conf_color = "#28a745"
        elif confidence_score >= 0.55:
            conf_color = "#ff9800"
        else:
            conf_color = "#dc3545"

        st.markdown(f"""
        <div class="confidence-box">
            <div class="theme-badge" style="background-color:{conf_color}; color:white;">
                {theme}
            </div><br>
            Confidence Score: {confidence_score} ({confidence_label})
        </div>
        """, unsafe_allow_html=True)

        st.success("🛡 Grounded Response — Fully Extractive Retrieval (No Hallucinated Content)")


        # Top Verse
        st.markdown("### 📖 Doctrinal Insight")

        top_verse = formatted["verses"][0]

        st.info(f"""
        Based on Chapter {top_verse['chapter']} Verse {top_verse['verse']},

        {top_verse['verse_text']}
        """)

        # Verse Cluster
        st.markdown("### 📜 Thematic Verse Cluster")

        for result in formatted["verses"]:
            st.markdown(f"""
            <div class="verse-card">
                <b>Chapter {result['chapter']} Verse {result['verse']}</b><br><br>
                {result['verse_text']}<br><br>
                <b>Commentary:</b><br>
                {result['commentary']}<br><br>
                <i>Similarity: {result['similarity']}</i>
            </div>
            """, unsafe_allow_html=True)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("<div class='footer'>GitaRAG — Hallucination-Resistant Thematic Retrieval System<br>Built with SentenceTransformers + FAISS + Streamlit</div>", unsafe_allow_html=True)
