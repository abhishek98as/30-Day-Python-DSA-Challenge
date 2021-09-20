#formating date and time
from datetime import datetime

dt=datetime.today()
print(dt)
print()


newd1=dt.strftime("%B,%d,%Y")
print(newd1)

print()

newd2=dt.strftime("%d/%b/%Y")
print(newd2)
print()
print(type(newd2))
newd3=dt.strftime("%d-%m-%Y")
print(newd3)

newt1 = dt.strftime("%H:%M:%S")
print(newt1)
print()


newt2 = dt.strftime("%I:%M:%S")
print(newt2)
