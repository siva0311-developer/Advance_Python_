import random
z=random.randint(111111,999999)
print(z)
a=int(input("Enter the Captacha"))
if(z==a):
    print("Successfull")
else:
    print("Invalid")
            

