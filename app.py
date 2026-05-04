import streamlit as st
import json
import os
from utils.parser import extract_text
from utils.chatbot import get_ai_response

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# =========================
# 📂 CHAT HISTORY FUNCTIONS
# =========================
def load_chat():
    if os.path.exists("chat_history.json"):
        try:
            with open("chat_history.json", "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_chat(messages):
    with open("chat_history.json", "w") as f:
        json.dump(messages, f)

# =========================
# 🎯 SIDEBAR
# =========================
st.sidebar.title("⚙️ Controls")

role = st.sidebar.selectbox(
    "Select Target Role",
    ["Data Scientist", "Data Engineer", "ML Engineer", "Cloud Engineer", "Data Analyst"]
)

# Load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat()

# Clear chat
if st.sidebar.button("🗑 Clear History"):
    st.session_state.messages = []
    save_chat([])

# Show recent history
st.sidebar.subheader("📜 Recent Chats")
for msg in st.session_state.messages[-5:]:
    role_icon = "👤" if msg["role"] == "user" else "🤖"
    st.sidebar.write(f"{role_icon} {msg['content'][:50]}...")

# =========================
# 🧾 MAIN TITLE
# =========================
st.title("🚀 AI Resume Analyzer & Career Chatbot")

# =========================
# 📂 RESUME UPLOAD
# =========================
uploaded_file = st.file_uploader("📂 Upload Resume", type=["pdf", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    text_lower = text.lower()

    st.success("✅ Resume uploaded!")

    # 🎯 ROLE DATA
    roles = {
        "Data Scientist": {
            "skills": ["python", "machine learning", "statistics", "pandas", "numpy"],
            "projects": ["prediction", "classification", "nlp", "analysis"]
        },
        "Data Engineer": {
            "skills": ["sql", "etl", "airflow", "spark"],
            "projects": ["pipeline", "data warehouse"]
        },
        "ML Engineer": {
            "skills": ["python", "tensorflow", "pytorch"],
            "projects": ["deployment", "ml pipeline"]
        },
        "Cloud Engineer": {
            "skills": ["aws", "docker", "kubernetes"],
            "projects": ["cloud", "ci/cd"]
        },
        "Data Analyst": {
            "skills": ["excel", "sql", "power bi"],
            "projects": ["dashboard", "analysis"]
        }
    }

    selected = roles[role]

    # 🔍 ANALYSIS
    found_skills = [s for s in selected["skills"] if s in text_lower]
    missing_skills = [s for s in selected["skills"] if s not in text_lower]

    found_projects = [p for p in selected["projects"] if p in text_lower]
    missing_projects = [p for p in selected["projects"] if p not in text_lower]

    sections = ["education", "skills", "project", "experience"]
    missing_sections = [s for s in sections if s not in text_lower]

    score = int(
        (len(found_skills)/len(selected["skills"]))*40 +
        (len(found_projects)/len(selected["projects"]))*30 +
        ((len(sections)-len(missing_sections))/len(sections))*30
    )

    # =========================
    # 📊 DISPLAY ANALYSIS
    # =========================
    st.subheader("📊 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Found Skills")
        st.write(found_skills)

        st.markdown("### 📁 Found Projects")
        st.write(found_projects)

    with col2:
        st.markdown("### ❌ Missing Skills")
        st.write(missing_skills)

        st.markdown("### ❌ Missing Projects")
        st.write(missing_projects)

    st.markdown(f"## 🎯 ATS Score: {score}/100")

    # =========================
    # 💡 SUGGESTIONS
    # =========================
    st.subheader("💡 Suggestions")

    if missing_skills:
        st.warning(f"Add skills: {missing_skills}")

    if missing_projects:
        st.warning(f"Add projects related to: {missing_projects}")

    if missing_sections:
        st.warning(f"Missing sections: {missing_sections}")

    # =========================
    # 📐 ATS TIPS
    # =========================
    st.subheader("📐 ATS Format Tips")

    st.info("""
✔ Use simple fonts (Arial/Calibri)  
✔ Font size: 10–12  
✔ Use clear headings  
✔ Avoid images/graphics  
✔ Keep resume 1 page  
✔ Maintain proper alignment  
""")

# =========================
# 🤖 CHATBOT
# =========================
st.divider()
st.subheader("🤖 Career Chatbot")

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask about skills, roles, projects...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    response = get_ai_response(user_input)
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    # Save chat
    save_chat(st.session_state.messages)