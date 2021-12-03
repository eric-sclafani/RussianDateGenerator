import csv

def create_dict(csv_file:str, option:str)->dict:
    the_dict = {}
    with open(csv_file, "r") as fin:
        reader = csv.reader(fin)
        if option == "numerals":
            for row in reader:
                the_dict[row[0]] = {"card": str(row[1]), "ord": str(row[2])}

        if option == "months":
            for row in reader:
                # the_dict[row[0]] = row[1]
                the_dict[row[0]] = {"cyr": row[1], "eng": row[2]}

        if option == "english_nums":
            for row in reader:
                the_dict[row[0]] = {"card": str(row[3]), "ord": str(row[4])}



    return the_dict

num_dict = create_dict("RussianNumerals.csv", "numerals")
month_dict = create_dict("RussianMonths.csv", "months")
english_nums_dict = create_dict("RussianNumerals.csv", "english_nums")
