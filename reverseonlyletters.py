# Reverse only the words, not the whole sentence
# Input: "I love python"
#  Output → "I evol nohtyp"


def reverse_letters(senc):
    result=[]
    word=""
    b=""
    for i in range(len(senc)):
        if i ==" ":
            result.append(b)
            b=""
            
        else:
            b=b+senc[i]
    result.append(b)
    print(result)
    new=""
    # new+=result
    # print(new)
    for el in result:
        new=new+el+""
    print(new)





reverse_letters("I love python")
    
