import os
import numpy as np
from openai_func import ChatGPT
import configparser
from organizer import testOrganizer

def test1(input):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    openai_config = config['OPENAI']
    llm = ChatGPT(openai_config)
    messages = testOrganizer(input)
    response = llm.get_response(messages)
    return response


def build_chatgpt():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    openai_config = config['OPENAI']
    llm = ChatGPT(openai_config)
    return llm

