'''
Problem Statement :
Write a Python function that takes in a string and returns the string with all the vowels removed.

Code :
'''

def remove_vowels(string):
    # String containing all vowel characters
    vowels = "aeiouAEIOU" 
    # Variable to store the modified string without vowels
    withoutvowels = ""    
    
    # Loop through each character in the input string
    for char in string:
        if char not in vowels:  # Check if the character is not a vowel
            withoutvowels += char  # Add the character to the modified string without vowels
    
    return withoutvowels  # Return the modified string without vowels

input_str =input("Enter any String : ")
result = remove_vowels(input_str)
print(result)

