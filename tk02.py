from tkinter import *
window = Tk()

window = Tk()
lavel1 = Label(window, text="label1", bg="FF0000")
lavel2 = Label(window, text="label2", bg="00FF00")
lavel3 = Label(window, text="label3", bg="0000FF")

lavel1.pack(side=LEFT)
lavel2.pack(side=LEFT)
lavel3.pack(side=LEFT)

window.mainloop()