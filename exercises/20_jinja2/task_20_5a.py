# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует
шаблоны из задания 20.5 для настройки VPN на маршрутизаторах
на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству 1
* dst_device_params - словарь с параметрами подключения к устройству 2
* src_template - имя файла с шаблоном, который создает конфигурацию для строны 1
* dst_template - имя файла с шаблоном, который создает конфигурацию для строны 2
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов
и данных на каждом устройстве с помощью netmiko.
Функция возвращает кортеж с выводом команд с двух
маршрутизаторов (вывод, которые возвращает метод netmiko send_config_set).
Первый элемент кортежа - вывод с первого устройства (строка),
второй элемент кортежа - вывод со второго устройства.

При этом, в словаре data не указан номер интерфейса Tunnel,
который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel,
взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 5.
И надо будет настроить интерфейс Tunnel 5.

Для этого задания тест проверяет работу функции на первых двух устройствах
из файла devices.yaml. И проверяет, что в выводе есть команды настройки
интерфейсов, но при этом не проверяет настроенные номера тунелей и другие команды.
Они должны быть, но тест упрощен, чтобы было больше свободы выполнения.
"""
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import yaml
import re
import os

data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    tunlist = []
    num = 0
    src_tem_path = os.path.split(os.path.abspath(src_template))
    dst_tem_path = os.path.split(os.path.abspath(dst_template))
    env_src = Environment(loader=FileSystemLoader(src_tem_path[0]), trim_blocks=True, lstrip_blocks=True)
    src_temp_name = env_src.get_template(src_tem_path[1])
    env_dst = Environment(loader=FileSystemLoader(dst_tem_path[0]), trim_blocks=True, lstrip_blocks=True)
    dst_temp_name = env_dst.get_template(dst_tem_path[1])
    for line in [src_device_params, dst_device_params]:
        retun = []
        with ConnectHandler(**line) as ssh:
            ssh.enable()
            tunr1 = ssh.send_command('show ip inter brief | in Tunnel')
            retun = re.findall(r'(Tunnel\d+)', tunr1)
            tunlist.extend(retun)
    print(tunlist)
    if tunlist:
        tunlist = [int(number.replace('Tunnel','')) for number in tunlist]
        tunlist.sort()
        num = tunlist[0]
        tunset = set(tunlist)
        while num in tunset:
            num += 1
    vpn_data_dict["tun_num"] = num
    src_config = src_temp_name.render(vpn_data_dict).split('\n')
    dst_config = dst_temp_name.render(vpn_data_dict).split('\n')
    print(src_config, '\n\n')
    print(dst_config, '\n\n')
    with ConnectHandler(**src_device_params) as ssh:
        ssh.enable()
        rep_src = ssh.send_config_set(src_config)
    print ("Done srtTunn")
    with ConnectHandler(**dst_device_params) as ssh:
        ssh.enable()
        rep_dst = ssh.send_config_set(dst_config)
    return (rep_src, rep_dst)

if __name__ == "__main__":
    src_dev = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',}
    dst_dev = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',}
    ftemp1 = 'templates/gre_ipsec_vpn_1.txt'
    ftemp2 = 'templates/gre_ipsec_vpn_2.txt'
    print(configure_vpn(src_dev, dst_dev, ftemp1, ftemp2, data))
