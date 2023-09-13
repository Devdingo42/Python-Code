#Magic Dates
#Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit year. The program should then determine whether the month times the day equals the
#year. If so, it should display a message saying the date is magic. Otherwise, it should display
#a message saying the date is not magic.

#User input
print()
month = int(input('Enter a month in numerical form, like "January would be 1": '))
print()
day = int(input('Enter a day out 31 days: '))
print()
year = int(input('Enter two digit year, like "00 to 99": '))
print()
#Response to User
if month * day == year:
    print("Wowww!!! The month times the day equals the year. The date is magic :)")
elif not (month * day == year):
    print('Oh Danggg. The month times the day does not equal the year. The date is not magic :(')