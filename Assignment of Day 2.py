age=int(input("Enter your age: "))

if age<18:
    print("You are a minor (Age is: {})".format(age))
elif age >=18 and age<65:
    print("You are an adult (Age is: {})".format(age))
elif age>=65:
    print("You are a senior (Age is: {})".format(age))