import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL)")
    db.commit()

class GUI():
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()
        
        self.master.title('Password Generator')
        self.master.geometry('500x300')
        self.master.config(bg='lightblue')
        self.master.resizable(False, False)

        self.label = Label(self.master, text="PASSWORD GENERATOR", anchor=N, fg='darkblue', bg='#FF8000', font='arial 15 bold underline')
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.user = Label(self.master, text="Enter User Name: ", font='times 12 bold', bg='lightblue', fg='darkblue')
        self.user.grid(row=1, column=0, padx=10, pady=5)

        self.textfield = Entry(self.master, textvariable=self.n_username, font='times 12', bd=3, relief='solid')
        self.textfield.grid(row=1, column=1, padx=10, pady=5)

        self.length = Label(self.master, text="Enter Password Length: ", font='times 12 bold', bg='lightblue', fg='darkblue')
        self.length.grid(row=2, column=0, padx=10, pady=5)

        self.length_textfield = Entry(self.master, textvariable=self.n_passwordlen, font='times 12', bd=3, relief='solid')
        self.length_textfield.grid(row=2, column=1, padx=10, pady=5)
        
        self.generated_password = Label(self.master, text="Generated Password: ", font='times 12 bold', bg='lightblue', fg='darkblue')
        self.generated_password.grid(row=3, column=0, padx=10, pady=5)

        self.generated_password_textfield = Entry(self.master, textvariable=self.n_generatedpassword, font='times 12', bd=3, relief='solid', fg='#DC143C')
        self.generated_password_textfield.grid(row=3, column=1, padx=10, pady=5)

        self.generate = Button(self.master, text="GENERATE PASSWORD", bd=3, relief='raised', font='Verdana 12 bold', fg='darkblue', bg='#FFD700', command=self.generate_pass)
        self.generate.grid(row=4, column=1, pady=10)

        self.accept = Button(self.master, text="ACCEPT", bd=3, relief='raised', font='Helvetica 12 bold italic', fg='darkblue', bg='#90EE90', command=self.accept_fields)
        self.accept.grid(row=5, column=1, pady=10)

        self.reset = Button(self.master, text="RESET", bd=3, relief='raised', font='Helvetica 12 bold italic', fg='darkblue', bg='#F08080', command=self.reset_fields)
        self.reset.grid(row=6, column=1, pady=10)

    def generate_pass(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        chars = "@#%&()\"?!"
        numbers = "1234567890"
        upper = list(upper)
        lower = list(lower)
        chars = list(chars)
        numbers = list(numbers)
        name = self.textfield.get()
        leng = self.length_textfield.get()

        if name=="":
            messagebox.showerror("Error","Name cannot be empty")
            return

        if not name.isalpha():
            messagebox.showerror("Error","Name must be a string")
            self.textfield.delete(0, END)
            return

        length = int(leng) 

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            self.generated_password_textfield.delete(0, END)
            return

        u = random.randint(1, length-3)
        l = random.randint(1, length-2-u)
        c = random.randint(1, length-1-u-l)
        n = length-u-l-c

        password = random.sample(upper, u)+random.sample(lower, l)+random.sample(chars, c)+random.sample(numbers, n)
        random.shuffle(password)
        gen_passwd = "".join(password)
        self.n_generatedpassword.set(gen_passwd)

    def accept_fields(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            find_user = ("SELECT * FROM users WHERE Username = ?")
            cursor.execute(find_user, [(self.n_username.get())])

            if cursor.fetchall():
                messagebox.showerror("This username already exists!", "Please use another username")
            else:
                insert = "INSERT INTO users(Username, GeneratedPassword) VALUES(?, ?)"
                cursor.execute(insert, (self.n_username.get(), self.n_generatedpassword.get()))
                db.commit()
                messagebox.showinfo("Success!", "Password generated successfully")

    def reset_fields(self):
        self.textfield.delete(0, END)
        self.length_textfield.delete(0, END)
        self.generated_password_textfield.delete(0, END)

if __name__=='__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
