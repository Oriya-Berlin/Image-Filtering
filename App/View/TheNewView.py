import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog

from App.Filters.Convolution import image_filtering
from App.Filters.Invert import *
from App.Filters.CleanNoises import clean_sp

from App.View.RequestWindow import RequestWindow
from App.Classes.ImageHandler import ImageHandler


class App(Frame):

    # properties
    image_handler = None
    img_holder_label = None
    view_img = None


    def __init__(self):
        Frame.__init__(self)
        self.master.title('Image Filtering')
        self.master.wm_minsize(1000, 800)


        ################## TOP GRID ##################
        top_grid = Frame(self.master)
        undo_button = Button(top_grid, text="Undo", state=DISABLED).grid(row=1, column=4, sticky=W)
        top_grid.pack(side=TOP)


        ################## BOTTOM GRID ##################
        bottom_grid = Frame(self.master)
        browse_button = Button(bottom_grid, text="Browse...", command=lambda: self.browse_image()).grid(row=1, column=0, sticky=W)
        save_button = Button(bottom_grid, text="Save", command=None).grid(row=1, column=2, sticky=W)
        exit_button = Button(bottom_grid, text="Exit", command=self.master.quit).grid(row=1, column=3, sticky=W)
        bottom_grid.pack(side=BOTTOM)


        ################## LEFT GRID ##################
        left_grid = Frame(self.master)
        effect_1_button = Button(left_grid, text="Clean Noises", command=lambda: self.execute_effct('Clean Noises')).grid(row=1, sticky=W)
        effect_2_button = Button(left_grid, text="Brightness", command=lambda: self.open_execute_effct_window('Brightness')).grid(row=2, sticky=W)
        effect_3_button = Button(left_grid, text="Color Filtering", command=lambda: self.open_execute_effct_window('Color Filtering')).grid(row=3, sticky=W)
        effect_4_button = Button(left_grid, text="Contrast", command=lambda: self.open_execute_effct_window('Contrast')).grid(row=4, sticky=W)
        effect_5_button = Button(left_grid, text="Invert", command=lambda: self.execute_effct('Invert')).grid(row=5, sticky=W)
        effect_6_button = Button(left_grid, text="Gamma Correction", command=lambda: self.open_execute_effct_window('Gamma Correction')).grid(row=6, sticky=W)
        effect_7_button = Button(left_grid, text="Sharpness", command=lambda: self.execute_effct('Sharpness')).grid(row=7, sticky=W)
        effect_8_button = Button(left_grid, text="8", command=None).grid(row=8, sticky=W)
        effect_9_button = Button(left_grid, text="Blur", command=lambda: self.execute_effct('Blur')).grid(row=9, sticky=W)
        effect_10_button = Button(left_grid, text="Outline", command=lambda: self.execute_effct('Outline')).grid(row=10, sticky=W)

        left_grid.pack(side=LEFT)


        ################## CENTER GRID ##################
        center_grid = Frame(self.master)
        center_grid.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img_holder_label = Label(center_grid)
        self.img_holder_label.pack()



    def browse_image(self):

        file_path = filedialog.askopenfilename()
        if file_path != "":
            self.image_handler = ImageHandler(file_path)
            self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.original_image.resize((400, 300)))
            # self.image_handler.image_copy = self.image_handler.original_image
            self.img_holder_label.config(image=self.view_img)



    def open_execute_effct_window(self, effect):
        request_window = RequestWindow(effect)
        request_window.display()
        print(request_window.user_value)

    def execute_effct(self, effect):

        if effect == 'Invert':
            self.image_handler.image_copy = set_invert(self.image_handler.image_copy)
        if effect == 'Sharpness':
            self.image_handler.image_copy = image_filtering(self.image_handler.image_copy, 'sharpen')
        if effect == 'Blur':
            self.image_handler.image_copy = image_filtering(self.image_handler.image_copy, 'blur')
        if effect == 'Outline':
            self.image_handler.image_copy = image_filtering(self.image_handler.image_copy, 'outline')
        if effect == 'Clean Noises':
            self.image_handler.image_copy = self.image_handler.image_copy.convert('RGB')
            self.image_handler.image_copy = clean_sp(self.image_handler.image_copy)

        self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.image_copy.resize((400, 300)))
        self.img_holder_label.config(image=self.view_img)



    def undo_btn(self):
        pass



if __name__ == "__main__":
    app = App()
    app.mainloop()

