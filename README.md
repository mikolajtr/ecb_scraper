# ecb_scraper
Simple API that scraps exchange rates from RSS feeds

Requires Python 3.6 or higher

To populate database with fresh data, run `python manage.py updateexchangerates`. This scripts scraps only the latest rates and save them to database.
API have one GET endpoint: `/exchange_rates`. I pass 3 optional arguments:
 * `page` (default `1`)
 * `page_size` (default `20`)
 * `order_by` (default `-updated`)

Endpoint response:
* `page`
* `page_size`
* `total` - total number of saved rates
* `data` - list of rate objects

Each exchange rate objects has 3 fields (and `id`, not displayed):
* `currency`
* `value` - price of 1 EUR
* `updated` - rate update date
