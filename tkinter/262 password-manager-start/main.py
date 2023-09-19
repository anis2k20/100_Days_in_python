from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password="".join(password_list)
    pass_fild.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    url = web_url.get()
    email= email_fild.get()
    pass_word= pass_fild.get()
    if url=="" or email=="" or pass_word=="":
        messagebox.showwarning(title="Error", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=url, message=f"These are entered details:\nEmail:{email}\nPassword: {pass_word}\nIs it ok to save?")
#please don't leave any field empty!
    if is_ok:
        with open("data.txt","a") as d:
            d.write(f"{url} | {email} | {pass_word}\n")
            web_url.delete(0,END)
            pass_fild.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website = Label(text="Website: ")
website.grid(column=0, row=1)

web_url = Entry(width=42)
web_url.grid(column=1, row=1,columnspan=2)
web_url.focus()

email = Label(text="Email/Username: ")
email.grid(column=0, row=2)
email_fild = Entry(width=42)
email_fild.grid(column=1, row=2, columnspan=2)
email_fild.insert(0,"anis2hasan@gmail.com")

password = Label(text="Password: ")
password.grid(column=0, row=3)
pass_fild = Entry(width=22)
pass_fild.grid(column=1, row=3)

pass_btn = Button(text=f"Generate Password", command=generate_password)
pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()