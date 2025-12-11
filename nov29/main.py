# Print words whose middle character is a vowel, but only if len of the word is odd  the first and last characters are consonants.

# words = ["cat", "idea", "apple", "road", "pep", "axis"]
# Expected printed output:
# cat
# pep

def middle(n):
    new=[]
    v="aeiou"
    for el in n:
        if len(el) %2!=0:
            middle=len(el)//2
            if el[middle] in v:
                if el[0] not in  v and el[-1] not in v:
                    new.append(el)
    print(new)
middle(["cat", "idea", "apple", "road", "pep", "axis","pie"])
            


# Given a list and a target value, return all indices where the target appears.
#  Example: [1, 2, 3, 2, 4, 2] → target 2 → indices [1, 3, 5].

n=[1, 2, 3, 2, 4, 2] 
x=2
for i in range(len(n)):
    if n[i] == x:
        print(i)




# . Keep Words Whose Vowels Follow the Pattern: a → e → i → o → u

# (Order must increase)**
# Example: "abeiou" → valid
# "aeiaou" → invalid (i comes before e)

# Input: ["aeiou", "aei", "aeuio", "aeeiou"]
# Output: aeiou aei aeeiou

word=["aeiou", "aei", "aeuio", "aeeiou"]
v="aeiou"
new=[]

for i in range(0,len(v)):
    if v[i] not in new:
        new.append(word)
print(new)


# Given a list of words, return only the words having length greater than 5.
# Input: ["car", "laptop", "python", "pen"]
# Output: ["laptop", "python"]

n=["car", "laptop", "python", "pen"]
new=[]
for el in n:
    if len(el)> 5:
        new.append(el)
print(new)


# Keep words where uppercase letters are more than lowercase.
# Input: ["HeLLo", "WORLD", "python", "ApP"]
#  Output: WORLD ApP


word=["HeLLo", "WORLD", "python", "ApP"]
count=0
c=0
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for el in word:
    for j in el:
        if j in alpha:
            count=count+1
        else:
            c=c+1
    if count >c:
        print(el)
    count = 0
    c = 0
   
   
#  Prime no
   
   
n = 7
def find_prime(n):
    res = None
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
            break
        return  True
    

a = [42, 57, 88, 91,21]
value = 0
for i in a:
    num = i
    while i > 0:
        b = i % 10
        i = i//10
        value = value +b
    if find_prime(value):
        print(num)
        
    


# without using split()

a = "hello world"
words = ''
w = ''

for i in a:
    if i == " ":
      words = words +w
      print(words)
      w = ''
    else:
        w = i+w
words = words +" " +w

print(words)
        
        
# Remove Consecutive Duplicate Characters
# Given a string, remove only consecutive duplicate characters.
#  Example: "aabbccaaa" → "abc ",


inputs = "aabbccaaaa","gghhhff"
for s in inputs:
    result = ""
    for i in range(len(s)):
        if s[i] != s[i-1]:
            result += s[i]
    print(result)


# input  = 'the python is art'
# output -->the nohtyp is art

n='the python is art'
new=n.split(" ")
n=""
for el in new:
    if len(el)>3:
        n=n+" "+el[::-1]
    else:
        n=n+" "+el
print(n)


# Merge Two Lists by Alternating Elements
# Given two lists of equal length, create a new list by taking one element from each list alternately.
#  Example: [1,2,3] & ["a","b","c"] → [1,"a",2,"b",3,"c"].

n=[1,2,3]
w=["a","b","c"]
new=[]
for i in range(0,len(n)):
    new.append(n[i])
    new.append(w[i])
print(new)

# Count Words That Start With a Vowel
# Given a list of words, count how many begin with vowels (a,e,i,o,u).


w=["Alice","Ashwin","Irafana","jayasuriya","baalaji"]
v="aeiouAEIOU"
count=0
for el in w:
    if el[0] in v:
        count+=1
print(count)



# Filter numbers that contain digit '0' in the end.
# Input: [10, 101, 2005, 340, 89]
#  Output: 10 340  


n=[10, 101, 2005, 340, 89]
for el in n:
    new=str(el)
    if new[-1]=="0":
        print(el)