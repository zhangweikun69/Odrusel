import openai
import tiktoken
from langchain.chat_models import ChatOpenAI

"""
openai_func.py
Customized OpenAI Functions.

This Document Mainly Implements:
    1. Use OpenAI Embedding to Vectorize Data.
    2. Use OpenAI ChatGPT.
"""


class ChatGPT:
    def __init__(self, openai_config):
        self.config = openai_config
        self.openai_api_key = openai_config['openai_api_key1']
        print("OpenAI Key has been successfully set!")

        self.encoding = tiktoken.get_encoding("cl100k_base")  # text-embedding-ada-002, gpt-3.5-turbo, gpt-4, use the cl100k_base encoding

    def calculate_tokens(self, input):
        count = len(self.encoding.encode(input))
        return count
    
    def get_response(self, messages):
        response = []
        chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=self.openai_api_key, model_kwargs={"stop": ["\n"]})
        return_msg = chat(messages)
        response = return_msg.content
        return response