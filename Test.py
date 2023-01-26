import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()

label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()