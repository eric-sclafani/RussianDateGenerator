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
