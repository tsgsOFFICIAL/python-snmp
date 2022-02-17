import tkinter as tk
import shared
import snmp

def toggle_state(oid, state):
    def wrapper(oid=oid, state=state):
        if state == 1:
            print("UP")
            snmp.set(shared.target, {'1.3.6.1.2.1.1.5.0': 'UP'}, shared.credentials)
        else:
            print("DOWN")
            snmp.set(shared.target, {'1.3.6.1.2.1.1.5.0': 'DOWN'}, shared.credentials)
    return wrapper

def open_gui(dict_list):
    window = tk.Tk()
    window.title("Interfaces and their status")
    window.iconbitmap("logo.ico")

    for i in range(3):
        window.rowconfigure(i, weight=1, minsize=25)
        
        for j in range(12):
            window.columnconfigure(j, weight=1, minsize=25)
            
            btn = tk.Button(
                text=f"Row {i}\nColumn {j}",
                bg="green",
                fg="white",
                command=toggle_state(0, i)
            )

            btn.grid(row=i, column=j, padx=5, pady=5)

    window.mainloop()