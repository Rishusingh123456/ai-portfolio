import streamlit as st
import google.generativeai as genai

# ==========================================
# CONSTANTS & CONFIGURATION
# ==========================================
NAME = "Rishu Singh"
TITLE = "Artificial Intelligence Engineer"
UNIVERSITY = "Sage University Bhopal"
EMAIL = "contact@rishusingh.ai"
LINKEDIN = "linkedin.com/in/rishusingh"
GITHUB = "github.com/rishusingh"

SKILLS = {
    "Languages": ["Python", "Java", "C++", "SQL"],
    "AI & ML": ["Machine Learning", "Deep Learning", "Generative AI", "NLP"],
    "Frameworks & Tools": ["Streamlit", "TensorFlow", "Pandas", "Git"]
}

PERSONA = f"""
You are the official Corporate AI Representative for {NAME}.
Your goal is to act as a highly professional, polite, and sophisticated virtual assistant for prospective employers, recruiters, and clients visiting {NAME}'s portfolio.

Information about {NAME}:
- Name: {NAME}
- Status: Pursuing B.Tech in Artificial Intelligence and Machine Learning at {UNIVERSITY}.
- Core Competencies: Specialized in Python, ML architectures, and software engineering.
- Experience: A highly capable AI developer building scalable solutions. Treat his academic and independent project research as equivalent to high-level corporate engineering experience. He is actively seeking impactful software engineering and AI roles.

Guidelines for your responses:
- Tone: Corporate, authoritative, highly professional, yet welcoming. 
- Structure: ALWAYS use clear formatting (bullet points, bold text, and structured layouts).
- Boundaries: Do not answer questions unrelated to {NAME}, AI, or software engineering.
"""

