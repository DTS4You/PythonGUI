import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Fenstergröße
w_breite = 400
w_hoehe = 300

# root window
root = tk.Tk()

# Bildschirmgröße ermitteln
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Position berechnen
x = (screen_width - w_breite) // 2
y = (screen_height - w_hoehe) // 2

root.geometry(f"{w_breite}x{w_hoehe}+{x}+{y}")
root.resizable(False, False)
root.title('Radio Button Demo')
icon = tk.PhotoImage(file="wks_logo.png")
root.iconphoto(True, icon)


def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

# label
label = ttk.Label(text="What's your t-shirt size?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()
