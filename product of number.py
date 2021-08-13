i=int(input("enter the given number"))
sum=1
while(i>0):
    sum=sum*(i%10)
    i=i//10
print("product od digit=",sum)