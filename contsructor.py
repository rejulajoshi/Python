class A:
    a=33
    def __init__(self,c,d):   #constructor
       self.c=c
       self.d=d
       print("heloo")
       
    def m(self,n):
        print(self.c*self.d)
        print(n)
obj=A(3,4)
print(obj.a)
obj.m("Hello world")