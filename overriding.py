# class A():
#     def m(self):
#         print("Hello World")
# class B(A):
#     def m(self):
#         print("Welcome home")
# obj=B()
# obj.m()         #  method overriding

class A():
    def m1(self):
        print("Hello World")
class B(A):
    def m(self):
        print("Welcome home")
obj=B()
obj.m1()
        