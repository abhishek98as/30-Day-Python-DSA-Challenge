class Mobile:
    def __init__(self,m):
        self.model=m

    def show_model(self,p):
        price = p
        print("model:",self.model,"price:",price)

realme = Mobile("realMe X")
realme.show_model(1000)
