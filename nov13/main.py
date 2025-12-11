# class ToDoList:
#     def __init__(self):
#         self.tasks=[]
#     def add_tasks(self,id,name,status):
#         my_task={"id":id,"name":name,"status":status}
#         self.tasks.append(my_task)
#     def view_tasks(self):
#         for task in self.tasks:
#             print(f"ID : {task['id']} , Name : {task['name']}, Status :{task['status']}")
         
         
#     def delete_tasks(self,task_id):
#         for i in self.tasks:
#             if i["id"] == task_id:
#                 self.tasks.remove(i)
#             else:
#                 print("The task is not available")

        

# new=ToDoList()
# new.add_tasks(1,"Alice","Sleeping")
# new.add_tasks(2,"Alice","Eating")
# new.add_tasks(3,"Alice","Studying Javascirpt")
# new.add_tasks(5,"Alice","Python pratices sum")
# new.view_tasks()
# new.delete_tasks(5)
# new.view_tasks()

# class Orders:
#     def __init__(self):
#         self.cart=[]
#     def add_items(self,id,product_name,quantity,price):
#         my_cart={"id":id,"product_name":product_name,"quantity":quantity,"price":price}
#         self.cart.append(my_cart)
#     def remove_items(self,user_id):
#         for i in self.cart:
#             if i["id"]==user_id:
#                 self.cart.remove(i)
#             else:
#                 print("The item is not found")
#     def total_cost(self,user_id):
#         for i in self.cart:
#             if i['id']== user_id:
#                 cost=i['quantity']*i['price']
#                 print(f"Total cost:{cost}")

# alice=Orders()
# alice.add_items(1,"puffs",2,30)
# alice.remove_items(2)
# alice.total_cost(1)


# Problem Statement: Simplified Customer Billing and Management System

# Design an Object-Oriented system using Python that manages customer records and their associated invoices. The system must utilize exactly **two classes**: `Customer` and `Invoice`, demonstrating a clear **compositional relationship** (where an `Invoice` object is created with and linked to a `Customer` object).

# ---
# ### `Customer` Class

# - **Purpose:** To store basic customer identification and maintain a record of all invoices associated with them.
# - **Attributes:** `customer_id` (Integer), `name` (String), `email` (String), and `invoices` (List of `Invoice` objects).
# - **Method:** `add_invoice(invoice)`: Adds an `Invoice` object to the customer's internal `invoices` list.

# ### `Invoice` Class

# - **Purpose:** To detail billed items and track the status and total amount owed by a specific customer.
# - **Inter-relation:** The constructor must accept and store an instance of the `Customer` class as an attribute (`self.customer`).
# - **Attributes:** `invoice_id` (String), `customer` (Customer Object), `items` (Dictionary: `{item_description: price_per_unit}`), and `is_paid` (Boolean, defaults to `False`).
# - **Methods:**
#   - `add_item(description, price)`: Adds or updates a line item.
#   - `remove_item(description)`: Deletes a specific line item.
#   - `calculate_total()`: Returns the sum of all prices.
#   - `display_details()`: Prints the invoice details, including status and total, accessing the customer's name via the inter-related `customer` attribute.