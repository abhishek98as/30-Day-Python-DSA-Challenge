a=int(input("enter the first number="))
b=int(input("enter the seconf number"))
c=int(input("enter the seconf number"))
if(a>b and a<c)or(a<b and a>c):
    print("the middle number is=",a)
elif(b>a and b<c)or(b<a and b>c):
    print("the middle number is=",b)
else:
    print("the middle number is:",c)