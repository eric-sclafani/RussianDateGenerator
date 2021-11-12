


def get_selection():
    """"""
    while True:
        print("""
Select your date input format:
1. Russian numeric
2. Russian Cyrillic
3. English long form""")
        selection = input(">>>")
        if selection.lower().strip() in ["1", "2", "3", "russian numeric", "russian cyrillic", "english long form"]:
            return selection
        else:
            print("Input not recognized. Try again.")

get_selection()

# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()