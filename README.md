# Russian Date Generator


## List of files:
- `main.py` = our main file. Pulls all of our regex functions and look-up dictionaries. 
- `dictionaries.py` = the file containing all the dictinaries required for the look-ups.
- `regexes.py` = the file containing all of our regular expressions and declining/undeclining functions.
- `ascii_arts.py` = the file containing ascii arts randomly selected in main.py
- `RussianMonths.csv` = csv containing the twelve months in Cyrillic and English, along with their numerals.
- `RussianNumerals.csv` = csv containing numbers and their written out forms in English and Cyrillic (both ordinal and cardinal Cyrillic forms)



## External libraries:
- re
- random

## Code layout and file interaction
Our main philosophy when starting the project was to seperate sections of our code into neat chunks to maintain readability. We stuck with this idea, so our code is layed out like the following:

`main.py` acts like the mainframe of our code, the glue that holds it all together. Before doing any regex detections or substitutions, **the user's input is validated depending on which input option they choose**.
After validation, regular expression functions from `regexes.py` are applied and **make the necessary detections / substitutions / deletions**. 

The main role `regexes.py` plays is **two fold**: to detect the Russian Cyrillic and make the proper changes (declining / undeclining),
and to properly convert numerals **into** Cyrillic. This conversion is possible because the correct forms are pulled directly from the dictionaries in `dictinaries.py`created from the two
`.csv` files (`RussianNumerals.csv` and `RussianMonths.csv`). Without the help of these files, we would have probably had to write
triple the amount of regular expressions.

The main role of `dictionaries.py` is to store our .csv data into an easily accessible format. The _create_dict_ function is the script that does so. 

Like previously mentioned, our two `.csv` files provide us with all of the Russian, English, and numeral forms we need for our program to work correctly.

## Linguistics

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

## How to run the code

To run the code, run the `main.py` file. Because of the awesome ascii arts, we recommend running it in fullscreen for the arts to display properly.
When the user is prompted with the seletion screen, they have the choice of selection one of three different forms of input. 

## Design decisions



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




## Future improvements
- For the program to tell the user exactly what goes wrong when an error occurs.
- Get the Cyrillic input option to work correctly.
- Format the program output to look prettier

