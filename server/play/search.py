import os
import sys
sys.path.insert(0, os.path.abspath('../'))

from loguru import logger
from core.crawler import search_for_term

if __name__ == '__main__':
    term = 'Quả bóng vàng 2024'
    logger.info('URLs: ')
    for i, url in enumerate(search_for_term(
        term, num_results=20
    )):
        logger.info('{}: {}'.format(i + 1, url))