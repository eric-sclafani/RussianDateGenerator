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