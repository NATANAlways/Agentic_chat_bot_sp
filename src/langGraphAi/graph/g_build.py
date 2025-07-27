from langgraph.graph import StateGraph
from src.langGraphAi.state.state import State
from langgraph.graph import StateGraph, START, END #Asynchronous and parallel processing:
from src.langGraphAi.nodes.chatbot_node import ChatbotNode

class GraphBuilder:
    def __init__(self, llm_model):
        self.llm = llm_model
        self.graph_builder = StateGraph(State)

    def chat_bot_build_graph(self):
        # init -> chatbot -> BasicChatBotNode class -> integrate into graph 

        self.chatbot_node = ChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.chatbot_node.process) # funality -> nodefolder
        self.graph_builder.add_edge(START, "chatbot") # graph: start -> chatbot (basic graph)
        self.graph_builder.add_edge("chatbot", END)