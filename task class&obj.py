def ram():
    print("Welcome To All")
    print("~Enter Your Option~")
    a=input("\n1.Add Student Details\n2.View Student")
    b=int(input("* The Given Values Must Be In Number."))
class taskname:
    Name:''
    Age:0
    MobileNo:0
    RollNo:0
    def getDetails(self):
        self.Name=input("Enter The Name:")
        self.Age=input("Enter The Age:")
        self.MobileNo=input("Enter The MobileNo :")
        self.RollNo=input("Enter The RollNo:")
    def putDetails(self):
        print("Name :",self.Name)
        print("Age :",self.Age)
        print("MobileNo :",self.MobileNo)
        print("RollNo :",self.RollNo)

        c=input("Do You Want Continue(yes/no):")
        if(c=="yes"):
          ram()
          self.getDetails()
        else:
            print("Existing..........Bye")
         
ram()

amaran=taskname()

amaran.getDetails()

amaran.putDetails()


