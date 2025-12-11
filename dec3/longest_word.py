# Write a Python program to find and print the longest word in a given sentence.

# ```python
# Sample Input: "Python makes programming enjoyable"
# Sample Output: "programming"


def longest_word(word):
    new=word.split(" ")
    for n in new:
        print(len(n))
        

longest_word("Python makes programming enjoyable")  
    
