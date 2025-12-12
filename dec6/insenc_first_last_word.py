# Return the first and last word
# Input:
#  "split makes string handling easy"
#  Output:
#  ["split", "easy"]



n="split makes string handling easy"
word=""
res=[]
result=[]
for el in n:
    if el ==" ":
        res.append(word)
        word=""
    else:
        word+=el
res.append(word)
for i in range(0,len(res),len(res)-1):
    result.append(res[i])
print(result)