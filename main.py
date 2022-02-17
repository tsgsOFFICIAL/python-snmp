from pysnmp import hlapi
import time
import requests
import tkinter as tk
import snmp

# Variables
target = "192.168.0.2"
credentials = hlapi.CommunityData('GRUPPE1')

# This is just an "enum" for colors in the console
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

target_oid = '1.3.6.1.2.1.2.2.1.8'
results = snmp.get_bulk(target, [target_oid], credentials, 27)

for result in results:
    for key in result:
        # print(f"Key: {key} - Value: {result[key]}")
        description_oid = f"{key[:key.rindex('.') - 1]}2{key[key.rindex('.'):len(key)]}"
        name = snmp.get(target, [description_oid], credentials)[description_oid]
        status = f"{color.OKGREEN + 'UP' if result[key] == 1 else color.FAIL + 'DOWN'}"

        print(f"{color.WARNING}{name} ({status}{color.WARNING}){color.ENDC}")

window = tk.Tk()
window.title("Interfaces and their status")

for i in range(len(results)):
    # print(results[i])
    button = tk.Button(
        text="Click me!",
        bg="blue",
        fg="yellow"
        )
    button.pack(side=tk.LEFT)
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

# set(target, {'1.3.6.1.2.1.1.5.0': 'S1'}, credentials)