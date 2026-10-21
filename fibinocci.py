a=0
b=1
n=int(input("enter the nth term"))
i=1
print(a,end=" ")
while i<=n:
   a,b=b,a+b
   print(b,end=" ")
   i+=1

# WAP fo factorial
n=int(input("enter the nth term"))
fact=1
for i in range (1,n+1):
 fact*=i
 print(fact)
 