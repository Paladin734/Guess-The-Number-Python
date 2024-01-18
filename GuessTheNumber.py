from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
import random
from ttkthemes import ThemedTk
window = ThemedTk(theme="black")




window.geometry("750x500")
uparrow = PhotoImage(file="uparrow.png")
downarrow = PhotoImage(file="downarrow.png")
correct = PhotoImage(file="correct.png")
dice = PhotoImage(file="die.png")

tries = 0
def randomise():
    global x
    global rb
    if rb.get() == "First":
        x = random.randrange(51)
    elif rb.get() == "Second":
        x = random.randrange(101)
    elif rb.get == "Third":
        x = random.randrange(201)

def exit():
    window.destroy()

def compare(event):
    global x
    global tries
    if int(ent.get()) > x:
        photolabel.configure(image=downarrow)
        tries += 1
        trylbl.configure(text="Tries:" + str(tries))
        ent.delete(0, END)
    elif int(ent.get()) < x:
        photolabel.configure(image=uparrow)
        tries += 1
        trylbl.configure(text="Tries:" + str(tries))
    else:
        photolabel.configure(image=correct)

style = ttk.Style()
style.configure('small.TButton', font=(None, 12))

photolabel = Label(window, image=dice, font=12)
photolabel.place(y=370, x=30)
Text1 = Label(window, text="Guess the number", font=18)
Text1.place(y=20, x=300)

rb = StringVar()
rb.set("First")
rad1 = Radiobutton(window, text="Easy(0-50)", value="First", variable=rb,font=12 )
rad1.place(y=100, x=40)

rad2 = Radiobutton(window, text="Normal(0-100)", value="Second", variable=rb,font=12)
rad2.place(y=100, x=300)

rad3 = Radiobutton(window, text="Hard(0-200)", value="Third", variable=rb,font=12)
rad3.place(y=100, x=585)

ranbtn = ttk.Button(window, text="Randomise", style="small.TButton", command=randomise)
ranbtn.place(y=400, x=600)

ent = ttk.Entry(window, font=12)
ent.place(y=400, x=270)

exit = ttk.Button(window, text="Exit", style="small.TButton", command=exit)
exit.place(y=360, x=600)



trylbl = Label(window, text="Tries:0", font=12)
trylbl.place(y=350, x=300)







window.bind("<Return>", compare )
window.mainloop()





