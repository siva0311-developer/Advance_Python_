'''
#os module
import os
print(os.path.abspath(__file__))
#os.mkdir('New')
print(os.getcwd())
os.chdir("D:\\project")
print(os.getcwd())
print(os.listdir())
#os.rename('sample.txt','student.txt')
print(os.path.exists("D:\\project" ))
'''

#file Handling:-
#open(),read(),write(),close()
#create a new file:
#f=open('sivaram.txt','x')
#f.close()
'''#write a particular file :-
f=open('sivaram.txt','w')
f.write("hello Python")
f.close()
f=open('sivaram.txt','r')
print(f.read())
#update file:
#with open ('samplefile.txt','a')as f:
'''

#random module:-

'''
random()
ranint()
~~list~~
sample()
shuffle()
choice()

'''

import random
z=random.randint(111,999,222,666)
print(z)
a=['ravi','raja','ram','arun','varun','vasanth']
#x=random.sample(a,k=1)
#random.shuffle(a)
#print(a)
x=random.choice(a)
print(x)
    
