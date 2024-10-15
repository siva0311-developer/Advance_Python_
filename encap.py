class grantparent:
    def __init__ (self):
        self._a=45        #protected
        self.__b=60        #private
class parent(grantparent):
    def add1(self):
        print(self._a)
class child(parent):
    def __init__(self):
        print("Child Constructor")
    def add1(self):
        print(self.__b)




x=child()
x.add1()
