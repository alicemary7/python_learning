### Lists

# - Given a list of words, print only the ones that start with an uppercase letter.
#   Use a single loop to check their first character.

# ```python
# # test case 1
# Input: ["Apple", "ball", "Cat", "dog"]
# Output: Apple Cat
#Explanation: They start with capital letters.

# problem -1



num=["Apple","ball","Cat","dog"]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new=""
for i in num:
    if i[0] in alpha:
        new+=i+" "
print(new)
        


# - Given two equal-length arrays maths and science,
#   return the indexes of students who scored > 80 in both subjects.

# ```python
# #test case 1
# Input:
# maths [92, 45, 81], science [88, 90, 70]

# Output: [0]


# problem -2


maths=[92,45,81]
science=[88,90,70]
new=[]
for i in range(0,len(maths)):
    if maths[i] >80 and science[i]> 80:
        new.append(i)
print(new)




# Filter numbers satisfying 3 conditions
#   Problem:
#   Print numbers that:
# 1. are 4 digits
# 2. end with an even digit
# ```python
# #Test Case:
# Input: [2481, 3572, 602, 7890, 4213]
# Expected Output: [3572,7890 ,4213]
# ```

n=[2481, 3572, 602, 7890, 4213]
new=[]
for el in n:
    if el>999 and el<10000 and el%2==0:
        new.append(el)
print(new)




### Strings

# - From a string, collect all the lowercase letters in the same order.
#   Use a single loop to scan the string.

# ```python
# # test case 1
# Input: "PyTHonProGRam"
# Output: "yonroam"


def upper_case(num):
    new="" 
    alpha="abcdefghijklmnopqrstuvwxyz"
    for el in num:
        if el in alpha:
            new=new+el
print(new)
upper_case("PyTHonProGRam")
