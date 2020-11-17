from tkinter import *
from tkinter import filedialog
from App.Classes.ImageHandler import ImageHandler
# from App.Controller.Controller import browse_image
from PIL import Image
from PIL import ImageTk


# we need to call that view
class App():

    def __init__(self):

        # properties
        self.root = Tk()
        self.center_grid = Frame(self.root)
        self.image_holder_label = Label()
        self.image_url = '/home/berlin/Desktop/Image-Filtering/images/f2.jpg'  # default image url
        self.selected_image = ImageTk.PhotoImage(Image.open(self.image_url))

        self.root.wm_minsize(700, 500)
        self.image_holder_label = Label(self.center_grid, image=self.selected_image)


        ################## TOP GRID ##################
        top_grid = Frame(self.root)
        undo_button = Button(top_grid, text="Undo", state=DISABLED).grid(row=1, column=4, sticky=W)
        top_grid.pack(side=TOP)


        ################## BOTTOM GRID ##################
        bottom_grid = Frame(self.root)
        browse_button = Button(bottom_grid, text="Browse...", command=lambda: self.browse_image()).grid(row=1, column=0, sticky=W)
        save_button = Button(bottom_grid, text="Save", command=None).grid(row=1, column=2, sticky=W)
        exit_button = Button(bottom_grid, text="Exit", command=self.root.quit).grid(row=1, column=3, sticky=W)
        bottom_grid.pack(side=BOTTOM)


        ################## LEFT GRID ##################
        left_grid = Frame(self.root)
        effect_1_button = Button(left_grid, text="1", command=None).grid(row=1, sticky=W)
        effect_2_button = Button(left_grid, text="2", command=None).grid(row=2, sticky=W)
        effect_3_button = Button(left_grid, text="3", command=None).grid(row=3, sticky=W)
        effect_4_button = Button(left_grid, text="4", command=None).grid(row=4, sticky=W)
        effect_5_button = Button(left_grid, text="5", command=None).grid(row=5, sticky=W)
        effect_6_button = Button(left_grid, text="6", command=None).grid(row=6, sticky=W)
        effect_7_button = Button(left_grid, text="7", command=None).grid(row=7, sticky=W)
        effect_8_button = Button(left_grid, text="8", command=None).grid(row=8, sticky=W)
        left_grid.pack(side=LEFT)


        ################## CENTER GRID ##################
        # center_grid = Frame(self.root)
        # self.selected_image = ImageTk.PhotoImage(Image.open("/home/berlin/Desktop/Image-Filtering/images/f2.jpg"))
        # self.image_holder_label = Label(self.center_grid, image=self.selected_image)
        # print(image_holder_label.__init__()) set new label/ image
        self.image_holder_label.grid(row=4, column=3, pady=120)
        self.center_grid.pack(side=TOP)


    def get_root(self):
        return self.root

    def set_image_url(self, image_url):
        self.image_url = image_url

    def set_image_holder_label(self):
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhh2")

        url_test = '/home/berlin/Desktop/Image-Filtering/images/cat.bmp'
        self.selected_image = ImageTk.PhotoImage(Image.open(url_test))
        self.image_holder_label = Label(self.center_grid, image=self.selected_imag)  #  self.selected_imag

        self.center_grid.destroy()
        center_grid = Frame(self.root)
        img1 = PhotoImage(file="url_test")
        self.image_holder_label = Label(self.center_grid, image=img1)
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhh4")
        self.root.destroy()
        self.refresh()


    def runApp(self):
        self.root.mainloop()

    def refresh(self):
        self.destroy()
        self.__init__()



    def browse_image(self):
        file_path = filedialog.askopenfilename()
        if file_path != "":

            url_test = '/home/berlin/Desktop/Image-Filtering/images/cat.bmp'

            self.selected_image = ImageTk.PhotoImage(Image.open(url_test))
            self.image_holder_label = Label(self.center_grid, image=self.selected_image)
            self.image_holder_label.configure(image=self.selected_image)
            self.root.configure()






