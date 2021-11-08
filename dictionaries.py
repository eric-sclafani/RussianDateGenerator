import csv

num_dict = {}
with open("RussianNumerals .csv", "r") as fin:
    reader = csv.reader(fin)
    for row in reader:
        num_dict[row[0]] = {"card": row[1], "ord": row[2]}

print(num_dict)