# a=[5,"ram",10,"ravi",10]
# a.remove(10)
# print(a)

a=[]
for i in range(5):
    x=input("enter the items in the list")
    a.append(x)
print("the original list is",a)
val=input("enter the value to remove")
a.remove(val)
print("list after the delet",a)