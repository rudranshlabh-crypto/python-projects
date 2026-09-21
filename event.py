from tkinter import *

window=Tk()
window.title("event handler")
window.geometry("100x100")

def handle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)

window.blind("<key>", handel_keypress)

def handle_click(event):
    print("\nthe button was clicked!")

button=Button(text="click me")
button.pack()

button.blind("<button-1>", handle_click)

window.mainloop()