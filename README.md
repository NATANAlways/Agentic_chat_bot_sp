# 😁 LangGraph: Nat-Bot

LangGraph: Nat-Bot is an **agentic chatbot** built using **LangGraph AI** concepts, designed to run with multiple LLM backends (e.g., Groq, OpenAI, etc.).  
It supports **modular agent workflows**, enabling different use cases such as a basic chatbot, Q&A assistant, and task automation.

---

## 📌 Features
- 🌐 **Multi-LLM Support** – Easily switch between providers like **Groq**.
- 🧠 **Modular Agent Architecture** – Built with `StateGraph` for flexible conversation flows.
- 🎨 **Interactive UI** – Powered by **Streamlit**.
- 🔌 **Configurable API Keys** – Securely use your own LLM API keys.
- 📂 **Use Case Selector** – Choose from predefined chatbot modes.
- 📊 **User-friendly Interface** – Responsive design with message formatting.

---

## 📷 Screenshots

### 🔹 Home Interface
<img width="1845" height="819" alt="image" src="https://github.com/user-attachments/assets/4f6f6ee5-96f7-4b0b-b469-f66f7dad3473" />


### 🔹 Chat in Action
<img width="1907" height="870" alt="image" src="https://github.com/user-attachments/assets/c9e491d4-0e07-4847-9221-a2f1b9d79993" />

---

## 📂 Project Structure

```plaintext
Agentic_chat_bot_sp-main/
│
├── app.py                        # Main entry point for the chatbot application
├── requirements.txt              # Python dependencies
├── src/
│   ├── langGraphAi/
│   │   ├── main.py                # Core logic to initialize and run LangGraph AI workflow
│   │   ├── LLms/                   # Language model integration
│   │   │   └── grokllm.py          # Example LLM backend
│   │   ├── UI/                     # User interface modules
│   │   │   ├── configfile_ui.py    # UI configuration logic
│   │   │   ├── configfile_ui.ini   # UI settings file
│   │   │   └── streamlit_UI/       # Streamlit-based chatbot UI
│   │   │       ├── load.py
│   │   │       └── result.py
│   │   ├── graph/                  # Conversation graph definitions
│   │   │   └── g_build.py
│   │   ├── nodes/                  # Conversation node definitions
│   │   │   └── chatbot_node.py
│   │   └── __init__.py
│   └── __init__.py
└── .gitignore


---

```
## 🚀 Features

- **Agent-based architecture** for modular chatbot design
- **Conversation graphs** to define chatbot workflow and decision paths
- **Custom nodes** for handling specific tasks in conversations
- **Streamlit-based UI** for interactive chatting
- **Configurable LLM integration** (example with `grokllm.py`)

---

## 🛠 Technologies Used
- **Python 3.10+**
- **Streamlit**
- **LangGraph**
- **Groq API**
- **Llama Guard / Gemma Models**







