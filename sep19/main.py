# Question1

x=int(input())
y=int(input())
sum=x+y
if sum%2==0:
    print("even")
else:
    print("odd")

Question2

n = int(input("enter the value"))
m = int(input("enter the value of m"))
j = int(input("enter the value of j"))
n = 59
m =5+9
j = 5*9
if m+j >=n:
    print("great")
else :
    print("not")

Question3


consumer = input("Enter consumer type (a for Residential, b for Commercial): ")
unit = int(input("Enter number of units: "))

a = "Residential"
b = "Commercial"

if consumer == "a" and 0 < unit <= 100:
    print(unit*3)
elif consumer == "a" and 101 <= unit <= 200:
    print(unit*5)
elif consumer == "a" and unit > 200:
    print(unit*7)
elif consumer == "b" and 0 < unit <= 100:
    print(unit*3)
elif consumer == "b" and 101 <= unit <= 200:
    print(unit*5)
elif consumer == "b" and unit > 200:
    print(unit*7)
else:
    print("Invalid")

Question4

d=int(input())
if d<=5:
    print("50")
elif 6<=d<=15:
    print(8*d)
elif d>15:
    print(6*d)
else:
    print("invalid")

Question6

n=int(input())
if n ==0:
    print(0)
elif n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%5==0:
    print("Buzz")
elif n%3==0:
    print("Fizz")
else:
    print(n)

Question7

s=input()
if s=="Science":
    print("Medical"or"Engineering")
elif s=="Commerce":
    print("CA" or "B.com")
elif e=="Arts":
    print("History"or"Literature")
else:
    print("Invalid")

Question8

m=int(input())
if 9<=m<=12:
    print("Morning Show")
elif 12<m<=16:
    print("Matinee Show")
elif 16<m<=20:
    print("Evening Show")
else:
    print("Night Show")

Question10

mode=input()
if mode=="UPI":
    print("You selected UPI Payment")
elif mode=="Card":
    print("You selected Credit/debit Card Payment")
elif mode=="Netbanking":
    print("You Selected Netbanking")
elif mode=="COD":
    print("You Selected Cash on Delivery")
else:
    print("Invalid Payment mode")




