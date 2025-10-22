# def calculator(operator, number1, number2):
#     match operator:
#         case '+':
#             print(number1 + number2)
#         case '-':
#             print(number1 - number2)
#         case '*':
#             print(number1 * number2)
#         case '/':
#             print(number1 / number2)
#         case _:
#             print("invalid operator")
        
# QUESTION 1
age=int(input())
if  0>= age <=5:
   print("Free")
elif 5< age >=13 :
   print("10")
elif age>13 and age<64:
   print("20")
elif age>65:
   print("15")
else:
   print("invalid")
