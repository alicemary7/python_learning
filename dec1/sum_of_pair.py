# Find All Pairs That Sum to a Target (without using set or map)
# Input: [1,5,7,-1,5], target = 6
#  Output:
#  Pairs: (1,5), (7,-1), (1,5)
 
 
 
n=[1,5,7,-1,5]
t=6
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]== t:
            print((n[i],n[j]))