# class Car:
#     def __init__(self,model,brand):
#         self.model=model
#         self.brand=brand
#     def start(self):
#     #     print("Car")
#     # def display(self,model,brand):
#     #     print(self.model)
#     #     print(self.brand)

# a = [2,7,6,4,3,0,1]


# Question 3: Default Values
# Create a class Employee with:
# __init__(self, name, salary=30000) → salary should have a default value if not given
# show() → print name and salary
# Expected Output:

# Employee: Rajan, Salary: 30000
# Employee: Meena, Salary: 45000

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         print(f"Employee :{self.name}")
#         print(f"Salary:{self.salary}")
        
# new=Employee("Alice",10000)
# new.show()
        
# Question 4: Area Calculator
# Create a class Rectangle with:
# __init__(self, length, width)
# area() → returns area (length × width)
# Expected Output:

# Area of Rectangle: 50

# class Rectangle:
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         print(f"Area of Rectangle:{self.length*self.breadth}")
# new=Rectangle(3,6)
# new.area()

# Question 5: Simple Bank Account
# Create a class BankAccount with:
# __init__(self, name, balance)
# deposit(amount) → adds money
# withdraw(amount) → subtracts money if balance enough
# display() → prints name and current balance
# Expected Output:

# Deposited: 500
# Withdrawn: 200
# Current Balance: 1300

# class BankAccount:
#     def __init__(self,name,balance,amount):
#         self.name=name
#         self.balance=balance
#         self.amount=amount
#     def deposit(self,amount):
#         self.balance+=self.amount
#         print(self.balance)
#     def withdraw(self,amount):
#         if self.balance>=self.amount:
#             self.balance-=self.amount
#             print(self.balance)
            
#         else:
#             print("Balance not available")
#     def display(self):
#         print(self.name)
#         print(self.balance)
# new=BankAccount("Alice",1000,1000)
# new.withdraw(1000)


# Question 6: Student Marks
# Create a class Student with:
# __init__(self, name, mark1, mark2, mark3)
# average() → prints average of 3 marks
# Expected Output:

# Student: Irfana
# Average: 87.0
        
        
# class Student:
    
#     def __init__(self,name,mark1,mark2,mark3):
#         self.name=name
#         self.marks=[mark1,mark2,mark3]
#     def average(self):
#         for i in self.marks:
#             count=0
#             total=0
#             total+=i
#             count+=1
#         avg=total/count
#         print(avg)
# new=Student("Alice",99,99,10)
# new.average()



# Create a class called Library with the following features:
# Attributes:
# books → a list that stores book names
# Methods:
# add_book(book_name) → adds a book to the list
# remove_book(book_name) → removes a book if it exists
# display_books() → prints all books available


# class Library:
#     def __init__(self,books):
#         self.books=["Alice in Wonderland"]
#     def add_book(self,book_name):
         
#         self.book_name=book_name
#         self.books.append(self.book_name)
#         print(self.books)
#     def remove_books(self,book_name):
#         if self.book_name in self.books:
#             self.books.remove(self.book_name)
#             print(self.books)
#         else:
#             print("The book is not in library")
#     def available_books(self):
#         print(self.books)
        
# new=Library("")
# new.add_book("Moana")
# new.add_book("Jungle Book")
# new.remove_books("Moanna")
# new.available_books()
        
    
# class Fruits:
#     def __init__(self,color):
#         self.color=color
# apple=Fruits("Red")
# print(apple.color)
    
# class Teacher:
#     def __init__(self,name,reg_no):
#         self.name=name
#         self.reg_no=reg_no
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Regno:{self.reg_no}")
        
# t1=Teacher("Alice",1)
# t2=Teacher("Anuja",2)
# t1.display()
# t2.display()



# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(f"Add:{self.a+self.b}")
#     def sub(self):
#         print(f"Subtract:{self.a-self.b}")
#     def mul(self):
#         print(f"MUltiplication:{self.a*self.b}")
#     def div(self):
#         print(f"Division:{self.a/self.b}")
# new=Calculator(20,10)
# new.add()
# new.sub()
# new.mul()
# new.div()


# class MovieTickets:
#     # constructor
#     def __init__(self):
#         self.movies = []

#     # methods
#     def add_movie(self, title, price, seat):
#         # current movie
#         current_movie = {"title": title, "price": price, "seats": seat}
#         # appending the movie to existing movies list
#         self.movies.append(current_movie)
#         print(f"Admin has added the movie - {title}")

#     def book_ticket(self, curr_show, friends_count):
#         # count - {seat} = revised_count
#         for el in self.movies:
#             # finding title of movie
#             if el["title"] == curr_show:
#                 # seat - decrease
#                 if friends_count > el["seats"]:
#                     return "Invalid Ticket count"
#                 else:
#                     el["seats"] -= friends_count
#                     print(f"{curr_show} - tickets {friends_count} sold out ")

#     def cancel_ticket(self, title, count):
#         for el in self.movies:
#             if el["title"] == title:
#                 el["seats"] += count
#                 print(f"{count} tickets for {title} have been cancelled.")
            
#         print("Movie not found!")

#     def check_availability(self, title):
#         result = 0
#         for el in self.movies:
#             if title == el["title"]:
#                 result = el["seats"]
#         print(f"{title} - current seat is {result}")

#     # extra method
#     def print_movies(self):
#         print(self.movies)


# bsr mall
# mall_bsr = MovieTickets()
# mall_bsr.add_movie(title="Interstellar", price=200, seat=100)
# mall_bsr.add_movie(title="Tenet", price=250, seat=150)

# # print entire movies
# mall_bsr.print_movies()

# # check availability
# mall_bsr.check_availability("Tenet")

# # ticket booking
# mall_bsr.book_ticket(curr_show="Interstellar", friends_count=20)
# mall_bsr.print_movies()
# mall_bsr.book_ticket(curr_show="Interstellar", friends_count=30)
# mall_bsr.check_availability(title="Interstellar")
# mall_bsr.cancel_ticket("Interstellar",)