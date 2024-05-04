from tkinter import *
from pynput.keyboard import Listener, Key
import os

root = Tk()

def get_middle_of_screen( width, height, size):
    return (width / 2 - size / 2, height / 2 - size / 2)


def redraw(root):
    middle = get_middle_of_screen(root.winfo_screenwidth(), root.winfo_screenheight(), 100)
    root.geometry(f"+{int(middle[0])}+{int(middle[1])}")


def on_press(key):
    global root

    if key == Key.delete:
        root.destroy()
        return False
    elif key == Key.left:
        root.attributes("-alpha", 1)
    elif key == Key.right:
        root.attributes("-alpha", 0)

if __name__ == "__main__":
    listener = Listener(on_press=on_press)

    ws = os.path.dirname(__file__)
    root.image = PhotoImage(file=f"{ws}/images/cross_square.png")
    root.image = root.image.zoom(10)
    root.image = root.image.subsample(20)
    middle = get_middle_of_screen(root.winfo_screenwidth(), root.winfo_screenheight(), 100)
    root.geometry(f"+{int(middle[0])}+{int(middle[1])}")

    label = Label(root, image=root.image, bg="white")
    root.overrideredirect(True)

    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")

    label.pack()
    listener.start()
    label.mainloop()
