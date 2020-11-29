import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog

from App.Filters.Brightness import set_brightness
from App.Filters.ColorFiltering import color_filtering
from App.Filters.Contrasts import set_contrast_1, set_contrast_2
from App.Filters.Convolution import image_filtering
from App.Filters.GammaCorrection import set_gamma_correction
from App.Filters.Invert import set_invert
from App.Filters.CleanNoises import clean_sp

from App.View.RequestWindow import RequestWindow
from App.Classes.ImageHandler import ImageHandler
from App.Classes.CreateStack import Stack



class App(Frame):

    #  main properties
    image_handler = None
    img_holder_label = None
    view_img = None  # the image on the window
    view_img_width = None
    view_img_height = None
    images_stack = None


    def __init__(self):
        Frame.__init__(self)
        self.master.title('Image Filtering')
        self.master.wm_maxsize(self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        self.master.wm_minsize(1250, 1000)
        self.images_stack = Stack()


        ################## TOP GRID ##################
        top_grid = Frame(self.master)
        text = "  I didn't spend much time on the UI...  "
        label = Label(top_grid, text=text, font="lucida 13 bold", bg="red")
        label.grid(row=1, column=4, sticky=W)
        top_grid.pack(side=TOP)


        ################## BOTTOM GRID ##################
        bottom_grid = Frame(self.master)
        self.undo_button = Button(bottom_grid, text="Undo", width=15, command=lambda: self.undo_btn())
        self.undo_button.grid(row=1, column=0, sticky=W)
        browse_button = Button(bottom_grid, text="Browse...", width=15, command=lambda: self.browse_image()).grid(row=1, column=1, sticky=W)
        save_button = Button(bottom_grid, text="Save", width=15, command=lambda: self.save_image()).grid(row=1, column=2, sticky=W)
        exit_button = Button(bottom_grid, text="Exit", width=15, command=self.master.destroy).grid(row=1, column=3, sticky=W)
        bottom_grid.pack(side=BOTTOM)


        ################## LEFT GRID ##################
        left_grid = Frame(self.master)
        effect_1_button = Button(left_grid, text="Clean Noises", width=15, command=lambda: self.execute_effect('Clean Noises')).grid(row=1, sticky=W)
        effect_2_button = Button(left_grid, text="Brightness", width=15, command=lambda: self.open_execute_effect_window('Brightness')).grid(row=2, sticky=W)
        effect_3_button = Button(left_grid, text="Color Filtering", width=15, command=lambda: self.open_execute_effect_window('Color Filtering')).grid(row=3, sticky=W)
        effect_4_button = Button(left_grid, text="Contrast (1)", width=15, command=lambda: self.open_execute_effect_window('Contrast_1')).grid(row=4, sticky=W)
        effect_5_button = Button(left_grid, text="Invert", width=15, command=lambda: self.execute_effect('Invert')).grid(row=5, sticky=W)
        effect_6_button = Button(left_grid, text="Gamma Correction", width=15, command=lambda: self.open_execute_effect_window('Gamma Correction')).grid(row=6, sticky=W)
        effect_7_button = Button(left_grid, text="Sharpness", width=15, command=lambda: self.execute_effect('Sharpness')).grid(row=7, sticky=W)
        effect_8_button = Button(left_grid, text="Contrast (2)", width=15, command=lambda: self.open_execute_effect_window('Contrast_2')).grid(row=8, sticky=W)
        effect_9_button = Button(left_grid, text="Blur", width=15, command=lambda: self.execute_effect('Blur')).grid(row=9, sticky=W)
        effect_10_button = Button(left_grid, text="Outline", width=15, command=lambda: self.execute_effect('Outline')).grid(row=10, sticky=W)
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

            # match image to window size if necessary
            if self.image_handler.width > 1200 or self.image_handler.height > 940:
                self.size_correction(self.image_handler.width, self.image_handler.height)
            else:
                self.view_img_width = self.image_handler.width
                self.view_img_height = self.image_handler.height

            self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.original_image.resize((self.view_img_width, self.view_img_height)))
            self.img_holder_label.config(image=self.view_img)



    def open_execute_effect_window(self, effect):
        request_window = RequestWindow(effect)
        request_window.display()
        user_value = request_window.get_user_value()
        self.execute_effect(effect, user_value)



    def execute_effect(self, effect, user_value=None):

        if self.images_stack.isEmpty():
            self.undo_button['state'] = 'normal'
            self.undo_button.configure()

        self.images_stack.push(self.image_handler.image_copy)
        self.image_handler.image_copy = self.image_handler.original_image

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
        if effect == 'Brightness':
            self.image_handler.image_copy = set_brightness(self.image_handler.image_copy, user_value)
        if effect == 'Color Filtering':
            self.image_handler.image_copy = color_filtering(self.image_handler.image_copy, user_value)
        if effect == 'Contrast_1':
            self.image_handler.image_copy = set_contrast_1(self.image_handler.image_copy, user_value)
        if effect == 'Contrast_2':
            self.image_handler.image_copy = set_contrast_2(self.image_handler.image_copy, user_value)
        if effect == 'Gamma Correction':
            self.image_handler.image_copy = set_gamma_correction(self.image_handler.image_copy, user_value)


        self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.image_copy.resize(self.view_img_width, self.view_img_heigh))
        self.img_holder_label.config(image=self.view_img)



    def undo_btn(self):
        if self.images_stack.isEmpty():
            self.undo_button['state'] = 'disabled'
        else:
            self.image_handler.image_copy = self.images_stack.peek()
            self.images_stack.pop()
            self.view_img = PIL.ImageTk.PhotoImage(self.image_handler.image_copy.resize(self.view_img_width, self.view_img_heigh))
            self.img_holder_label.config(image=self.view_img)



    def save_image(self):
        file_path = filedialog.asksaveasfilename()
        if file_path != "":
            img = self.image_handler.image_copy
            img.save(f'{file_path}.jpg')



    def runApp(self):
        self.master.mainloop()



    def get_window_height(self):
        return self.master.winfo_height()



    def get_window_width(self):
        return self.master.winfo_width()



    def size_correction(self, width, height):

        temp_width = width
        temp_height = height
        scaler = 1.0

        while temp_width > 1200 or temp_height > 940:

            if temp_width*scaler <= 1200 and temp_height*scaler <= 940:
                self.view_img_width = int("%.0f" % (temp_width*scaler))
                self.view_img_height = int("%.0f" % (temp_height*scaler))
                return

            scaler = float(scaler-0.01)


