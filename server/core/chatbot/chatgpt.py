import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from utils.postprocess import random_crop_paragraph

def chatgpt_predict(template_path, input, default_value="Không rõ"):
    
    # Build prompt
    template = open(template_path, 'r').read()
    prompt = PromptTemplate(input_variables=["input", "default"], template=template)
    
    # Build chain
    chatgpt_chain = LLMChain(
        llm=ChatOpenAI(temperature=0),
        prompt=prompt
    )
    
    output = chatgpt_chain.predict(
        input=input,
        default=default_value
    )
    
    return output


def chatgpt_extract_kws(template_path, input, default_value='Không rõ', max_input_size=400):
    
    # Get output
    output = chatgpt_predict(template_path, random_crop_paragraph(input, max_input_size), default_value)
    
    # Postprocess
    if default_value in output:
        return []
    else:
        kws = [kw.strip() for kw in output.replace('"', '').split(',')]
        return kws
    