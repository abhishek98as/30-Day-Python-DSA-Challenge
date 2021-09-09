#instance variable
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'   #instance variable

    def show_model(self):
        print(self.model)    #accessing instance Variable

realme = Mobile()
redmi= Mobile()
geek=Mobile()
print(realme.model)
print(redmi.model)
print(geek.model)


redmi.model='Redmi 7s'
print(realme.model)
print(redmi.model)
print(geek.model)
