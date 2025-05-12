# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""

from netmiko import ConnectHandler, NetMikoAuthenticationException

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import yaml
import logging
import re
from pprint import pprint

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
)
#comm1, reline

def connect_dev (ust, coms):
    try:
        with ConnectHandler(**ust) as ssh:
            ssh.enable()
            res = ssh.send_command(coms)
            prompt = ssh.find_prompt()
        return f"{prompt}{coms}\n{res}\n"
    except  NetMikoAuthenticationException as err:
        logging.warning(err)

def send_show_command_to_devices (devices, command, filename, limit=3):
    text = ""
    with ThreadPoolExecutor(max_workers=limit) as executer:
        result = executer.map(connect_dev, devices, repeat(command))
    with open(filename, 'w') as wf:
        for line in result:
            wf.write(line)

if __name__ == "__main__":
    with open('devices.yaml') as f:
        dev = yaml.safe_load(f)
    comd = "sh ip int br"
    print (send_show_command_to_devices(dev, comd, 'resipbri.txt'))
    
