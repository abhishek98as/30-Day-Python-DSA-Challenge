#lambada expression practice

# def is_even(a):
#     if a%2==0:
#         return True
#     else:
#         return False
#
# print(is_even(7))
#
# #by lambda function
#
# iseven2 = lambda a : a%2==0
# print(iseven2(6))

# def last_char(s):
#     return[-1]
last_char = lambda s : s[-1]
print(last_char('harshit'))


#lambda with if else
def func1(s):
   return len(s)>5



func=lambda s : True if len(s)>5  else False
print(func('abcgfg'))
















