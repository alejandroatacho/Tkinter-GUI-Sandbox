from tkinter import *
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

# test
label = Label(window, text="Hello", font=(
    'Arial', 40, 'bold'), fg='pink', bg="black",  # font-text
    relief=RAISED, bd=10, padx=20, pady=20,  # Border
    image=photo, compound='bottom')  # image

label.pack()
#label.place(x=0, y=0)


window.mainloop()
