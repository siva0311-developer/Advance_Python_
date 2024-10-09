class over:
    def __init__(self):
        self.a=int(input("Enter Value:"))
    def __add__(self,x):
        return(self.a-x.a)



a=over()
b=over()
print(a+b)
