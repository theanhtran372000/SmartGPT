import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

from loguru import logger
from langchain.document_loaders import UnstructuredURLLoader

from utils.timeout import run_with_timeout
from utils.postprocess import postprocess_web_content

# TODO: Dynamic Web Load
class WebLoader:
    
    def load(self, url):
        return postprocess_web_content(self.load_urls([url])[0])
    
    def try_load(self, url, timeout=5):
        
        def wrap_function():
            contents = self.load_urls([url])
            if len(contents) > 0:
                return postprocess_web_content(contents[0])
            else:
                return None
        
        return run_with_timeout(wrap_function, max_wait=timeout, default_value=None)
    
    def load_urls(self, urls):
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        return data
    
if __name__ == '__main__':
    webLoader = WebLoader()
    content = webLoader.load('https://vietnamnet.vn/vet-den-cua-dai-gia-xang-dau-bi-diem-mat-trong-vu-bat-ong-le-duc-tho-2227084.html')
    logger.success('Content: \n{}'.format(content.page_content))