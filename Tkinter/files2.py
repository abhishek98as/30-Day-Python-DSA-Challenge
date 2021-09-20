f=open("student.txt", mode="w")
f.write("Hello\n")
f.write("geekyshows\n")
f.write("How are you")
f.close()

print("writing success")

f=open("student.txt", mode="r")
data = f.read()
print(data)
f.close()

f=open("student.txt", mode="rb")
data=f.read()
print(data)
f.close()