#namespace in oops-class variable

class Mobile:
    fp = "Yes"     #class variable

    @classmethod
    def is_fp(cls):      #class method
        print("finger print",cls.fp)      #accessing class variable



realme = Mobile()
redmi = Mobile()
Geek = Mobile


print("class fp:",Mobile.fp)
print("Realme:",realme.fp)
print("Redmi",redmi.fp)
print("Geek:",Geek.fp)

print()
Mobile.fp="No"

print("class fp:",Mobile.fp)
print("Realme:",realme.fp)
print("Redmi",redmi.fp)
print("Geek:",Geek.fp)


realme.fp="not working"

print("Realme:",realme.fp)

