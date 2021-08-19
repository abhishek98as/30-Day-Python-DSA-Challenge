#program to find sum in the list

a=[]
size=int(input("how many number you want to add"))
for i in range(size):
    val=int(input("enter the number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("sum of the list",sum)