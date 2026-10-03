players = [
    {"player": "rex", "brand": "MegaBot SG",   "deposit": 500.00,  "tags": ["ftd", "vip"]},
    {"player": "finn",  "brand": "GoldfishWin", "deposit": "80.50", "tags": ["ftd"]},
    {"player": "phoon",  "brand": "MegaBot SG",   "deposit": 1300.00, "tags": ["ftd", "vip"]},
    {"player": "jim",   "brand": "PragmaticBot",                    "tags": ["ftd"]},
    {"player": "sakai",  "brand": "GoldfishWin",  "deposit": 700.00,  "tags": ["ftd", "vip"]}
]


def total_deposits(rows):
    total = 0
    for row in rows:
        try:
            total += row["deposit"]
        except (KeyError, TypeError):
            continue
    return total

def ftd_players(rows):
    ftd_list = []
    for row in rows:
        try:
            if "ftd" in row["tags"]:
                ftd_list.append(row["player"])
        except (KeyError, TypeError):
            continue
    return ftd_list

def players_with_high_deposits(rows):
    high_deposit_players = []
    for row in rows:
        try:
            if row["deposit"] > 500:
                high_deposit_players.append(row["player"])
        except (KeyError, TypeError):
            continue
    return high_deposit_players

def label(deposit):
    if deposit < 100:
        return "low"
    elif 100 <= deposit <= 500:
        return "mid"
    else:
        return "high"


for row in players:
    try:
        print(row["player"], row["brand"], row["deposit"], label(row["deposit"]))
    except (TypeError, KeyError) as error:
        print(f"Bad row (status unavailable): {row} ({error})")
