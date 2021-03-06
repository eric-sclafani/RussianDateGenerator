from dictionaries import *
import re


def parse_year(year: str) -> list:
    """
    deconstructs a numeral year into components to be translated into cyrillic
    :param year: string year to be broken down
    :return: list of year components
    """

    # if the year a digit followed by 3 or 4 zeros. (EX: 2000 or 300) Gets printed as the ordinal form instead of cardinal
    if re.search(r"^\d000?", year):
        return num_to_cyrillic_dict[year]["ord"] # returns the cyrillic form straight from num_dict

    # break up the year into its components
    # if year is length 4
    if len(year) == 4:

        # if last two digits are 11-19, gets pulled directly from num_dict instead of deconstructed (linguistic exceptions)
        if re.search(r"1[1-9]$", year):
            components = [year[0] + "000", year[1] + "00", year[2] + year[3]] # EX: 2011-2019
        else:
            components = [year[0] + "000", year[1] + "00", year[2] + "0", year[3]]

    # if year is length 3
    else:
        if re.search(r"1[1-9]$", year):
            components = [year[0] + "00", year[1] + year[2]]
        else:
            components = [year[0] + "00", year[1] + "0", year[2]]

    # filter out 0 numbers created by the above list to avoid key errors
    return [component for component in components if component not in ["000", "00", "0"]]

def numeral_to_cyrillic(numeral:str, option)->str:
    """
    converts numerals into Cyrillic
    :param numeral: numeral to be converted
    :param option: which code block to execute
    :return: numeral in Cyrillic form
    """

    # delete 0 from single number inputs to avoid key errors
    single_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if numeral in single_nums:
        numeral = re.sub(r"0", "", numeral)

    # day processing
    # pulls the ordinal form from a dict
    if option == "day":
        return re.sub(rf"{numeral}", num_to_cyrillic_dict[numeral]["ord"], numeral)

    # month processing
    # pulls the Cyrillic month from a dict
    if option == "month":
        return re.sub(rf"{numeral}", num_to_month_dict[numeral]["cyr"], numeral)

    # year processing
    if option == "year":
        year = ""
        for component in parse_year(numeral):

            if not component.isnumeric():
                # parse_year returns the cyrillic here instead of a list of numbers, so return it when that happens
                return parse_year(numeral)

            # last number in a year is printed in it's ordinal form.
            if len(component) == 1:
                year += num_to_cyrillic_dict[component]["ord"] + " "
            else:
                # every other number gets its cardinal form
                year += num_to_cyrillic_dict[component]["card"] + " "

        return year.strip()

def decline_day(day:str) -> str:
    """
    declines Russian day from nominitive -> prepositional case
    :param day: last number in date string to be declined
    :return day: day in prepositional case
    """
    day = numeral_to_cyrillic(day, "day")
    day = re.sub(r"????????????$", "????????????", day)
    day = re.sub(r"????$", "????", day)
    day = re.sub(r"????$", "????", day)
    return day

def undecline_day(day: str) -> str:
    """
    declines Russian day from prepositional -> nominative case
    :param day: last number in date string to be declined
    :return day: day in nominative case
    """
    day = re.sub(r"????????????", "????????????", day)
    day = re.sub(r"????????????", "????????????", day)
    day = re.sub(r"??????", "??????", day)
    day = re.sub(r"????????", "????????", day)
    day = re.sub(r"????", "????", day)
    return day
    
def decline_month(month:str) -> str:
    """
    declines Russian month from nomitive -> genitive case
    :param month: month to be declined
    :return month: month in genitive case
    """
    month = numeral_to_cyrillic(month, "month")
    month = re.sub(r"??$", "??", month)
    month = re.sub(r"??$", "??", month)
    month = re.sub(r"??$", "????", month)
    return month

def undecline_month(month: str) -> str:
    """
    declines Russian month from genitive -> nominative case
    :param month: month to be declined
    :return month: month in nominative case
    """
    month = re.sub(r"??????", "??????", month)
    month = re.sub(r"????????????", "????????????", month)
    month = re.sub(r"??????????????", "??????????????", month)
    month = re.sub(r"??????????", "????????", month)
    month = re.sub(r"????????????", "????????????", month)
    month = re.sub(r"????????", "????????", month)
    month = re.sub(r"????????", "????????", month)
    month = re.sub(r"??????????????", "????????????", month)
    month = re.sub(r"????????????????", "????????????????", month)
    month = re.sub(r"??????????????", "??????????????", month)
    month = re.sub(r"????????????", "????????????", month)
    month = re.sub(r"??????????????", "??????????????", month)
    return month
    
