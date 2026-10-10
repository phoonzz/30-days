# Pull live crypto prices in MYR and write them to a CSV.
# No API key needed.

# URL:
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=myr&order=market_cap_desc&per_page=10&page=1


# ---- step 1: imports ----
# you need: requests, csv
import requests
import csv

# ---- step 2: fetch ----
# call the URL
# print the status code  (200 means OK)
# turn the response into python with .json()
# print type() of what you got, and len()
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=myr&order=market_cap_desc&per_page=10&page=1"

r = requests.get(url)
print(r.status_code)
data = r.json()
print(data[0])
print(data[0].keys())
print(type(data))
print(len(data))

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

print(rows[0])
print(len(rows))


# ---- step 5: write the csv ----
# csv.DictWriter, writeheader(), writerows()
# filename: prices.csv
with open("prices.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

# ---- step 6: make it not break ----
# what if the request fails?
# what if a coin is missing a field?
# print a one-line summary at the end: how many written, how many skipped
