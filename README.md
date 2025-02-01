# DeepSeek ChatHub

DeepSeek ChatHub is a locally hosted AI chatbot powered by **DeepSeek-R1**, **LangChain**, and **Streamlit**. It provides a privacy-focused and responsive chatbot experience without relying on cloud services.

![Chatbot Screenshot](https://github.com/shiivamgupta/DeepSeek-ChatHub/blob/c0f35a5118a74d7ff7fcbe24db8d63294d359655/chatbot-ui.png)

## 🚀 Features
- 🛡️ **Privacy-Focused**: Runs entirely on your machine.
- ⚡ **Fast & Responsive**: No cloud dependency, ensuring low latency.
- 🧠 **Powered by Ollama DeepSeek-R1**: Uses a robust AI model for intelligent responses.
- 🎨 **Intuitive UI**: Modern, easy-to-use chat interface.

## 📋 Prerequisites
Before running the chatbot, ensure you have the following installed:

### 1️⃣ Install Ollama
Follow the installation guide at: [Ollama](https://ollama.ai)

### 2️⃣ Run DeepSeek-R1 Model in Ollama
```sh
ollama run deepseek-r1:1.5b
```
This will ensure the model is available for the chatbot.

### 3️⃣ Install Required Python Packages
```sh
pip install -qU langchain-ollama
pip install langchain streamlit
```

## 🏃 Running the Chatbot
Once all prerequisites are set up, you can launch the chatbot using:
```sh
streamlit run deepseek-chathub.py
```
This will start the chatbot UI in your browser, allowing you to interact with DeepSeek-R1 seamlessly.

## 🎯 Usage
1. **Enter your question** in the text area.
2. **Select Explanation Type** (Layman, Short, Long) for customized responses.
3. **Click Send** to receive AI-generated answers.
4. **View Chat History** to track previous conversations.

## 🤝 Contributing
Feel free to contribute by opening issues or submitting pull requests. 🚀

## 📜 License
BSD 3-Clause License

---
### 🌟 Connect with me:
- 🔗 [GitHub](https://github.com/shiivamgupta)
- 🔗 [LinkedIn](https://www.linkedin.com/in/theembeddedsoftwareengineer)
