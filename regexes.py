#month is the russian month in nom case
import re
month=input("Input a Russian month: ")
def decline_month(month):
    if re.search(r"ь$", month):
        month=re.sub(r"ь$", "я", month)
    elif re.search(r"й$", month):
        month=re.sub(r"й$", "я", month)
    elif re.search(r"т$", month):
        month=re.sub(r"т$", "та", month)
    return month
print(decline_month(month)) 
        