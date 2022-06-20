#python program to display calendar of the given year

#importing calendar module for calendar operations
import calendar

#to take the input(year) from the user
year = int(input("Enter a year : "))
yyyy = calendar.calendar(year,1,1,6,4)

#prints or displays calender of the entered input from user
print(yyyy)
