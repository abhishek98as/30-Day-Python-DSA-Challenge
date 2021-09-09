# #method overriding
#
# class Add:
#     def result(self,a,b):
#         print("Addition",a+b)
#
#
# class Multi(Add):
#     def result(self,a,b):
#         print("Multiplication",a*b)
#
# m=Multi()
# m.result(10,20)
#
#
#
# class Add:
#     def result(self,a,b):
#         print("Addition",a+b)
#
#
# class Multi(Add):
#     pass
#
# m=Multi()
# m.result(10,20)
#
#
# a=Add()
# a.result(10,20)

class Add:
    def result(self,x,y):
        print("Addition",x+y)


class Multi(Add):
    def result(self,a,b):
        super().result(10,20)       #calling parent class method
        print("Multiplication",a*b)

m=Multi()
m.result(10,20)




