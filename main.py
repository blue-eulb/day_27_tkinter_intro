from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Mile/Km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

mile_input = Entry(width=5)
mile_input.grid(column=2, row=1)
mile_input.insert(END, "0")
mile_input.focus()

text2 = Label(text="mil")
text2.grid(column=3, row=1)

text1 = Label(text="is equal to")
text1.grid(column=1, row=2)

converted_text = Label(text="0")
converted_text.grid(column=2, row=2)
converted_text.config(padding=10)

text3 = Label(text="km")
text3.grid(column=3, row=2)
text3.config(padding=20)


def listbox_used(event):
    g = float(mile_input.get())
    if list_unit.get(list_unit.curselection()) == units[0]:
        text2.config(text="mil")
        text3.config(text="km")
        converted_text.config(text=f"{round((g / 1.609344), 2)}")
    else:
        text2.config(text="km")
        text3.config(text="mil")
        converted_text.config(text=f"{round((g * 1.609344), 2)}")


def reset():
    converted_text.config(text="0")
    mile_input.delete(0, END)
    mile_input.insert(END, "0")


units = ["mil to km", "km to mil"]
list_unit = Listbox(height=2, width=10, justify="center")
for unit in units:
    list_unit.insert(units.index(unit), unit)
list_unit.grid(column=4, row=2)
list_unit.bind("<<ListboxSelect>>", lambda event: listbox_used(event))

bt_convert = Button(text="Reset", command=reset)
bt_convert.grid(column=2, row=3)

window.mainloop()
