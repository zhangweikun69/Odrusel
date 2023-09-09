from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)



"""
organizer.py
Core File. Organizer creates valid Prompt.

This Document Mainly Implements:
    1. 
    2. 
"""

def testOrganizer(user_input):
    system_prompt = "You are a translator, translate English to Chinese!"
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    messages2 = [
        SystemMessage(content="You are an assistant."),
        HumanMessage(content="Hello, my name is Larry Zhang."),
        AIMessage(content="Hi Larry Zhang, How can I help you."),
        HumanMessage(content=user_input)
    ]

    return messages2