# Rearrange by Length
# Given a list of words, rearrange them so shorter words come first.
#  (Don't use sort() or sorted())
# Input:
#  ["banana", "cat", "watermelon", "apple"]
# Output:
#  ["cat", "apple", "banana", "watermelon"]   

n=  ["banana", "cat", "watermelon", "apple"]
new=[]
temp=0
for i in range(0,len(n),+1):
    for j in range(i+1,len(n)):
        if len(n[i]) > len(n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)
