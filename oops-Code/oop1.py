class Person:
    def __init__(self,first_name,last_name,age):
        #instance variable
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('hersit','vasisth',24)
p2=Person("mohit","singh",23)

print(p1.first_name)
print(p2.first_name)