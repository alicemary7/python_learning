def remove_repeated_word(word):
    result=""
    count=0
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            if word[i]== word[j]:
                count+=1
        if count<1:
            result+=word[i]
        count=0
    print(result)
    
remove_repeated_word("hellloo") 