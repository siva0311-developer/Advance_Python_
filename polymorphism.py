# polymorphism

class person1:
    def action(self):
        print("Run")
class person2(person1):
    def action(self):
        print("Walk")
class person3(person2):
    def action(self):
        print("Jump")
obj=[person1(),person2(),person3()]
for i in obj:
    i.action()
        
        
