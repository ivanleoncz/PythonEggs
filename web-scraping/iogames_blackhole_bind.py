""" Extracts list of IO domains from iogames.fun, a creates strings for
DNS blackholes (BIND9) style.
"""

from requests import get
from contextlib import closing
from bs4 import BeautifulSoup

URI = "http://iogames.fun/list"

bind_rule_start = 'zone "'
bind_rule_end = '" { type master; file "/etc/bind/zones/db.blackhole"; };'

with closing(get(URI, stream=True)) as resp:
    content_type = resp.headers['Content-Type'].lower()
    if resp.status_code == 200 and content_type is not None:
        raw_html = resp.content
        soup = BeautifulSoup(raw_html, 'html.parser')
        results = soup.find_all("option")
        for opt in results:
            domain = str(opt).split('"')[1]
            s = bind_rule_start + domain + bind_rule_end
            print(s)
