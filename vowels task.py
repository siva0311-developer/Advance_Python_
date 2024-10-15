a=['a','A','E','e','F','f','o','O','u','U']
x=input("Enter String")
y=[]
for i in x:
    if i in a:
        y.append(i)
    else:
        pass
print(len(y))
