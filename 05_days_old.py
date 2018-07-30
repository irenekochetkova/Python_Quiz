# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
# ****************************************************************************

def dayInFeb(year):
  daysOfMonths = []
  if is_leap_year(year):
    daysOfMonths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  return daysOfMonths

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  countDays = 0
  if year2 > year1:
    countDays = daysInBirthdayYearBefore(year1, month1, day1, year2, month2, day2) + daysInCurrentYearAfter(year1, month1, day1, year2, month2, day2) + countYears(year1, year2)
  elif year1 == year2:
    countDays = daysCountBetween(year1, month1, day1, year2, month2, day2)
  return countDays  

def countYears(year1, year2):
  countLeapYear = 0
  countCommonYear = 0
  i = year1 + 1
  while i < year2:
    if is_leap_year(i):
      countLeapYear = countLeapYear + 1
      i = i + 1
    else:
      countCommonYear = countCommonYear + 1
      i = i + 1
  countDaysYear = countLeapYear * 365 + countLeapYear + countCommonYear * 365
  return countDaysYear

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and not year % 100 == 0:
        return True
    return False

def daysInBirthdayYearBefore(year1, month1, day1, year2, month2, day2):
  daysInBirthdayMonth = dayInFeb(year1)[month1 - 1] - day1
  print(daysInBirthdayMonth) 
  daysCountBefore = daysInBirthdayMonth
  i = month1
  while i < 12:
    daysCountBefore = daysCountBefore + dayInFeb(year1)[i]
    i = i + 1
  print("before", daysCountBefore)  
  return daysCountBefore

def daysInCurrentYearAfter(year1, month1, day1, year2, month2, day2):
  daysCountAfter = day2  
  i = 0
  while i < month2 - 1:
    daysCountAfter = daysCountAfter + dayInFeb(year2)[i]
    i = i + 1
  print("after", daysCountAfter)  
  return daysCountAfter

def daysCountBetween(year1, month1, day1, year2, month2, day2):
  daysInBirthdayMonth = dayInFeb(year1)[month1 - 1] - day1 
  daysCount = daysInBirthdayMonth + day2
  i = month1  
  while i < month2 - 1: 
    daysCount = daysCount + dayInFeb(year1)[i]
    i = i + 1
  return daysCount 

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
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
