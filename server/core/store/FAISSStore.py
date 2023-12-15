import pickle
from langchain.vectorstores import FAISS


def build_faiss_store(docs, embs):
    return FAISS.from_documents(docs, embs)

def save_faiss_store(store, folder_path):
    store.save_local(folder_path=folder_path)
        
def load_faiss_store(localpath, embs):
    local_index = FAISS.load_local(localpath, embs)
    return local_index

def update_faiss_store(store, localpath, embs):
    local_index = load_faiss_store(localpath, embs)
    local_index.merge_from(store)
    return local_index

def to_retriever(store):
    return store.as_retriever()