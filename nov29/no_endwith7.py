# Print numbers ending with digit 7
# Input: [17, 23, 47, 59, 70]
#  Output: 17 47

# n=[17, 23, 47, 59, 70]
# for el in n:
#     l=el%10
#     if l == 7:
#         print(el)


a = [42, 57, 88, 91]
value = 0
for i in a:
    while i > 0:
        b = i % 10
        c = i//10
        value = value +b
    print(value)
    break