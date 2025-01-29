import re
import streamlit as st
from langchain_ollama import ChatOllama


# App Configuration
st.set_page_config(page_title="DeepSeek ChatHub", page_icon="🧠", layout="wide")


# Custom CSS for better readability
st.markdown(
   """
   <style>
   body { background-color: #1e1e1e; color: white; }
   .chat-container { background-color: #2e2e2e; padding: 10px; border-radius: 10px; }
   .user-message { background-color: #3a3a3a; color: white; padding: 10px; border-radius: 10px; }
   .assistant-message { background-color: #4a90e2; color: white; padding: 10px; border-radius: 10px; }
   .input-container { display: flex; align-items: center; justify-content: space-between; }
   .input-container textarea { flex-grow: 1; margin-right: 10px; }
   .small-dropdown { font-size: 12px; padding: 5px; }
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


# Chat Interface
st.markdown("---")
st.subheader("💡 Start Chatting Below:")


# Input and Controls Layout
col1, col2, col3 = st.columns([5, 1, 2])
with col1:
   text = st.text_area("Enter your question:", height=100, label_visibility='collapsed')
with col2:
   send_button = st.button("Send", use_container_width=True)
with col3:
   explanation_type = st.selectbox(
       "Choose Explanation Type:",
       ["Layman", "Short", "Long"],
       label_visibility='collapsed',
       key="explanation_type",
       format_func=lambda x: x.capitalize()
   )


# Define System Message based on Selection
system_messages = {
   "Layman": "You are a helpful AI Assistant. You work as a teacher for 5th grade students.",
   "Short": "You are a concise AI Assistant. Provide short and to-the-point answers.",
   "Long": "You are a detailed AI Assistant. Provide long and elaborate explanations."
}


def generate_response(input_text, system_message):
   model = ChatOllama(model="deepseek-r1:1.5b", base_url="http://localhost:11434/")
   prompt = f"{system_message}\nUser: {input_text}\nAssistant: "
   response = model.invoke(prompt)
   clean_response = re.sub(r"<think>.*?</think>", "", response.content, flags=re.DOTALL).strip()
   return clean_response


if send_button and text:
   with st.spinner("Generating response..."):
       response = generate_response(text, system_messages[explanation_type])
       st.session_state["chat_history"].append({"user": text, "deepseek": response})


# Display Chat History
st.markdown("## 📝 Chat History")
st.markdown("---")
for chat in reversed(st.session_state["chat_history"]):
   st.markdown(f"<div class='chat-container user-message'><b>🧑 User:</b> {chat['user']}</div>", unsafe_allow_html=True)
   st.markdown(f"<div class='chat-container assistant-message'><b>🧠 Assistant:</b> {chat['deepseek']}</div>", unsafe_allow_html=True)
   st.markdown("---")
