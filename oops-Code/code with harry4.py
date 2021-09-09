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

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)


harry = Employee("harry","jackson",40000)
lovish=Employee.from_str("lovish-jackson-76000")
rohan=Employee("rohan","das",74000)

print(harry.salary)
print(lovish.salary)
