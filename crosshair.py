from tkinter import *
from pynput.keyboard import Listener, Key
import os

root = Tk()

size = 100
width = 3440
height = 1440

middle = (width / 2 - size / 2, height / 2 - size / 2)


def redraw(root, width, height, size):
    root.geometry(f"+{int(middle[0])}+{int(middle[1])}")


def on_press(key):
    global root, height, width, middle, size
    # print(key)
    if key == Key.delete:
        root.destroy()
        return False
    elif key == Key.left:
        root.attributes("-alpha", 1)
    elif key == Key.right:
        root.attributes("-alpha", 0)
    if hasattr(key, "vk"):
        if key.vk == 73:  # i
            height -= 5
            redraw(root, width, height, size)
        elif key.vk == 74:  # j
            print("j")
        elif key.vk == 75:  # k
            print("k")
        elif key.vk == 76:  # l
            print("l")


if __name__ == "__main__":
    listener = Listener(on_press=on_press)

    ws = os.path.dirname(__file__)
    root.image = PhotoImage(file=f"{ws}/images/cross_square.png")
    root.image = root.image.zoom(10)
    root.image = root.image.subsample(20)
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
