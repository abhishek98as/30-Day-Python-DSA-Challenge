#strong typing

class Duck:
    def walk(self):
        print("thapak thpak thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("mew mew mew")


def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
c=Cat()
myfunction(c)
