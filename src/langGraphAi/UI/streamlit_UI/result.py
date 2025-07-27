#  to display the msg -> op

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultSt:

    def __init__(self, usecase, graph, user_msg):
        self.usecase = usecase
        self.graph = graph
        self.user_msg = user_msg

    def display_result_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_msg = self.user_msg
        print(user_msg)
        if usecase == "Basic Chatbot":
            for event in graph.stream({'msgs':("user", user_msg)}):
                print(event.values())
                for value in event.values():
                    print(value['msgs'])
                    with st.chat_message("user"):
                        st.write(user_msg)
                    with st.chat_message("assistant"):
                        st.write(value["msgs"].content)





