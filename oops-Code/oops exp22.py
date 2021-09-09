#method overloading


# class Myclass:
#     def sum(self,a):
#         print("1st sum method",a)
#
#     def sum(self):
#         print("2nd sum Method")
#
#
# obj=Myclass()
# obj.sum()
# obj.sum(10)



# class Myclass:
#     def sum(self,a,b,c):
#         s=a+b+c
#         return s
#
# obj= Myclass()
# print(obj.sum(10,20,30))


class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            s="provide at least two numbers"
        return s

obj= Myclass()
print(obj.sum(10,20,30))





























































