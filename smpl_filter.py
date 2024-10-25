data={'101':{'Name':'Raja','Age':'19','City':'Mdu'},
      '102':{'Name':'Ragu','Age':'15','City':'Mdu'},
      '103':{'Name':'Viji','Age':'22','City':'Mdu'}}
field=['Name','Age','City']
def put(x):
    key,value=x
    return value['Name']==data


x=filter(put,data.items())
x=dict(x)
print(x)
