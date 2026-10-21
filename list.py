a=[12,24,12.5,"Orange",True]
print(a)
print(a[2])
print(a[3][2])
print(a[2::3]) #slicing 
print(a[::-1])
print(a)
# print(len(a))
# # check if list is empty
# if len(a)==0:
#  print("empty list")
# else:
#  print("list is not empty")
# a[1]=200
# print(a)
# a.append(600)
# a.insert(2,300)
# print(a)
# a.remove(600)
# print(a)
# a.pop(1)
# print(a)
# sum and average
x=[12,34,56,78,25]
total=sum(x)
print("Sum =",total)
average=total/len(x)
print("Average =",average)
print(max(x))
print(min(x))
even=0
odd=0
for i in x:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)  
print(x[::-1])
x.sort()
print(x)
y=x.copy()
print(y)
z=x+y
print(z)

