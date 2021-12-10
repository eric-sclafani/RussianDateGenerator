# Russian Date Generator








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

The regexes.py file contains all of the regular expressions we used in our project. The first function in the file is called parse_year(year). This function takes a numeral year string as the input and deconstructs it into components to be translated into Cyrillic. For example, if you inputed the year "1999", then the function would deconstruct it into ["1000", "900", "90", "9"]. The functions makes sure that if it detects any string of 0s that is in the list ["000", "00", "0"] that it does not include it in the output as there is no equivalent word in the Russian Cyrillic output. For example, if the input was "2000" then the output would be ["2000"] not ["2000", "000", "00", "0"]. It also takes into account the error that would occur if we followed this process with the numbers between 11-19. If the function detects a number in this range in the ending of the year, it makes sure to keep it as that in the list. For example, if the input was "2115", then the output is ["2000", "100", "15"] not ["2000", "1000", "10", "5"], as this would give the incorrect form of the date once it has been translated to Cyrillic.

The next function in the file is the numeral_to_cyrillic(numeral, option) function. This function takes the 

The decline_day(day) function takes a string that contains the Russian form of the day in nominative case as the input and outputs the day in prepositional case. This is done using re.sub. If the function detects "-ый" or "-ой" at the end of the string, then it replaces it with "-ое". This function also accounts for the irregular form of the ordinal form of three. If the function detects "третий" at the end of the string, it replaces it with the prepositional form of three, "третье". This function returns day.

The underline_day(day) function is needed in the second option in the main file. When the user inputs the Cyrillic long form of the date it is in its proper form, declensions and all. Therefore, in order to retrieve the right thing from the CSVs, the input needs to be underlined. This function searches the day string for the adjective endings in prepositional case, and declines them back into nominative masculine singular. This function's regexes are a little more specified than the decline_day function because it has to account for how despite some numbers having the same ending in prepositional case, they are different in nominative case.

The decline_month function works similarly to the decline day function. It takes the month string in nominative case as the input and outputs the month in genitive case. This is done through re.sub. If the function detects a specific ending, it will replace it with its corresponding genitive ending. For how these endings change, please refer to the linguistics section of the README.md file.

The undecline_month function takes the Cyrillic input in its correct form, genitive case, and changes it back to nominative in order to find the month in its numeral form in the CSVs. Since most of the months have the same endings in genitive case, we decided that it was easiest to simply write a re.sub expression for each of the twelve months.

The decline_year(year) function takes the year string in nominative case and outputs it in genitive case. It detects the adjective ending of the ordinal form of the last number in the year and replaces the nominative ending with genitive. For how this is done, please refer to the linguistics section of the README.md file. This function also adds the Russian word for year, "год" onto the end of the year string and declines "год" into genitive case by appending "-а" onto the end of it using an re.sub expression.

The underline_year(year) function takes the year in genitive case and outputs it in nominative case. Using regular expressions, the function detects the genitive masculine singular endings and replaces them with their nominative equivalents. Because the genitive masculine singular ending is the same for different nominative masculine singular endings, the regular expressions had to be a little more specific than their decline_year function equivalents. Therefore, more regular expressions were written to account for the correct forms needed. This function also uses regular expressions to replace the genitive form of year "года" with an empty string as it is no longer needed.

The undecline_cyrillic(date) function takes the correct form of a Russian date in Cyrillic and returns the date with all of its parts in nominative case, this is needed for option 2 in main. The function calls on the undecline_day, undecline_month, and undecline_year functions and returns a stripped version of the string once it has finished.

The transliterate_cyr function takes the correct form of a Russian cyrillic date and transliterates it into the Roman alphabet. This is done through a long serious of re.sub expressions. Every time the function detects an instance of a specified Russian character, it replaces it with its specified roman equivalent. This function contains regexes for the entire Russian alphabet, for both upper and lower cases. The function returns the transliterated version of the Russian cyrillic input.

