# * Create and Print a List
# Write a Python program to create a list of 5 fruits and print them one by one using a loop.
# ​
# python
# Input: ["apple", "banana", "cherry", "grapes", "mango"]  
# Output:  
# apple  
# banana  
# cherry  
# grapes  
# mango
        
# fruits=["apple","banana","cherry"]
# for i in fruits:
#     print(i)
        
        
# * Sum of Numbers in a List
# Write a program to find the sum of all numbers in a list entered by the user.
# ​
# python
# Input: [10, 20, 30, 40, 50]  
# Output: 150 # 10+20+30+40+50

# n=[10, 20, 30, 40, 50]  
# sum=0
# for i in n:
#     sum+=i
# print(sum)

#  Reverse a List (Without using reverse() method)
# Write a program to reverse a given list using loops 
# (Hint: Create a New List called final and print the final list at the last)
# ​
# python
# Input: [10, 20, 30, 40]  
# Output: [40, 30, 20, 10]

# n=[10, 20, 30, 40] 
# final=[]
# reverse=0
# for i in range(len(n)-1,-1,-1):
#     final.append(n[i])
# print(final)



# * Even Numbers from a List
# Write a program that prints only the even numbers from a given list.
# (Hint: Create a condition inside the loop to check through each number in the list 
# if number is even, print the number one by one)
# ​
# python
# Input: [3, 6, 9, 12, 15, 18]  
# Output: [6, 12, 18]

# n=[3, 5, 9, 17, 15, 1]
# final=[]
# for i in n:
#     if i%2==0:
#         final.append(i)
#     else:
#         final
# print(final)
        
    
# * Add All Positive Numbers Only
# Write a program to calculate the sum of all positive numbers in a list.
# (Create a variable called total
# Check each number in the list, if number above zero means, add to total)
# ​
# python
# Input: [12, -7, 5, -3, 9, 0]  
# Output: 26

# n=[12, -7, 5, -3, 9, 0]
# sum=0
# number= ["0123456789"]
# final=[]
# for i in n:
#     if i == number:
#         print(i)
        # final.append(i)
 
        
        
        
# Given an array nums and an integer K, remove the last K elements from the array and print the remaining elements.
# Test Case 1:
# Input : nums = [10, 20, 30, 40, 50]
# K = 2
# Output: [10, 20, 30]
# Test Case 2:
# Input: nums = [5, 15, 25]
# K = 5
# Output: Invalid Input   



# def remove_last_elem(nums,k):
#     for i in nums:
#         result=[]
#         if k < len(nums):
#             for j in range(0,len(nums)-k):
#                 result.append(nums[j])
#     print(result)
#         else:
#             print("Invalid input")
            
    
# remove_last_elem([10, 20, 30, 40, 50],4)



#  Given two lists, calculate the total count of odd numbers in each list. Print the list that contains the highest count of odd numbers. If the counts are the same, print "Odd counts are equal".
# Test Case 1:
# Input:
# data_x = [1, 2, 3, 4, 5, 6, 7]
# data_y = [11, 22, 33, 44, 55]
# Output: [1, 2, 3, 4, 5, 6, 7]


# def highest_count(data_x,data_y):
#     sum_data_x=0
#     sum_data_y=0
#     for i in data_x:
#         if i%2!=0:
#             sum_data_x+=i
#     # print(sum_data_x)
#     for j in data_y:
#         if j%2!=0:
#             sum_data_y+=j
#     # print(sum_data_y)
#     if sum_data_x <sum_data_y:
#         print(data_x)
#     else:
#         print(data_y)
# highest_count([1, 2, 3, 4, 5, 6, 7],[11, 22, 33, 44, 55])