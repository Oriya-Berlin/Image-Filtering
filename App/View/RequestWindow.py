from tkinter import *


class RequestWindow:

    def __init__(self):
        self.window = Tk()
        self.label = Label()
        self.text_field = Entry()
        self.execute_btn = Button()
        self.user_value = ''


    # TODO: maybe we need tu put this function to the constructor
    def display(self, effect):

        # TODO: here we need to put switch for efects and to add suitable instractions
        self.window.wm_minsize(400, 300)

        self.label = Label(self.window, text='dsfsffsdf')
        self.text_field = Entry(self.window, font=('arial', 16, 'bold'), bd=2, width=8, justify=LEFT)
        self.execute_btn = Button(self.window, text='hhh', command=lambda: self.get_user_value())

        self.label.pack()
        self.text_field.pack()
        self.execute_btn.pack()

        self.window.mainloop()


    def get_user_value(self):
        self.window.quit()
        self.user_value = self.text_field.get()
        return self.user_value

#
# s = RequestWindow()
# s.display('')
