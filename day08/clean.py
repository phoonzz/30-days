import csv

# ---- 1. read it. print how many rows. then print the FIRST row on its own. ----
#         look hard at that first row before writing anything else.

with open("deposits_raw.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(len(rows))
print(rows[0])


# ---- 2. clean_deposit(value) -> float, or None if unusable ----
#         handle: "250.00"  "1200"  ""  "RM500.00"  "abc"

def clean_deposit(value):
    pass


# ---- 3. clean_rows(rows) -> (clean_list, report_dict) ----
#         strip whitespace off every field
#         convert deposit with clean_deposit
#         drop exact duplicate players
#         report how many were dropped and why

def clean_rows(rows):
    pass


# ---- 4. write the clean rows to deposits_clean.csv ----

def write_clean(rows, path):
    pass
