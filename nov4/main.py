# Write a program to find the sum of digits of a number without converting it to a string.
n=1234
sum=0
for i in str(n):
    sum+= int(i)
print(sum)

n = 1234
sum = 0

while n > 0:
    digit = n % 10       # Get last digit
    sum = sum + digit     # Add it to sum
    n = n // 10           # Remove last digit

print(sum)

# Write a program to reverse the digits of a number (without converting to string)
    
    
    # method 1
    
n="Alice Mary"
rev=n[::-1]
print(rev)

#  method 2

word = "hello world"
rev = ""

for i in range(len(word) - 1, -1, -1): 
    rev += word[i]

print("Reversed word:", rev)



# n = 1736978
# rev = 0

# while n > 0:
#     digit = n % 10         
#     rev = rev * 10 + digit 
#     n = n // 10             

# print("Reversed number:", rev)


# Palindrome Check

# def find_higher_average(a,b):
#     m_count=0
#     f_count=0
#     m_mark=0
#     f_mark=0
#     for i in range (0,len(a),+1):
#         if a[i]=="M":
#             m_count+=1
#             m_mark+=b[i]
#         else:
#             f_count+=1
#             f_count+=b[i]
#     m_avg=m_mark/m_count
#     f_avg=f_mark/f_count
#     if m_avg >f_avg:
#         print(m_avg)
#     else:
#         print(f_avg)

# find_higher_average(['M','F','M','F','M','F','M'],
#                     [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0])


# Question 1:
# Write a Python program to check if a given string is a Pangram or not.
# A Pangram is a sentence that contains every letter of the English alphabet (a–z) at least once. 
# The check should be case-insensitive, meaning both uppercase and lowercase letters are treated the same.

# Test Case 1:
# Input:The quick brown fox jumps over the lazy dog
# Output:True

# Explanation:
# The input string contains all the letters from ‘a’ to ‘z’, so it is a Pangram.

# Test Case 2:
# Input: The quick brown fox jumps over the dog
# Output: False

# Explanation:
# The input string is missing some letters (‘l’, ‘z’, and ‘y’), so it is not a Pangram.

num="The quick brown fox jumps over  lazy the dog"
alpha="abcdefghijklmnopqrstuvwxyz"
result="" 


# for i in alpha:
#     if i in num:
#         result+=i
# if len(alpha)==len(result):
#     print(True)
# else:
#     print(False)


for i in alpha:
    if i in num:
        z="true"
    else:
        z="false"
print(z)