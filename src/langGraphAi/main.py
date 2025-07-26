import streamlit as st
from src.langGraphAi.UI.streamlit_UI.load import LoadStramlitUI

def load_langgraph_agenticai_app():
    """
        loads and runs the application with streamlit UI, initializes
        the ui , handling user input , and config the llm models
        sets up the graph based on the selected use case
    """

    # load UI
    ui = LoadStramlitUI()
    user_input = ui.load_stream_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input from the ui")
        return
    
    user_msg = st.chat_input("Enter your message: ")
    
    # if user_msg:
    #     try:
    #         # config llm
    #         obj_llm_config = GroqLLM 
    