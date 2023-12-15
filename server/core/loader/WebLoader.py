from loguru import logger
from langchain.document_loaders import UnstructuredURLLoader

# TODO: Dynamic Web Load

class WebLoader:
    def __init__(self):
        pass
    
    def load(self, url):
        return self.load_urls([url])[0]
    
    def load_urls(self, urls):
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        return data
    
if __name__ == '__main__':
    webLoader = WebLoader()
    content = webLoader.load('https://vietnamnet.vn/vet-den-cua-dai-gia-xang-dau-bi-diem-mat-trong-vu-bat-ong-le-duc-tho-2227084.html')
    logger.success('Content: \n{}'.format(content.page_content))