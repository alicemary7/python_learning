# a="abcdefg"
# b=""
# rev=a[::-1]
# for i in range(0,len(a)):
#     if i % 2 ==0:
#         b+=rev[i]
#     else:
#         b+=a[i]
# print(b)


# sentence = "hello world this is python"
# words = sentence.split()

# result = ""

# for w in words:
#     print(w)
#     result += w[0].upper() + w[1:]+" "

# print(result)


# n="hello world this is python"
# print(n[0].upper()+n[1:]+" ")


# Highest Rainfall Day
#   Find the index (day number) of the maximum rainfall in the week (assuming day starts from 1).
# python
# Input: rainfall = [22, 45, 38, 55, 41, 35, 29]
# Output: Day 4
# finding the maximum rainfall in the week
# print the corresponding index of the max value


# rainfall = [22, 45, 38, 41,55,  35, 29]
# max_count=rainfall[0]
# max_index=0
# for i in range(0,len(rainfall)):
#     # print(rainfall[i])
#     if rainfall[i] > max_count:
#         max_count=rainfall[i]
#         max_index=i
# # print(max_index)
# print("Day:",max_index+1)


# arr =  [0, 10, 20,0, 30] 

# pos = -1

# for i in range(len(arr)):
#     if arr[i] == 0:
#         pos = i + 1
#         break

# print(pos)


# nums = [ 20,34,66, 0,2,3,4,0,88,99]
nums = [1,2,3,4]


# word ="alice mary"
# result = ""
# for ch in word:
#     if ch not in result:
#         result += ch
# print(result)


# mississippi-> count letters

# new=""
# for i in num:
#     count=0
#     if i not in new:
#         for j in num:
#             if i == j:
#                 count=count+1
#         # if count> max_count:
#         #     max_count = count
#                 new = new+i
# print(max_count,new)
        
        
    # count=0
    
# def check(n):
#     b = ""
#     for i in n:
#         count = 0
#         if i not in b:
#             for j in n:
#                 if i == j:
#                     count+=1
#                     b+=i
#             print(i,"->",count)
# check("mississippi")



# def check(x):
#     b=""
#     a=x[0]
#     b+=a
#     count=0
#     for el in range(1,len(x)):
#         if x[el] not in b:
#             b+=x[el]
#     # print(b)
#     for j in b:
#         for i in x:
#             if i == j:
#                 count+=1
#         print(j,"->",count)
#         count=0
    
# check("mississipi")
            

# - You are given a list of integers and a target number.
#   Your task is to identify two different elements in the list whose sum equals the target.
#   Return the indices of those two elements.

# ```python
# Input:
# # nums = [2, 7, 11, 15]
# # target = 9
# Output:
# # [0,1]

# Input:
# # nums = [3,2,4], target = 6
# Output:
# # [1,2]


            
# nums=[3,2,4]
# target=6
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i],nums[j])
         
         
            
# - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# ```python
# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

# Input:  nums = [1,2,3,4]
# Output: False

# def is_even(nums):
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 print(True)
#                 return
#     print(False)    
# is_even([1,2,3,1])
            


# new=[]
# for i in nums:
#     if i in new:
#         result=False
#     else:
#         result=True
# print(result)