# 🧠 Agentic Chat Bot

An **agent-based conversational chatbot** built using modular Python architecture.  
The system leverages **LangGraph AI** concepts to design a flexible chatbot workflow that can integrate multiple LLM backends and interactive user interfaces.

---

## 📂 Project Structure

```
Agentic_chat_bot_sp-main/
│
├── app.py                        # Main entry point for the chatbot application
├── requirements.txt              # Python dependencies
├── src/
│   ├── langGraphAi/
│   │   ├── main.py                # Core logic to initialize and run LangGraph AI workflow
│   │   ├── LLms/                  # Language model integration
│   │   │   └── grokllm.py         # Example LLM backend
│   │   ├── UI/                    # User interface modules
│   │   │   ├── configfile_ui.py   # UI configuration logic
│   │   │   ├── configfile_ui.ini  # UI settings file
│   │   │   └── streamlit_UI/      # Streamlit-based chatbot UI
│   │   │       ├── load.py
│   │   │       └── result.py
│   │   ├── graph/                 # Conversation graph definitions
│   │   │   └── g_build.py
│   │   ├── nodes/                 # Conversation node definitions
│   │   │   └── chatbot_node.py
│   │   └── __init__.py
│   └── __init__.py
└── .gitignore
```

---

## 🚀 Features

- **Agent-based architecture** for modular chatbot design
- **Conversation graphs** to define chatbot workflow and decision paths
- **Custom nodes** for handling specific tasks in conversations
- **Streamlit-based UI** for interactive chatting
- **Configurable LLM integration** (example with `grokllm.py`)

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Agentic_chat_bot_sp-main.git
cd Agentic_chat_bot_sp-main

