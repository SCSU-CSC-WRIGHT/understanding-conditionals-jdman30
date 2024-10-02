# This is Assignment 3 for Jordan Drabek, CSC 152, 10/2/2024

#Temperature Check
#Write a Python program that asks the user to input the current temperature in Celsius. If the temperature is above 30 degrees, print "It's a hot day." Otherwise, print "The weather is cool."

#Number Comparison
#Write a program that asks the user to input two numbers. Use an if condition to print which number is larger or if they are equal.

#Password Checker
#Set an admin password. Ask the user to input a password. If the entered password matches the admin password, print "Access granted." If not, print "Access denied."

#Simple Calculator
#Write a program that asks the user for two numbers and an arithmetic operator (+, -, *, /). Use if statements to perform the corresponding arithmetic operation and print the result.

#Positive, Negative, or Zero
#Write a program that asks the user for a number. Check whether the number is positive, negative, or zero, and print an appropriate message.

#Day of the Week
#Create a program that asks the user to input a number between 1 and 7. Use an if statement to print the day of the week (e.g., 1 = Monday, 2 = Tuesday, etc.).

# This is Assignment 3 for Jordan Drabek, CSC 152, 10/2/2024


# Temperature Check

tempinput = float(input("Please enter the temperature in celsius: "))

if (tempinput > 30 ):
    print("It's a hot day.")
else:
    print("The weather is cool")


# Number Comparison

firstnum = float(input("Please enter a number "))
secondnum = float(input("Please enter a second number "))

if (firstnum > secondnum):
    print(firstnum)
elif (secondnum > firstnum):
    print(secondnum)
else:
    print("The numbers are equal")

# Password Checker

adminpass = 16785
passin = int(input("Please enter your password: "))

if (passin == adminpass):
    print ("Access Granted")
else:
    print ("Access Denied")

# Simple Calculator

num_calc_one = float(input("Please enter a number "))
num_calc_two = float(input("Please enter a second number "))
arithmetic_op = input("Enter and arithetic operator, +, -, *, or / ")

if (arithmetic_op == "+"):
    print(num_calc_one+num_calc_two)
elif (arithmetic_op == "-"):
    print(num_calc_one-num_calc_two)
elif (arithmetic_op == "*"):
    print(num_calc_one*num_calc_two)
elif (arithmetic_op == "/"):
    print(num_calc_one/num_calc_two)
else:
    print("You didnt enter an operator or number")

# Positive, Negative, or Zero

posnum = float(input("Please enter a number: "))

if (posnum > 0):
    print("The number is Positive")
elif (posnum < 0):
    print("The number is Negative")
else:
    print("The number is 0")

# Day of the Week

dayinput = int(input("Please enter a number 1-7: "))

if (dayinput == 1):
    print("The day is Monday")
elif (dayinput == 2):
    print("The day is Tuesday")
elif (dayinput == 3):
    print("The day is Wednesday")
elif (dayinput == 4):
    print("The day is Thursday")
elif (dayinput == 5):
    print("The day is Friday")
elif (dayinput == 6):
    print("The day is Saturday")
elif (dayinput == 7):
    print("The day is Sunday")
else:
    print("You didnt enter one of the numbers.")