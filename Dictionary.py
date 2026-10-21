a={"Name":"reju", "age":17}
print(a)
print(a["age"])
a["location"]="kerela"
print(a)
a["Name"]="rejula"
print(a)
del a["age"]
print(a)
#convert two list to ductionary
b=["name","age","location"]
c=["reju",22,"cslifut"]
newdic=dict(zip(b,c))
print(newdic)
a.clear()
print(a)
#merge two dictionary
y={"name":"rejua" ,"age":12}
x={"class":12,"place":"kerela"}
z={*y,*x}
print(z)
#nested dictionary
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print(person["address"]["zip"])
#initialise dictionary
newlist=['name','age']
value=34
c=dict.fromkeys(newlist,value)
print(c)
#renqme a key 
y["first name"]=y.pop