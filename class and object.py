#Class name:-
class studentname:
    Name:''
    Age:0
    MobileNo:0
    RollNo:0
    def getdetails(self):
        self.Name=input("Enter The Name:")
        self.Age=input("Enter The Age:")
        self.MobileNo=input("Enter The MobileNo :")
        self.RollNo=input("Enter The RollNo:")
    def putDetails(self):
        print("Name :",self.Name)
        print("Age :",self.Age)
        print("MobileNo :",self.MobileNo)
        print("RollNo :",self.RollNo)
         

ram=studentname()
amaran=studentname()

ram.getdetails()
ram.putDetails()






'''#Object name:-    
amaran=studentname()
amaran.Name="Amaran"
amaran.Age=20
amaran.MobileNo=6374183263
amaran.RollNo=12116143
print(amaran.Name)
print(amaran.Age)
print(amaran.MobileNo)
print(amaran.RollNo)




ram=studentname()
ram.Name="Ram"
ram.Age=20
ram.MobileNo=6374183263
ram.RollNo=12116143
print(ram.Name)
print(ram.Age)
print(ram.MobileNo)
print(ram.MobileNo)'''
