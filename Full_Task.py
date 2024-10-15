#OOPs Concepts

#1. Class & Objects   like a function

class Students:
    StudentData={}                                                                      #secondary dictionary
    StudentDetails=['RollNo','Name','Age','Class']
    stuDict={}                                                                              #primary dictionary
    RollNo=0


#Getting Value via method:
    def getDetails(self):
        self.StudentData={}
        RollNo=input("Enter Student RollNo:")
        for i in self.StudentDetails: 
            if i=='RollNo':
                self.StudentData[i]=RollNo
                continue
            else:
                print("Enter Student {}:".format(i),end="")
                self.secDict=input()
                self.StudentData[i]=self.secDict
        self.stuDict[RollNo]=self.StudentData
        '''print(self.stuDict)'''

#Database & Printing Values :                


class studentHub(Students):
    def search(self,a):
        Search=input("\n~~Searching Details~~\nEnter Student {}:".format(a))
        for i in  self.stuDict:
            if self.stuDict[i][a]==Search:
                for j in self.StudentDetails:
                    print(j,":",self.stuDict[i][j])
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            else:
                return(print(" The Searching  Value '{} :{}' is not Found".format(a,Search)))


#Main Content
x=studentHub()
count=0
while True:
    print("\n1.Enter Student Details\n2.View Details\n3.Exit")
    Choose=int(input())
    if Choose==1:
        count+=1
        x.getDetails()
    elif count!=0 and Choose == 2:
        print("\n1.Search by Id\n2.Search by Name\n 3.Search by Age\n4.Search by Class")
        i=int(input())
        if i==1:
            x.search('RollNo')
        elif i==2:
            x.search('Name')
        elif i==3:
            x.search('Age')
        elif i==4:
            x.search('Class')
        else:
            print("Invalid Input")
        
    elif Choose==3:

        print("Thank You")
        break
    else:
        print("Enter Atleast One Student Detail")
    


    

