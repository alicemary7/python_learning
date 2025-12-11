# Write a program to read a list of integers containing exactly two zeros.
# Your task is to print all the numbers that appear between these two zeros, without using slicing or nested loops.

# If there is no closing zero after the first one, print -1.

# Example 1:

# Input: [1, 2, 0, 3, 4, 5, 0, 6, 7] Output: [3, 4, 5]


# a = [1,2,3,0,4,5,6,0,7,8]
# first = 0
# second = 0
# result = []
# for i in range (0,len(a)):
#     if a[i] == 0:
#         first = i
#         break
  

# for j in range(first+1,len(a)):
#     if a[j] == 0:
#         second = j
#         break
 

# for k in range(first+1,second):
#     if k!=0:
#         result.append(k)
#     else:
#         print(result)
# print(result)  




# Count Words in a Sentence
# Question:
#  Write a program to count how many words are present in a given sentence.
# You must:
# Solve it using split(), and
# Solve it without using split(), by counting spaces manually.
# Given:

# text = "Python is a powerful language"
# Expected Output:

# Total words: 5

# method 1

# text = "Python is a powerful language"
# count=1
# for i in text:
#     if i ==" ":
#         count=count+1
        
# print(count)
         
         
    # method2
    
text = "Python is a powerful language"    
word=text.split(" ")
count=0
for i in word:
    count+=1
print(count)


# maximum count

num="success"
count=1
max_count=1
for i in range(0,len(num),+1):
    for j in range(i+1,len(num),+1):
        if num[i]==num[j]:
            count=count+1
    if count>max_count:
        max_count=count
    count = 1
print(max_count)
