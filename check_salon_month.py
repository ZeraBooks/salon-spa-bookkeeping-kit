"""Check a salon's card deposits and month in this repo's layout.

1. Every card deposit row reads across: services + retail + tips = card
   volume, and card volume - processor fee = net deposited.
2. The month file: profit is every "In profit" line added up, and each
   account kept out of profit (tips payable, gift cards) shows what is left
   in it at month end. Tips payable should be 0.00 after the last payroll.
3. The card deposit totals agree with the card lines in the month file.

Usage: python3 check_salon_month.py card-deposits.csv october-2026-month.csv
Python 3, standard library only.
"""
import csv
import sys
from collections import defaultdict
from decimal import Decimal


def d(cell):
    return Decimal(cell.strip()) if cell and cell.strip() else Decimal("0")


def check_deposits(path):
    ok = True
    tot = defaultdict(Decimal)
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            s, rt, tp = d(r["Card services"]), d(r["Card retail"]), d(r["Card tips"])
            vol, fee, net = d(r["Card volume"]), d(r["Processor fee"]), d(r["Net deposited"])
            if s + rt + tp != vol:
                ok = False
                print(f"{r['Week']}: services + retail + tips is {s + rt + tp:,.2f}, card volume says {vol:,.2f}")
            if vol - fee != net:
                ok = False
                print(f"{r['Week']}: volume - fee is {vol - fee:,.2f}, deposit says {net:,.2f}")
            for k, v in (("services", s), ("retail", rt), ("tips", tp), ("volume", vol), ("fee", fee), ("net", net)):
                tot[k] += v
    rate = (tot["fee"] / tot["volume"] * 100) if tot["volume"] else Decimal("0")
    print(f"Card volume {tot['volume']:,.2f}, fees {tot['fee']:,.2f} ({rate:.2f}%), deposited {tot['net']:,.2f}")
    print(f"  of which services {tot['services']:,.2f}, retail {tot['retail']:,.2f}, tips owed to staff {tot['tips']:,.2f}")
    return ok, tot


def check_month(path):
    income = expenses = Decimal("0")
    held = defaultdict(Decimal)
    lines = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            amt = d(r["Amount"])
            lines.append((r["Line"], amt))
            if r["In profit"].strip().lower() == "yes":
                if amt >= 0:
                    income += amt
                else:
                    expenses -= amt
            else:
                held[r["Account"]] += amt
    print(f"Revenue {income:,.2f}, expenses {expenses:,.2f}, profit {income - expenses:,.2f}")
    for acct, bal in held.items():
        print(f"Kept out of profit: {acct} moved {bal:,.2f} this month")
    return held, lines


if __name__ == "__main__":
    dep = sys.argv[1] if len(sys.argv) > 1 else "card-deposits.csv"
    month = sys.argv[2] if len(sys.argv) > 2 else "october-2026-month.csv"
    ok, tot = check_deposits(dep)
    held, lines = check_month(month)
    if held.get("Tips payable", Decimal("0")) != 0:
        ok = False
        print("Tips payable did not net to zero: some card tips were not paid out, or tips were booked as revenue.")
    amounts = dict(lines)
    pairs = [("Card sales, services", "services"), ("Card sales, retail product", "retail"), ("Card tips collected", "tips")]
    for line, key in pairs:
        if line in amounts and amounts[line] != tot[key]:
            ok = False
            print(f"'{line}' is {amounts[line]:,.2f} in the month, {tot[key]:,.2f} in the deposits")
    print("All checks pass." if ok else "Some checks failed; see above.")
    sys.exit(0 if ok else 1)
