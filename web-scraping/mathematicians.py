""" Scrapindg data from fabpedigree.com. """

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from json import dumps

URI = "http://www.fabpedigree.com/james/mathmen.htm"

def http_get(uri):
    """ Performs content get from a URI. """
    try:
        with closing(get(uri, stream=True)) as resp:
            if response_200(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print("Error during requests to {0}: {1}".format(uri, str(e)))
        return None

def response_200(resp):
    """ Returns True if response is a HTML. """
    content_type = resp.headers['Content-Type'].lower()
    # print("Content:", content_type)
    return (resp.status_code == 200 and content_type is not None)


def html_parser():
    """ Performs the HTML parsing, based on http_get(uri) return. """
    raw_html = http_get(URI)
    ranking = dict()
    html = BeautifulSoup(raw_html, 'html.parser')
    for i, li in enumerate(html.select('li'), 1):
        ranking[i] = li.text.split('\n')[0]
    return dumps(ranking, indent=4)


print(html_parser())
