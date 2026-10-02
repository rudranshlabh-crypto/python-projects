import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Opens a file and displays its content in the text editor."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    
    text_edit.delete("1.0", tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)

def save_file():
    """Saves the current text under a new filename."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    
    # Write the text content to the selected filepath
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = text_edit.get("1.0", tk.END)
        output_file.write(text)

window = tk.Tk()
window.title("Letter Writer Application")

window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

text_edit = tk.Text(window)
fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()