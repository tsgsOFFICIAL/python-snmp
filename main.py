from pysnmp import hlapi
import time
import requests
import snmp
import gui

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

target_oid = '1.3.6.1.2.1.2.2.1.8' # Interface status
results = snmp.get_bulk(target, [target_oid], credentials, 27)

gui_dictionaries = []

# Result is a dictionary, key value pair, with oid as key and status as value
for result in results:
    for key in result:
        # print(f"Key: {key} - Value: {result[key]}")
        description_oid = f"{key[:key.rindex('.') - 1]}2{key[key.rindex('.'):len(key)]}"
        name = snmp.get(target, [description_oid], credentials)[description_oid]
        status = f"{color.OKGREEN + 'UP' if result[key] == 1 else color.FAIL + 'DOWN'}"

        dictionary = {
            "status_oid": key,
            "name": name,
            "status": result[key]
        }

        gui_dictionaries.append(dictionary)

        # print(f"{color.WARNING}{name} ({status}{color.WARNING}){color.ENDC}")

gui.open_gui(gui_dictionaries)

# set(target, {'1.3.6.1.2.1.1.5.0': 'S1'}, credentials)

# print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


# while True:
#     # print(get(target, [target_oid], credentials)[target_oid]) # Simple method to do this

#     result = get(target, [target_oid], credentials)
#     for key in result:
#         print(result[key])
#     time.sleep(1)

