# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



def get_int_vlan_map (config_filename):
    daccess = {}
    dtrunk = {}
    ct = 0
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface '):
                key = str(line.split()[-1])
                ct = 1
            elif 'switchport access vlan' in line:
                value = int(line.split()[-1])
                daccess[key]=value
                ct = 0
            elif 'switchport trunk allowed vlan' in line:
                valuet = [int(vls) for vls in(line.split()[-1].split(','))]
                dtrunk[key]=valuet
                ct = 0
            elif 'duplex auto' in line and ct:
                daccess[key]=1
    result = (daccess, dtrunk)
    return result

print(get_int_vlan_map('config_sw2.txt'))
