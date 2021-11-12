from regexes import *

ERROR = "~~~ INVALID INPUT. PLEASE TRY AGAIN ~~~"

def get_input(optional_text=""):
    return input(optional_text).strip().lower()

def get_selection()->str:
    print("""
  _____               _               _____        _          _____                           _             
 |  __ \             (_)             |  __ \      | |        / ____|                         | |            
 | |__) |   _ ___ ___ _  __ _ _ __   | |  | | __ _| |_ ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _  / | | / __/ __| |/ _` | '_ \  | |  | |/ _` | __/ _ \ | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | | \ \ |_| \__ \__ \ | (_| | | | | | |__| | (_| | ||  __/ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  \_\__,_|___/___/_|\__,_|_| |_| |_____/ \__,_|\__\___|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
""")
    while True:
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Select your date input format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|1| Russian numeric
|2| Russian Cyrillic
|3| English long form""")
        selection = get_input(">>>")
        if selection in ["1", "2", "3", "russian numeric", "russian cyrillic", "english long form"]:
            return selection
        else:
            print(ERROR)

def validate_selection(is_valid=True):

    # input validation differs depending on which option the user chose
    # possibly split this function into seperate ones in the future

    selection = get_selection()
    if selection in ["1", "russian numeric"]:
        while True:
            print("Please enter a Russian date in dd.mm.yyyy")
            user_input = get_input(">>>")

            if user_input == "b": break # testing

            # only checks formatting
            # still need to check for valid date numbers
            search = re.search(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", user_input)
            if not search:
                print(ERROR)
            else:
                return user_input



    if selection in ["2", "russian cyrillic"]:
        raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")

    if selection in ["3", "english long form"]:
        raise NotImplementedError("Woops! Feature not implemented yet. Check back later!")







def main():
    validate_selection()
    # regexes will apply here
    pass



if __name__ == "__main__":
    main()