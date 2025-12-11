# 2. Write a Python program to find the word that has maximum number of vowels from the given sentence
# Sample Input:
# Learning Python is interesting
# Sample Output:

# interesting
      
       
def max_vowels(s):
    v="aeiou"
    words=s.split(" ")
    count=0
    max_count=0
    new=0
    for word in words:
        for i in range(len(word)):
            # print(word[i])
            if word[i] in v:
                count=count+1
        
            if count > max_count:
                max_count=count
                new= word
        count=0
    print(new)
max_vowels("Learning Python is interesting owl")