import csv

list1 = [["Top Gun", "Risky Business","Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man of Fire", "Flight"]]

print(list1)

with open("output.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list1)

