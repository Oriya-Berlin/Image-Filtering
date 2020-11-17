from tkinter import filedialog


def save_image():
    pass


def browse_image():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        try:
            print("app_1")
            from App.Main.Run import app
            print(app)
            root = app
            app.set_image_url(file_path)
            app.set_image_holder_label()

            app.refresh()
        except:
            print('handle this later...')

        # root = app.get_root()
        # root.set_image_url(file_path)
        # root.set_image_holder_label()
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




