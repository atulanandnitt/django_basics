from bs4 import BeautifulSoup as Soup
import requests
from . db_api import get_movie_db_session
from . db_api import Movie
from . db_api import Theaters
import time


def get_page_contents(source):
    """
    Get page content in html parsed format
    :param soup: BS Soup Object
    :return: None
    """
    req = requests.get(source)

    content = Soup(req.text, 'html.parser')

    return content



def get_movie_page_contents(movie_url):
    """
    Get page content in html parsed format
    :param soup: BS Soup Object
    :return: None
    """
    req = requests.get(movie_url)

    content = Soup(req.text, 'html.parser')

    return content
