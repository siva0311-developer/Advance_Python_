#single inheritance
'''class person1():#parent 
    a=''
    b=0
    def getdetails(self):
        self.a=input("Enter Name:")
        self.b=input("Enter id:")
        
class person2(person1):#child
    def print(self):
        print(self.a)
        print(self.b)



a1=person2()
a1.getdetails()
a1.print()'''





#multi inhertance
'''class student():#parent 
    a=''
    b=0
    def getdetails(self):
        self.a=input("Enter Name:")
        self.b=input("Enter id:")
class subject():
    sub_name=''
    sub_mark=0
    def subdetails(self):
        self.sub_name=input("Enter subject name:")
        self.sub_mark=int(input("Enter a mark:"))
        
class person(student,subject):#child
    def print(self):
        print(self.a)
        print(self.b)
        print(self.sub_name)
        print(self.sub_mark)

x=person()
x.getdetails()
x.subdetails()
x.print()'''



#single inheritance
'''class parent():
    def print1(self):
        print("this is the lokii")
class child(parent):
    pass
a1=child()
a1.print1()'''




#multiple inheritance
'''class parent1:
    def c1(self):
        print("this is the first person")

class parent2:
    def c2(self):
        print("this the second person")


class child(parent1,parent2):
    pass

a1=child()
a1.c1()
a1.c2()'''
  


#multi level inheritance
'''class parent1:
    def c1(self):
        print("this is the first person")

class parent2(parent1):
    def c2(self):
        print("this the second person")


class child(parent2):
    pass

a1=child()
a1.c1()
a1.c2()



#hierarchical inheritance
class father:
    def c1(self):
        print("father")
class anna(father):
    def c2(self):
        print("anna")
class thambi(father):
    def c3(self):
        print("thambi")
a2=anna()
a2.c1()
a2.c2()
a1=thambi()
a1.c1()
a1.c3()'''


#hybrid inheritance
class father:
    def c1(self):
        print("father")
class anna(father):
    def c2(self):
        print("anna")
class thambi(father):
    def c3(self):
        print("thambi")
class cousin(anna,thambi):
    def c4(self):
        print("cousin")

'''
a3=cousin()
a3.c1()
a3.c2()
a3.c3()
a3.c4()
'''
#(or)

a3=[father(),anna(),thambi(),cousin()]

for i in a3:
    i.c1,c2,c3,c4()




    
    
