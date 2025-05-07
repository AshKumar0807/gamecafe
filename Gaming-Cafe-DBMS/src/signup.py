import tkinter
from tkinter import *
from tkinter import ttk
import os

import tkinterCommands
import database

cwd = os.path.dirname(os.path.realpath(__file__))
unique_ID_path = cwd + '/unique_id.py'


# database commands
def add_gamer_info(gamer_name, gamer_email, gamer_tag, age):
    """Inserting New Gamer data into gamer table"""
    unique_ID = 0
    # getting Unique id
    with open(unique_ID_path) as unique_IDFile:
        unique_ID = unique_IDFile.read()
        print(unique_ID)
    unique_ID = int(unique_ID) + 1

    print(gamer_name, gamer_email)
    database.insert(int(unique_ID), gamer_name, gamer_email, gamer_tag, age)

    # storing incremented unique id
    with open(unique_ID_path, "w") as unique_IDFile:
        unique_IDFile.write(str(unique_ID))
        unique_IDFile.close()


# main window
def window():
    """New Window for signing up the new user"""
    new_user = Toplevel()
    new_user.title("Sign up")
    
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    demoCafe = cwd + '/images/welcome1.png'
    print(demoCafe)
    cafe = PhotoImage(file=demoCafe)
    label = Label(new_user, image=cafe)
    label.grid(row=0, column=0, columnspan=4)

    def get_info():
        name = gamer_name_entry.get()
        email = gamer_email_entry.get()
        gamer_tag = gamer_tag_entry.get()
        age = gamer_age_entry.get()
        print(name, ' ', email, ' ', gamer_tag, ' ', age)  # debug line
        add_gamer_info(name, email, gamer_tag, age)
        new_user.destroy()

    # Using ttk widgets
    ttk.Label(new_user, text='Name: ').grid(row=1, column=0, sticky=E)
    gamer_name_entry = ttk.Entry(new_user, width=40)
    gamer_name_entry.grid(row=1, column=1)

    ttk.Label(new_user, text='Email: ').grid(row=2, column=0, sticky=E)
    gamer_email_entry = ttk.Entry(new_user, width=40)
    gamer_email_entry.grid(row=2, column=1)

    ttk.Label(new_user, text='Gamer Tag: ').grid(row=3, column=0, sticky=E)
    gamer_tag_entry = ttk.Entry(new_user, width=40)
    gamer_tag_entry.grid(row=3, column=1)

    ttk.Label(new_user, text='Age: ').grid(row=4, column=0, sticky=E)
    gamer_age_entry = ttk.Entry(new_user, width=40)
    gamer_age_entry.grid(row=4, column=1)

    submit_button = ttk.Button(new_user, text='Submit', command=get_info)
    submit_button.grid(row=5, column=1)

    new_user.mainloop()