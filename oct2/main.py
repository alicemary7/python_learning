def generate_series(n):
    output = ""
    for i in range(1, n):
        term = i * 2
        output = output + str(term) + " "
    print (output)