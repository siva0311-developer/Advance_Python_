
import datetime as d

print("LOGIN FORM")

class Login:
    def ram(self):
        self.UserName = ''
        self.Password = ''

    def getvalues(self):
        self.UserName = input("Enter The Username: ")
        self.Password = input("Enter The Password: ")
        
    def getdetails(self):
        
        if self.UserName=="siva" and self.Password=="amaran":
            print("Login Successful")
            self.x= (d.datetime.now()).date()
            self.printdetails()
        else:
            print("Login Failed")
    def printdetails(self):
        print(f"Last Log in Time :{self.x}")


amaran=Login()
amaran.getvalues()
amaran.getdetails()














'''
import datetime as d

print("LOGIN FORM")

a=input("Enter The UserName")

b=input("Enter The Password")

if(a=='siva' and b=='amaran'):
    print("View Login Form")
    x=input()
    print(d.datetime.now())
else:
    print("Login Form Invalid")

'''

