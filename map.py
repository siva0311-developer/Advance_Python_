'''#map
def add1(a):
    return a*2
x=map(add1,[1,2,3,4,5,6])
print(list(x))      
'''


'''
x=[1,2,3,4,5,6]
def add1(a):
    return a*2
for i in range(len(x)):
    x[i]=add1(i)
print(x)    

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
                print("\n1.Search By RollNo\n2.Search By Name\n3.Search By Major")
                x=int(input())
                if x==1:
                    self.search('RollNo')
                elif x==2:
                    self.search('Name')
                elif x==3:
                    self.search('Major')
                
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
   
        print("Student Details Created Successfully")
            
       
        
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
ram=student()
ram.person()

                    
