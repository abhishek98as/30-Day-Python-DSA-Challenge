#creating object of timedelta class

from datetime import timedelta, date

td= timedelta(days=10)

d=date.today()
print(d-td)

