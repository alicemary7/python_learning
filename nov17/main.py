# Input: nums = [4,6,9,2,3,11], k = 2
# Output: [3,11,4,6,9,2]

# nums = [4,6,9,2,3,11]
# k = 2
# new=nums[-k:]
# result=[]
# for i in range(0,len(nums)-k):
#     result=new
#     result.append(nums[i])
# print(result)


# - You are given a list of numbers and a target value.
#   Your task is to find all the indices at which the target value appears and PUT THOSE IN A NEW LIST.
# ```python
# #test case 1
# Input: nums = [4,2,7,2,9,3,2,8], k = 2
# Output: [1,3,6]
# #test case 2
# Input: nums = [10,55,17,29,3], k = -45
# Output: "Not Found"


# nums = [4,2,7,2,9,3,2,8]
# k = 2
# n=[]

# for i in range(0,len(nums),+1): 
#     if nums[i]==k:
#         n.append(i)
# print(n)



# nums = [10,55,17,29,3]
# k = 5
# a=[]

# for i in range(0,len(nums),+1):
#         if nums[i] == k :
#             a.append(i)
#             break
#     print(a)


# - Given a list of numbers, print the list in reverse order without using list slicing ([::-1]).
# ```python
# # test case 1
# Input: nums = [1,3,7,8,9]
# Output: [9,8,7,3,1]
# # test case 2
# Input: nums = []
# Output: []
        
    
# nums = [1,3,7,8,9]
# new=[]
# for i in range(len(nums)-1,-1,-1):
#     new.append(nums[i])
# print(new)


### STRINGS
# - Write a program that takes a string as input and counts the number of uppercase letters in it.
# ```python
# # test case 1
# Input: "HelloWorld"
# Output: 2
# explanation -> H , W are upper case so, output is 2
    
    
# nums="HelloWorld"
# alpha="ABCDEFGHIJKLMNOPRSTUVWXYZ"
# count=0
# for i in range(0,len(nums)):
#     if nums[i] in alpha:
#         count=count+1
# print(count)



# - Write a program that finds the longest word in a given sentence.
#   (Bonus: If you are too studious, try without using `split(" ")` and solve)
# ```python
# # test case 1
# Input: "Johannesburg is the most populous city of South Africa"
# Output: "Johannesburg"
# based on the word length -> it is Johannesburg
    
# nums="Johannesburg is the most populous city of South Africa"
# n=nums.split(" ")

# high = 0
# result = ""
# count=0
# for i in  n:
#     for j in i:
#         count = count +1
#     if count > high:
#         high = count
#         result = i
#     count = 0
# print(result)



# - Given a sentence, interchange the words that appear before and after every occurrence of the word `and`. The word `and` should remain in the same position, but the surrounding words must be swapped.
# ```python
# Input: apple and banana
# Output: banana and apple


nums="apple and banana "
string = ""
lst = []
for i in nums:
    if i != " ":
        string = string +i 
    elif i == " ":
        lst.append(string)
        string = " "
print(lst)
        
 
 
# lst[0],lst[-1] = lst[-1],lst[0]
# result = " ".join(lst)
# print(result)


# mississippi-> count letters

# num= "mississippi"
# count=0
# for i in num:
#     for j in num:
#         if i == j:
#             count=count+1
#     print(i,count)
#     count=0

 


# swiss -> w

# a="swiss"
# count = 0
# result = ""
# for i in a:
#     for j in a:
#         if i == j:
#             count = count+1
#             break
#         if count == 1 :
#             result = i
# print(result)

