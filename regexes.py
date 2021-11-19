from dictionaries import *
import re

def decline_month(month:str) -> str:
    """
    declines Russian month from nomitive -> genitive case
    :param month: month to be declined
    :return month: month in genitive case
    """
    if re.search(r"ь$", month):
        month = re.sub(r"ь$", "я", month)
    elif re.search(r"й$", month):
        month = re.sub(r"й$", "я", month)
    elif re.search(r"т$", month):
        month = re.sub(r"т$", "та", month)
    return month

def daynumeral_to_cyrillic(day:str)->str:

    single_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if day in single_nums:
        day = re.sub(r"0", "", day)

    day = re.sub(rf"{day}", num_dict[day]["ord"], day)
    return day

def decline_day(day:str) -> str:
    """
    declines Russian day from nominitive -> prepositional case
    :param day: last number in date string to be declined
    :return day: day in prepositional case
    """
    if re.search(r"третий$", day):
        day = re.sub(r"третий$", "третье", day)
    elif re.search(r"ый$", day):
        day = re.sub(r"ый$", "ое", day)
    elif re.search(r"ой$", day):
        day = re.sub(r"ой$", "ое", day)
    return day
    
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
    
