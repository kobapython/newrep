# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

import subprocess
from concurrent.futures import ThreadPoolExecutor
import logging


def ping_exec(ip1list):
    reply = subprocess.run(['ping', '-c', '2', ip1list], stdout=subprocess.DEVNULL)
    if reply.returncode == 0:
        reation = '{} is Active'.format(ip1list.strip())
    else:
        reation  = '{} is Unreachable'.format(ip1list.strip())
    return reation
        

def ping_ip_addresses(ip_list, limit=3):
    active = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_exec, ip_list)
        for host, result in zip(ip_list, result):
            if 'Active' in result:
                active.append(host)
            else:
                unreachable.append(host)
    return (active, unreachable)
                
            
if __name__ == '__main__':
    print (ping_ip_addresses(['192.168.100.1', '192.168.100.33', '192.168.100.2', '192.168.100.56', '192.168.100.3', '192.168.100.39']))


