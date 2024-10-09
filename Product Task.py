'''class product:
    Name:''
    Id:0
    Quantity:0                                       #PRODUCT Task(class & object)
    Price:0
    Expire:0
    def getdetails(self):
        self.Name=input("Enter the name:")
        self.Id=input("Enter the id:")
        self.Price=int(input("Enter the price:"))
        self.Quantity=int(input("Enter the quantity:"))
        self.Expire=input("Enter the expire Date:")
        
    def print(self):
        print(self.Name)
        print(self.Id)
        print(self.Quantity)
        print(self.Price)
        print(self.Expire)
        print("Total Amt:",self.Price*self.Quantity)

    


    
           
ram=product()
ram.getdetails()
ram.print()'''



'''class product:
    Name:''
    Id:0
    Quantity:0                                       
    Price:0
    Expire:0
    def getdetails(self):
        self.Name=input("Enter the name:")
        self.Id=input("Enter the id:")
        self.Price=int(input("Enter the price:"))
        self.Quantity=int(input("Enter the quantity:"))
        self.Expire=input("Enter the expire Date:")
class product1(product):
    def print(self):
        print(self.Name)
        print(self.Id)
        print(self.Quantity)
        print(self.Price)
        print(self.Expire)
        print("Total Amt:",self.Price*self.Quantity)
        
a1=product1()
a1.getdetails()
a1.print()'''



class Product:
    def __init__(self):
        self.Name = ''
        self.Id = 0
        self.Quantity = 0
        self.Price = 0
        self.Expire = ''

    def get_details(self):
        self.Name = input("Enter the name: ")
        self.Id = input("Enter the id: ")
        self.Price = int(input("Enter the price: "))
        self.Quantity = int(input("Enter the quantity: "))
        self.Expire = input("Enter the expire date: ")

class Product1(Product):
    def print_details(self):
        print(f"Name: {self.Name}")
        print(f"Id: {self.Id}")
        print(f"Quantity: {self.Quantity}")
        print(f"Price: {self.Price}")
        print(f"Expire Date: {self.Expire}")
        print(f"Total Amount: {self.Price * self.Quantity}")

class Product2(Product1):
    def discount_price(self, discount_percent):
        total_amount = self.Price * self.Quantity
        discount_amount = (discount_percent / 100) * total_amount
        final_amount = total_amount - discount_amount
        print(f"Final Amount after {discount_percent}% discount: {final_amount}")


csr = Product2()
csr.get_details()
csr.print_details()
csr.discount_price(10)                                                               # Applying a 10% discount











        
        
    


      








    
