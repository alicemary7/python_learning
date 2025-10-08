# Question-1

tara=int(input())
jyoti=int(input())
sum=tara+jyoti
print(sum)
if sum%5==0:
    print("1")
else:
    print("0")

# Question-2

N=int(input())
if N%7==0:
    print("yes")
else:
    print("no")

# Question-3

or_amount=int(input())
charge=50
if or_amount>500:
    print("Free Delivery,Total Amount is",or_amount)
else :
    print("Total Amount is",or_amount+charge)

# Question-4

mark=int(input(""))
if 80<= mark <=100 :
    print("s")
elif 60<= mark <=79:
    print("A")
elif 50<= mark <=59:
    print("B")
elif 40<= mark <=49:
    print("E")
else:
    print("Fail")
