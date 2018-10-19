from datetime import datetime
from time import mktime

from django.core.management import BaseCommand

from currencies.models import ExchangeRate
from currencies.utils import get_feeds_urls, get_exchange_rates


class Command(BaseCommand):
    help = "Get the first entry about exchange rate for every currency in feeds"

    def handle(self, *args, **options):
        feeds_urls = get_feeds_urls("https://www.ecb.europa.eu/home/html/rss.en.html", "https://www.ecb.europa.eu")

        for url in feeds_urls:
            exchange_rates = get_exchange_rates(url)
            for rate in exchange_rates:
                exchange_rate = ExchangeRate(currency=rate['currency'],
                                             value=rate['value'],
                                             updated=datetime.fromtimestamp(mktime(rate['updated'])))
                print(f'1 EUR = {rate["value"]} {rate["currency"]}')
                exchange_rate.save()
                break
