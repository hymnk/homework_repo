import csv

list1 = [["トップガン", "Risky Business","Minority Report"],
        ["タイタニック", "The Revenant", "Inception"],
        ["Training Day", "Man of Fire", "Flight"]]

print(list1)

with open("output2.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list1)

