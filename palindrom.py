i=int(input("enter the number"))
pali=i
rev=0
while(i>0):
    rev=(rev*10)+(i%10)
    i=i//10
if (pali==rev):
    print("the no. is palindrom")
else:
    print("the no. is not palindrome")