# a=(5)
# b=(5,)
# c=5
# print(type(a))
# print(type(b))
# print(type(c))
# x=(2,2.4,"reju",True)
# y=1,4,9,8
# print(x[2])
# print(y[3])
# print(len(x))
# print(y[-1])  # print last element
# # Tupple repetition
# n=int(input("enetr the number of times to repeat"))
# result=x*2
# print(result)
# # Tupple concatenation
# print(x+y)
# #Tupple Slicing
# print(x[1:3])
# #Tupple reversal
# print(x[::-1])
# Tupple counting
z=(1,2,3,2,5,6)
print(z.count(1))
#Tupple unpacking
a,b,c,d,e,f=z
print(c)
# Tupple swap trick
m=2,3,4
n=6,7,8
m,n=n,m
print(n)
#Nested Tupple access
a=(5,6,8,"reju",True,(9,7,8,"reju",(1,1,1.6,"reju"),True))
print(a[5][4][2])