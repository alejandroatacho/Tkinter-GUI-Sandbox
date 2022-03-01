from tkinter import *


def display():
    if(x.get() == 1):
        print("You Agree!")
    else:
        print("You Don't Agree :c")


window = Tk()

photo3 = PhotoImage(file='views/ft3.png')
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
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo3,
                           compound='left')

check_button.pack()
window.mainloop()
