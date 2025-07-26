import streamlit as st
import os
from src.langGraphAi.UI.configfile_ui import Config

class LoadStramlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_stream_ui(self):
        # Get title (and handle if it's a list)
        page_title = self.config.get_page_title()
        if isinstance(page_title, list):
            page_title = page_title[0]

        st.set_page_config(page_title='😊' + page_title, layout='wide')
        st.header('😊 ' + page_title)

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("select llm", llm_options)

            if self.user_controls['selected_llm'] == 'Groq':
                # model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY", type="password")

                # validate api key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please Enter your GROQ API key to proceed. If you Don't have an API Key then refer: https://groq.com/")
            
            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

        return self.user_controls