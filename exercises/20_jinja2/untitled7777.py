
import yaml
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler, NetMikoAuthenticationException
from itertools import repeat



def send_command_to(device, command):
    tutun = ['Tunnel 1', 'Tunnel 2', 'Tunnel 3', 'Tunnel 5', 'Tunnel 6', 'Tunnel 7', 'Tunnel 8', 
    'Tunnel 9', 'Tunnel 56', 'Tunnel3', 'Tunnel 4', 'Tunnel 5', 'Tunnel 9', 'Tunnel 55']
    spis = []
    for tun in tutun:
        com = command+tun
        spis.append(com)
    print(spis) 
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(spis, strip_prompt=False)
    print (result)

if __name__ == "__main__":
    src_dev = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'}
    dst_dev = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'}
    print (send_command_to (dst_dev, "no interface "))
