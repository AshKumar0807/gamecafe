import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import tkinterCommands
import gamesList
import database

# main Window
def window(selected_tuple):
    gamer_info = database.view_gamer(selected_tuple[0])
    print('Selected Gamer: ', gamer_info)

    gamer_ID = gamer_info[0][0]
    gamer_tag = gamer_info[0][1]
    email = gamer_info[0][2]
    tag = gamer_info[0][3]
    age = gamer_info[0][4]

    def open_games_list():
        gamesList.window(gamer_ID)
        print('Back to userinfo')  # Debug line
        view_command()
        print('view_command executed')  # Debug line

    def get_selected_row(event):
        try:
            index = inventory_list.curselection()[0]
            global selected_tuple_games
            selected_tuple_games = inventory_list.get(index)
            print(selected_tuple_games)
        except IndexError:
            pass  # Prevent error when no item is selected

    def view_command():
        inventory_list.delete(0, END)
        for row in database.view_inventory(gamer_ID):
            inventory_list.insert(END, row)

    def remove_game_command():
        try:
            if messagebox.askokcancel(
                'Delete Game',
                f'Are you sure you want to remove {selected_tuple_games[2]} permanently from {gamer_tag}?',
            ):
                database.delete_game(selected_tuple_games[0])
            view_command()
        except NameError:
            messagebox.showinfo("Warning", "Select a Game.")

    user_info = Tk()
    user_info.title(f'Gamer Info: {gamer_tag}')
    user_info.geometry("900x700")  # Set window size

    def remove_gamer_command():
        if messagebox.askokcancel(
            'Delete User',
            f'Are you sure you want to remove {gamer_tag} permanently?',
        ):
            database.delete(gamer_ID)
            user_info.destroy()

    # Configure ttk theme (black and beige)
    style = ttk.Style()
    style.theme_use("default")
    style.configure("TFrame", background="#000000")
    style.configure("TLabel", background="#000000", foreground="#f5f5dc", font=("Arial", 12))
    style.configure("TButton", background="#f5f5dc", foreground="#000000", font=("Arial", 10, "bold"))
    style.map("TButton", background=[("active", "#dbdbdb")], foreground=[("active", "#000000")])

    # Main content frame
    main_frame = ttk.Frame(user_info, style="TFrame")
    main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

    # User info labels
    ttk.Label(main_frame, text='Name:').grid(row=0, column=0, sticky=W, padx=10, pady=5)
    ttk.Label(main_frame, text=gamer_tag).grid(row=0, column=1, sticky=W, padx=10, pady=5)

    ttk.Label(main_frame, text='Email:').grid(row=1, column=0, sticky=W, padx=10, pady=5)
    ttk.Label(main_frame, text=email).grid(row=1, column=1, sticky=W, padx=10, pady=5)

    ttk.Label(main_frame, text='Gamer Tag:').grid(row=2, column=0, sticky=W, padx=10, pady=5)
    ttk.Label(main_frame, text=tag).grid(row=2, column=1, sticky=W, padx=10, pady=5)

    ttk.Label(main_frame, text='Age:').grid(row=3, column=0, sticky=W, padx=10, pady=5)
    ttk.Label(main_frame, text=age).grid(row=3, column=1, sticky=W, padx=10, pady=5)

    # Buttons
    button_frame = ttk.Frame(main_frame, style="TFrame")
    button_frame.grid(row=0, column=3, rowspan=4, sticky=N, padx=20, pady=10)

    ttk.Button(button_frame, text='Add Game', width=15, command=open_games_list).grid(row=0, column=0, pady=10)
    ttk.Button(button_frame, text='Remove Game', width=15, command=remove_game_command).grid(row=1, column=0, pady=10)
    ttk.Button(button_frame, text='Delete User', width=15, command=remove_gamer_command).grid(row=2, column=0, pady=10)
    ttk.Button(button_frame, text='Refresh', width=15, command=view_command).grid(row=3, column=0, pady=10)

    # Inventory list (games list)
    list_frame = ttk.Frame(main_frame)
    list_frame.grid(row=5, column=0, columnspan=4, sticky=W + E, padx=10, pady=20)

    inventory_list = Listbox(list_frame, height=20, width=80, font=("Arial", 10))
    inventory_list.pack(side=LEFT, fill=BOTH, expand=True)
    inventory_list.bind('<<ListboxSelect>>', get_selected_row)

    scrollbar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=inventory_list.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    inventory_list.config(yscrollcommand=scrollbar.set)

    # Load inventory data
    view_command()

    user_info.mainloop()