from tkinter import *
#main GUI
window = Tk()#instantiate an instance of a window
window.geometry("420x420")
window.title("GUI for app")
#test
label = Label(window,text="Hello")
label.pack()
#label.place(x=0, y=0)
#foto
icon = PhotoImage(file='views/icon1.png')
window.iconphoto(True, icon)
window.config(background="grey")



window.mainloop()