# Russian Date Generator

Linguistics Report: 
  Russian dates work a little differently than English dates. First, the day, month and year are not separated by "/" but rather with ".". In Russian, days always come before month and year. This has to do with the structure of how dates are formed in Russian. When referring to a specific day of a month, the day is in ordinal form, which in Russian acts like an adjective. That is, it declines like adjectives do. The day is in prepositional case followed by the specific month. Because we are indicating a day of a specific month, the month is in genitive case, as it is the possessor of the day. Finally, while in English we can refer to the year 2021 as "twenty twenty-one", in Russian this is not possible. Years are always referred to in full numeral form. So, in English it would be "two thousand twenty first year" and the Russian translation would be "две тысячи двадцать первого года." In Russian, when referring to the year, the numeral form of it will always be followed by the russian word for year, "год." So, if we wanted to put all these ideas together to give a Russian date, as we do in our project, then March 31st, 1997 would be input would be 31.03.1997 and the Russian translation would be "тридцать первое марта тысяча девятьсот девяносто седьмого года."
  
    Now, since we are 







# List of files:
- `main.py` = our main file. Pulls all of our regex functions and look-up dictionaries. 
- `dictionaries.py` = the file containing all the dictinaries required for the look-ups.
- `regexes.py` = the file containing all of our regular expressions and declining/undeclining functions.
- `ascii_arts.py` = the file containing ascii arts randomly selected in main.py
- `RussianMonths.csv` = csv containing the twelve months in Cyrillic and English, along with their numerals.
- `RussianNumerals.csv` = csv containing numbers and their written out forms in English and Cyrillic (both ordinal and cardinal Cyrillic forms)



# External libraries:
- None

# Code layout
- Our main philosophy when starting the project was to seperate sections of our code into neat chunks to maintain readability. We stuck with this idea, so our code is layed out like the following:
    
  - `main` acts like the mainframe of our code, the glue that holds it all together.. Before doing any regex detections or substitutions, the user's input is validated depending on which input option they choose.
After validation, regular expression functions from `regexes.py` are applied and make the necessary detections / substitutions / deletions.


# How to run the code

# Design decisions

# Linguistics

# What worked and what didn't?

# Future improvements