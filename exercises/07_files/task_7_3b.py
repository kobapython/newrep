# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = input('Введите номер vlan: ')

lstore = []

with open('CAM_table.txt') as f:
    for line in f:
        ls = line.split()
        if len(ls) < 2:
            continue 
        elif ls[0][0].isdigit():
            ls.pop(2)
            ls[0] = int(ls[0])
            lstore.append(ls)
        else:
            pass

lsres = sorted(lstore)

for tab in lsres:
    if int(vlan) == tab[0]:
        print('{:<8}{:18}{:10}'.format(tab[0], tab[1], tab[2]))
    else:
        pass
