# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
cor = True
while cor:
    ip = input('Введите ip адрес: ')
    iplist = ip.strip().split('.')
    for cont in iplist:
        if not cont.isdigit() or len(iplist) != 4 or int(cont) > 255:
            print('Неправильный IP-адрес')
            break
    else:
        cor = False
        if 1 <= int(iplist[0]) <= 223:
            print('unicast')
        elif 224 <= int(iplist[0]) <= 239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
