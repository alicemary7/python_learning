def move_zeros(nums):
    list_no=[]
    count=0
    for n in nums:
        if n==0:
            count+=1
        else:
            list_no.append(n)
    list_no+=[0]*count
    return list_no



print(move_zeros([0, 1, 0, 3, 12]))


# Find Second Largest Number
# Write a Python program to find the second largest number in a list without using max() or sort().
#  Example:
#  Input → [10, 40, 30, 20, 50]
#  Output → 40

def second_largest(numbers):
    first = second = -100  # Start with very small numbers

    for num in numbers:
        if num > first:
            second = first
            first=num
        elif num > second and num != first:
            second = num
             
    return second
print(second_largest([10,20,30,40]))

# Write a Python program to find the sum of digits of a number (don’t convert to string).
#  Example:
#  Input → 987
#  Output → 24 (9 + 8 + 7)
            
# def sumof_no(num):
#     s=0
#     for i in range(1,num+1,+1):
#         s=s+i
#         print(s)
            
# sumof_no(24)

# Given an array of integers, move all zeros to the end without changing the order of the non-zero elements.
# Example Input:
#  [0, 1, 0, 3, 12]
# Example Output:
#  [1, 3, 12, 0, 0]

def move_zeros(nums):
    list_no=[]
    count=0
    for n in nums:
        if n==0:
            count+=1
        else:
            list_no.append(n)
    list_no+=[0]*count
    return list_no



print(move_zeros([0, 1, 0, 3, 12]))  
# Output: [1, 3, 12, 0, 0]



# first letter vowel

word = "i the man is aiming an animal to kill"
v="aeiou"
count=0
if word[0] in v:
    count = count + 1
print(count)
for i in range (0,len(word)):
    if word[i] == " ":
        if word[i+1] in v:
            count = count+1
print(count)
        

        #   sum of digits

# num = int(input("Enter number: "))
# sum_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_digits += digit
#     num //= 10
# print("Sum of digits:", sum_digits)


#               add zero at end

nums = [0, 1, 0, 3, 12]
result = []
for n in nums:
    if n != 0:
        result.append(n)
zeros = [0] * nums.count(0)
print(result + zeros)


#                 show duplicates


# nums = [1, 2, 3, 1, 2, 4]
# dupes = []
# for n in nums:
#     if nums.count(n) > 1 and n not in dupes:
#         dupes.append(n)
# print("Duplicates:", dupes)