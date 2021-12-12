# List of files:
- `main.py` = our main file. Pulls all of our regex functions and look-up dictionaries. 
- `dictionaries.py` = the file containing all the dictinaries required for the look-ups.
- `regexes.py` = the file containing all of our regular expressions and declining/undeclining functions.
- `ascii_arts.py` = the file containing ascii arts randomly selected in main.py
- `RussianMonths.csv` = csv containing the twelve months in Cyrillic and English, along with their numerals.
- `RussianNumerals.csv` = csv containing numbers and their written out forms in English and Cyrillic (both ordinal and cardinal Cyrillic forms)



# External libraries:
- csv
- re
- random

# Code layout and file interaction
Our main philosophy when starting the project was to seperate sections of our code into neat chunks to maintain readability. We stuck with this idea, so our code is layed out like the following:

`main.py` acts like the mainframe of our code, the glue that holds it all together. Before doing any regex detections or substitutions, **the user's input is validated depending on which input option they choose**.
After validation, regular expression functions from `regexes.py` are applied and **make the necessary detections / substitutions / deletions**. 

The main role `regexes.py` plays is **two fold**: to detect the Russian Cyrillic and make the proper changes (declining / undeclining),
and to properly convert numerals **into** Cyrillic. This conversion is possible because the correct forms are pulled directly from the dictionaries in `dictinaries.py`created from the two
`.csv` files (`RussianNumerals.csv` and `RussianMonths.csv`). Without the help of these files, we would have probably had to write
triple the amount of regular expressions.

The main role of `dictionaries.py` is to store our .csv data into an easily accessible format. The _create_dict_ function is the script that does so. 

Like previously mentioned, our two `.csv` files provide us with all of the Russian, English, and numeral forms we need for our program to work correctly.

# Linguistics

Russian dates work differently than in English:
First, the **day**, **month** and **year** are not separated by " / " but  with " . ". 
In Russian, **days always come before month and year**. When referring to a specific day of a month, the day is in **ordinal** form, which in Russian acts like an adjective. 
That is, it **declines** like adjectives do. The day is in prepositional case followed by the specific month.
Because we are indicating a day of a specific month, the **month is in genitive case**.

While in English we refer to the year 2021 as "twenty twenty-one", in Russian this is not possible. **Years** are always referred to in full numeral form. So, in English it would be: 
    
    two thousand twenty first year

and the Russian translation would be 

    две тысячи двадцать первый год.
With years in Russian, the numeral form of the year is always followed by the Russian word for year, **"год."** Because we are referring to a specific year, 
the year can be thought of as the possessor of the day and month; therefore, **the year must be in genitive case**.  

When it comes to declining the day and year, this is how it works: 
    
    Beginning with the day, as stated above ordinal forms of numbers act like adjectives. 
    They have the same endings as adjectives do in Russian, so all the ordinal forms of the numbers 
    end with either "-ый" , "-ий" or "-ой". 

    Now, to decline an adjective from nominative to prepositional, 
    we take off the adjective ending and replace it with "-ое", 
    the masculine singular prepositional adjective ending. 

    Declining the year into genitive case works the same way in that we take 
    the last number of the year, which should be an ordinal number ending in "-ый", "-ий", or "-ой".
    We take off the adjective ending and replace it with the genitive masculine singular ending "-ого".
    
    Now, this is obviously a very simplified version of Russian adjective declension, and there are
    some exceptions to this, for example with the ordinal form of three. 
    The nominative masculine singular ordinal form of three is "третий", 
    the prepositional masculine singular form of three is "третье" and the 
    genitive masculine singular form is "третего." 


**Russian months** can also be **declined** in the same way as adjectives:

    If an adjective **ends in a consonant**, then "-а" is appended onto the end. 
    So, "год" , which means "year", becomes "года" in genitive singular. 
    
    If a noun is masculine and ends in the soft sign "-ь" then the "-ь" is deleted and replaced with "-я". 
    
    If a noun ends in "-й", then "-й" is deleted and replaced with "-я". 

Since all of the nouns that are used in this project are masculine and singular we do not need to be concerned with feminine, neuter or plural declensions for the genitive or any other case.

# How to run the code

To run the code, run the `main.py` file. Because of the awesome ascii arts, we recommend running it in fullscreen for the arts to display properly.
When the user is prompted with the seletion screen, they have the choice of selection one of three different forms of input. 

# Design 

## main.py

### get_input() 
- receives user input

### display_options()
- displays the options for the user to choose from

### display_dates
- prints the program's output depending on which input option the user selects. 

### validate_numeral_input()
- performs multiple checks using base Python on regular expressions. Checks if the given numeral date is valid.

### process_selection()
- processes the user input depending on which input it is. This includes validating it and then doing some necessay dictionary look ups.


## Regexes.py

### parse_year()
- takes a numeral string and deconstructs it into components to be translated into Cyrillic. 

- EX: **"1999"** becomes **["1000", "900", "90", "9"]**. 

