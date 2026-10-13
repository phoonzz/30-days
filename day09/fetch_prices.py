# Pull live crypto prices in MYR and write them to a CSV.
# No API key needed.

# URL:
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=myr&order=market_cap_desc&per_page=10&page=1


# ---- step 1: imports ----
# you need: requests, csv
import requests
import csv
import argparse

parser = argparse.ArgumentParser(description="Pull crypto prices to CSV")
parser.add_argument("--currency", default="myr", help="currency code, e.g. usd")
parser.add_argument("--coins", type=int, default=10, help="how many coins")
parser.add_argument("--out", default="prices.csv", help="output filename")
args = parser.parse_args()
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
# ---- step 2: fetch ----
# call the URL
# print the status code  (200 means OK)
# turn the response into python with .json()
# print type() of what you got, and len()
url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={args.currency}&order=market_cap_desc&per_page={args.coins}&page=1"

r = requests.get(url)
logging.info("HTTP status: %s", r.status_code)
data = r.json()
logging.debug("First response record: %s", data[0])
logging.debug("Response fields: %s", data[0].keys())
logging.debug("Response type: %s", type(data))
logging.info("fetched %d coins", len(data))

# ---- step 3: look at one record ----
# print the first item
# print its keys  (what fields are available?)


# ---- step 4: build your rows ----
# loop over the data
# for each coin, build a dict with ONLY the fields you want:
#   name, symbol, current_price, market_cap, price_change_percentage_24h
# collect them into a list
rows = []

rows = []                                  

for coin in data:
    row = {
        "name": coin["name"],
        "symbol": coin["symbol"],
        "current_price": coin["current_price"],
        "market_cap": coin["market_cap"],
        "price_change_percentage_24h": coin["price_change_percentage_24h"],
    }
    rows.append(row)                       

logging.debug("First output row: %s", rows[0])
logging.info("Prepared %d rows", len(rows))


# ---- step 5: write the csv ----
# csv.DictWriter, writeheader(), writerows()
# filename: prices.csv
with open(args.out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

logging.info(f"wrote {len(rows)} rows to {args.out}")
