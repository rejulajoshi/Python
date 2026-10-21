# a={1,0,1.2,12,12,"reju",True}
# print(a)
# a.add(50)
# print(a)
# a.remove(12)
# print(a)
# a.discard(1.2)
# print(a)
# a.clear()
# print(a)
set1={1,2,3,4,"Orange"}
print(len(set1))
if set1==0:
    print("empty")
else:
    print("not empty")
set2={3,5,6,7,"Apple"}
union_set=set1|set2
print(union_set)
inter_set=set1&set2
print(inter_set)
diff_set=set1-set2
print(diff_set)
#Symetric set
symetric_set=set1.symmetric_difference(set2)
print(symetric_set)
# min and max
set3={1,45,67,89,40}
set4={3,5,6,7,8}
print(max(set3))
print(min(set3))
#Sum of set
sum=sum(set4)
print(sum)