from tkinter import *



class RequestWindow():

    def display(self):
        window = Tk()

        text = Label()
        txtBira = Entry(window, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, textvariable="E_Bira")

        txtBira.pack()
        window.wm_minsize(400, 300)
        window.mainloop()


RequestWindow.display(self=None)
