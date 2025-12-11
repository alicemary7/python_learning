# 3. Write a python program to find the words that has 
# more than 4 characters
# Sample Input:
# This is a python program
# Sample Output:
# python
# program


def morethan_4charc(s):
    words=s.split(" ")
    for word in words:
        if len(word) > 4:
            print(word)
            
morethan_4charc("This is a python program")