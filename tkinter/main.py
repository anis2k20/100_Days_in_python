from tkinter import *

window = Tk()

window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 28, "bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)


new_button = Button(text="New button")
# button.pack()
new_button.grid(column=3,row=0)

#my_label.config(text="New Text")


def button_clicked(*user_input):
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=2,row=2)

input = Entry(width=20)
# input.pack()
input.grid(column=4,row=3)







window.mainloop()