players = [
    {"player": "phoon88", "brand": "MegaBot SG",   "deposit": 250.00,  "tags": ["ftd", "vip"]},
    {"player": "lily22",  "brand": "GoldfishWin",  "deposit": 80.50,   "tags": ["ftd"]},
    {"player": "ahseng",  "brand": "MegaBot SG",   "deposit": 1200.00, "tags": ["ftd", "vip"]},
    {"player": "mei",     "brand": "PragmaticBot", "deposit": 45.00,   "tags": ["ftd"]},
    {"player": "danial",  "brand": "GoldfishWin",  "deposit": 500.00,  "tags": ["ftd", "vip"]}
]


# ---- 1. worked example: read it, don't change it ----

def total_deposits(rows):
    total = 0
    for p in rows:
        total += p["deposit"]
    return total 
    pass

     


# ---- 2. your turn: count the vips, RETURN the number ----

def count_vips(rows):
    total = 0
    for p in rows:
        if "vip" in p["tags"]:
            total += 1
    return total

# ---- 3. return a LIST of players who deposited more than `minimum` ----

def big_spenders(rows, minimum):
    big_spenders_list = []
    for p in rows:
        if p["deposit"] > minimum:
            big_spenders_list.append(p["player"])
    return big_spenders_list


# ---- 4. takes ONE deposit amount, returns "high roller" / "mid" / "low" ----

def label(deposit):
    if deposit > 500:
        return "high roller"
    elif deposit > 100:
        return "mid"
    else:
        return "low"


# ---- calling them ----

print(total_deposits(players))
print(count_vips(players))
print(big_spenders(players, 100))
print(label(1200))