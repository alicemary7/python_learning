# Count how many words start with a vowel
# Problem:
# Use split() to extract words and count the ones starting with a, e, i, o, u.
# Input:
# "apple is on the orange table"
# Output:
# 4

        
n="apple is on the orange table"
m=n.split(" ")
x="aeiou"
count=0
for el in m:
    if el[0] in x:
        count+=1
print(count)