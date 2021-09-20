#time module


from time import time,ctime,localtime
epoch= time()
print(epoch)

et = ctime(epoch)
print(et)


print(ctime())





stobj=localtime()

print(stobj)

print(stobj.tm_year)
print(stobj.tm_mon)
print(stobj.tm_mday)
print(stobj.tm_hour)
print(stobj.tm_min)
print(stobj.tm_sec)

print(stobj.tm_mday,end="/")
print(stobj.tm_mon,end="/")
print(stobj.tm_year)
print()
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)




