def decline_year(year: str) -> str:
    """
    declines Russian year from nominitive -> genitive case
    :param year: last number in year string to be declined
    :return year: year in genitive case
    """

    year = numeral_to_cyrillic(year, "year")

    year = re.sub(r"????????????$", "????????????????", year)
    year = re.sub(r"????$", "??????", year)
    year = re.sub(r"????$", "??????", year)

    year = year + " ??????"
    year= re.sub(r"??????$", "????????", year)
    return year

def undecline_year(year: str) -> str:
    """
    declines Russian year from genitive -> nominative case
    :param year: last number in string to be declined
    :return year: year in nominative case
    """
    year = re.sub(r"????????????????", "????????????", year)
    year = re.sub(r"??????????????", "????????????", year)
    year = re.sub(r"????????", "??????", year)
    year = re.sub(r"??????????", "????????", year)
    year = re.sub(r"??????", "????", year)
    year = re.sub(r"????????", "", year)
    return year

def undecline_cyrillic(date: str) -> str:
    """
    declines full Russian date into nominative forms
    :param date: date string in different cases
    :return date: date string in nominative case
    """
    date = undecline_day(date)
    date = undecline_month(date)
    date = undecline_year(date)
    return date.strip()

def transliterate_cyr(translit):
    """
    this takes the Russian cyrillic and transliterates it into the Roman alphabet
    :param translit: changes cyrillic letters to roman equivalents
    :return translit_rus: translitered russian form of string
    """
    translit=re.sub(r"??", "A", translit)
    translit=re.sub(r"??", "a", translit)
    translit=re.sub(r"??", "B", translit)
    translit=re.sub(r"??", "b", translit)
    translit=re.sub(r"??", "V", translit)
    translit=re.sub(r"??", "v", translit)
    translit=re.sub(r"??", "G", translit)
    translit=re.sub(r"??", "g", translit)
    translit=re.sub(r"??", "D", translit)
    translit=re.sub(r"??", "d", translit)
    translit=re.sub(r"??", "Je", translit)
    translit=re.sub(r"??", "je", translit)
    translit=re.sub(r"??", "Jo", translit)
    translit=re.sub(r"??", "jo", translit)
    translit=re.sub(r"??", "Zh", translit)
    translit=re.sub(r"??", "zh", translit)
    translit=re.sub(r"??", "Z", translit)
    translit=re.sub(r"??", "z", translit)
    translit=re.sub(r"??", "I", translit)
    translit=re.sub(r"??", "i", translit)
    translit=re.sub(r"??", "J", translit)
    translit=re.sub(r"??", "j", translit)
    translit=re.sub(r"??", "K", translit)
    translit=re.sub(r"??", "k", translit)
    translit=re.sub(r"??", "L", translit)
    translit=re.sub(r"??", "l", translit)
    translit=re.sub(r"??", "M", translit)
    translit=re.sub(r"??", "m", translit)
    translit=re.sub(r"??", "N", translit)
    translit=re.sub(r"??", "n", translit)
    translit=re.sub(r"??", "O", translit)
    translit=re.sub(r"??", "o", translit)
    translit=re.sub(r"??", "P", translit)
    translit=re.sub(r"??", "p", translit)
    translit=re.sub(r"??", "R", translit)
    translit=re.sub(r"??", "r", translit)
    translit=re.sub(r"C", "S", translit)
    translit=re.sub(r"??", "s", translit)
    translit=re.sub(r"??", "T", translit)
    translit=re.sub(r"??", "t", translit)
    translit=re.sub(r"??", "U", translit)
    translit=re.sub(r"??", "u", translit)
    translit=re.sub(r"??", "F", translit)
    translit=re.sub(r"??", "f", translit)
    translit=re.sub(r"??", "Kh", translit)
    translit=re.sub(r"??", "kh", translit)
    translit=re.sub(r"??", "Ts", translit)
    translit=re.sub(r"??", "ts", translit)
    translit=re.sub(r"??", "Ch", translit)
    translit=re.sub(r"??", "ch", translit)
    translit=re.sub(r"??", "Sh", translit)
    translit=re.sub(r"??", "sh", translit)
    translit=re.sub(r"??", "Shch", translit)
    translit=re.sub(r"??", "shch", translit)
    translit=re.sub(r"??", '"', translit)
    translit=re.sub(r"??", '"', translit)
    translit=re.sub(r"??", "Y", translit)
    translit=re.sub(r"??", "y", translit)
    translit=re.sub(r"??", "'", translit)
    translit=re.sub(r"??", "'", translit)
    translit=re.sub(r"??", "Eh", translit)
    translit=re.sub(r"??", "eh", translit)
    translit=re.sub(r"??", "Ju", translit)
    translit=re.sub(r"??", "ju", translit)
    translit=re.sub(r"??", "Ya", translit)
    translit=re.sub(r"??", "ya", translit)
    return translit

