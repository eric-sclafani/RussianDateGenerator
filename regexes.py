from dictionaries import *
import re

def decline_day(day:str) -> str:
    """
    declines Russian day from nominitive -> prepositional case
    :param day: last number in date string to be declined
    :return day: day in prepositional case
    """
    day = numeral_to_cyrillic(day, "day")
    if re.search(r"третий$", day):
        day = re.sub(r"третий$", "третье", day)
    elif re.search(r"ый$", day):
        day = re.sub(r"ый$", "ое", day)
    elif re.search(r"ой$", day):
        day = re.sub(r"ой$", "ое", day)
    return day

def decline_month(month:str) -> str:
    """
    declines Russian month from nomitive -> genitive case
    :param month: month to be declined
    :return month: month in genitive case
    """
    month = numeral_to_cyrillic(month, "month")
    if re.search(r"ь$", month):
        month = re.sub(r"ь$", "я", month)
    elif re.search(r"й$", month):
        month = re.sub(r"й$", "я", month)
    elif re.search(r"т$", month):
        month = re.sub(r"т$", "та", month)
    return month

def decline_year(year: str) -> str:
    """
    declines Russian year from nominitive -> genitive case
    :param year: last number in year string to be declined
    :return year: year in genitive case
    """
    year = numeral_to_cyrillic(year, "year")
    if re.search(r"третий", year):
        year = re.sub(r"третий$", "третьего", year)
    elif re.search(r"ый$", year):
        year = re.sub(r"ый$", "ого", year)
    elif re.search(r"ой$", year):
        year = re.sub(r"ой$", "ого", year)
    elif re.search(r"год$", year):
        year= re.sub(r"год$", "года", year)
    return year

def parse_year(year:str)->list:
    """
    takes a year as input and returns a list of year components
    :param year: string to be parsed
    :return: ordinal form of year if its a number followed by three zeros otherwise list of components
    """
    # if year is a number followed by three zeros (ex:1000, 2000,etc...), convert to cardinal form
    if re.search(r"\d000", year):
        return num_dict[year]["ord"]

    # break up the year into its components
    components = [year[0] + "000", year[1] + "00", year[2] + "0", year[3]] # ex: 2000 + 300 + 20 + 1 = 2321

    # filter out 0 numbers created by the above list to avoid key errors
    return [component for component in components if component not in ["000", "00", "0"]]

def numeral_to_cyrillic(numeral: str, option) -> str:
    single_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if numeral in single_nums:
        numeral = re.sub(r"0", "", numeral)

    # day processing
    if option == "day":
        return re.sub(rf"{numeral}", num_dict[numeral]["ord"], numeral)

    # month processing
    if option == "month":
        return re.sub(rf"{numeral}", month_dict[numeral], numeral)

    # year processing
    if option == "year":
        year = ""
        for component in parse_year(numeral):

            # if year is numeral followed by three zeros (already processed in parse_year)
            if not component.isnumeric():
                return parse_year(numeral)
            if len(component) == 1:
                year += num_dict[component]["ord"] + " "
            else:
                year += num_dict[component]["card"] + " "
        return year

