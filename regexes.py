from dictionaries import *
import re


def parse_year(year: str) -> list:
    """
    deconstructs a numeral year into components to be translated into cyrillic
    :param year: string year to be broken down
    :return: list of year components
    """
    if re.search(r"^\d000?", year):
        return num_dict[year]["ord"] # returns the cyrillic form straight from num_dict

    # break up the year into its components

    # if year is length 4
    if len(year) == 4:

        # if last two digits are 11-19, gets pulled directly from num_dict instead of deconstructed
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

    # docstrings to be added

    single_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if numeral in single_nums:
        numeral = re.sub(r"0", "", numeral)

    # day processing
    if option == "day":
        return re.sub(rf"{numeral}", num_dict[numeral]["ord"], numeral)

    # month processing
    if option == "month":
        return re.sub(rf"{numeral}", month_dict[numeral]["cyr"], numeral)

    # year processing
    if option == "year":
        year = ""
        for component in parse_year(numeral):

            if not component.isnumeric():
                # parse_year returns the cyrillic here instead of a list of numbers
                return parse_year(numeral)

            if len(component) == 1:
                year += num_dict[component]["ord"] + " "
            else:
                year += num_dict[component]["card"] + " "

        return year.strip()

def decline_day(day:str) -> str:
    """
    declines Russian day from nominitive -> prepositional case
    :param day: last number in date string to be declined
    :return day: day in prepositional case
    """
    day = numeral_to_cyrillic(day, "day")
    day = re.sub(r"третий$", "третье", day)
    day = re.sub(r"ый$", "ое", day)
    day = re.sub(r"ой$", "ое", day)
    return day

def undecline_day(day: str) -> str:
    day = re.sub(r"третье$", "третий", day)
    day = re.sub(r"шестое$", "шестой", day)
    day = re.sub(r"рое$", "рой", day)
    day = re.sub(r"ьмое", "ьмой", day)
    day = re.sub(r"ое$", "ый", day)
    return day
    
def decline_month(month:str) -> str:
    """
    declines Russian month from nomitive -> genitive case
    :param month: month to be declined
    :return month: month in genitive case
    """
    month = numeral_to_cyrillic(month, "month")
    month = re.sub(r"ь$", "я", month)
    month = re.sub(r"й$", "я", month)
    month = re.sub(r"т$", "та", month)
    return month

def undecline_month(month: str) -> str:
    month = re.sub(r"мая$", "май", month)
    month = re.sub(r"я$", "ь", month)
    month = re.sub(r"та$", "т", month)
    return month
    
def decline_year(year: str) -> str:
    """
    declines Russian year from nominitive -> genitive case
    :param year: last number in year string to be declined
    :return year: year in genitive case
    """

    year = numeral_to_cyrillic(year, "year")

    year = re.sub(r"третий$", "третьего", year)
    year = re.sub(r"ый$", "ого", year)
    year = re.sub(r"ой$", "ого", year)

    year = year + " год"
    year= re.sub(r"год$", "года", year)
    return year

def undecline_year(year: str) -> str:
    year = re.sub(r"третьего$", "третий", year)
    year = re.sub(r"шестого$", "шестой", year)
    year = re.sub(r"рого$", "рой", year)
    year = re.sub(r"ьмого$", "ьмой", year)
    year = re.sub(r"ого$", "ый", year)
    year = re.sub(r"года$", "", year)
    return year

def transliterate_cyr(translit):
    """
    this takes the Russian cyrillic and transliterates it into the Roman alphabet
    :param cyrillic: changes cyrillic letters to roman equivalents
    :return translit_rus: translitered russian form of string
    """
    translit=re.sub(r"А", "A", translit)
    translit=re.sub(r"а", "a", translit)
    translit=re.sub(r"Б", "B", translit)
    translit=re.sub(r"б", "b", translit)
    translit=re.sub(r"В", "V", translit)
    translit=re.sub(r"в", "v", translit)
    translit=re.sub(r"Г", "G", translit)
    translit=re.sub(r"г", "g", translit)
    translit=re.sub(r"Д", "D", translit)
    translit=re.sub(r"д", "d", translit)
    translit=re.sub(r"Е", "Je", translit)
    translit=re.sub(r"е", "je", translit)
    translit=re.sub(r"Ё", "Jo", translit)
    translit=re.sub(r"ё", "jo", translit)
    translit=re.sub(r"Ж", "Zh", translit)
    translit=re.sub(r"ж", "zh", translit)
    translit=re.sub(r"З", "Z", translit)
    translit=re.sub(r"з", "z", translit)
    translit=re.sub(r"И", "I", translit)
    translit=re.sub(r"и", "i", translit)
    translit=re.sub(r"Й", "J", translit)
    translit=re.sub(r"й", "j", translit)
    translit=re.sub(r"К", "K", translit)
    translit=re.sub(r"к", "k", translit)
    translit=re.sub(r"Л", "L", translit)
    translit=re.sub(r"л", "l", translit)
    translit=re.sub(r"М", "M", translit)
    translit=re.sub(r"м", "m", translit)
    translit=re.sub(r"Н", "N", translit)
    translit=re.sub(r"н", "n", translit)
    translit=re.sub(r"О", "O", translit)
    translit=re.sub(r"о", "o", translit)
    translit=re.sub(r"П", "P", translit)
    translit=re.sub(r"п", "p", translit)
    translit=re.sub(r"Р", "R", translit)
    translit=re.sub(r"р", "r", translit)
    translit=re.sub(r"C", "S", translit)
    translit=re.sub(r"с", "s", translit)
    translit=re.sub(r"Т", "T", translit)
    translit=re.sub(r"т", "t", translit)
    translit=re.sub(r"У", "U", translit)
    translit=re.sub(r"у", "u", translit)
    translit=re.sub(r"Ф", "F", translit)
    translit=re.sub(r"ф", "f", translit)
    translit=re.sub(r"Х", "Kh", translit)
    translit=re.sub(r"х", "kh", translit)
    translit=re.sub(r"Ц", "Ts", translit)
    translit=re.sub(r"ц", "ts", translit)
    translit=re.sub(r"Ч", "Ch", translit)
    translit=re.sub(r"ч", "ch", translit)
    translit=re.sub(r"Ш", "Sh", translit)
    translit=re.sub(r"ш", "sh", translit)
    translit=re.sub(r"Щ", "Shch", translit)
    translit=re.sub(r"щ", "shch", translit)
    translit=re.sub(r"Ъ", '"', translit)
    translit=re.sub(r"ъ", '"', translit)
    translit=re.sub(r"Ы", "Y", translit)
    translit=re.sub(r"ы", "y", translit)
    translit=re.sub(r"Ь", "'", translit)
    translit=re.sub(r"ь", "'", translit)
    translit=re.sub(r"Э", "Eh", translit)
    translit=re.sub(r"э", "eh", translit)
    translit=re.sub(r"Ю", "Ju", translit)
    translit=re.sub(r"ю", "ju", translit)
    translit=re.sub(r"Я", "Ya", translit)
    translit=re.sub(r"я", "ya", translit)
    return translit

def gregorian_cal(datelist):
    """
    takes a string of numerals in the gregorian calendar and outputs julian equivalent
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

