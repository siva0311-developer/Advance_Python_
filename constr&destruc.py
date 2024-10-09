'''
class person:
    def __init__(self,name,age):
        print("constructor is Executed")
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class person1:
    a='Hello1'
    __a1='Hello'
    def hello(self):
        print("constructor is executed")
        print(self.__a1)

a1=person('siva',21)
a2=person1()
a2.hello()
print(a2.a)

'''

#single inheritance
class student():#parent
    a=''
    b=0
    def getDetails(self):
       self.a=input("Enter Name:")
       self.b=input("Enter id:")

class Subject():
    sub_name=''
    sub_mark=0
    def subDetails():
        self.sub_name=input("Enter Subject Name:")
        self.sub_mark=input("Enter Subject Mark:")
        
class person2(student,subject):#child
    def print(self):
        print(self.a)
        print(self.b)
        print(self.sub_name)
        print(self.sub_mark)
    
a1=student()
a1.getDetails()
a1.subDetails()
a1.print()
    
        
        

  
