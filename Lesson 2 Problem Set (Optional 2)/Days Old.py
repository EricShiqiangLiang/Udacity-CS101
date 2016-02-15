# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def isLeapYear(year):
    if year % 100 != 0:
        if year % 4 == 0:
            return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
def days_of_month(month):
    days_of_month = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,month):
        days_of_month = days[i-1] + days_of_month
    return days_of_month

def daysBetweenDates(year1, month1, day1, year2, month2, day2): 
    leap = 0
    year = year1
    while year <= year2:
        if isLeapYear(year):
            leap = leap + 1     
        year = year + 1
    if isLeapYear(year2):
        if month2 == 1:
            leap = leap - 1
        if month2 == 2:
            if day2 < 29:
                leap = leap - 1
    result =leap + (year2 - year1) * 365 + days_of_month(month2) - days_of_month(month1) + day2 - day1
    return result



# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()