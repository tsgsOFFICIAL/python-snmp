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

for result in results:
    for key in result:
        # print(f"Key: {key} - Value: {result[key]}")
        description_oid = f"{key[:key.rindex('.') - 1]}2{key[key.rindex('.'):len(key)]}"
        name = snmp.get(target, [description_oid], credentials)[description_oid]
        status = f"{color.OKGREEN + 'UP' if result[key] == 1 else color.FAIL + 'DOWN'}"

        print(f"{color.WARNING}{name} ({status}{color.WARNING}){color.ENDC}")

gui.open_gui()

# set(target, {'1.3.6.1.2.1.1.5.0': 'S1'}, credentials)