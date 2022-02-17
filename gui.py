import tkinter as tk

def open_gui():
    window = tk.Tk()
    window.title("Interfaces and their status")
    window.iconbitmap("logo.ico")

    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack()

    window.mainloop()
# window = tk.Tk()
# label = tk.Label(
#     text="Interfaces and their status",
#     fg="white",
#     bg="black",
#     width=175,
#     height=2
# )
# label.pack()

# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow"
# )
# button.pack(side=tk.LEFT)


# window.mainloop()

# print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


# while True:
#     # print(get(target, [target_oid], credentials)[target_oid]) # Simple method to do this

#     result = get(target, [target_oid], credentials)
#     for key in result:
#         print(result[key])
#     time.sleep(1)

