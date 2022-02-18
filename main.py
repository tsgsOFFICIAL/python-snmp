import requests
import time
import shared
import snmp
import gui


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

if_status_oid = '1.3.6.1.2.1.2.2.1.8' # Interface status
if_admin_status_oid = '.1.3.6.1.2.1.2.2.1.7' # Interface admin status
if_number_oid = '1.3.6.1.2.1.2.1.0' # Interface number/count
interface_count = snmp.get(shared.target, [if_number_oid], shared.credentials)[if_number_oid] - 1

while shared.run:
    if_status_results = snmp.get_bulk(shared.target, [if_status_oid], shared.credentials, interface_count)

    if_admin_status_results = snmp.get_bulk(shared.target, [if_admin_status_oid], shared.credentials, interface_count)

    gui_dictionaries = []

    # Result is a dictionary, key value pair, with oid as key and status as value
    for index, result in enumerate(if_status_results):
        # print(result)
        # print(if_admin_status_results[index])
        for key in result:
            # print(f"Key: {key} - Value: {result[key]}")
            description_oid = f"{key[:key.rindex('.') - 1]}2{key[key.rindex('.'):len(key)]}"
            name = snmp.get(shared.target, [description_oid], shared.credentials)[description_oid]
            status = f"{color.OKGREEN + 'UP' if result[key] == 1 else color.FAIL + 'DOWN'}"
            admin_key = ""
            state = ""

            for k in if_admin_status_results[index]:
                admin_key = k
            
            if result[key] == if_admin_status_results[index][admin_key]:
                state = result[key]
            else:
                state = 0
            
            dictionary = {
                "status_oid": key,
                "name": name,
                "status": state
            }

            gui_dictionaries.append(dictionary)

            # print(f"{color.WARNING}{name} ({status}{color.WARNING}){color.ENDC}")

    gui.get_dict_list(gui_dictionaries)

    # if open_gui:
        # gui.open_gui()
        # open_gui = False

    # time.sleep(1)
    # set(target, {'1.3.6.1.2.1.1.5.0': 'S1'}, credentials)

    # print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")