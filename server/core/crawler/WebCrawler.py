import time
import pprint
from loguru import logger

from .search import search_for_term
from ..loader import WebLoader
from ..chatbot import chatgpt_extract_kws


class SingleTermsWebCrawler:
    def __init__(
        self,
        list_width=[10, 3],
        prefer_lang='vi',
        sleep_interval=5,
        max_trials=3,
        max_display=200
    ):
        # Params
        self.list_width = list_width
        self.prefer_lang = prefer_lang
        self.sleep_interval = sleep_interval
        self.max_trials = max_trials
        self.max_display = max_display
        
        # Loader
        self.loader = WebLoader()
        
    def crawl(self, term, extract_template_path, save_folder):
        start = time.time()
        main_term = term
        
        logger.info('Start searching web urls for term "{}"...'.format(term))
        
        all_urls        = []
        all_contents    = []
        all_terms       = []
        terms           = [term]
        
        # For each layer with different width
        for i, width in enumerate(self.list_width):
            logger.info('===== Layer: {} - Width: {} ====='.format(i+1, width))
            logger.info('TERMS:')
            for l, term in enumerate(terms):
                logger.info('[{}] {}'.format(l+1, term))
            
            urls = []
            
            # For each term in this layer
            for j, term in enumerate(terms):
                # Crawl urls about this term
                logger.info('[{}/{}] Process term "{}"...'.format(j + 1, len(terms), term))
                _urls = []
                
                for url in search_for_term(
                        term=term, 
                        num_results=width,
                        lang=self.prefer_lang, 
                        sleep_interval=self.sleep_interval,
                        max_trials=self.max_trials
                    ):
                    if url not in _urls:
                        _urls.append(url)
                
                logger.success('Found {} urls for term "{}"!'.format(len(_urls), term))
            
                for url in _urls:
                    # Update url list in this layer
                    if url not in urls:
                        urls.append(url)
                    
                    # Update all urls so far
                    if url not in all_urls:
                        all_urls.append(url)
                    
                logger.success('Layer {}: \t{} urls'.format(i+1, len(urls)))
                logger.info('Total: \t\t{} urls'.format(len(all_urls)))
                
            # Create new terms
            # Load website content
            logger.info('Load url contents...')
            contents = []
            terms = [] # Reset terms
            for k, url in enumerate(urls):
                logger.info('[{}/{}] Load url {}...'.format(k+1, len(urls), url))
                content = self.loader.try_load(url)
                
                if content:
                    contents.append(content)
                    all_contents.append(content)
                    logger.success("Content: {}...".format(content.page_content[:self.max_display]))
                    
                    # If not last depth
                    if i != len(self.list_width) - 1:
                        # Extract terms
                        kws = chatgpt_extract_kws(
                            extract_template_path, 
                            input=content.page_content
                        )
                        
                        for kw in kws:
                            if kw not in terms:
                                terms.append(kw)
                            if kw not in all_terms:
                                all_terms.append(kw)
                        
                        logger.info('Extracted keywords: \n{}'.format(pprint.pformat(kws)))
                    else:
                        logger.info('Skip extracting keywords at last layer!')
                else:
                    logger.error('Fail to load content!')
                    
            logger.info('Load {}/{} pages!'.format(len(contents), len(urls)))
        
        logger.info('All done after {:.2f}s!'.format(time.time() - start))
        logger.info('=== FINAL RESULT ===')
        logger.info('= Terms: \t{}'.format(len(all_terms)))
        logger.info('= URL: \t{}'.format(len(all_urls)))
        logger.info('= Loaded:\t{}/{}urls'.format(len(all_contents), len(all_urls)))
        # logger.info('=> Avg: \t{:.1f} urls/term'.format(len(all_urls) / len(all_terms)))
        
        return all_urls, all_terms, all_contents