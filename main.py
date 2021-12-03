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

def get_selection()->str:
    """
    prompts user for input format selection
    :return selection: user selection
    """
    choices = [art1, art2, art3]
    print(random.choice(choices))
    while True:
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select your date input format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|1| Russian numeric
|2| Russian Cyrillic
|3| English long form""")
        selection = get_input()
        if selection in ["1", "2", "3", "russian numeric", "russian cyrillic", "english long form"]:
            return selection
        else:
            print(ERROR)

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
    if len(year) not in [3,4]:
        return False
    if month in month_exceptions and int(day) > 30 or \
                   month == "02" and int(day) > 28 or \
                   int(month) > 12 or int(day) > 31:
        return False
    else:
        return True

# input validation differs depending on which option the user chose
# probably split this function into seperate ones in the future

def process_selection(selection:str)->list:
    """wont add docstrings yet since function will probably be split up"""
    if selection in ["1", "russian numeric"]:
        while True:
            print("Please enter a Russian date in dd.mm.yyyy format.")
            user_input = get_input()

            if not re.search(r"(\d\d)\.(\d\d)\.(\d\d\d)", user_input):
                print(ERROR)
            else:
                split_date = user_input.split(".")
                if not validate_date(split_date):
                    print(ERROR)
                else:
                    return split_date

    if selection in ["2", "russian cyrillic"]:
        raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")

    if selection in ["3", "english long form"]:
        raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")


def main():
    selection = get_selection()
    date_list = process_selection(selection)

    day = decline_day(date_list[0])
    month = decline_month(date_list[1])
    year = decline_year(date_list[2])

    print(f"""
DAY: {day}
MONTH: {month}
YEAR: {year}
TRANSLITERATION: {transliterate_cyr(day + " " + month + " " + year)}""")




if __name__ == "__main__":
    main()
