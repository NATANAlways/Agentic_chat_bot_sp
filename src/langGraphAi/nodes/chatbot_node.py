# what does the chat_bot_will do, defined here

from src.langGraphAi.state.state import State

class ChatbotNode:
    # chatbot

    def __init__(self, llm_model):
        self.llm = llm_model

    def process(self, state:State)->dict: #return type is dict
        # process the ip state and generate response by chatbot 
        return {"msgs":self.llm.invoke(state['msgs'])} #state msgs will be the ip and for that response evoke from llm
    
