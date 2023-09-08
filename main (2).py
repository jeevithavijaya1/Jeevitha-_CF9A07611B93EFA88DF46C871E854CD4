def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(" {} is a Leap year.". format(year))
  else:
    print(" {} is not a Leap year.". format(year))

# Main program
year = int(input ("Enter a year: "))
res = isLeapyear(year)