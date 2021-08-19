a=[]
for i in range(10):
    x=input("enter item to add in the list:")
    a.append(x)
x=input("enter the value whose frequency you want")
f=a.count(x)
print("frequency of ",x,"is=",f)

