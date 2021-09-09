#class varibale / static variable

# class Mobile:
#     fp='Yes'                       #class variable
#
#     @classmethod
#     def is_fp(cls):
#         print(cls.fp)
#
#
# realme = Mobile()
# Mobile.is_fp()

class Mobile:
    fp='yes'    #class variable

    def __init__(self):
        self.model = 'Realme X'    #instant variable

    def show_model(self):      #instant method
        print("Model:",self.model)    #Accessing Instance Variable

    @classmethod
    def is_fp(cls):      #class Method
        print("Finger Print",cls.fp)   #accessing class variable


realme=Mobile()
realme.show_model()
Mobile.is_fp()