class Employee:


    increment = 1.5
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employees +=1
    def increase(self):
        self.salary=self.salary*Employee.increment

print(Employee.no_of_employees)
harry= Employee("harry","jackson",44000)
rohan=Employee("rohan","das",40000)
print(Employee.__dict__)
print(harry.__dict__)
harry.increment=9
print(harry.salary)
harry.increase()
print(harry.salary)
