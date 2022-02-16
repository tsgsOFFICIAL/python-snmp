from pysnmp import hlapi
import time

# Variables
target = "192.168.0.2"
credentials = hlapi.CommunityData('GRUPPE1')
engine = hlapi.SnmpEngine()
context = hlapi.ContextData()

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

def get(target, oids, credentials, engine=engine, context=context, port=161):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )

    return fetch(handler, 1)[0]

def set(target, value_pairs, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.setCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_value_pairs(value_pairs)
    )

    return fetch(handler, 1)[0]

def construct_object_types(list_of_oids):
    object_types = []

    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
        
    return object_types

def construct_value_pairs(list_of_pairs):
    pairs = []
    for key, value in list_of_pairs.items():
        pairs.append(hlapi.ObjectType(hlapi.ObjectIdentity(key), value))

    return pairs

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)

            if not error_indication and not error_status:
                items = {}

                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])

                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break

    return result

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
            
    return value

# set(target, {'1.3.6.1.2.1.1.5.0': 'S1'}, credentials)

target_oid = '1.3.6.1.2.1.2.2.1.10.10001'
while True:
    # print(get(target, [target_oid], credentials)[target_oid]) # Simple method to do this

    result = get(target, [target_oid], credentials)
    for key in result:
        print(result[key])
    time.sleep(5)