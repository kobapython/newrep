# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map (config_filename):
    daccess = {}
    dtrunk = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface '):
                key = str(line.split()[-1])
                print(key)
            elif 'switchport access vlan' in line:
                value = int(line.split()[-1])
                daccess[key]=value
                print(daccess)
            elif 'switchport trunk allowed vlan' in line:
                valuet = [int(vls) for vls in(line.split()[-1].split(','))]
                dtrunk[key]=valuet
    print(daccess)
    print(dtrunk)
    result = (daccess, dtrunk)
    return result

print(get_int_vlan_map('config_sw1.txt'))
