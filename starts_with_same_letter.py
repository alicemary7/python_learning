# An array of strings.
# Task:
#  Print all strings that start with the same first letter as the previous string.
#  Use just one loop.
# Example:
#  Input: ["cat", "cow", "dog", "door", "doll", "fish"]
#  Output: cow, door, doll
#  (cow starts with c like cat, door starts with d like dog, doll starts with d like dog


def same_letters(words):
    result=[]
    for i in range(0,len(words)):
        if words[i][0] == words[i-1][0]:
            result.append(words[i])
    print(result)
same_letters(["cat", "cow", "dog", "door", "doll", "fish"])