def gregorian_cal(datelist):
    """
    takes a list of numerals corresponding to a date in the julian calendar and outputs gregorian equivalent
    :param datelist: takes a date in julian calendar and adds 13 or 14 days onto it to get correct gregorian equivalent
    :return datelist: list of numerals corresponding to a date in the gregorian calendar
    """
    day=datelist[0]
    month=datelist[1]
    year=datelist[-1]
    month31=["01", "03", "05", "07", "08", "10"]
    month30=["09", "04", "06", "11"]
    if month=="02":
        if float(year)>=2100:
            gregd=int(day)+14
            if float(year)%4 ==0:
                if re.search("00$", year):
                    if float(year)%400 ==0:
                        if int(gregd)>29:
                            monthg=int(month)+1
                            dayg=14-(29-int(day))
                            yearg=year
                        else:
                            monthg=month
                            dayg=gregd
                            yearg=year
                    else:
                        if int(gregd)>28:
                            monthg=int(month)+1
                            dayg=14-(28-int(day))
                            yearg=year
                else:
                    if int(gregd)>29:
                        monthg=int(month)+1
                        dayg=14-(29-int(day))
                        yearg=year
                    else:
                        monthg=month
                        dayg=gregd
                        yearg=year
            else:
                if int(gregd)>28:
                    monthg=int(month)+1
                    dayg=14-(28-int(day))
                    yearg=year
                else:
                    monthg=month
                    dayg=gregd
                    yearg=year
        else:
            gregd=int(day)+13
            if float(year)%4 ==0:
                if re.search("00$", year):
                    if float(year)%400 ==0:
                        if int(gregd)>29:
                            monthg=int(month)+1
                            dayg=13-(29-int(day))
                            yearg=year
                        else:
                            monthg=month
                            dayg=gregd
                            yearg=year
                    else:
                        if int(gregd)>28:
                            monthg=int(month)+1
                            dayg=13-(28-int(day))
                            yearg=year
                else:
                    if int(gregd)>29:
                        monthg=int(month)+1
                        dayg=13-(29-int(day))
                        yearg=year
                    else:
                        monthg=month
                        dayg=gregd
                        yearg=year
            else:
                if int(gregd)>28:
                    monthg=int(month)+1
                    dayg=13-(28-int(day))
                    yearg=year
                else:
                    monthg=month
                    dayg=gregd
                    yearg=year
    elif month=="12":
        if float(year)>=2100:
            gregd=int(day)+14
            if int(gregd)>31:
                monthg="01"
                yearg=int(year)+1
                dayg=14-(31-int(day))
            else:
                monthg=month
                yearg=year
                dayg=gregd
        else:
            gregd=int(day)+13
            if int(gregd)>31:
                monthg="01"
                yearg=int(year)+1
                dayg=13-(31-int(day))
            else:
                monthg=month
                yearg=year
                dayg=gregd
    elif month in month31:
        if float(year)>=2100:
            gregd=int(day)+14
            if int(gregd)>31:
                monthg=int(month)+1
                dayg=14-(31-int(day))
                yearg=year
            else:
                monthg=month
                dayg=gregd
                yearg=year
        else:
            gregd=int(day)+13
            if int(gregd)>31:
                monthg=int(month)+1
                dayg=13-(31-int(day))
                yearg=year
            else:
                monthg=month
                dayg=gregd
                yearg=year
    elif month in month30:
        if float(year)>=2100:
            gregd=int(day)+14
            if int(gregd)>30:
                monthg=int(month)+1
                dayg=14-(30-int(day))
                yearg=year
            else:
                monthg=month
                dayg=gregd
                yearg=year
        else:
            gregd=int(day)+13
            if int(gregd)>30:
                monthg=int(month)+1
                dayg=13-(30-int(day))
                yearg=year
            else:
                monthg=month
                dayg=gregd
                yearg=year
    gregorian=str(dayg)+"."+str(monthg)+"."+str(yearg)
    return gregorian

