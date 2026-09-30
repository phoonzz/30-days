response = {
    "status": "ok",
    "count": 2,
    "data": [
        {"player": "phoon88", "brand": "MegaBot SG", "deposit": 250.00, "tags": ["ftd", "vip"]},
        {"player": "lily22", "brand": "GoldfishWin", "deposit": 80.50, "tags": ["ftd"]}
    ]
}
first = response["data"][0]

print(first["player"])
print(first["deposit"])
print(f"{first['player']} deposited {first['deposit']}")