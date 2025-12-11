#  Write a Python program to remove all duplicate characters from a given string and return the result.
#   The final string should contain only the first occurrence of each character, in the same order.

# ```python
# #test case 1
# Sample Input: 'programming'
# Sample Output: 'progamin'


def remove_duplicate(word):
    new=""
    for el in word:
        if el not in new:
            new=new+el
    print(new)
remove_duplicate("programming")