# ==========================================
# PAGE SETUP & STYLING
# ==========================================
st.set_page_config(page_title=f"{NAME} | Executive AI Portfolio", page_icon="💼", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background-color: #0E1117;
        color: #F8FAFC;
    }

    /* Hero Section */
    .hero-container {
        padding: 3rem 1rem;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0) 100%);
        border: 1px solid rgba(255,255,255,0.05);
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        background: linear-gradient(to right, #FFFFFF, #94A3B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px !important;
        padding-bottom: 5px;
    }
    
    .hero-subtitle {
        font-size: 1.4rem !important;
        color: #60A5FA !important;
        font-weight: 500 !important;
        margin-bottom: 1.5rem !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Cards */
    .corporate-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        height: 100%;
        transition: transform 0.2s ease-in-out;
    }
    .corporate-card:hover {
        transform: translateY(-4px);
        border-color: rgba(96, 165, 250, 0.5);
    }

    /* Skills Pill */
    .tech-pill {
        display: inline-block;
        background: rgba(37, 99, 235, 0.1);
        color: #93C5FD;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid rgba(59, 130, 246, 0.3);
        transition: all 0.2s ease;
    }
    .tech-pill:hover {
        background: rgba(37, 99, 235, 0.2);
        color: #FFFFFF;
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        color: #F8FAFC;
        border-bottom: 2px solid #1E293B;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.markdown(f"## {NAME}")
    st.markdown(f"*{TITLE}*")
    st.divider()
    
    st.markdown("### 📞 Contact Info")
    st.markdown(f"**Email:** {EMAIL}")
    st.markdown(f"**LinkedIn:** {LINKEDIN}")
    st.markdown(f"**GitHub:** {GITHUB}")
    
    st.divider()
    st.markdown("### 🔒 AI Engine Config")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Enter authorization key...")
    if not api_key:
        st.warning("Secure API Connection Required.")
    else:
        st.success("Secure Connection Active.")
        
    model_choice = st.selectbox("LLM Architecture", ["gemini-1.5-flash", "gemini-1.5-pro"])
    if st.button("🔄 Clear Chat History"):
        st.session_state.messages = []
        st.rerun()


# ==========================================
# MAIN INTERFACE
# ==========================================

# Hero Section
st.markdown(f"""
<div class="hero-container">
    <h1 class="hero-title">{NAME}</h1>
    <div class="hero-subtitle">{TITLE}</div>
    <div style="font-size: 1.1rem; color: #94A3B8; max-width: 900px; line-height: 1.7;">
        Focused on translating theoretical algorithmic complexities into scalable, production-grade enterprise software. Architecting solutions emphasizing machine learning paradigms and data-driven computational models.
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation
tab_resume, tab_chat = st.tabs(["📄 Professional Dossier", "🤖 Interactive AI Proxy"])

# ----------------- RESUME TAB -----------------
with tab_resume:
    
    # 1. Competencies Section
    st.markdown('<div class="section-header">🛠️ Core Technical Competencies</div>', unsafe_allow_html=True)
    
    skill_col1, skill_col2, skill_col3 = st.columns(3)
    
    with skill_col1:
        st.markdown('<div class="corporate-card">', unsafe_allow_html=True)
        st.markdown("#### Programming Languages")
        st.markdown("<div>" + "".join([f'<span class="tech-pill">{s}</span>' for s in SKILLS["Languages"]]) + "</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with skill_col2:
        st.markdown('<div class="corporate-card">', unsafe_allow_html=True)
        st.markdown("#### AI & Machine Learning")
        st.markdown("<div>" + "".join([f'<span class="tech-pill">{s}</span>' for s in SKILLS["AI & ML"]]) + "</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with skill_col3:
        st.markdown('<div class="corporate-card">', unsafe_allow_html=True)
        st.markdown("#### Architecture & Tools")
        st.markdown("<div>" + "".join([f'<span class="tech-pill">{s}</span>' for s in SKILLS["Frameworks & Tools"]]) + "</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. Education Section
    st.markdown('<div class="section-header">🎓 Educational Background</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="corporate-card" style="border-left: 4px solid #3B82F6;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <h3 style="margin:0; color:#F8FAFC;">{UNIVERSITY}</h3>
            <span style="color: #60A5FA; font-weight: 500;">Currently Pursuing</span>
        </div>
        <h4 style="margin-top: 5px; color:#94A3B8; font-weight: 400;">Bachelor of Technology in Artificial Intelligence & Machine Learning</h4>
        <ul style="color: #CBD5E1; margin-top: 15px;">
            <li>Comprehensive coursework strictly focused on Algorithms, Data Structures, and Applied Machine Learning.</li>
            <li>Conducting extensive independent research into Generative AI models and Neural Networks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ----------------- CHATBOT TAB -----------------
with tab_chat:
    st.markdown("### 💬 Executive AI Representative")
    st.caption(f"This AI has been authorized to answer inquiries regarding {NAME}'s professional qualifications on his behalf.")
    
    if "messages" not in st.session_state or st.session_state.get("current_model") != model_choice:
        st.session_state.current_model = model_choice
        st.session_state.messages = [] 

    # Suggested Prompts
    if not st.session_state.messages:
        cols = st.columns(3)
        if "prompt_trigger" not in st.session_state:
            st.session_state.prompt_trigger = None
            
        if cols[0].button("Summarize Profile"):
            st.session_state.prompt_trigger = "Provide an executive summary of Rishu's profile."
        if cols[1].button("List Core Competencies"):
            st.session_state.prompt_trigger = "What are the primary programming languages and frameworks Rishu uses?"
        if cols[2].button("Review Education"):
            st.session_state.prompt_trigger = "Summarize Rishu's ongoing academic studies."

    user_input = st.chat_input("Input inquiry here...")
    
    if getattr(st.session_state, "prompt_trigger", None):
        user_input = st.session_state.prompt_trigger
        st.session_state.prompt_trigger = None 
        
    for msg in st.session_state.messages:
        avatar = "💼" if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)
        
        with st.chat_message("assistant", avatar="💼"):
            if not api_key:
                st.error("Authentication required. Please enter API key in the secure sidebar.")
                st.session_state.messages.pop() 
            else:
                message_placeholder = st.empty()
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel(model_choice, system_instruction=PERSONA)
                    
                    contents = []
                    for msg in st.session_state.messages:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append({"role": role, "parts": [msg["content"]]})

                    with st.spinner("Processing inquiry via secure LLM tunnel..."):
                        response = model.generate_content(contents)
                    
                    message_placeholder.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                    
                except Exception as e:
                    st.error(f"Server Exception: {e}")
                    st.session_state.messages.pop()
