import os
import sys
sys.path.insert(0, os.path.abspath('../'))

from loguru import logger
from core.crawler import SingleTermsWebCrawler

os.environ['OPENAI_API_KEY'] = open('/home/asus/SmartGPT/server/save/keys/openai.txt', 'r').read().strip()

crawler = SingleTermsWebCrawler()
crawler.crawl("Tài chính Việt Nam", "/home/asus/SmartGPT/server/save/prompt_templates/extract_keyword.txt")