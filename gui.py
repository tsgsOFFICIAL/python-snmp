import tkinter as tk
from tkinter import messagebox
import shared
import snmp
import ssh

dict_list = []
window = ""

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\nCancel to reload data"):
        window.destroy()
        shared.run = False
    else:
        window.destroy()

def get_dict_list(list):
    global dict_list
    dict_list = list
    open_gui()

def toggle_state(oid, state, name):
    def wrapper(oid=oid, state=state, name=name):
        ssh.send_config_commands([
            f"interface {name}",
            f"{'no ' if state == 2 else ''}shutdown"
        ])
        # print(oid)
        # snmp.set(shared.target, {'1.3.6.1.2.1.1.5.0': name}, shared.credentials) # Set hostname     
        # snmp.set(shared.target, {oid, '1'}, shared.credentials)
        
        window.destroy()
    return wrapper

def open_gui():
    global window
    window = tk.Tk()
    window.title("Interfaces and their status")
    window.iconbitmap("logo.ico")

    for i in range(int(len(dict_list) + 1)):
        window.rowconfigure(i, weight=0)
        
        for j in range(12):
            window.columnconfigure(j, weight=1)
            
    for i in range(len(dict_list)):
        # int(i / 12) = row
        # i % 12 = column
        # print(f"{i} % 12 = {i % 12}")
        # print(f"{i} / 12 rounded = {int(i / 12)}")
        
        btn = tk.Button(
            text = f"{dict_list[i]['name']}\n{'UP' if dict_list[i]['status'] == 1 else 'DOWN' if dict_list[i]['status'] == 0 else 'ADM. DOWN'}",
            bg = f"{'green' if dict_list[i]['status'] == 1 else 'yellow' if dict_list[i]['status'] == 0 else 'red'}",
            fg = f"{'white' if dict_list[i]['status'] != 0 else 'black'}",
            command = toggle_state(dict_list[i]['status_oid'], dict_list[i]['status'], dict_list[i]['name'])
        )

        btn.grid(row = int(i / 12), column = i % 12, padx = 5, pady = 5, sticky="ew")


    window.protocol("WM_DELETE_WINDOW", on_closing)
    # window.attributes("-fullscreen", True)
    window.state('zoomed')
    window.mainloop()