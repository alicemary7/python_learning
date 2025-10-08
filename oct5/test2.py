# Question-1

# age=int(input())
# if age<18:
#     print("150")
# elif age>=18 and age<=60:
#     print("250")
# elif age>60:
#     print("100")
# else:
#     print("invalid")

# Question-2

# age=int(input())
# if age<12:
#     ticket=50
# elif age>=12 and age<=59:
#     ticket=120
# else:
#     ticket=80
# if age%2==0:
#     ticket-=5
# print(ticket)

# QUESTION3

# m=int(input())
# n=0
# if m>0:
#     n=m%5
#     m//=5
#     print("Full Bucket",m)
#     print("Left over  mangoes is",n)

# Question5

# n=int(input())
# x=int(input())
# if x>=100:
#     print(n*10/100)
# elif x>=55 and x<=99:
#     print(n*5/100)
# else:
#     print(n)

# Question6
# n=int(input())
# if n<=5000:
#     print(n*5/100)
# elif n>=5001 and n<=10000:
#     print(n*10/100)
# else:
#     print(n*15/100)

#  Question7
# p=int(input())
# if p>100:
#     print(p*10/100)
# elif p>=50 and p<=100:
#     print(p*5/100)
# else:
#     print(p)

#Question8

# e=input()
# if e==".csv":
#     print("This is an Excel file")
# elif e==".jpg":
#     print("This iS an JPEG file")
# elif e==".doc":
#     print("This iS an Word file")
# elif e==".pdf":
#     print("This iS an PDF file")
# elif e==".py":
#     print("This iS an Python file")
# else:
#     print("Unknown file type")

# Question9

k=int(input())
if k<=10 :
    print(k*15)
elif k>10 and k<=20:
    print(k*12)
else:
    print(k*10)

# Question10

# n=int(input())
# if n%2==0:
#     for i in range (1,n)


# PRACTICE PROBLEM
# QUESTION1
# for i in range (1,6):
#     print(i)

# a=1
# while a<=5:
#     print(a)
#     a+=1

# Question2

# a=1
# b=100
# count= 0
# n=int(input("enter"))
# while a<=b:

#     if a%n==0:
#         count = count + 1
       
#     a+=1
# print(count)

# Question3

# n=int(input("enter the value of n :"))
# point = 0

# if n>=1000:
#     count=(n//1000)*5
#     point = point +count
#     if n>=5000:
#         count = (n//5000)*20
#         point=point+count
# else:
#     print("invalid input")
# print("total star points",point)

#fibonacci


fact=1
a=0
while a>=10:
    fact=fact+1
    a=a-1
    print(fact)

 