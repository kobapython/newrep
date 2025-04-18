# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import ipaddress
import subprocess as sub



spisok = ['8.8.4.4', '1.1.1.1', '1.1.1.3', '342.32.123.555', '172.21.41.128']


def ping_ip_addresses(iplist):
    active = []
    unreachable = []
    for ip in iplist:
        pin = sub.run(['ping', '-c', '2', ip], stdout=sub.DEVNULL, stderr=sub.DEVNULL)
        if pin.returncode == 0:
            active.append(ip)
        else:
            unreachable.append(ip)
    result = (active, unreachable)
    return result

print (ping_ip_addresses(spisok))
