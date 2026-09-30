players = [
    {"player": "phoon88", "brand": "MegaBot SG",   "deposit": 250.00, "tags": ["ftd", "vip"]},
    {"player": "lily22",  "brand": "GoldfishWin",  "deposit": 80.50,  "tags": ["ftd"]},
    {"player": "ahseng",  "brand": "MegaBot SG",   "deposit": 1200.00,"tags": ["ftd", "vip"]},
    {"player": "mei",     "brand": "PragmaticBot", "deposit": 45.00,  "tags": ["ftd"]},
    {"player": "danial",  "brand": "GoldfishWin",  "deposit": 500.00, "tags": ["ftd", "vip"]}
]


total = 0

vips = 0

for p in players:
    if "vip" in p["tags"]:
        vips += 1

print(vips)
