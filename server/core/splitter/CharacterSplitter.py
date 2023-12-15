from langchain.text_splitter import CharacterTextSplitter

class CharacterSplitter:
    def __init__(
        self, 
        seperator='\n',
        chunk_size=1000,
        chunk_overlap=200
    ):
        self.seperator = seperator
        self.chunk_size = chunk_size
        self.chunk_overlab = chunk_overlap
        
        self.splitter = CharacterTextSplitter(
            separator=seperator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
    def split(self, docs):
        return self.splitter.split_documents(docs)