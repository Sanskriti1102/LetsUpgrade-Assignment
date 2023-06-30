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
