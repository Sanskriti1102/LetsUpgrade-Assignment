'''
Problem Statement :

Code the following

1. Create a list of 10 index values. add 2 new values, create 3 values, and slice it.
2. Create a dictionary, add key values,delete key values
3. Create list with duplicates-> convert it into a set & then back to the list (remove duplicates)
'''
#  1.
# Create a list of 10 index values
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Add 2 new values
mylist.append(11)
mylist.append(12)

# Create 3 values
value1 = 13
value2 = 14
value3 = 15

# Add the created values to the list
mylist.extend([value1, value2, value3])

# Slice the list
slicedlist = mylist[3:8]

# Print the list and the sliced list
print("Original List:", mylist)
print("Sliced List:", slicedlist)

# 2.
# Create an empty dictionary
mydict = {}

# Add key-value pairs to the dictionary
mydict['name'] = 'John'
mydict['age'] = 25
mydict['city'] = 'New York'

# Print the dictionary
print("Original Dictionary:", mydict)

# Delete a key-value pair from the dictionary
del mydict['age']

# Print the dictionary after deletion
print("Updated Dictionary:", mydict)

# 3.
# Create a list with duplicates
mylist = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 9, 4]

# Convert the list into a set to remove duplicates
myset = set(mylist)

# Convert the set back to a list
uniquelist = list(myset)

# Print the original list and the list without duplicates
print("Original List:", mylist)
print("List without Duplicates:", uniquelist)
