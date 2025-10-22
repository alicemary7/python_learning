# Question-1

# Find all the sum of all numbers which are greater than a given number (eg a = [2, 3, 1, 4, 5] num = 3 answer = 9 (5 + 4))

# def check(a,b):
#     sum = 0
#     for i in a:
#         if i>b:
#             sum = sum+i
#     print(sum)
    
# check(a = [2, 3, 1, 4, 5],b = 3)            
        
# Question-2

# Print all the odd numbers in a given list.

# def check_odd_no(n):
#     for i in n:
#         if i%2!=0:
#             print(i)
            
# check_odd_no([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

# Question-3

# A mobile operator charges for internet data usage as follows:
# First 1 GB: ₹50
# Next 2 GB: ₹30 per GB
# Next 2 GB: ₹20 per GB
# Any usage above 5 GB: ₹10 per GB
# Additionally, a service tax of ₹15 is added to every bill.
#  If the data usage is negative, print "Invalid Input".
# Write a program that accepts data usage in GB and prints the total bill.
# Sample Input:
# 4
# Sample Output:
# 145

def total_bill(n):
    if n<=0:
        print("invalid input")
    else:
        initial=65
        if n==1:
            return initial
        elif n>=2 and n<=3:
            return initial+20*n
        elif n>=4 and n<=5:
            return initial+20*n
        else:
            return initial+10*n
            
print(total_bill(1))
print(total_bill(2))
print(total_bill(4))
print(total_bill(5))
print(total_bill(10))
print(total_bill(-18))



# Question-4
# Given a positive Integer, write a function isPrime(num) which will return true if its a prime or false otherwise.

# def is_prime_no(n):
#     if n<=1:
#         return False
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True
# print(is_prime_no(1))
# print(is_prime_no(3))
