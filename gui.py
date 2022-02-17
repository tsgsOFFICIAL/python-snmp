import tkinter as tk
import shared
import snmp
import ssh

def toggle_state(oid, state, name):
    def wrapper(oid=oid, state=state, name=name):
        ssh.send_config_commands([
            f"interface {name}",
            f"{'no ' if state == 2 else ''}shutdown"
        ])
    return wrapper

def open_gui(dict_list):
    window = tk.Tk()
    window.title("Interfaces and their status")
    window.iconbitmap("logo.ico")

    for i in range(10):
        window.rowconfigure(i, weight=1, minsize=25)
        
        for j in range(12):
            window.columnconfigure(j, weight=1, minsize=25)
            
    for i in range(len(dict_list)):
        # int(i / 12) = row
        # i % 12 = column
        # print(f"{i} % 12 = {i % 12}")
        # print(f"{i} / 12 rounded = {int(i / 12)}")
        
        btn = tk.Button(
            text = f"{dict_list[i]['name']}\n{'UP' if dict_list[i]['status'] == 1 else 'OPEN' if dict_list[i]['status'] == 0 else 'DOWN'}",
            bg = f"{'green' if dict_list[i]['status'] == 1 else 'yellow' if dict_list[i]['status'] == 0 else 'red'}",
            #f"{color.OKGREEN + 'UP' if result[key] == 1 else color.FAIL + 'DOWN'}"
            fg = f"{'white' if dict_list[i]['status'] != 0 else 'black'}",
            command = toggle_state(dict_list[i]['status_oid'], dict_list[i]['status'], dict_list[i]['name'])
        )

        btn.grid(row = int(i / 12), column = i % 12, padx = 5, pady = 5)
    # for dict in dict_list:
    #     print(dict)
    window.mainloop()