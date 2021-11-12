import csv

def create_dict(csv_file:str, option:str)->dict:
    the_dict = {}
    with open(csv_file, "r") as fin:
        reader = csv.reader(fin)
        if option == "numerals":
            for row in reader:
                the_dict[row[0]] = {"card": row[1], "ord": row[2]}

        if option == "months":
            for row in reader:
                the_dict[row[0]] = row[1]
    return the_dict

num_dict = create_dict("RussianNumerals.csv", "numerals")
month_dict = create_dict("RussianMonths.csv", "months")