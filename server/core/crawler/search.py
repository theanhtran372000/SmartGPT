import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

import time
import requests

from loguru import logger
from bs4 import BeautifulSoup

from utils.agent import get_useragent


def send_request(
    term, results, 
    start_index,
    lang, timeout
):
    resp = requests.get(
        url="https://www.google.com/search",
        headers={
            "User-Agent": get_useragent()
        },
        params={
            "q": term,                                      # Search term
            "num": results + 2,                             # Number of returned result -> +2 to prevents multiple requests
            "hl": lang,                                     # Desired language
            "start": start_index,                           # Start index for pagination
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp


def search_for_term(term, num_results, lang="vi", sleep_interval=5, timeout=10, max_trials=3):
    """Search the Google search engine"""

    escaped_term = term.replace(" ", "+")
    
    # Fetch
    start = 0
    n_trials = 0
    while start < num_results and n_trials < max_trials:
        n_trials += 1
        
        # Send request
        resp = send_request(
            escaped_term, 
            num_results - start,
            start, 
            lang, timeout
        )

        # Parse HTML
        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        for result in result_block:
            # Find link, title, description
            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find(
                "div", {"style": "-webkit-line-clamp:2"})
            if description_box:
                description = description_box.text
                if link and title and description:
                    start += 1
                    yield link["href"]
        
        # logger.info('Google Search: Trial {} - Found {} urls, {} remained!'.format(n_trials, start, num_results - start))
        
        # Sleep between requests
        # logger.info('Google Search: Sleep for {}s!'.format(sleep_interval))
        time.sleep(sleep_interval)
