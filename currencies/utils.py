import re
from decimal import Decimal

import feedparser
import requests
from bs4 import BeautifulSoup


def get_feeds_urls(ecb_url, base_url):
    page = requests.get(ecb_url)
    html = BeautifulSoup(page.text, features="html.parser")
    for a in html.find_all('a', href=re.compile("/rss/fxref")):
        url = base_url + a['href']
        currency = a['href'][11:14].upper()
        yield {
            "url": url,
            "currency": currency
        }


def get_exchange_rates(url):
    feed = feedparser.parse(url)
    entries = feed.entries

    for entry in entries:
        title_split = entry.title.split()
        updated = entry.updated_parsed
        value, currency = title_split[0], title_split[1]

        yield {
            "currency": currency,
            "value": Decimal(value),
            "updated": updated
        }
