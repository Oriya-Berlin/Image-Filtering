from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from App.Classes.ImageHandler import ImageHandler





image_holder_label = object
root = Tk()
root.wm_minsize(700, 500)



def browse_image():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        print(filepath)
        img = ImageHandler(filepath)
        print(img.size)
        img.image.show()


def main():
    # root = Tk()
    # root.wm_minsize(700, 500)

    ############

    top_grid = Frame(root)
    undo_button = Button(top_grid, text="Undo", state=DISABLED).grid(row=1, column=4, sticky=W)
    top_grid.pack(side=TOP)

    ##################

    bottom_grid = Frame(root)
    browse_button = Button(bottom_grid, text="Browse...", command=lambda: browse_image()).grid(row=1, column=0, sticky=W)
    save_button = Button(bottom_grid, text="Save", command=None).grid(row=1, column=2, sticky=W)
    exit_button = Button(bottom_grid, text="Exit", command=root.quit).grid(row=1, column=3, sticky=W)
    bottom_grid.pack(side=BOTTOM)

    ##################

    left_grid = Frame(root)
    effect_1_button = Button(left_grid, text="1", command=None).grid(row=1, sticky=W)
    effect_2_button = Button(left_grid, text="2", command=None).grid(row=2, sticky=W)
    effect_3_button = Button(left_grid, text="3", command=None).grid(row=3, sticky=W)
    effect_4_button = Button(left_grid, text="4", command=None).grid(row=4, sticky=W)
    effect_5_button = Button(left_grid, text="5", command=None).grid(row=5, sticky=W)
    effect_6_button = Button(left_grid, text="6", command=None).grid(row=6, sticky=W)
    effect_7_button = Button(left_grid, text="7", command=None).grid(row=7, sticky=W)
    effect_8_button = Button(left_grid, text="8", command=None).grid(row=8, sticky=W)
    left_grid.pack(side=LEFT)

    ############

    center_grid = Frame(root)
    selected_image = ImageTk.PhotoImage(Image.open("/home/berlin/Desktop/Image-Filtering/images/f1.jpg"))
    image_holder_label = Label(center_grid, image=selected_image)
    import time
    time.sleep(6)
    selected_image = ImageTk.PhotoImage(Image.open("/home/berlin/Desktop/Image-Filtering/images/f2.jpg"))
    image_holder_label = Label(center_grid, image=selected_image)
    image_holder_label.grid(row=4, column=3, pady=120)
    center_grid.pack(side=TOP)



    root.mainloop()



if __name__ == "__main__":

    main()
