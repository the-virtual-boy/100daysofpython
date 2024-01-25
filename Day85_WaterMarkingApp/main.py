from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class MyImage():
    def __init__(self):
        self.image = None
        self.image_path = None
        self.tkimage = None

def load_image():
    im.image_path = tkinter.filedialog.askopenfilename(initialdir=".")    
    im.image = Image.open(im.image_path)
    x, y = im.image.size
    x = x if x < 1280 else 1280
    y = y if y < 720 else 720
    if x > 1280 and x / y < 1.78:
        y = y * 1280 / x
        x = 1280
    elif x > 1280 or y > 720:
        x = x * 720 / y
        y = 720
    im.image = im.image.resize((x, y))
    imagebox.config(height=y, width=x)
    im.tkimage = ImageTk.PhotoImage(im.image)
    imagebox.config(image=im.tkimage)
    imagebox.image = im.tkimage # save a reference of the image to avoid garbage collection

def mark_image():
    image_w, image_h = im.image.size[0], im.image.size[1]    
    text = mark_entry.get()
    t_size = len(text)

    if im.image.mode != "RGBA":
        im.image = im.image.convert("RGBA")

    txt = Image.new("RGBA", (image_w * 3, image_h * 3), (255, 255, 255, 0))
    fnt = ImageFont.load_default(size=50)
    d = ImageDraw.Draw(txt)

    text_size_offset = t_size * 35
    y_coord_x_offset = text_size_offset / 3
    y_step = 120

    if image_w > 400 and image_h > 300:
        for y in range(0, (image_h*3) // 35):
            for x in range (0, (image_w*3) // text_size_offset):
                coordinates = ((y * y_coord_x_offset + x * text_size_offset) % (image_w*3), y * y_step)

                d.text(coordinates, text, font=fnt, fill=(255, 255, 255, 128))
        txt = txt.crop((text_size_offset, 0, image_w + text_size_offset, image_h))
    else:
        d.text((0 , image_h*.5), text, font=fnt, fill=(255, 255, 255, 128))
        txt = txt.crop((0, 0, image_w, image_h))
    
    im.image = Image.alpha_composite(im.image, txt)

    im.tkimage = ImageTk.PhotoImage(im.image)
    imagebox.config(image=im.tkimage)
    imagebox.image = im.tkimage

def save_image():
    
    file = tkinter.filedialog.asksaveasfilename(initialdir=".", defaultextension='.png')
    if file is None:
        return
    im.image.save(file)


im = MyImage()
window = Tk()
window.title("WaterMarker App")
window.config(padx=50, pady=50)

imagebox = Label(window, width=50, height=10, padx=0, pady=0)
imagebox.grid(column=0, row=0, columnspan=3)

load_button = Button(text="Load", highlightthickness=0, command=load_image)
load_button.grid(column=0, row=1)

mark_entry = Entry()
mark_entry.grid(column=1, row=1)

mark_button = Button(text="Mark it!", highlightthickness=0, command=mark_image)
mark_button.grid(column=1, row=2)

save_button = Button(text="Save", highlightthickness=0, command=save_image)
save_button.grid(column=2, row=1)

window.mainloop()