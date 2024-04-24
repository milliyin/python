import qrcode
from tkinter import *
from PIL import ImageTk, Image

def genqr(text):
    global labelimg
    img = qrcode.make(text)
    img.save("qrcode.png")
    print("Succefull genrated")
    callback()

m= Tk()
m.title("Qr Code Gen")
label = Label(m,text="Text").grid(row=0)
e1 = Entry(m)
e1.grid(row=0,column=1)
canvas = Canvas(m, width = 300, height = 300)
canvas.grid(rowspan=20,columnspan=20)
button = Button(m,text="Generarte", width=15,command=lambda: {genqr(e1.get())})
button.grid(row=1)
image_no_1 = ImageTk.PhotoImage(Image.open("qrcode.png"))
panel = Label(m,image=image_no_1)
panel.grid(row=2)

def callback():
    image_no_2 = ImageTk.PhotoImage(Image.open("qrcode.png"))
    panel.configure(image=image_no_2)
    panel.image =  image_no_2

m.mainloop()
