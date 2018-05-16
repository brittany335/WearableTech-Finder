
#PLEASE note: code fully adapted from http://edmundmartin.com/scraping-google-with-python/
# I do not take credit for this scraper of a google search, I changed something to use for my personal purpose


import requests
from bs4 import BeautifulSoup

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def fetch_results(search_term, number_results, language_code):
    """returns the html from the google search and the keyword """
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')

    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT, timeout=5)
    response.raise_for_status()

    return search_term, response.text


# keyword, html = fetch_results('edmund martin', 1, 'en')
# print(html)
