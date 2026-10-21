
#WAP To check grades
marks=int(input("enter your marks :"))
if(marks>=76 and marks<=100):
    print("your grade is A")
elif(marks>=51 and marks<76):
    print("your grade is B")
elif(marks>=26 and marks<51):
    print("your grade is C")
else:
    print("your grade is D")
#WAP a number is positive,negative or zero
number=int(input("enter your number :"))
if(number>0):
    print("Number is positive")
elif(number<0):
     print("Number is negative")
else:
    print("Number is zero")
#WAP even or odd
num=int(input("enter your number :"))
if(num%2==0):
    print("number is even")
else:
    print("numebr is odd")
num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
num3=int(input("enter your third number :"))
print(max(num1,num2,num3))