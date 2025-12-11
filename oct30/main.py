# # Create a class BankAccount with attributes name and balance.
# # Add methods deposit(amount) and withdraw(amount) that update the balance and showbalance().
# # Prevent withdrawal if the balance is less than the amount and print a warning message.
# # Create two BankAccount objects and try deposit and withdraw money from the account
# # Bonus: simulate a transfer(amount, to_account) method to transfer between two bank accounts


# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"{self.name}{amount} deposited:Rupees{self.balance}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient money")
#         else:
#             self.balance-=amount
#             print(f"{self.name}{amount} withdraw amount: Rupees{self.balance}")
            
#     def transfer(self, amount, to_account):
#         if amount> self.balance:
#             print(f"Transfer failed! {self.name}{amount} doesn’t have enough balance.")
#         else:
#             self.balance -= amount
#             to_account.balance += amount
#             print(f"₹{amount} transferred from {self.name} to {to_account.name} and current balance of {self.name} is {self.balance}.")
    
# Alice = BankAccount("Alice", 5000)
# Bob = BankAccount("Bob", 3000)
# Alice.deposit(2000)
# Bob.withdraw(1000)
# Bob.withdraw(1000)  
# Alice.transfer(1500, Bob)

# 2. Create a class LibraryBook with attributes title, author, and available_copies.
# Add the following methods:
# borrow_book() → Decreases available copies by 1 if available.
# If no copies are left, print “Book not available!”
# return_book() → Increases available copies by 1.
# show_status() → Displays the title, author, and available copies.
# Create two LibraryBook objects and simulate borrowing and returning books.

# class LibraryBook:
#     def __init__(self, title, author, available_copies):
#         self.title = title
#         self.author = author
#         self.available_copies = available_copies

#     def borrow_book(self):
#         if self.available_copies >= 1:
#             self.available_copies -= 1
#             print(f"Borrowed '{self.title}'. Copies left: {self.available_copies}")
#         else:
#             print(f"'{self.title}' is not available right now 😢")

#     def return_book(self):
#         self.available_copies += 1
#         print(f"Returned '{self.title}'. Copies now: {self.available_copies}")

#     def show_status(self):
#         print(f"📘 Title: {self.title}\n✍️ Author: {self.author}\n📚 Available Copies: {self.available_copies}\n")

# # Create book objects
# book1 = LibraryBook("Harry Potter", "J.K. Rowling", 3)
# book2 = LibraryBook("Atomic Habits", "James Clear", 1)

# # Show status
# book1.show_status()
# book2.show_status()

# # Borrow and return books
# book1.borrow_book()
# book1.borrow_book()
# book1.return_book()

# book2.borrow_book()
# book2.borrow_book()  # Should show "not available"
# book2.return_book()



# class Calculator():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
          
#     def add(self):
#         print(self.a+self.b)
#     def subtract(self):
#         print(self.a-self.b)
#     def multiply(self):
#         print(self.a*self.b)
    
#     try:
#         def divide(self):
#             print(self.a /self.b)
#     expect:


# var1=Calculator(10,20)
# var1.add()        



# parent
# class Factory:
#     def __init__(self):
#         pass

#     def make_vehicle(self):
#         print("I am making a general vehicle")


# # class Child_class_name(Parent_Class_name)
# class CarFactory(Factory):
#     def __init__(self):
#         pass

#     # manufacturing cars
#     def make_cars(self):
#         print("I am manufacturing only CARS")

#     def make_vehicle(self):
#         print("I am changing my grandparent class to my own")


# class BikeFactory(Factory):
#     def __init__(self):
#         pass

#     def make_bikes(self):
#         print("I am manufacturing only bikes")

#     def make_vehicle(self):
#         print("I am changing my grandparent class to my own")


# new_car_factory = CarFactory()
# # self property
# new_car_factory.make_cars()
# # parent property
# new_car_factory.make_vehicle()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  
        

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        

# Example
student1 = Student("Alice", 20)
student1.show_details()