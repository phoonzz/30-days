# Pull live crypto prices and save them to a SQLite DATABASE instead of a CSV.

import requests
import argparse
import logging
import sqlite3
from datetime import datetime

parser = argparse.ArgumentParser(description="Pull crypto prices into SQLite")
parser.add_argument("--currency", default="myr", help="currency code")
parser.add_argument("--coins", type=int, default=10, help="how many coins")
parser.add_argument("--db", default="prices.db", help="database file")
args = parser.parse_args()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


# ---- fetch: this is your day 9 code, unchanged ----

url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={args.currency}&order=market_cap_desc&per_page={args.coins}&page=1"

r = requests.get(url)
logging.info("HTTP status: %s", r.status_code)
data = r.json()
logging.info("fetched %d coins", len(data))

rows = []
for coin in data:
    rows.append({
        "symbol": coin["symbol"],
        "name": coin["name"],
        "price": coin["current_price"],
        "market_cap": coin["market_cap"],
        "change_24h": coin["price_change_percentage_24h"],
        "fetched_at": datetime.now().isoformat(timespec="seconds"),
    })
logging.info("prepared %d rows", len(rows))


# ================= NEW PART STARTS HERE =================


# ---- step 1: open the database ----
# sqlite3.connect(args.db)  -> gives you a CONNECTION
# connection.cursor()       -> gives you a CURSOR (the thing that runs SQL)
# the file is created automatically if it doesn't exist
conn = sqlite3.connect(args.db)
cur = conn.cursor()




# ---- step 2: create the table if it isn't there yet ----
# cur.execute("""  ...your CREATE TABLE statement...  """)
#
# columns: symbol TEXT, name TEXT, price REAL, market_cap REAL,
#          change_24h REAL, fetched_at TEXT
#
# use:  CREATE TABLE IF NOT EXISTS prices ( ... )
# the IF NOT EXISTS means running twice is safe
cur.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        symbol TEXT,
        name TEXT,
        price REAL,
        market_cap REAL,
        change_24h REAL,
        fetched_at TEXT,
        UNIQUE(symbol, fetched_at)
    )
""")




# ---- step 3: insert the rows ----
# for each row:
#   cur.execute(
#       "INSERT INTO prices (symbol, name, price, market_cap, change_24h, fetched_at) "
#       "VALUES (?, ?, ?, ?, ?, ?)",
#       (row["symbol"], row["name"], row["price"], row["market_cap"],
#        row["change_24h"], row["fetched_at"])
#   )
#
# NEVER build SQL with an f-string. the ? placeholders are not a style choice.
for row in rows:
    cur.execute(
        "INSERT OR IGNORE INTO prices (symbol, name, price, market_cap, change_24h, fetched_at) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (row["symbol"], row["name"], row["price"],
         row["market_cap"], row["change_24h"], row["fetched_at"])
    )




# ---- step 4: save and close ----
# conn.commit()   <- nothing is written to disk until you do this
# conn.close()

conn.commit()
conn.close()



# ---- step 5: read it back and log how many rows are in there now ----
# cur.execute("SELECT COUNT(*) FROM prices")
# cur.fetchone()  -> gives you a tuple like (10,)

