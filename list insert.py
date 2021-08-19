# a=[5,"ram",10]
# a.insert(3,"shyam")
# print(a)

a=[]
for i in range(5):
    x=input("enter the value")
    a.append(x)
print("original list is:",a)
index=int(input("enter the vlaue want to insert"))
value=input("enter the value to insert")
a.insert(index,value)
print("list after insertion",a)