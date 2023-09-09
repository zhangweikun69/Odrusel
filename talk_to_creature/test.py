import json
import os
import numpy as np
import openai
import tiktoken
import torch
from openai_func import ChatGPT
import configparser
from organizer import testOrganizer

os.chdir("./talk_to_creature")

def test(input):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    openai_config = config['OPENAI']
    llm = ChatGPT(openai_config)
    messages = testOrganizer(input)
    print(f"Send messages: {messages}")
    response = llm.get_response(messages)
    return response