- The function also prevents 0's from entering the list. EX:**"2000"** becomes **["2000"]** not ["2000", "000", "00", "0"].
- Numbers 11-19 are special cases and do not get broken down. Instead, they get pulled from a dictionary.
- Handles year if length 3 and 4 separately.
 
### numeral_to_cyrillic( )
- **Takes a numeral and converts it into Cyrillic** by pulling the Cyrillic form from the corresponding dictionary.
- If the year needs to be translated, it uses _parse_year()_ to descontruct it. 
- After pulling each segment from a dict, **concatenates them into a single string** and returns it.

### Decline functions:

- All of our decline functions use **regular expressions** to make the necessary substitutions. We found this to be the most sensical option.

#### decline_day()
- Takes the day in **Cyillic nominative case** and outputs the **declined** form (**propositional case**)

- **"-ый"** or **"-ой"** change into **"-ое"** word finally. 

- The ending of the irregular form of "three" is also accounted for. **"третий"** changes to the prepositional form **"третье"**.

#### decline_month()

- Takes the month in **Cyillic nominative case** and outputs the declined form (**genitive case**)

- "**ь**" and **"й"** change to **"я"**, **""т"** changes to **"та"**, word finally

#### decline_year()
- Takes the year in **Cyrillic nominative case** and outputs the declined form (**genitive case**)
- Adds the Russian word for year, **"год"** word finally declines it into **"годa"**


### Undecline functions: undecline_day, undecline_month, undecline_year

- These functions would have been used to process the **Cyrillic user input** (see the _result_ section below as to why this input form is not included here). They would have operated in the exact opposite
fashion as the above decline functions by changing the **day** from **prepositional to nominative**, **month** from **genitive to nominitive**, and 
**year** from **genitive** to **nominitive**. 
- The functions are still included in the code to show partly what we had in mind when thinking about how to process the Cyrillic input.

### transliterate_cyr()
- Transliterates a given **Cyrillic form** for printing.
- This function contains regexes for the entire Russian alphabet, for both upper and lower cases.

## gregorian_cal()
- takes a list of numbers that corresponds to a date in the Julian calendar and outputs a list of numbers that corresponds to the input date converted to the Gregorian calendar.
- First, the function takes into account whether the year in the list is greater than or equal to 2100 because the difference between the Julian and Gregorian calendars increases from 13 days to 14 days
- If the day exceeds the number of days in the specified month, then 1 is added to the numeral form of the month and the day is set equal to 13
- If the day exceeds the number of days in the specified month, then 1 is added to the numeral form of the month and the day is set equal to 13



Another part of our project has to do with the Julian calendar. The Julian calendar is currently 13 days behind the Gregorian. In 2100, this difference will increase to 14 days. Before the October Revolution and the start of the Soviet Union, the Russian Empire used the Julian calendar instead of the Gregorian calendar that is commonly used today. Because of this, most important days in Russian history, such as the October Revolution actually have two dates listed, one in the Julian calendar and one in the Gregorian calendar. Therefore, we thought that it would be interesting to have an option in our project to convert a day in the Julian calendar to its Gregorian equivalent. As the Julian calendar is not used today, we felt that it was more important to be able to convert from Julian to Gregorian as it would be more applicable in the case of Russian dates, as most Russian history books refer to important dates before 1918 in the Julian calendar.

## dictionaries.py

### create_dict()
- creates a dictionary consisting of the data from the csv files. The arguments dictate what the key:value pairs are.


## Result

### What worked?

We are happy to say that the input options of "Russian numeric date", "English date", and "Julian date" work flawlessly (to our knowledge).
That is, they account for leap years, months that end on the 30th vs 31st, and correctly achieve the desired output. 



### What didn't?

Originally, we wanted the second input option to let the user input Cyrillic and the program would output the transliteration, English
date, and Russian format numeral date. 


However, this task was much more difficult to complete than the other input options.
This is because when the user enters the Russian numeric date or English date, they are directly providing the program
with the year in numeral form, which is relatively simple to break down and look up in our dictionaries. 

When the user would enter the Cyrillic form,
however, that lookup was no longer possible. Because of how years are formed in Russian. it was very difficult to extract numbers given the Cyrillic year 
(since the year can consist of many components). We tried many methods, one such was using bigrams to check for groups of year components, but no dice. Retrieving the month
and day was simple, but the year made it very difficult

It is very unfortunate that we couldn't get that input option to work. I'm sure if we spent more time on it, we could have thought of the complex solution
something like this requires. But because this was just one part of our project, we decided to shift our attention to polish the 
parts that do work correctly and make sure they are fool proof.

The code that would have been used for handling the Cyrillic input is still included in the source code, however. It exists to give an idea as to how
we were approaching the problem.




## Future improvements
- For the program to tell the user exactly what goes wrong when an error occurs.
- Get the Cyrillic input option to work correctly.
- Format the program output to look prettier

