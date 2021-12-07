from ascii_arts import *
from regexes import *
import random

ERROR = "~~~ INVALID INPUT. PLEASE TRY AGAIN ~~~"

def get_input()->str:
    """
    retrieves user input and adds visual >>>
    :return: user input
    """
    return input(">>>").strip()

def display_options()->str:
    """
    displays options for the user
    :return: None
    """
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select your date input format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|1| Russian numeric
|2| Russian Cyrillic
|3| English long form""")

def display_dates(day:str, month:str, year:str, date_list:list):
    """WIP"""
    print(f"""
{day} {month} {year}
{transliterate_cyr(day + " " + month + " " + year)}
\"{month_dict[date_list[1]]["eng"].title()} {english_nums_dict[date_list[0]]["ord"]}, {date_list[2]}\"""")

# input validation differs depending on which option the user chose
# probably split this function into seperate ones in the future

def validate_date(date:list)->bool:
    """
    validates day and month with three checks:
         1. months that end on the 30th
         2. feb 28th edgecase
         3. general date checks (month <= 12, day <= 31)
    :param date: date to be evaluated
    :return: True if date is valid False otherwise
    """
    day,month,year = date[0], date[1], date[2]
    month_exceptions = ["04", "06", "09", "11"]

    # checks if year not length 3 or 4
    if len(year) not in [3,4]:
        return False

    # checks to see if feb 29th is allowed (leap years)
    if month == "02" and int(day) == 29:
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

def process_selection(user_input:str)->list:
    """wont add docstrings yet since function will probably be split up"""
    if not re.search(r"(\d\d)\.(\d\d)\.(\d\d\d)", user_input):
        print(ERROR)
        return False
    else:
        split_date = user_input.split(".")
        if not validate_date(split_date):
            print(ERROR)
            return False
        else:
            return split_date


def main():
    choices = [art1, art2, art3]
    print(random.choice(choices))

    while True:
        display_options()
        selection = get_input()
        if selection in ["1", "2", "3", "russian numeric", "russian cyrillic", "english long form"]:
            print("Type \" back\" to revisit the options menu.")
            print("Type \" exit\" to exit the program.")
            while True:

                # user selects russian numeric date
                if selection in ["1", "russian numeric"]:
                        print("\nPlease enter a Russian date in dd.mm.yyyy format.\n")

                        user_input = get_input()
                        if user_input == "back":
                            break

                        elif user_input == "exit":
                            exit()

                        date_list = process_selection(user_input)
                        if date_list:
                            day = decline_day(date_list[0])
                            month = decline_month(date_list[1])
                            year = decline_year(date_list[2])
                            display_dates(day, month, year, date_list)


                if selection in ["2", "russian cyrillic"]:
                    raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")

                if selection in ["3", "english long form"]:
                    raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")



        elif selection == "exit":
            exit()
        else:
            print(ERROR)








if __name__ == "__main__":
    main()
