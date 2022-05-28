import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, PhotoImage
import os
from PIL import Image, ImageDraw, ImageFont, ImageTk

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def addImg():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(filetypes=(("Images",
                                          "*.jpeg;*.jpg;*.png"),))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runImg():
    for app in apps:
        os.startfile(app)


def editImg():
    for app in apps:
        img = Image.open(app)
        img = img.resize((1080, 1080))
        img = img.convert("1")
        width, height = img.size

        draw = ImageDraw.Draw(img)
        text = "Nurislam"

        font = ImageFont.truetype('arial.ttf', 50)
        textwidth, textheight = draw.textsize(text, font)

        margin = 5
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, font=font)

        img.save(app)


imageD = Image.open('alatoo.jpg')
imageD = imageD.resize((400, 400))
fon = ImageTk.PhotoImage(imageD)

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Select File", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addImg)
openFile.pack()

runImgs = tk.Button(root, text="Open File", padx=25,
                pady=10, fg='white', bg="#263D42", command=runImg)
runImgs.pack()

edit = tk.Button(root, text="Edit File", padx=25,
                  pady=10, fg='white', bg="#263D42", command=editImg)
edit.pack()

lb = Label(frame, image=fon)
lb.place(x=0, y=0, relheight=1, relwidth=1)
lb.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
