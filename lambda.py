a=lambda x,y,z:print(x*y+z)
a(2,8,10)
b=lambda x,y:print("sum is ", x+y)
b(9,3)
#write a python program to square and cube every number in a given list of integers using lambda
l1=[2,3,4,6,9,7,12]
square=list(map(lambda x:x**2,l1))
print(square)
cube=list(map(lambda x:x**3,l1))
print(cube)
#write a python program to count odd and even numbers in a lsit
even_num=list(filter(lambda x:x%2==0,l1))
print(even_num)
print(len(even_num))
odd_num=list(filter(lambda x:x%2!=0,l1))
print(odd_num)
print(len(odd_num))
# Program to add two given lists using map amd lambda
m=[2,3,4]
n=[4,5,6]
add=list(map(lambda x,y:x+y,m,n))
print(add)
#sort tuples using lambda
a=(3,4,5,6,9)
b=list(a)
sort=sorted(b,key=lambda y:y)
print(sort)
k=tuple(sort)
print(k)