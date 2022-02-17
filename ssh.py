import netmiko

def send_command(command, debug = False):
    connection = netmiko.ConnectHandler(device_type="cisco_ios", ip="192.168.0.2", username="cisco3", password="cisco3")

    if debug:
        print(connection.send_command(command))
    else:
        connection.send_command(command)


    connection.disconnect()

def send_config_commands(commands, debug = False):
    connection = netmiko.ConnectHandler(device_type="cisco_ios", ip="192.168.0.2", username="cisco3", password="cisco3")

    if debug:
        print(connection.send_config_set(commands))
    else:
        connection.send_config_set(commands)
        
    connection.disconnect()