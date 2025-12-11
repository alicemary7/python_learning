# x =[1,2,3,4,5,7,8,7,9,7,5,3,3]
# Sample [1,2,3,4,5,7]


a=len(x)//2
b=x[:a]
print(b)


# input=[10,20,30,40]
# output=[40, 10, 20, 30]


a=[10,20,30,40]
new=[a[-1]]
# print(new)
for i in range(len(a)-1):
    # print(a[i])
    new.append(a[i])
print(new)


# a = "today is this programming kiss is"
# b = "is"
# output=4


new=a.split(" ")
count=0
for i in new:
    for j in i:
        if i in b:
            count=count+1
print(count)


# Return all non-repeating numbers
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 3, 5]
# nums = [1, 2, 2, 3, 4, 4, 5]
# result = []

for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    if count == 1:
        result.append(i)

print(result)



# Given an array print the difference between the maximum and minimum element without using max() and min() built-in functions
# For example:
# TestResultmin_max_diff([9, 3, 1, 7, 6])
# 8
nums=[9, 3, 1, 7, 6]
max_count=nums[0]
min_count=nums[0]
 
for i in nums:
    if i  > max_count:
        max_count=i
        
    elif i < min_count:
        min_count=i
        
        
print(max_count - min_count)



def highest_marks(names, maths, physics, chemistry):
    # enter your code here
    my_name = ""
    for i in range(len(names)):
        if maths[i] > 90 and physics[i] > 90 and chemistry[i] > 90:
            total = maths[i] + physics[i] + chemistry[i]
            my_name = names[i]
    if total:
        print(my_name)
    else:
        print("No student found")
 
highest_marks(["jason", "priya", "madhan", "syed"],


              [91, 92, 99, 75],
              [91, 89, 100, 90],
              [91, 95, 100, 90])

# # mississippi-> count letters

def check(n):
    b = ""
    for i in n:
        count = 0
        if i not in b:
            for j in n:
                if i == j:
                    count+=1
                    b+=i
            print(i,"->",count)
check("mississippi")


#  method -2


def check(x):
    b=""
    a=x[0]
    b+=a
    count=0
    for el in range(1,len(x)):
        if x[el] not in b:
            b+=x[el]
    # print(b)
    for j in b:
        for i in x:
            if i == j:
                count+=1
        print(j,"->",count)
        count=0
    
check("mississipi")




# - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# ```python
# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

# Input:  nums = [1,2,3,4]
# Output: False

# method-1

def is_even(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                print(True)
                return
    print(False)    
is_even([1,2,3,1])

# method-2

nums = [1,2,3,4,1]
new = []

for i in nums:
    if i in new:
        result = True
        break
    new.append(i)
    print(new)
else:
    result = False

print(result)


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


            
nums=[3,2,4]
target=6
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i],nums[j])