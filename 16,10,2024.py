class parent:
    def __init__(self,Id,name):
        self.Id=Id
        self.name=name
class child(parent):
     def __init__(self,Id,name,age):
         super().__init__(Id,name)
         self.age=age
     def print(self):
         print(self.Id)
         print(self.name)
         print(self.age)
         
c1=child(101,"Raja",20)
c1.print()
    
