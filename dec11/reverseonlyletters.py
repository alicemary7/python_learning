# Reverse only the words, not the whole sentence
# Input: "I love python"
#  Output → "I evol nohtyp"


def reverse_only_letters(sen):
    result=[]
    word=""
    words=""
    for el in sen:
        if el ==" ":
            result.append(word[::-1])
            word=""
        else:
            word=word+el
    
    result.append(word[::-1])
    for el in result:
        words=words+el+" "
    print(words)
reverse_only_letters("I love python")




# sentence = "I love python"
# result=""
# words = sentence.split()      
# # reversed_words = words[::-1]
# for el in words:
#     new=el[::-1]
#     result=result+new+" "
# print(result)


def reverse_only_letters(sen):
    result=[]
    word=""
    words=""
    for el in sen:
        if el ==" ":
            result.append(word)
            word=""
        else:
            word=word+el
    
    result.append(word)
    for el in result:
        words=el+" "+words
    print(words)
reverse_only_letters("I love python")

    
