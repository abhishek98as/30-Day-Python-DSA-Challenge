class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary


harry= Employee("harry","jackson",44000)
rohan=Employee("rohan","das",40000)


print(harry.salary,rohan.fname)
