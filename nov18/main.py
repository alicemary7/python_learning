a = "aswisna"
seen = []
repeated = []

for i in a:
    if i in seen:
        repeated.append(i)

    else:
        seen.append(i)
for i in a:
    if i not in repeated:
        print(i)
        break


# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is
 
# nums="Python is super powerful"
# new=nums.split(" ")
# low= 100
# result = ""
# count=0
# for i in  new:
#     for j in i:
#         count = count +1
#     if count < low:
#         low=count
#         result = i
#     count = 0
# print(result)
     
# nums="Python is super powerful "
# word=""
 
# b=[]
# for i in nums:
#     if i != " ":
#         word+=i
#     else:
#         b.append(word)
#         word=""
# # print(b)
# count=b[0]

# print(b)
# for i in b:
#     if len(i) < len(count):
#         count = i
# print(count)



# 2. A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)


# nums=[1,7,5,9]
# for i in range(0,len(nums)):
#     # for j in range (1,len(nums)):
#         if nums[i]<nums[i-1]:
#             new=True
#         else:
#             new=False
#         print(new)



# 3. Reverse characters only at even index positions Indices: 0,2,4,6,...
# Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# Final Output: "gbecdfa"

# nums="abcdefg"

# result=""
# for i in range(len(nums)):
#     if i % 2 != 0:
#         result+= nums[i]
#     else:
#         result=nums[i]+result
        
# print(result)


# - Sum of First and Last Elements
# ​
# Write a program to find the sum of the first and last elements of a list.
# ​
# python
# Input: [10, 20, 30, 40, 50]
# Output: 60  # (10 + 50)


# nums=[10, 20, 30, 40, 50]
# count=0
# for i in range(0,len(nums),len(nums)-1):
#     count+=nums[i]
# print(count)


# Write a program to find the index position of a given number manually using loops.
# ​
# python
# Input:
# numbers = [11, 22, 33, 44, 55]
# search = 33
# Output: 2


# nums=[11, 22, 33, 44, 55]
# k=33
# for i in range(0,len(nums)):
#     if nums[i]==k:
#         print(i)



# 4. Replace characters at odd indexes with *.
# Example: "hello" → "h*l*o"


# nums="hello"
# result=""
# for i in range (0,len(nums)):
#     if i%2!=0:
#         result=result+"*"
#     else:
#         result=result+nums[i]
# print(result)




# sentence = "hello world this is python"
# (without using split)

word = ""
words = []

for ch in sentence:
    if ch == " ":
        if word != "":
            words.append(word)
            word = ""
    else:
        word += ch
if word != "":
    words.append(word)

print(words)




# nums="hello"
# result=""
# for i in range (0,len(nums)):
#     if i%2!=0:
#         result=result+"*"
#     else:
#         result=result+nums[i]
# print(result)


            
#  Input: words = ["cat", "eagle", "umbrella", "sky"]
# Output: umbrella

# words = ["cat", "eagle", "umbrella", "sky"]
# v=['a','e','i','o','u']
# count=0
# for i in words:
#     if i in v:
#         print(i)
        
#         count=count+1
# print(count)
    # if count > high:
    #     high = count
    #     result = i
    # count = 0
    
# nums=[10,20,23,30,40]
# sum=0
# for i in range(0,len(nums),len(nums)-1):
#     sum=sum+nums[i]
# print(sum)

# print(nums[0]+nums[-1])

# find_indices([1, 2, 3, 2, 4, 2], 2) ➞ [1, 3, 5]
# a = [1, 2, 3, 2, 4, 2]
# b = 2

# for i in range(0,len(a)):
#     if a[i] == b:
#         print(i)



# capitalize_title("the art of programming") ➞ "The Art of Programming"

# words="the art of programming"
# new=words.split(" ")
# for i in range(0,len(new)):
#     if new[0].upper():
#         print(new[i])

# Input:
# S = "APPLE" 
# T = "APRON"
# Output:
# GGBBB


# s= "APPLE" 
# t = "APRON"
# new=""
# for i in range(0,len(s)):
#         if s[i]==t[i]:
#             new=new+"G"
#         else:
#             new=new+"B"
# print(new)



# I= [4, 1, 2, 3, 5] 
# Output:
# [4, 0, 2, 0, 5] 


# I= [4, 1, 2, 3, 5] 
# for i in range(0,len(I)):
#     if i%2!=0:
#         I[i]=0
# print(I)