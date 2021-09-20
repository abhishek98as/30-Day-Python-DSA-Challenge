from tkinter import *

root = Tk()
e=Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"enter you name:")


def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="enter you stock quote",command=myClick, fg="black",bg="green")
myButton.pack()

root.mainloop()
