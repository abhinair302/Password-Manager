from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password1 = ""
    for char in password_list:
      password1 += char
    pass_int.insert(0,password1)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=web_int.get()
    email=email_int.get()
    password=pass_int.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        print(messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty!"))
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        web_int.delete(0, END)
        pass_int.delete(0, END)
        messagebox.showinfo(title="Success", message="Password saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
photo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website: ",font=('Calibri',12))
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username: ",font=('Calibri',12))
email_label.grid(column=0,row=2)

password_label=Label(text="Password: ",font=('Calibri',12))
password_label.grid(column=0,row=3)

web_int=Entry(width=35)
web_int.grid(column=1,row=1,columnspan=2)
print(web_int.get())
web_int.focus()

email_int=Entry(width=35)
email_int.grid(column=1,row=2,columnspan=2)
print(email_int.get())
email_int.insert(0,"example@gmail.com")
pass_int=Entry(width=21)
pass_int.grid(column=1,row=3,columnspan=2)
print(pass_int.get())

pass_butt=Button(text="Generate Password",command=generate_password)
pass_butt.grid(row=3,column=2)

add_butt=Button(text="Add",width=36,command=save)
add_butt.grid(row=4,column=1,columnspan=2)

window.mainloop()


