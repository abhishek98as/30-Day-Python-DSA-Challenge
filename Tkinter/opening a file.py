f = open ("student.txt",mode="a+", encoding="utf-8")

print(f.closed)
print("file name:",f.name)
print("file mode:",f.mode)

print("file readable:",f.readable())
print("file writable:",f.writable())
f.close()
print("file closed:",f.closed)
print("file mode:",f.closed)
































































