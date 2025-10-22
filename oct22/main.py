# Question-1

# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist

def splitting_sentence(sentence):
    words_split= sentence.split('-')
    for word in words_split:
        print(word_spilt)
sentence="The-Spider-Man"
splitting_sentence(sentence)
    

# Question-2

# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP

def reverse_string(str1):
    print(str1[::-1])
str1="Python"
reverse_string(str1)


def reverse_string(s):
    str1 = ""
    for i in s:
        str1 = i +str1 # prepend each character
    print(str1)
str1="Python"
reverse_string(str1)

# Question-3

#  Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def no_of_consonants(consonants):
    if consonants=="a" and consonants=="e" and consonants=="i" and consonants=="o" and consonants=="u" :
        
        print(consonants)
    else:
        v=len(consonants)
        print(v)

consonants="Hello World"
no_of_consonants(consonants)


# Question-4

# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

def remove_spaces_(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

string = "Hello world"
print(remove_spaces_manual(string))


#Question-5

# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def check_password_strong(s):
    special = "!@#$%^&*"
    if len(s) >= 8:
        for c in s:
            if c in special:
                print("Password is strong")
                break
        else:
            print("Password is not strong")
    else:
        print("Password is not strong")

check_password_strong("my!password")