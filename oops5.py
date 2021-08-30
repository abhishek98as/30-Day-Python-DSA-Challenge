#class variable
#circle
#area
#circum
class Circle:
    pi=3
    def __init__(self,radius):
        self.radius=radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c=Circle(4)
c1=Circle(5)
print(c.calc_circumference)