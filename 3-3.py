import datetime
from datetime import date

def days_since_special_relativity_paper(year,month,day):
    days = 0
    st = date(1905, 9, 26)
    ed = date(year, month, day)
    delta = ed - st
    days = delta.days
    print(st)


    return days
if __name__ == '__main__':
    days_since_special_relativity_paper(2020,2,28)