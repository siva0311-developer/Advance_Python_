
class InnovaCrysta:
  Name:''
  Model:0
  Engine_CC:0
  Price:0
  def getDetails(self):
      self.Name=input("Enter The Car Name:")
      self.Model=int(input("Enter The Model:"))
      self.Engine_CC=int(input("Enter The Displacement(CC) :"))
      self.Price=int(input("Enter The Price :"))
  def putDetails(self):
      print(f"Name :",self.Name)
      print(f"Model :",self.Model)
      print(f"Engine_CC :",self.Engine_CC)
      print(f"Price:",self. Price)


task=InnovaCrysta()
task.getDetails()
task.putDetails()
