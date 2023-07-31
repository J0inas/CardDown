import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames

entry: ttk.Entry


def get_filenames_and_set():

    filenames = askopenfilenames()
    index = 0
    for name in filenames:
        entry.insert(index=index, string=name)
        index += 1


padding = 10

padding_x = padding
padding_y = padding
# Main window is called root by convention

root = tk.Tk()

root.title("CardDown")
root.geometry("300x150")
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(master=frm, text="Select Files for Parsing").grid(column=0, row=0)
ttk.Button(master=frm, text="Quit", command=root.destroy).grid(column=0, row=8)

input_frame = ttk.Frame(master=frm)
input_frame.grid()
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Open Files",
                    command=get_filenames_and_set)


entry.grid(column=0, row=0)
button.grid(column=1, row=0, padx=padding_x, pady=padding_y)
input_frame.grid(column=0, row=1)


# creating a widget can work like this
# widget = WidgetName(container, **options)
# container is the root window/frame the widget is place in
# options are arguments for configuring the widget


# keeps window visible on screen
# runs until not called
# usually last statement in window
root.mainloop()
