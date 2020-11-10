from tkinter import filedialog


def save_image():
    pass


def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        try:
            from App.Main.Run import app
        except:
            print('handle this later...')

        root = app.get_root()
        # root.ima
        # self.im = PIL.Image.open(filename)
        print("fsdf")


def exit():
    pass


def undo():
    pass





#
# def effect_x():
#     pass
#
# def effect_x():
#     pass
#
# def effect_x():
#     pass
#
# def effect_x():
#     pass
#
# def effect_x():
#     pass
# def effect_x():
#     pass
# def effect_x():
#     pass
# def effect_x():
#     pass
# def effect_x():
#     pass
#




