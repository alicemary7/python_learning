x = 10
print("x="+ str(x))

pi = 3.14
print("pi=" + str(pi))

name = "Rajnikanth"
print("My name is " + name)

firstName = "Stephen"
lastName = "Hawking"
# + is a string concatenation operator
fullname = firstName +" "+ lastName 
print(fullname)

# Converting String to Integer
age_str = "23"
age_num = int(age_str) + 20
print(age_num)  # Output: 43

# Converting String to Float
pi_str = "3.14"
pi_float_num = float(pi_str)
print(pi_float_num)  # Output: 3.14

# Converting Float to Integer
num_float = 31.01
print(num_float)  # Output: 31.01

# Removing the Fractional Part
import math
num_int = math.trunc(num_float)
print(num_int)  # Output: 3