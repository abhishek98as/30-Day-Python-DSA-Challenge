a=int(input("enter the 1st marks"))
b=int(input("enter the 2nd marks"))
c=int(input("enter the 3rd marks"))
d=int(input("enter the 4rth marks"))
e=int(input("enter the 5th marks"))

total= a+b+c+d+e
percentage=(total/500)*100
print("total marks",total,"total percentage",percentage)

if percentage>=80:
    print("Grade A")
elif percentage>=60:
    print("grade B")
elif percentage>=40:
    print("grade C")
else:
    print("your Grade D")