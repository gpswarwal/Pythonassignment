# 1. Write a Python program to print the following string in a specific format
"""print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are")"""

# 2. Write a Python program to get the Python version you are using.
# from wsgiref.simple_server import sys_version
"""print(sys_version)"""

"""import sys
print(sys.version)"""

#3. Write a Python program to display the current date and time.
"""import datetime
x = datetime.datetime.now()
print(x) #To show current year:month:date hour:minute:second
print(x.hour) #To show hour
print(x.minute) #To show minute
print(x.second) #To show second 
print(x.day)  #To show current day
print(x.month) #To show current Month
print(x.year) #To show current year
print(x.strftime("%A")) #To show day of the week """

# import datetime
# current_time = datetime.datetime.now()
# print(current_time.strftime("%B")) #this is ("%B") show the month
# print(current_time.strftime("%Y")) #This is ("%Y") show the year
# print(current_time.strftime("%A")) #This is ("%A") show the weekday

#4. Write a Python program which accepts the radius of a circle from the user and compute the area.



# x = int(input("Radius of circle= "))
# y = (22/7)*x**2
# print(y)

# x = int(input("Radius of circle= "))
# y = (3.14)*x**2
# print(y)

radius = int(input("Radius of circle= "))
pi = 3.14
area = pi*radius**2
print(area)