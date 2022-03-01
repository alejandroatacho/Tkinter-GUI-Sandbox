from tkinter import *
from tkinter.tix import AUTO
#from PIL import Image, ImageTk

# main GUI
window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("GUI for app")

# foto
icon = PhotoImage(file='views/icon1.png')
window.iconphoto(True, icon)
window.config(background="grey")
# photo
photo = PhotoImage(file='views/ft1.png')
photo2 = PhotoImage(file='views/icon2.png')  # button image linked

# button
count = 0


def click():
    global count
    count += 1
    print("You click the button! " + str(count) + " Times!!!")


# test
label = Label(window, text="SMART-OBC File Comparison", font=(
    'Arial', 40, 'bold'), fg='pink', bg="black",  # font-text
    relief=RAISED, bd=10, padx=20, pady=20,  # Border
    image=photo, compound='bottom')  # image

label.pack()
# label.place(x=0, y=0)

# button
button = Button(window, text="Submit",
                command=click,
                font=("Comic Sans", 30), fg="pink", bg="black",
                activeforeground="pink",  # button color flash removed
                activebackground="black",
                state=ACTIVE,
                # image=photo2,  # button image
                compound='top',
                width=100,
                height=33)
button.pack()
window.mainloop()
