#python program to display calendar of the given year
#and checking whether it's a leap year or not

#importing calendar module for calendar operations
import calendar

#to take the input(year) from the user
year = int(input("Enter a year : "))
yyyy = calendar.calendar(year,1,1,6,4)

#prints or displays calender of the entered input from user
print(yyyy)

#prints whether it's a leap year or not
if calendar.isleap(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