The gregorian_cal function takes a list of numbers that corresponds to a date in the Julian calendar and outputs a list of numbers that corresponds to the input date converted to the Gregorian calendar. The list is in the order [day, month, year]. This function uses if statements to make sure the correct and validate date is outputted once the correct number of dates has been added onto the Julian date to convert it to the Gregorian calendar. First, the function takes into account whether the year in the list is greater than or equal to 2100, as the difference between the Julian and Gregorian calendars increases from 13 days to 14 days. It takes into account leap years, as well as if adding 13 or 14 days to the date causes a change in month. If the day exceeds the number of days in the specified month, then 1 is added to the numeral form of the month and the day is set equal to 13 (or 14) minus (the number of days in the month minus the inputted day). If the month is "12" the function also takes into account if the day plus 13 (or 14) days exceeds 31. If that occurs, then the month is changed to "01", 1 is added to the year, and the day is 13 (or 14) minus (31 minus the inputted day). The function returns a list of numbers in the order [day, month, year] that corresponds to a date in the Gregorian calendar.



# Linguistics

	Russian dates work a little differently than English dates. First, the day, month and year are not separated by "/" but rather with ".". In Russian, days always come before month and year. This has to do with the structure of how dates are formed in Russian. When referring to a specific day of a month, the day is in ordinal form, which in Russian acts like an adjective. That is, it declines like adjectives do. The day is in prepositional case followed by the specific month. Because we are indicating a day of a specific month, the month is in genitive case, as it is the possessor of the day. Finally, while in English we can refer to the year 2021 as "twenty twenty-one", in Russian this is not possible. Years are always referred to in full numeral form. So, in English it would be "two thousand twenty first year" and the Russian translation would be "две тысячи двадцать первый год." In Russian, when referring to the year, the numeral form of it will always be followed by the Russian word for year, "год." Now, because we are referring to a specific year, the year can be thought of as the possessor of the day and month; therefore, the year must be in genitive case. Hence, "две тысячи двадцать первый год" becomes "две тысячи двадцать первого года." So, if we wanted to put all these ideas together to give a Russian date, as we do in our project, then March 31st, 1997 would be input would be 31.03.1997 and the Russian translation would be "тридцать первое марта тысяча девятьсот девяносто седьмого года."
  

    Now, since we are discussing declining ordinal forms and months into different cases, it is important to know how this works in Russian. So, beginning with the day, as stated above ordinal forms of numbers act like adjectives. They have the same endings as adjectives do in Russian, so all the ordinal forms of the numbers with end with either "-ый" or "-ий" or "-ой", the masculine singular nominative endings of adjectives. Now, to decline an adjective from nominative case to prepositional case, we take off the adjective ending and replace it with "-ое", the masculine singular prepositional adjective ending. Declining the year into genitive case works the same way, we take the last number of the year, which should be an ordinal number ending in "-ый", "-ий", or "-ой". So, we take off the adjective ending and replace it with the genitive masculine singular ending "-ого". Now, this is obviously a very simplified version of Russian adjective declension, and there are some exceptions to this, for example with the ordinal form of three. The nominative masculine singular ordinal form of three is "третий", the prepositional masculine singular form of three is "третье" and the genitive masculine singular form is "третего." 


	Russian months are nouns that can be declined into different cases much like adjectives. However, for the purposes of this project we are only concerned with the genitive case as it pertains to months and the Russian word for year "год." If an adjective ends in a consonant, then "-а" is appended onto the end. So, "год" becomes "года" in genitive singular. If a noun is masculine and ends in the soft sign "-ь" then the "-ь" is deleted and replaced with "-я". If a noun ends in "-й", then "-й" is deleted and replaced with "-я". Since all of the nouns that are used in this project are masculine and singular we do not need to be concerned with feminine, neuter or plural declensions for the genitive or any other case.

Another part of our project has to do with the Julian calendar. The Julian calendar is currently 13 days behind the Gregorian. In 2100, this difference will increase to 14 days. Before the October Revolution and the start of the Soviet Union, the Russian Empire used the Julian calendar instead of the Gregorian calendar that is commonly used today. Because of this, most important days in Russian history, such as the October Revolution actually have two dates listed, one in the Julian calendar and one in the Gregorian calendar. Therefore, we thought that it would be interesting to have an option in our project to convert a day in the Julian calendar to its Gregorian equivalent. As the Julian calendar is not used today, we felt that it was more important to be able to convert from Julian to Gregorian as it would be more applicable in the case of Russian dates, as most Russian history books refer to important dates before 1918 in the Julian calendar.


# What worked and what didn't?

# Future improvements


десятое марта двухтысячного года

четырнадцатое декабря тысяча девятьсот девяносто первого года

тридцать первое апреля две тысячи четвёртого года

двадцать девятое февраля две тысячи двадцатого года

двадцать девятое февраля тысяча девятьсот девяносто первого года

шестнадцатое октября две тысячи первого года