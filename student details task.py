'''
def ram():
    print("1.Enter student Details")
    print("2.View Details")
    print("3.Exist")
    Option=input("Enter The Option")


    
ram()
'''


'''class student:
    Students={}

    def person(self):
        while True: 
            print("1.Enter student Details")
            print("2.View Details")
            print("3.Search Rollno")
            print("4.Search Name")
            print("5.Search Major")
            print("6.Exist")
            Option=input("Enter The Option")

            if(Option=='1'):
                self.getvalues()
            elif(Option=='2'):
                self.viewDetails()
            elif(Option=='3'):
                self.getrollno()
            elif(Option=='4'):
                self.getname()
            elif(Option=='5'):
                self.getmajor()    
            elif(Option=='6'):
                print("Exiting....Bye")
                break
            else:
                print("Invalid Error")
                
    def getvalues(self):
        student_Rollno = input("Enter Student Rollno: ")
        name = input("Enter Student Name: ")
        major = input("Enter Student major: ")
        self.Students[student_Rollno] = {'Name': name, 'Major': major}
        print(f" Student Details Added successfully!")
       
        
    def viewDetails(self):
        if not self.Students:
            print("Enter Atleast One Student Details")
            
        else:
            for student_Rollno,Details in (self.Students.items()):
                print(f"Student Rollno: {student_Rollno}")
                print(f"Name:{Details['Name']}")
                print(f"Major:{Details['Major']}")
                
                     

    def getrollno(self):
        student_Rollno=input("Search The Student Rollno:")
        Details=self.Students.get(student_Rollno)
        if Details:
            print(f"Student Rollno: {student_Rollno}, Name: {Details['Name']}, Major: {Details['Major']}")
        else:
            print("Invalid rollno")
        

    def getname(self):
        name=input("Search The Student Name:")
        for Details in (self.Students.values()):
            if Details['Name']== name:
                print(f" RollNo:{self.students[student_Rollno]} Name: {Details['Name']}, Major: {Details['Major']}")
                return
        print("Name Not Found")
                
        
    def getmajor(self):
        major=input("Search The Student Major:")
        for Details in (self.Students.values()):
            if Details['Major']== major:
                print(f" Major: {Details['Major']}, Name: {Details['Name']} ")
                return
        print("Major Not Found")
                
ram=student()
ram.person()



'''

class student:
    Students={}

    def person(self):
        while True: 
            print("1.Enter student Details")
            print("2.View Details")
            print("3.Exist")
            Option=int(input())

            if(Option==1):
                self.getvalues()
                
            elif(Option==3):
                print("Exiting....Bye")
            
            elif(Option==2):
                self.viewDetails()
                print("\n1.Search by Rollno\n2.Search by Name\n3.Search by major")
                x=int(input())
                if x==1:
                    self.getrollno()
                elif x==2:
                    self.getname()
                elif x==3:
                    self.getmajor()
            else:
                print("Invalid Error")
                
    def getvalues(self):
        student_Rollno = input("Enter Student Rollno: ")
        name = input("Enter Student Name: ")
        major = input("Enter Student major: ")
        self.Students[student_Rollno] = {'Name': name, 'Major': major}
        print(f" Student Details Added successfully!")
       
        
    def viewDetails(self):
        if not self.Students:
            print("Enter Atleast One Student Details")
            
        else:
            for student_Rollno,Details in (self.Students.items()):
                print(f"Student Rollno: {student_Rollno}")
                print(f"Name:{Details['Name']}")
                print(f"Major:{Details['Major']}")
                
                     

    def getrollno(self):
        student_Rollno=input("Search The Student Rollno:")
        Details=self.Students.get(student_Rollno)
        if Details:
            print(f"Student Rollno: {student_Rollno}, Name: {Details['Name']}, Major: {Details['Major']}")
        else:
            print("Invalid rollno")
        

    def getname(self):
        name=input("Search The Student Name:")
        for Details in (self.Students.values()):
            if Details['Name']== name:
                print(f" Name: {Details['Name']}, Major: {Details['Major']}")
                return
        print("Name Not Found")
                
        
    def getmajor(self):
        major=input("Search The Student Major:")
        for Details in (self.Students.values()):
            if Details['Major']== major:
                print(f" Major: {Details['Major']}, Name: {Details['Name']} ")
                return
        print("Major Not Found")
                
ram=student()
ram.person()





















'''
a=int(input("1.Enter student Details"))
print("1.Enter student Details")
b=int(input("2.View Details"))
print("2.View Details")
c=int(input("3.Exist"))
print("3.Exist")

b=int(input("2.View Details"))
c=int(input("3.Exist"))

if(a==1):
    print("hey ram")
else:
    print("hey dude")

'''
'''
class student:
    Students={}
    field=['RollNo','Name','Major']
    temp={}

    def person(self):
        while True: 
            print("1.Enter student Details")
            print("2.View Details")
            print("3.Exist")
            Option=int(input())

            if(Option==1):
                self.getvalues()
                
            elif(Option==3):
                print("Exiting....Bye")
            
            elif(Option==2):
                self.viewDetails()
                print("\n1.Search by Rollno\n2.Search by Name\n3.Search by major")
                x=int(input())
                if x==1:
                    self.search('RollNo')
                elif x==2:
                    self.search('Name')
                elif x==3:
                    self.search('Major')
                else:
                    print('INvalid')
            else:
                print("Invalid Error")
                
    def getvalues(self):
        for i in self.field:
            t=input('Enter {} :'.format(i))
            if i=='RollNo':
                t=int(t)
                RollNo=t
            self.temp[i]=t
        self.Students[RollNo]=self.temp
        print(" Student Details Created Successfully")
            
       
        
    def viewDetails(self):
        if not self.Students:
            print("Enter Atleast One Student Details")
            
    def search(self,a):
        temp=input("Enter {} :".format(a))
        if a=='RollNo':
            temp=int(temp)
        for i in self.Students.keys():
            if self.Students[i][a]==temp:
                for j in self.field:
                    print(f"{j} : {self.Students[i][j]}")
            else:
                print('Invalid')
   '''                 
