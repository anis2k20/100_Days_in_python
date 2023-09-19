from tkinter import *
FONT = "Arial"
SIZE = 15
FACE = "normal"

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=350, height=250)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)
# input.config(padx=10,pady=10)

miles = Label(text="Miles",font=(FONT,SIZE,FACE))
miles.grid(column=2, row=0)
miles.config(padx=10,pady=10)

is_equal = Label(text="is equal to", font=(FONT,SIZE,FACE))
is_equal.grid(column=0, row=1)
is_equal.config(padx=10,pady=10)

output = Label(text="0", font=(FONT,SIZE,FACE))
output.grid(column=1, row=1)
output.config(padx=10,pady=10)

km = Label(text="Km", font=(FONT,SIZE,FACE))
km.grid(column=2, row=1)
km.config(padx=10,pady=10)

def calculate():
    miles_unit = float(input.get())
    km_unit = miles_unit*1.609
    output.config(text=km_unit)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
km.config(padx=10, pady=30)

#1.609 km = 1 mile
window.mainloop()