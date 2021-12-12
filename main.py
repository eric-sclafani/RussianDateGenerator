from ascii_arts import *
from regexes import *
import random

ERROR = "~~~ INVALID INPUT. PLEASE TRY AGAIN ~~~"

def get_input()->str:
    """
    retrieves user input and adds visual >>>
    :return: user input
    """
    return input(">>> ").strip()


def display_options()-> None:
    """
    displays options for the user
    :return: None
    """
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select your date input format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|1| Russian numeric
|2| Russian Cyrillic
|3| English long form
|4| Julian to Gregorian Calendar""")


def display_dates(option,date_list:list, day="", month="", year="")-> None:
    """
    displays the dates depending on which input option the user chose
    :param option: which code block to execute
    :param date_list: numeral date in list form ([day, month, year]) for easy dictionary look up
    :param day: Cyrillic day
    :param month: Cyrillic month
    :param year: Cyrillic year
    :return: None
    """

# INPUT OPTION 1 PRINTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if option == "1":

        print("~" * 60)
        # prints cyrillic
        print(f"{day} {month} {year}")

        # prints transliteration
        print(f"""{transliterate_cyr(day + " " + month + " " + year)}""")

        # removes 0's (01-09) from input to be looked up in dicts
        day = re.sub(r"^0", "",date_list[0])
        month = re.sub(r"^0","",date_list[1])

        # prints English translation by looking it up in a dictionary
        print(f"""{num_to_month_dict[month]["eng"]} {english_nums_dict[day]["ord"]}, {date_list[2]}""")
        print("~" * 60)

# INPUT OPTION 2 PRINTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if option == "2":

        print("~" * 60)

        print("Unfortunately, this feature has not been implemented. Refer to the README.md for more details! Type \"back\" to view the other options.")

        print("~" * 60)

# INPUT OPTION 3 PRINTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if option == "3":

        print("~" * 60)

        # print cyrillic
        print(f"{day} {month} {year}")

        # print transliteration
        print(transliterate_cyr(day + " " + month + " " + year))

        # prints numeral form looked up from a dictionary
        print(f"""{cyrillic_to_num[date_list[0]]}.{cyrillic_to_month[date_list[1]]["num"]}.{date_list[-1]}""")
        print("~" * 60)


# INPUT OPTION 4 PRINTING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








def validate_numeral_input(date:list)->bool:
    """
    validates day and month with multiple checks:
         1. months that end on the 30th
         2. valid leap years
         3. feb 28th edgecase
         4. general date checks (month <= 12, day <= 31)
    :param date: date to be evaluated
    :return: True if date is valid False otherwise
    """
    day,month,year = date[0], date[1], date[2]
    month_exceptions = ["04", "4", "06", "6", "09", "9", "11"]

    # checks if year not length 3 or 4
    if len(year) not in [3,4]:
        return False

    # checks to see if feb 29th is allowed (leap years)
    if month in ["02", "2"] and int(day) == 29:
        if re.search(r"00$", year):
            if float(year) % 400 == 0:
                return True

        if float(year) % 4 == 0:
            return True

    # CHECKS FOR: - months ending on the 30th
    #             - month > 12
    #             - day > 31
    #             - February date if not leap year
    if month in month_exceptions and int(day) > 30 or \
                   int(month) > 12 or int(day) > 31 or \
                   int(month) == 2 and int(day) > 28:
        return False
    else:
        return True

def process_selection(user_input:str, option:str)->list:
    """
    processes the user input by validating it and making dictonary look ups when needed.
    :param user_input: direct user input to help with printing some forms
    :param option: which code block to execute
    :return: OPTION 1 = returns the numeral date in [day, month, year] format
             OPTION 2 = None
             OPTION 3 = returns the date in Cyrillic form in [day, month, year] format
    """

# INPUT OPTION 1 PROCESSING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if option == "1":
        if not re.search(r"(\d\d)\.(\d\d)\.(\d\d\d)", user_input):
            print(ERROR)
            return False
        else:
            split_date = user_input.split(".")
            if not validate_numeral_input(split_date):
                print(ERROR)
                return False
            else:
                return split_date

# INPUT OPTION 2 PROCESSING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif option == "2":

        decl_cyrillic_months = ["мая", "января", "февраля", "марта", "апреля", "июля",
                                "августа", "сентября", "октября", "ноября", "декабря"]

        # comments will be moved to the readme
        # difficult to validate cyrillic user input. Days and year strings can be two parts, so need a way to properly find the month:
        # split the user input on space, checks which component is in the list of cyrillic months, set the component equal to the month when found
        # now split user input on the month, which means even if the day or year are two parts, they will still be part of the same token as opposed to being split on space.

        components = user_input.split()


        date = ""
        for component in components:
            if component in decl_cyrillic_months:
                month = component

                # splits the day and year to allow each to have one or two parts.
                date = list(map(lambda x: x.strip(), re.split(rf"{month}", user_input)))
                date.insert(1, month)
                break

        # undeclines each date segment to be looked up in the dicts
        undeclined_date = [undecline_cyrillic(element) for element in date]

        # deprecated


# INPUT OPTION 3 PROCESSING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif option == "3":

        # deletes comma in input and tokenizes english input. EX: ["December", "10th", "2021"]
        date = list(map(lambda x: re.sub(r",", "", x), user_input.split()))

        # check to make sure no letters are in the year
        if not date[-1].isnumeric():
            print(ERROR)
            return False

        try:
            #translates into Cyrillic by pulling the Cyrillic from a dictionary given the cardinal number, and English month. Year is processed differently.
            day = cardnums[date[1]]["cyr"]
            month = english_months[date[0]]["cyr"]
            year = numeral_to_cyrillic(date[2], "year")
            cyrillic_date = [day, month, year]

            numeral_date = [cardnums[date[1]]["num"], english_months[date[0]]["num"], date[2]]

            # validates the date
            if not validate_numeral_input(numeral_date):
                print(ERROR)
                return False

        # to catch any input error not caught by the previous checks
        except LookupError:
            print(ERROR)
            return False

        else:
            cyrillic_date.append(date[2]) # appends the numeral year for easy printing
            return cyrillic_date



def main():
    choices = [art1, art2, art3]
    print(random.choice(choices))
    while True:
        display_options()
        selection = get_input()

        if selection in ["1", "2", "3", "russian numeric", "russian cyrillic", "english long form", "cyr", "eng", "num"]:
            print("~" * 60)
            print("Type \" back\" to revisit the options menu.")
            print("Type \" exit\" to exit the program.")
            print("~" * 60)

            while True:

# USER SELECTS INPUT OPTION 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if selection in ["1", "russian numeric", "num"]:
                    print("\nPlease enter a Russian date in dd.mm.yyyy format.\n")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    date_list = process_selection(user_input, "1")

                    # if validation is successful, declines the Cyrillic form and ships it for printing
                    if date_list:
                        day = decline_day(date_list[0])
                        month = decline_month(date_list[1])
                        year = decline_year(date_list[2])
                        display_dates("1",date_list, day, month, year)

# USER SELECTS INPUT OPTION 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if selection in ["2", "russian cyrillic", "cyr"]:
                    print("\nPlease enter a date in Cyrillic\n")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    display_dates("2", [])

# USER SELECTS INPUT OPTION 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                if selection in ["3", "english long form", "eng"]:
                    print("\nPlease enter a date in English of the format: Month XXth, XXXX")
                    user_input = get_input()

                    if user_input == "back":
                        break

                    elif user_input == "exit":
                        exit()

                    date_list = process_selection(user_input,"3")

                    if date_list:

                        day = decline_day(date_list[0])
                        month = decline_month(date_list[1])
                        year = decline_year(date_list[2])

                        display_dates("3", date_list, day, month, year)

# USER SELECTS INPUT OPTION 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




        elif selection == "exit":
            exit()
        else:
            print(ERROR)

if __name__ == "__main__":
    main()
