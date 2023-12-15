from langchain.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def get_emb():
    return OpenAIEmbeddings()

def get_llm(model_name, temperature=0, streaming=False):
    return ChatOpenAI(
        temperature=temperature, 
        model_name=model_name, 
        streaming=streaming,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        verbose=True
    )