import os
import streamlit as st
from langchain_groq import ChatGroq
# from src.langGraphAi.UI.streamlit_UI.load import 

# loading specific llm
class Grok_LLM:
    def __init__(self, user_controls_ip):
        self.user_controls_ip = user_controls_ip

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_ip["GROQ_API_KEY"]
            select_qroq_model = self.user_controls_ip["selected_groq_model"] 
            if groq_api_key == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("Enter the Groq-API-KEY")

            llm = ChatGroq(api_key=groq_api_key, model=select_qroq_model)
        
        except Exception as e:
            raise ValueError(f"Error Occured: {e}")
        return llm

        