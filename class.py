class A:
    a=30   # Class attribute
    def m(self):
        print("hello world")
# print(A.a)
# A.m()
obj=A()
print(obj.a)
obj.m()# inordernto call a method with object we need to pass self in method
