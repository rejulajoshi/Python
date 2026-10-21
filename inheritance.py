class A():
    a=11
class B(A):
    b=22
class C(B):
   c=33
obj=C()
print(obj.a)
print(obj.b)
print(obj.c)