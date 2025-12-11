# import json

# json_new_string={"name":"Alice","age":18,"isStudent":True,"skills":["python","SQL"],"address":{"city":"chennai","pincode":16000}}

# details=json.dumps(json_new_string)
# print(type(details))

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and
import json
import requests
# Step 1: Make a GET request to the API
response = requests.get("https://randomuser.me/api/")
# Step 2: Convert response JSON → Python dict
data = response.json()
# Step 3: Extract some values
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)






# - Vowel Extractor  
#   Write a program to extract only the vowels from a given word and store them in a list.  
#   Print the list at the end.
  
# def show_vowels(word):
#     v= "aeiou"  # both lowercase & uppercase
#     v_list = []
#     for char in word:
#         if char in v:
#             v_list.append(char)
#     return(v_list)
# print(show_vowels("alice"))
        
        
# Find Word with Maximum Vowels
# Given a list of words, find which word has the highest number of vowels and print that word.

# ```python
# Input: words = ["cat", "eagle", "umbrella", "sky"]
# Output: umbrella  

# def show_maxvowels(words):
#     v="aeiou"
#     v_list=[]
#     count=0
#     total=0
#     for char in words:
#         for i in char:
#             if i in v:
#                 count = count+1
#                 break
#         print(count,end = " ")
          
    
#         # if count>total:
#         #         total = count
#         #         v_list=words
#     return v_list
# show_maxvowels(["cat", "eagle", "umbrella", "sky"])
                


# - Given an array of integers, count how many numbers are even and how many are odd.

# ```python
# Example Input: [1, 2, 3, 4, 5, 6, 7]
# Example Output: { even: 3, odd: 4 }

# def count_even_odd(num):
#     count=0
#     for i in range (1,len(num),+1):
#         if i%2==0:
#             count=count+1
#             print(count)
#         # else:
#         #     count=count+1
#         #     print(count)
# count_even_odd([1,2,3,4,5])


# for i in range(1,6):
#     print()
#     for j in range(1,i+1):
#         print("*",end=" ")
        
# for i in range(5,0,-1):
#     print("*" * i)
         
# row=5  
# for i in range(row):
#     print(" " * (row - i - 1) + "*" * (2 * i + 1))

# rows = 5
# for i in range(1, rows + 1):
#     print(str(i) * i)