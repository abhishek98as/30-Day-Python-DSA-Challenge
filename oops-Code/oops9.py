#class method
#difference between class methods and instance methods

#instance method
class Person:
    count_instance=0  #class varibale or class attribute
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age


    def full_name(self):#instance method
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1=Person('hersit','singh',2)
p2=Person('abhishek','singh',24)

"you have created four instances Person class"

















