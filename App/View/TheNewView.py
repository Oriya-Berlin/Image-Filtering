import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk

from App.Classes.ImageHandler import ImageHandler


class App(Frame):

    # properties
    image_handler = None
    img_holder_label = None
    view_img = None


    def __init__(self):
        Frame.__init__(self)
        self.master.title('Image Filtering')
        self.master.wm_minsize(700, 500)



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
        effect_1_button = Button(left_grid, text="Clean Noises", command=None).grid(row=1, sticky=W)
        effect_2_button = Button(left_grid, text="Brightness", command=None).grid(row=2, sticky=W)
        effect_3_button = Button(left_grid, text="Color Filtering", command=None).grid(row=3, sticky=W)
        effect_4_button = Button(left_grid, text="Contrast", command=None).grid(row=4, sticky=W)
        effect_5_button = Button(left_grid, text="Invert", command=None).grid(row=5, sticky=W)
        effect_6_button = Button(left_grid, text="Gamma Correction", command=None).grid(row=6, sticky=W)
        effect_7_button = Button(left_grid, text="Sharpness", command=None).grid(row=7, sticky=W)
        effect_8_button = Button(left_grid, text="8", command=None).grid(row=8, sticky=W)
        left_grid.pack(side=LEFT)


        ################## CENTER GRID ##################
        center_grid = Frame(self.master)
        center_grid.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img_holder_label = Label(center_grid)
        self.img_holder_label.pack()


        #  define default image
        # self.image_url = '/home/berlin/Desktop/Image-Filtering/images/f2.jpg'
        # self.selected_image = PIL.Image.open(self.image_url).resize((100, 100))
        # self.image = PIL.ImageTk.PhotoImage(self.selected_image)





    def browse_image(self):

        file_path = filedialog.askopenfilename()
        if file_path != "":
            self.image_handler = ImageHandler(file_path)
            self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.image.resize((100, 100)))
            self.img_holder_label.config(image=self.view_img)




if __name__ == "__main__":
    app = App()
    app.mainloop()

