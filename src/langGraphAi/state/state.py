# define the state
from pydantic import BaseModel, Field
from typing_extensions import TypedDict, list
from langgraph.graph.message import add_messages
from typing import Annotated # labelling 

class State(TypedDict):
    #  to represent the Structure of the State in Graph
    msgs: Annotated[list, add_messages]