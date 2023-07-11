'''
Problem Statement :
Write a Python program that asks the user to enter their age and then prints "You are a minor" if their age is less than 18,
"You are an adult" if their age is greater than or equal to 18 and less than 65,
and "You are a senior" if their age is 65 or greater.

Solution :
'''


# Prompt the user to enter their age and convert it to an integer
age = int(input("Enter your age: "))  

if age < 18:

	# If age is less than 18, print "You are a minor" along with the age
    print("You are a minor (Age is: {})".format(age))  

elif age >= 18 and age < 65:

	# If age is between 18 and 64 (inclusive), print "You are an adult" along with the age
    print("You are an adult (Age is: {})".format(age))  

elif age >= 65:

	# If age is 65 or greater, print "You are a senior" along with the age
    print("You are a senior (Age is: {})".format(age))  
