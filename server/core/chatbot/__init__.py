from langchain.chains import ConversationalRetrievalChain

def build_chain(llm, store):
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=store.as_retriever(search_kwargs={"k": 1}))