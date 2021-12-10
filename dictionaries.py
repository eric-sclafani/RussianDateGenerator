import csv

def create_dict(csv_file:str, option:str)->dict:
    the_dict = {}
    with open(csv_file, "r") as fin:
        reader = csv.reader(fin)
        if option == "numerals":
            for row in reader:
                the_dict[row[0]] = {"card": str(row[1]), "ord": str(row[2])}

        elif option == "months":
            for row in reader:
                the_dict[row[0]] = {"cyr": row[1], "eng": row[2]}

        elif option == "english_nums":
            for row in reader:
                the_dict[row[0]] = {"card": str(row[3]), "ord": str(row[4])}

        elif option == "cyrillic_days":
            i = 0
            for row in reader:
                i += 1
                the_dict[row[2]] = row[4]
                if i == 31:
                    break

        elif option == "cyrillic_months":
            for row in reader:
                the_dict[row[1]] = {"eng": row[2], "num": row[0]}

        elif option == "cyrillic_numyear":
            for row in reader:
                the_dict[row[2]] = row[0]

        elif option == "englishmonths":
            for row in reader:
                the_dict[row[2]] = {"cyr":row[1], "num": row[0]}

        elif option == "cardnums":
            for row in reader:
                the_dict[row[4]] = {"cyr": row[2], "num": row[0]}

    return the_dict

# used in input option 1
num_to_cyrillic_dict = create_dict("RussianNumerals.csv", "numerals")
num_to_month_dict = create_dict("RussianMonths.csv", "months")
english_nums_dict = create_dict("RussianNumerals.csv", "english_nums")

# used in input option 2
cyrillic_to_cardinalday = create_dict("RussianNumerals.csv", "cyrillic_days")
cyrillic_to_month = create_dict("RussianMonths.csv", "cyrillic_months")
cyrillic_to_num = create_dict("RussianNumerals.csv", "cyrillic_numyear")

# used in input option 3
english_months = create_dict("RussianMonths.csv", "englishmonths")
cardnums = create_dict("RussianNumerals.csv", "cardnums")