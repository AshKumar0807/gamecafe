import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

import tkinterCommands
import userInfo
import signup
import database


def home(username):
    def get_selected_row(event):
        try:
            index = gamer_list.curselection()[0]
            global selected_tuple
            selected_tuple = gamer_list.get(index)
        except IndexError:
            pass  # Prevent errors when no item is selected

    def view_command():
        gamer_list.delete(0, END)
        for row in database.view('gamer'):
            id_name = (row[0], row[1])
            gamer_list.insert(END, id_name)

    def add_gamer_command():
        signup.window()
        view_command()

    def remove_gamer_command():
        try:
            ID = selected_tuple[0]
            if messagebox.askokcancel('Delete User', f'Are you sure you want to remove {selected_tuple[1]} permanently?'):
                database.delete(ID)
            view_command()
        except NameError:
            print('Select a tuple')
            messagebox.showinfo("Warning", "Select a Gamer.")

    def view_gamer_command():
        try:
            ID = selected_tuple[0]
            print(ID)
            userInfo.window(selected_tuple)
        except NameError:
            print('Select a tuple')
            messagebox.showinfo("Warning", "Select a Gamer.")

    # Main home window GUI
    root = Tk()
    root.title(f"{username}'s Gaming Cafe")
    root.geometry("1280x800")  # Set the window size

    # Configure grid rows and columns to center-align contents
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Configure the new theme
    style = ttk.Style()
    style.theme_use("default")

    # General background and foreground colors
    style.configure("TFrame", background="#000000")  # Black
    style.configure("TLabel", background="#000000", foreground="#d1d1d1")  # Timberwolf text
    style.configure("TButton", background="#f5f5dc", foreground="#000000", font=("Arial", 12, "bold"))  # Beige button
    style.map("TButton", background=[("active", "#dbdbdb")], foreground=[("active", "#000000")])  # Button hover
    style.configure("Treeview", background="#ffffff", foreground="#000000", fieldbackground="#ffffff", font=("Arial", 12))  # White background

    cwd = os.path.dirname(os.path.realpath(__file__))

    def on_closing():
        if messagebox.askokcancel('Quit', 'Are you sure you want to quit?'):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Background image
    bg_image_path = cwd + '/images/background.png'  # Replace with your background image path
    bg_image = PhotoImage(file=bg_image_path)
    background_label = Label(root, image=bg_image)
    background_label.place(relwidth=1, relheight=1)  # Set it to cover the entire window

    # Create a frame to hold all widgets (centered)
    content_frame = ttk.Frame(root, style="TFrame")
    content_frame.grid(row=1, column=1, sticky="NSEW", padx=20, pady=20)

    # Buttons Section
    button_frame = ttk.Frame(content_frame, style="TFrame")
    button_frame.grid(row=0, column=1, padx=20, pady=20, sticky="N")

    ttk.Button(button_frame, text='', width=0, command=view_command).grid(row=1, column=0, pady=(0, 50))
    ttk.Button(button_frame, text='Refresh', width=20, command=view_command).grid(row=2, column=0, pady=(0, 20))
    ttk.Button(button_frame, text='Add Gamer', width=20, command=add_gamer_command).grid(row=3, column=0, pady=(0, 20))
    ttk.Button(button_frame, text='Remove Gamer', width=20, command=remove_gamer_command).grid(row=4, column=0, pady=(0, 20))
    ttk.Button(button_frame, text='View Gamer', width=20, command=view_gamer_command).grid(row=5, column=0 , pady=(0, 50))
    ttk.Button(button_frame, text='', width=0, command=view_command).grid(row=6, column=0)

    # Listbox Section with Scrollbar
    list_frame = ttk.Frame(content_frame)
    list_frame.grid(row=0, column=0, rowspan=4, padx=20, pady=20, sticky="NSEW")

    # Make the gamer list box bigger
    gamer_list = Listbox(list_frame, height=20, width=90, font=("Arial", 12, "bold"))  # Larger dimensions with white background
    gamer_list.pack(side=LEFT, fill=BOTH)
    gamer_list.bind('<<ListboxSelect>>', get_selected_row)

    scrollbar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=gamer_list.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    gamer_list.config(yscrollcommand=scrollbar.set)

    view_command()  # Display the Gamers on the home screen

    root.mainloop()


if __name__ == "__main__":
    home('Atharva')