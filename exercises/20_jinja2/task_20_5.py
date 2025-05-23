# -*- coding: utf-8 -*-
"""
Задание 20.5

Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt,
которые генерируют конфигурацию IPsec over GRE между двумя маршрутизаторами.

Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля,
а templates/gre_ipsec_vpn_2.txt - для второй.

Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах:
cisco_vpn_1.txt и cisco_vpn_2.txt.

Шаблоны надо создавать вручную, скопировав части конфига в соответствующие шаблоны.

Создать функцию create_vpn_config, которая использует эти шаблоны
для генерации конфигурации VPN на основе данных в словаре data.

Параметры функции:
* template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* template2 - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна возвращать кортеж с двумя конфигурациями (строки),
которые получены на основе шаблонов.

Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах
cisco_vpn_1.txt и cisco_vpn_2.txt.
"""
from jinja2 import Environment, FileSystemLoader
import yaml
import os


data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}


def create_vpn_config(template1, template2, data_dict):
    pathtemp1 = os.path.split(os.path.abspath(template1))
    pathtemp2 = os.path.split(os.path.abspath(template2))
    env1 = Environment(loader=FileSystemLoader(pathtemp1[0]), trim_blocks=True, lstrip_blocks=True)
    temp1 = env1.get_template(pathtemp1[1])
    temp2 = env1.get_template(pathtemp2[1])
    ftemp1 = temp1.render(data_dict)
    ftemp2 = temp2.render(data_dict)
    return (ftemp1, ftemp2)
    
if __name__ == "__main__":
    template_file1 = "templates/gre_ipsec_vpn_1.txt"
    template_file2 = "templates/gre_ipsec_vpn_2.txt"
    print(create_vpn_config(template_file1, template_file2, data))
