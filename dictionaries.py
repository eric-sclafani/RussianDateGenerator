import csv

def create_dict(csv_file:str, option:str)->dict:
    """
    creates a dictionary based on specified csv file and whatever type of dictionary is needed
    :param csv_file: file to extract data from
    :param option: what type of key:value pairs are needed.
    :return: dictionary with specified key:value pairs from information taken from specified csv
    """
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

        elif option == "cyrillic_nums":
            for row in reader:
                the_dict[row[2]] = {"num":row[0], "card": row[4]}

        elif option == "englishmonths":
            for row in reader:
                the_dict[row[2]] = {"cyr":row[1], "num": row[0]}

        elif option == "cardnums":
            for row in reader:
                the_dict[row[4]] = {"cyr": row[2], "num": row[0]}

    return the_dict

# used in input option 1
num_to_cyrillic_dict = create_dict("RussianNumerals.csv", "numerals")
# {1: {"card":cyillic_cardinal_form, "ord": cyrillic_ordinal_form},
#  2:...}

num_to_month_dict = create_dict("RussianMonths.csv", "months")
# {1:{"cyr": cyrillic_month, "eng": english_month},
#  2...}

english_nums_dict = create_dict("RussianNumerals.csv", "english_nums")
# {1: {"card": eng_card_form, "ord": eng_ord_form},
#  2:...}

# would have been used in input option 2
cyrillic_to_cardinalday = create_dict("RussianNumerals.csv", "cyrillic_days")
cyrillic_to_month = create_dict("RussianMonths.csv", "cyrillic_months")
cyrillic_to_num = create_dict("RussianNumerals.csv", "cyrillic_nums")

# used in input option 3
english_months = create_dict("RussianMonths.csv", "englishmonths")
# {eng_month:{"cyr": cyrillic_month, "num": numeral},
#  eng_month...}

cardnums = create_dict("RussianNumerals.csv", "cardnums")
# {card_num: {"cyr": cyrillic_form, "num": numeral_form},
#  card_num...}