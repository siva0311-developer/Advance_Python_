'''
def find1(x):
    a=['a','A','E','e','F','f','o','O','u','U']
    if x in a:
        return True
    else:
        return False
x=input("Enter String")
y=filter(find1,x)
print(list(y))
    

[or]
'''

a=['a','A','E','e','F','f','o','O','u','U']
x=input("Enter String")
y=[]
for i in x:
    if i in a:
        y.append(i)
    else:
        pass
print(len(y))
