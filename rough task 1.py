class student:
    Students={}
    dic=["RollNo","Name","Major"]
    temp={}

    def person(self):
           print("\n1.Enter The Student Details\n2.View Student Details\n3.Exit")
           option=int(input())
           if(option==1):
                self.getvalues()
                
           elif(option==3):
                print("Exiting....Bye")
                
           elif(option==2):
               self.viewdetails()
               
               
           else:
               print("Invalid Error")




           
    def getvalues(self):
        for i in self.dic:
            x=input("Enter{}:".format(i))
            if i=="RollNo":
                x==int(x)
                RollNo=x
                self.temp[i]=x
        self.Students[RollNo]=self.temp
        print("Student Details Created Successfully")

    def viewdetails(self):
       if not self.Students:
            print("Enter Atleast One Student Details")

    def search(self,r):
        temp=input("Enter{}:".format(r))
        if r=="RollNo":
           temp=int(temp)
        for i in self.Students.items():
            if self.students[i][r]==temp:
               for j in self.dic:
                 print(f"{j} : {self.Students[i][j]}")
            else:
                print('Invalid')
    
            
ram=student()
ram.person()
