from tkinter import *
from tkinter import ttk


class RequestWindow:

    def __init__(self, effect):
        self.window = Tk()
        self.label = Label()
        self.combo_box = ttk.Combobox()
        self.text_field = Entry()
        self.generate_button = Button()
        self.user_value = None
        self.label_text = ''
        self.effect = effect



    # TODO: maybe we need to put this function in the constructor
    def display(self):

        if self.effect == 'Brightness':
            self.label_text = 'Please enter number greater then 0. \n NOTE: numbers overt then 200 could be too bright.'
        if self.effect == 'Color Filtering':
            self.label_text = 'Please choose color:'
        if self.effect == 'Contrast_1' or 'Contrast_2':
            self.label_text = 'Please enter number in range of -255 to 255:'
        if self.effect == 'Gamma Correction':
            self.label_text = 'Please enter number in range 0 - 1: \n NOTE: the recommended value is 0.45'

        self.label = Label(self.window, text=self.label_text)
        self.label.pack()

        if self.effect == 'Color Filtering':
            self.combo_box = ttk.Combobox(self.window, values=['Red', 'Green', 'Blue'])
            self.combo_box.pack()
        else:
            self.text_field = Entry(self.window, font=('arial', 16, 'bold'), bd=2, width=8, justify=LEFT)
            self.text_field.pack()

        self.generate_button = Button(self.window, text='Generate!', command=lambda: self.generate_btn())
        self.generate_button.pack()

        self.window.title('Window')
        self.window.wm_minsize(400, 300)
        self.window.mainloop()



    def generate_btn(self):
        if self.effect == 'Color Filtering':
            self.user_value = self.combo_box.get()
        else:
            self.user_value = self.text_field.get()
            self.user_value = float(self.user_value)

        self.window.quit()
        self.window.destroy()



    def get_user_value(self):
        return self.user_value

