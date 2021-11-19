from dictionaries import *
import re

def numeral_to_cyrillic(numeral:str, option)->str:

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
    # to be added

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
    if re.search(r"третий", year):
        year = re.sub(r"третий$", "третьего", year)
    elif re.search(r"ый$", year):
        year = re.sub(r"ый$", "ого", year)
    elif re.search(r"ой$", year):
        year = re.sub(r"ой$", "ого", year)
    return year

def transliterate_cyr(cyrillic):
    """
    this takes the Russian cyrillic and transliterates it into the Roman alphabet
    :param cyrillic: changes cyrillic letters to roman equivalents
    :return translit_rus: translitered russian form of string
    """
    for char in cyrillic:
        if re.search(r"А", cyrillic):
            cyrillic=re.sub(r"А", "A", cyrillic)
        if re.search(r"а", cyrillic):
            cyrillic=re.sub(r"а", "a", cyrillic)
        if re.search(r"Б", cyrillic):
            cyrillic=re.sub(r"Б", "B", cyrillic)
        if re.search(r"б", cyrillic):
            cyrillic=re.sub(r"б", "b", cyrillic)
        if re.search(r"В", cyrillic):
            cyrillic=re.sub(r"В", "V", cyrillic)
        if re.search(r"в", cyrillic):
            cyrillic=re.sub(r"в", "v", cyrillic)
        if re.search(r"Г", cyrillic):
            cyrillic=re.sub(r"Г", "G", cyrillic)
        if re.search(r"г", cyrillic):
            cyrillic=re.sub(r"г", "g", cyrillic)
        if re.search(r"Д", cyrillic):
            translit_rus=re.sub(r"Д", "D", cyrillic)
        if re.search(r"д", cyrillic):
            translit_rus=re.sub(r"д", "d", cyrillic)
        if re.search(r"Е", cyrillic):
            translit_rus=re.sub(r"Е", "Je", cyrillic)
        if re.search(r"е", cyrillic):
            translit_rus=re.sub(r"е", "je", cyrillic)
        if re.search(r"Ё", cyrillic):
            translit_rus=re.sub(r"Ё", "Jo", cyrillic)
        if re.search(r"ё", cyrillic):
            translit_rus=re.sub(r"ё", "jo", cyrillic)
        if re.search(r"Ж", cyrillic):
            translit_rus=re,sub(r"Ж", "Zh", cyrillic)
        if re.search(r"ж", cyrillic):
            translit_rus=re.sub(r"ж", "zh", cyrillic)
        if re.search(r"З", cyrillic):
            translit_rus=re.sub(r"З", "Z", cyrillic)
        if re.search(r"з", cyrillic):
            translit_rus=re.sub(r"з", "z", cyrillic)
        if re.search(r"И", cyrillic):
            translit_rus=re.sub(r"И", "I", cyrillic)
        if re.search(r"и", cyrillic):
            translit_rus=re.sub(r"и", "i", cyrillic)
        if re.search(r"Й", cyrillic):
            translit_rus=re.sub(r"Й", "J", cyrillic)
        if re.search(r"й", cyrillic):
            translit_rus=re.sub(r"й", "j", cyrillic)
        if re.search(r"К", cyrillic):
            translit_rus=re.sub(r"К", "K", cyrillic)
        if re.search(r"к", cyrillic):
            translit_rus=re.sub(r"к", "k", cyrillic)
        if re.search(r"Л", cyrillic):
            translit_rus=re.sub(r"Л", "L", cyrillic)
        if re.search(r"л", cyrillic):
            translit_rus=re.sub(r"л", "l", cyrillic)
        if re.search(r"М", cyrillic):
            translit_rus=re.sub(r"М", "M", cyrillic)
        if re.search(r"м", cyrillic):
            translit_rus=re.sub(r"м", "m", cyrillic)
        if re.search(r"Н", cyrillic):
            translit_rus=re.sub(r"Н", "N", cyrillic)
        if re.search(r"н", cyrillic):
            translit_rus=re.sub(r"н", "n", cyrillic)
        if re.search(r"О", cyrillic):
            translit_rus=re.sub(r"О", "O", cyrillic)
        if re.search(r"о", cyrillic):
            translit_rus=re.sub(r"о", "o", cyrillic)
        if re.search(r"П", cyrillic):
            translit_rus=re.sub(r"П", "P", cyrillic)
        if re.search(r"п", cyrillic):
            translit_rus=re.sub(r"п", "p", cyrillic)
        if re.search(r"Р", cyrillic):
            translit_rus=re.sub(r"Р", "R", cyrillic)
        if re.search(r"р", cyrillic):
            translit_rus=re.sub(r"р", "r", cyrillic)
        if re.search(r"C", cyrillic):
            translit_rus=re.sub(r"C", "S", cyrillic)
        if re.search(r"с", cyrillic):
            translit_rus=re.sub(r"с", "s", cyrillic)
        if re.search(r"Т", cyrillic):
            translit_rus=re.sub(r"Т", "T", cyrillic)
        if re.search(r"т", cyrillic):
            translit_rus=re.sub(r"т", "t", cyrillic)
        if re.search(r"У", cyrillic):
            translit_rus=re.sub(r"У", "U", cyrillic)
        if re.search(r"у", cyrillic):
            translit_rus=re.sub(r"у", "u", cyrillic)
        if re.search(r"Ф", cyrillic):
            translit_rus=re.sub(r"Ф", "F", cyrillic)
        if re.search(r"ф", cyrillic):
            translit_rus=re.sub(r"ф", "f", cyrillic)
        if re.search(r"Х", cyrillic):
            translit_rus=re.sub(r"Х", "Kh", cyrillic)
        if re.search(r"х", cyrillic):
            translit_rus=re.sub(r"х", "kh", cyrillic)
        if re.search(r"Ц", cyrillic):
            translit_rus=re.sub(r"Ц", "Ts", cyrillic)
        if re.search(r"ц", cyrillic):
            translit_rus=re.sub(r"ц", "ts", cyrillic)
        if re.search(r"Ч", cyrillic):
            translit_rus=re.sub(r"Ч", "Ch", cyrillic)
        if re.search(r"ч", cyrillic):
            translit_rus=re.sub(r"ч", "ch", cyrillic)
        if re.search(r"Ш", cyrillic):
            translit_rus=re.sub(r"Ш", "Sh", cyrillic)
        if re.search(r"ш", cyrillic):
            translit_rus=re.sub(r"ш", "sh", cyrillic)
        if re.search(r"Щ", cyrillic):
            translit_rus=re.sub(r"Щ", "Shch", cyrillic)
        if re.search(r"щ", cyrillic):
            translit_rus=re.sub(r"щ", "shch", cyrillic)
        if re.search(r"Ъ", cyrillic):
            translit_rus=re.sub(r"Ъ", '"', cyrillic)
        if re.search(r"ъ", cyrillic):
            translit_rus=re.sub(r"ъ", '"', cyrillic)
        if re.search(r"Ы", cyrillic):
            translit_rus=re.sub(r"Ы", "Y", cyrillic)
        if re.search(r"ы", cyrillic):
            translit_rus=re.sub(r"ы", "y", cyrillic)
        if re.search(r"Ь", cyrillic):
            translit_rus=re.sub(r"Ь", "'", cyrillic)
        if re.search(r"ь", cyrillic):
            translit_rus=re.sub(r"m", "'", cyrillic)
        if re.search(r"Э", cyrillic):
            translit_rus=re.sub(r"Э", "Eh", cyrillic)
        if re.search(r"э", cyrillic):
            translit_rus=re.sub(r"э", "eh", cyrillic)
        if re.search(r"Ю", cyrillic):
            translit_rus=re.sub(r"Ю", "Ju", cyrillic)
        if re.search(r"ю", cyrillic):
            translit_rus=re.sub(r"ю", "ju", cyrillic)
        if re.search(r"Я", cyrillic):
            translit_rus=re.sub(r"Я", "Ya", cyrillic)
        if re.search(r"я", cyrillic):
            translit_rus=re.sub(r"я", "ya", cyrillic)
    return translit_rus