def transliterate_cyr(translit:str)->str:
    """
    takes the Russian cyrillic as input and transliterates it into the Roman alphabet
    :param translit: changes cyrillic letters to roman equivalents
    :return translit: translitered russian form of string
    """
    if re.search(r"А", translit):
        translit=re.sub(r"А", "A", translit)
    if re.search(r"а", translit):
        translit=re.sub(r"а", "a", translit)
    if re.search(r"Б", translit):
        translit=re.sub(r"Б", "B", translit)
    if re.search(r"б", translit):
        translit=re.sub(r"б", "b", translit)
    if re.search(r"В", translit):
        translit=re.sub(r"В", "V", translit)
    if re.search(r"в", translit):
        translit=re.sub(r"в", "v", translit)
    if re.search(r"Г", translit):
        translit=re.sub(r"Г", "G", translit)
    if re.search(r"г", translit):
        translit=re.sub(r"г", "g", translit)
    if re.search(r"Д", translit):
        translit=re.sub(r"Д", "D", translit)
    if re.search(r"д", translit):
        translit=re.sub(r"д", "d", translit)
    if re.search(r"Е", translit):
        translit=re.sub(r"Е", "Je", translit)
    if re.search(r"е", translit):
        translit=re.sub(r"е", "je", translit)
    if re.search(r"Ё", translit):
        translit=re.sub(r"Ё", "Jo", translit)
    if re.search(r"ё", translit):
        translit=re.sub(r"ё", "jo", translit)
    if re.search(r"Ж", translit):
        translit=re.sub(r"Ж", "Zh", translit)
    if re.search(r"ж", translit):
        translit=re.sub(r"ж", "zh", translit)
    if re.search(r"З", translit):
        translit=re.sub(r"З", "Z", translit)
    if re.search(r"з", translit):
        translit=re.sub(r"з", "z", translit)
    if re.search(r"И", translit):
        translit=re.sub(r"И", "I", translit)
    if re.search(r"и", translit):
        translit=re.sub(r"и", "i", translit)
    if re.search(r"Й", translit):
        translit=re.sub(r"Й", "J", translit)
    if re.search(r"й", translit):
        translit=re.sub(r"й", "j", translit)
    if re.search(r"К", translit):
        translit=re.sub(r"К", "K", translit)
    if re.search(r"к", translit):
        translit=re.sub(r"к", "k", translit)
    if re.search(r"Л", translit):
        translit=re.sub(r"Л", "L", translit)
    if re.search(r"л", translit):
        translit=re.sub(r"л", "l", translit)
    if re.search(r"М", translit):
        translit=re.sub(r"М", "M", translit)
    if re.search(r"м", translit):
        translit=re.sub(r"м", "m", translit)
    if re.search(r"Н", translit):
        translit=re.sub(r"Н", "N", translit)
    if re.search(r"н", translit):
        translit=re.sub(r"н", "n", translit)
    if re.search(r"О", translit):
        translit=re.sub(r"О", "O", translit)
    if re.search(r"о", translit):
        translit=re.sub(r"о", "o", translit)
    if re.search(r"П", translit):
        translit=re.sub(r"П", "P", translit)
    if re.search(r"п", translit):
        translit=re.sub(r"п", "p", translit)
    if re.search(r"Р", translit):
        translit=re.sub(r"Р", "R", translit)
    if re.search(r"р", translit):
        translit=re.sub(r"р", "r", translit)
    if re.search(r"C", translit):
        translit=re.sub(r"C", "S", translit)
    if re.search(r"с", translit):
        translit=re.sub(r"с", "s", translit)
    if re.search(r"Т", translit):
        translit=re.sub(r"Т", "T", translit)
    if re.search(r"т", translit):
        translit=re.sub(r"т", "t", translit)
    if re.search(r"У", translit):
        translit=re.sub(r"У", "U", translit)
    if re.search(r"у", translit):
        translit=re.sub(r"у", "u", translit)
    if re.search(r"Ф", translit):
        translit=re.sub(r"Ф", "F", translit)
    if re.search(r"ф", translit):
        translit=re.sub(r"ф", "f", translit)
    if re.search(r"Х", translit):
        translit=re.sub(r"Х", "Kh", translit)
    if re.search(r"х", translit):
        translit=re.sub(r"х", "kh", translit)
    if re.search(r"Ц", translit):
        translit=re.sub(r"Ц", "Ts", translit)
    if re.search(r"ц", translit):
        translit=re.sub(r"ц", "ts", translit)
    if re.search(r"Ч", translit):
        translit=re.sub(r"Ч", "Ch", translit)
    if re.search(r"ч", translit):
        translit=re.sub(r"ч", "ch", translit)
    if re.search(r"Ш", translit):
        translit=re.sub(r"Ш", "Sh", translit)
    if re.search(r"ш", translit):
        translit=re.sub(r"ш", "sh", translit)
    if re.search(r"Щ", translit):
        translit=re.sub(r"Щ", "Shch", translit)
    if re.search(r"щ", translit):
        translit=re.sub(r"щ", "shch", translit)
    if re.search(r"Ъ", translit):
        translit=re.sub(r"Ъ", '"', translit)
    if re.search(r"ъ", translit):
        translit=re.sub(r"ъ", '"', translit)
    if re.search(r"Ы", translit):
        translit=re.sub(r"Ы", "Y", translit)
    if re.search(r"ы", translit):
        translit=re.sub(r"ы", "y", translit)
    if re.search(r"Ь", translit):
        translit=re.sub(r"Ь", "'", translit)
    if re.search(r"ь", translit):
        translit=re.sub(r"ь", "'", translit)
    if re.search(r"Э", translit):
        translit=re.sub(r"Э", "Eh", translit)
    if re.search(r"э", translit):
        translit=re.sub(r"э", "eh", translit)
    if re.search(r"Ю", translit):
        translit=re.sub(r"Ю", "Ju", translit)
    if re.search(r"ю", translit):
        translit=re.sub(r"ю", "ju", translit)
    if re.search(r"Я", translit):
        translit=re.sub(r"Я", "Ya", translit)
    if re.search(r"я", translit):
        translit=re.sub(r"я", "ya", translit)
    return translit

def julian_cal(datelist):
    """
    takes a string of numerals in the gregorian calendar and outputs julian equivalent
    """
    day=datelist[0]
    month=datelist[1]
    year=datelist[-1]
    juld=int(day)+13
    month31=["01", "03", "05", "07", "08", "10"]
    month30=["09", "04", "06", "11"]
    if month=="02":
        if float(year)%4 ==0:
            if re.search("00$", year):
                if float(year)%400 ==0:
                    if int(juld)>29:
                        monthj=int(month)+1
                        dayj=13-(29-int(day))
                        yearj=year
                    else:
                        monthj=month
                        dayj=juld
                        yearj=year
                else:
                    if int(juld)>28:
                        monthj=int(month)+1
                        dayj=13-(28-int(day))
                        yearj=year
            else:
                if int(juld)>29:
                    monthj=int(month)+1
                    dayj=13-(29-int(day))
                    yearj=year
                else:
                    monthj=month
                    dayj=juld
                    yearj=year
        else:
            if int(juld)>28:
                monthj=int(month)+1
                dayj=13-(28-int(day))
                yearj=year
            else:
                monthj=month
                dayj=juld
                yearj=year
    elif month=="12":
        if int(juld)>31:
            monthj="01"
            yearj=int(year)+1
            dayj=13-(31-int(day))
        else:
            monthj=month
            yearj=year
            dayj=juld
    elif month in month31:
        if int(juld)>31:
            monthj=int(month)+1
            dayj=13-(31-int(day))
            yearj=year
        else:
            monthj=month
            dayj=juld
            yearj=year
    elif month in month30:
        if int(juld)>30:
            monthj=int(month)+1
            dayj=13-(30-int(day))
            yearj=year
        else:
            monthj=month
            dayj=juld
            yearj=year
    julian=str(dayj)+"."+str(monthj)+"."+str(yearj)
    return julian
