def m(a,b):
    print("uncodemy")
    print(a+b)
m(4,7)
#function for difference,mul,sum,division
def operation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
operation(8,3)
#To find max of numbers
def maximum(x,y,z):
    print(max(x,y,z))
(maximum(23,89,56))
# Sum of all number in a List
def sumOfList(list1):
   print(sum(list1))
sumOfList([2,4.1,6.9])
#Write a Python function to multiply all the numbers in a list.___To DO
def multiplication(list2):
  print()
#Write a Python function to calculate the factorial of a number 
def fact(n):
    total=1
    for i in range(1,n+1):
        total=total*i
    print(total)
fact(5)

#5. Write a Python program to print the even numbers from a given list
def even_num(list3):
   even=0
   odd=0
   for i in list3:
     if i%2==0:
            even+=1
     else:
            odd+=1
   print(even,odd)
even_num([2,5,8,5])
   
          