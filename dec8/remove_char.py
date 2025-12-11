def remove_charc(word):
    result=""
    a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for el  in word:
        for letter in el:
            if letter in a:
                result+=el
            
            
    print(result)
remove_charc("Best-selling! Laptop 2024")