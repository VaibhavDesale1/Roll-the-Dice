# Roll The Dice Game

from tkinter import *
from random import choice
from PIL import Image, ImageTk

root = Tk()
root.title("Roll the Dice ")
root.geometry("400x400+400+100")

dice = ['1rr.png','2rr.png','3rr.png','4rr.png','5rr.png','6rr.png']

def f1():
	img1 = ImageTk.PhotoImage(Image.open(choice(dice)))
	lab1.configure(image=img1)
	lab1.image = img1

btn = Button(root, text="Roll", font=('calibri', 20, 'bold'), command=f1)
btn.pack(pady=10)

img1 = ImageTk.PhotoImage(Image.open(choice(dice)))
lab1 = Label(root, image=img1)
lab1.pack()

root.mainloop()
