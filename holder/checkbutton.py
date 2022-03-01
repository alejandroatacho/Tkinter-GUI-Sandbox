from tkinter import *


def display():
    if(x.get() == 1):
        print("You Agree!")
    else:
        print("You Don't Agree :c")


window = Tk()

x = IntVar()
check_button = Checkbutton(window, text="I Agree To The Terms And Service",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='pink',
                           bg='black',
                           activeforeground='pink',
                           activebackground='black')

check_button.pack()
window.mainloop()
