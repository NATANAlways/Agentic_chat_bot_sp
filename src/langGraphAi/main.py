import streamlit as st
from src.langGraphAi.UI.streamlit_UI.load import LoadStramlitUI
from src.langGraphAi.LLms.grokllm import Grok_LLM
from src.langGraphAi.graph.g_build import GraphBuilder
from src.langGraphAi.UI.streamlit_UI.result import DisplayResultSt

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
    
    if user_msg:
        try:
             # config llm
            obj_llm_config = Grok_LLM(user_controls_ip=user_input) 
            llm_model = obj_llm_config.get_llm_model()

            if not llm_model:
                st.error("Error: llm model not get initialized !")
                return
            # initialize and setup the graph based on use case

            usecase=user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: usecase not selected !")
                return
            
            # Graph builder
            graph_builder_class = GraphBuilder(llm_model)
            try:
                graph=graph_builder_class.setup_whichgraph(usecase)
                DisplayResultSt(usecase, graph, user_msg).display_result_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph set up failed - {e}")
            return
            

