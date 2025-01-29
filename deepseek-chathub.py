import re
import streamlit as st
from langchain_ollama import ChatOllama
from langchain.prompts import SystemMessagePromptTemplate


# App Configuration
st.set_page_config(page_title="DeepSeek ChatHub", page_icon="🧠", layout="wide")


# Custom CSS for better readability and dropdown width
st.markdown(
   """
   <style>
   body { background-color: #1e1e1e; color: white; }
   .chat-container { background-color: #2e2e2e; padding: 10px; border-radius: 10px; }
   .user-message { background-color: #3a3a3a; color: white; padding: 10px; border-radius: 10px; }
   .assistant-message { background-color: #4a90e2; color: white; padding: 10px; border-radius: 10px; }
   .stSelectbox > div { width: 150px !important; } /* Adjust dropdown width */
   </style>
   """,
   unsafe_allow_html=True
)


# Sidebar with App Info
with st.sidebar:
   st.title("🧠 DeepSeek ChatHub")
   st.markdown(
       """
       **Locally Hosted AI Chatbot** using **DeepSeek-R1**, **LangChain**, and **Streamlit**.
       - ✅ **Privacy-focused**: Runs entirely on your machine.
       - ✅ **Fast & Responsive**: No cloud dependency.
       - ✅ **Powered by Ollama DeepSeek-R1**
       """
   )
   st.markdown("### 🌟 Connect with me:")
   st.markdown("🔗 [**GitHub**](https://github.com/shiivamgupta)")
   st.markdown("🔗 [**LinkedIn**](https://www.linkedin.com/in/theembeddedsoftwareengineer)")
   st.markdown("---")


# Chat Title
st.markdown("<h1 style='text-align: center;'>💬 DeepSeek ChatHub</h1>", unsafe_allow_html=True)


# Initialize Chat History
if "chat_history" not in st.session_state:
   st.session_state["chat_history"] = []


# Create first row for user input and explanation type selection
col1, col2 = st.columns([3, 1])  # Adjust ratios as needed


with col1:
   text = st.text_area("Enter your question:", height=100)


with col2:
   explanation_type = st.selectbox(
       "Explanation Type:",
       ["Layman", "Short", "Long"]
   )


# Create second row for the Send button
send_col = st.columns(1)  # A single column for the button


with send_col[0]:  # Access the first (and only) column in the list
   if st.button("Send", use_container_width=True):
       if text:
           with st.spinner("Generating response..."):
               response = generate_response(text)
               st.session_state["chat_history"].append({"user": text, "deepseek": response})
       else:
           st.warning("Please enter a question to continue.")


# Display Chat History
st.markdown("## 📝 Chat History")
st.markdown("---")
for chat in reversed(st.session_state["chat_history"]):
   st.markdown(f"<div class='chat-container user-message'><b>🧑 User:</b> {chat['user']}</div>", unsafe_allow_html=True)
   st.markdown(f"<div class='chat-container assistant-message'><b>🧠 Assistant:</b> {chat['deepseek']}</div>", unsafe_allow_html=True)
   st.markdown("---")
