class ContactBook:
    def __init__(self):
        self.contact=[]
    def add_contact(self,name,phone_no,email):
        my_contact={"name":name,"phone_no":phone_no,"email":email}
        self.contact.append(my_contact)
    def get_phone(self,name):
        for el in self.contact:
            if el["name"]==name:
                print(el["phone_no"])
    def update_phone(self,name,phone_no):
        for el in self.contact:
            if el["name"]==name:
                el["phone_no"]=phone_no
                print(self.contact)

    def remove_contact(self,name):
        for el in self.contact:
            if el["name"]==name:
                self.contact.remove(el["name"])
    
my_book=ContactBook()
my_book.add_contact("alice","123456789","alice@123")
my_book.add_contact("ashwin","123456789","ashwin@123")


my_book.get_phone("alice")
my_book.update_phone("alice","987654321")
my_book.remove_contact("alice")
