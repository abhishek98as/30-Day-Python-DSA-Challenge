#Accessor method
#mutator method
#1.........accessor


class Mobile:
    def __init__(self):
        self.model="Real me X"     # Instance Variable

    def get_model(self):             #accessor method
        return self.model
realme=Mobile()
m=realme.get_model()         #calling accessor method
print(m)

#2.    mutator
class Mobile:
    def __init__(self):
        self.model="Ralme X"

    def set_model(self):
        self.model = "REalme 2"           #mutator method

realme=Mobile()
realme.set_model()                #calling mutator method
print(realme.model)

#3......with parameter

class Mobile:
    def set_model(self,m):
        self.model=m

realme=Mobile()
realme.set_model("RealMe X")
print(realme.model)