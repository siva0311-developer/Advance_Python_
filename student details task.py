'''
def ram():
    print("1.Enter student Details")
    print("2.View Details")
    print("3.Exist")
    Option=input("Enter The Option")


    
ram()
'''


class student:
    Students={}

    def person(self):
        for i in range(25): 
            print("1.Enter student Details")
            print("2.View Details")
            print("3.Search Rollno")
            print("4.Search Name")
            print("5.Exist")
            Option=input("Enter The Option")

            if(Option=='1'):
                self.getvalues()
            elif(Option=='2'):
                self.viewDetails()
            elif(Option=='3'):
                self.getrollno()
            elif(Option=='4'):
                self.SearchName()    
            elif(Option=='5'):
                print("Exiting....Bye")
                break
            else:
                print("Invalid Error")
                
    def getvalues(self):
        student_Rollno = input("Enter Student Rollno: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        self.Students[student_Rollno] = {'Name': name, 'Age': age}
        print(f" Student Details Added successfully!")
       
        
    def viewDetails(self):
        if not self.Students:
            print("Enter Atleast One Student Details")
            
        else:
            for student_Rollno,Details in (self.Students.items()):
                print(f"Student Rollno: {student_Rollno}")
                print(f"Name:{Details['Name']}")
                print(f"Age:{Details['Age']}")
                
                     

    def getrollno(self):
        student_Rollno=input("Search The Student Rollno:")
        Details=self.Students.get(student_Rollno)
        if Details:
            print(f"Student Rollno: {student_Rollno}, Name: {Details['Name']}, Age: {Details['Age']}")
        else:
            print("Invalid rollno")
        
    def SearchAge(self):
        student_Rollno=input("Search The Student Age:")
        Details=self.Students.get(student_Rollno)
        if Details:
            print(f"Student Rollno: {student_Rollno}, Name: {Details['Name']}, Age: {Details['Age']}")
        else:
            print("Invalid Name")
 
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
