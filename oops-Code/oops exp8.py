#class method without parameter

class Mobile:
    @classmethod    #Decorator
    def show_model(cls):   #class mthod
        print("Realme X")

realme=Mobile()
Mobile.show_model()


class Mobile:
    fp='yes'
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("Fingerprint:",cls.fp)
        print("RAM",cls.ram)


realme=Mobile()
Mobile.show_model('4gb')

