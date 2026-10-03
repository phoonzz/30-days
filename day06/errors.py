# Real API data is messy. Three of these five rows are broken.

players = [
    {"player": "phoon88", "brand": "MegaBot SG",   "deposit": 250.00,  "tags": ["ftd", "vip"]},
    {"player": "lily22",  "brand": "GoldfishWin",  "deposit": "80.50", "tags": ["ftd"]},
    {"player": "ahseng",  "brand": "MegaBot SG",                       "tags": ["ftd", "vip"]},
    {"player": "mei",     "brand": "PragmaticBot", "deposit": None,    "tags": ["ftd"]},
    {"player": "danial",  "brand": "GoldfishWin",  "deposit": 500.00,  "tags": ["ftd", "vip"]}
]


# ---- 1. this is your Day 5 function. run it. it WILL crash. ----

def total_deposits(rows):
    total = 0
    for p in rows:
        total += p["deposit"]
    return total


# ---- 2. make it survive. skip any row you can't add, count how many you skipped. ----
#         return the total AND the skip count.

def safe_total(rows):
    total = 0
    skip_count = 0
    for p in rows:
        try:
            total += p["deposit"]
        except (KeyError, TypeError):
            skip_count += 1
    return total, skip_count


# ---- 3. clean_deposit(value) -> a float, or None if it can't be one ----
#         "80.50" should become 80.5
#         None, a missing key, or "abc" should give back None

def clean_deposit(value):
    pass


# ---- 4. rewrite safe_total to use clean_deposit ----

def safe_total_v2(rows):
    pass


print(total_deposits(players))
print(safe_total(players))
# print(clean_deposit("80.50"), clean_deposit("abc"), clean_deposit(None))
# print(safe_total_v2(players))
