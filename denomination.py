from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTK

root=Tk()
root.title("denomination counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload=Image.open("app_img.jpg")
upload=upload.resize((300, 300))
image=ImageTK.PhotoImage(upload)

label=Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1=Label(
    root,
    text="hey user! welcome to denomination counter application"
    bg="light blue"
)

def msg():
    Msgbox=messagebox.showinfo(
        "alert", 
        "do you want to calculate the denomination count?"
    )
    if MsgBox=="ok":
        topwin()

button1=Buotton(
    root, 
    text="let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)