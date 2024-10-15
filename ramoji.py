#file Handling:-
#open(),read(),write(),close()
#create a new file:
f=open('sivaram.txt','x')
f.close()
#write a particular file :-
f=open('sivaram.txt','w')
f.write("hello Python")
f.close()

f=open('sivaram.txt','r')
print(f.read())

#update file:
f=open('sivaram.txt','a')
f.write("hello Python hello world")
f.close()

#with open ('samplefile.txt','a')as f:

