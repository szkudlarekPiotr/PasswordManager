import random
import secrets
import string
import pyperclip
from tkinter import *
from tkinter import messagebox

FONT_TYPE = "Arial"
CHARACTERS = list(string.printable)[:-6]


def generate():
    password.delete(0, END)
    new_pass = []
    pass_length = random.randint(10, 18)
    while pass_length > 0:
        new_pass.append(secrets.choice(CHARACTERS))
        pass_length -= 1
    if not any(item in string.ascii_uppercase for item in new_pass):
        new_pass[random.randint(0, len(new_pass) - 1)] = (secrets.choice(string.ascii_uppercase))
    if not any(item in string.punctuation for item in new_pass):
        new_pass[random.randint(0, len(new_pass) - 1)] = (secrets.choice(string.punctuation))
    password.insert(0, ''.join(new_pass))


def save_pass():
    pas = password.get()
    username = user.get()
    webpage = website.get()

    if pas == '' or username == '' or webpage == '':
        messagebox.showinfo(title="Error", message="Please provide valid information.")
    else:
        confirm = messagebox.askyesno(title="Confirm password", message=f"Do you want to add these credentials?: \n"
                                                                        f"Username: {username}\n"
                                                                        f"Password: {pas}")
        if confirm:
            with open("hasla.txt", "a+") as f:
                f.write(f'{webpage} | {username} | {pas} \n')
            pyperclip.copy(pas)
            website.delete(0, END)
            password.delete(0, END)


# GUI
window = Tk()
window.minsize(width=600, height=500)
window.title("Password Manager")
window.config(bg='white', padx=40, pady=30)

canvas = Canvas(width=200, height=172, bg='white', highlightthickness=0)
lock = PhotoImage(file="lock.png")
canvas.create_image(100, 86, image=lock)
canvas.grid(column=1, row=0, pady=40, padx=20, sticky='w')

# Labels
web_label = Label(text="Website: ", bg="white", font=(FONT_TYPE, 16))
web_label.grid(column=0, row=1, pady=5)

user_label = Label(text="Email/Username: ", bg="white", font=(FONT_TYPE, 16))
user_label.grid(column=0, row=2, pady=5)

pass_label = Label(text="Password: ", bg="white", font=(FONT_TYPE, 16))
pass_label.grid(column=0, row=3, pady=5)

# Entries
website = Entry(width=35, font=(FONT_TYPE, 14), highlightthickness=1)
website.focus()
website.grid(column=1, row=1)

user = Entry(width=35, font=(FONT_TYPE, 14), highlightthickness=1)
user.insert(0, "szkudlarekp5@gmail.com")
user.grid(column=1, row=2)

password = Entry(width=18, font=(FONT_TYPE, 14), highlightthickness=1)
password.grid(column=1, row=3, sticky='w')

# Buttons
generate_pass = Button(text='Generate password', bg='white', width=20, font=(FONT_TYPE, 10), command=generate)
generate_pass.grid(column=1, row=3, sticky='e')

add_password = Button(text='Add password', bg='#5290f2', width=55, command=save_pass)
add_password.grid(column=1, row=4, pady=5)

window.mainloop()
