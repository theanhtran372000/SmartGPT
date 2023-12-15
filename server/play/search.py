import pprint
from loguru import logger
from googlesearch import search


def search_urls(term, num_results):
    results = []
    for url in search(term, num_results=num_results, lang='vi', sleep_interval=5):
        results.append(url)
    return results


if __name__ == '__main__':
    keyword = 'Quả bóng vàng 2024'
    urls = search_urls(keyword, num_results=1)
    logger.info('URLs: \n{}'.format(pprint.pformat(urls)))