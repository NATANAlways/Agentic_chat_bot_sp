# define the state
from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated # labelling 

class State(TypedDict):
    #  to represent the Structure of the State in Graph
    msgs: Annotated[List, add_messages]