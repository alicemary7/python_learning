# - Write a function that merges two lists by taking elements alternately.

# ```python
# Input: x= [1, 2, 3] y= ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']


x= [1, 2, 3]
y= ['a', 'b', 'c']
new=[]
for i in range(0,len(x)):
    new.append(x[i])
    new.append(y[i])
print(new)


# - Write a Program that Keep Words That Start and End With the Same Letter

# ```python
# Case-insensitive matching.
# Example:
#  Input: ["level", "Apple", "mana", "cool"]
#  Output: ["level"]


num=["level", "Apple", "mana", "cool"]
for el in num:
    if el[0] == el[-1]:
        print(el)



# - Given a list of names, print only the ones that contain “a” or “A”.

# ```python
# Input: ["Meera", "John", "Kavi", "Sona"]
# Output: Meera Kavi Sona
# Explanation: These names include the letter 'a'


word=["Meera", "John", "Kavi", "Sona"]
for i in range(0,len(word)):
    if "a" in word[i] or "A" in word[i]:
        print(word[i])



# - Given a list of strings , For Each word, Check whether the length of the element is odd and the middle letter of that word must be a vowel , print the words line by line

# ```python
# # test case 1
# Input: ["cat", "read", "room", "hello", "sky"]
# Output: cat room hello


word=["cat", "read", "room", "hello", "sky"]
v="aeiou"
for el in word:
    if len(el) %2 != 0:
        mid = (len(el) // 2)
        if el[mid] in v:
            print(el)

            
