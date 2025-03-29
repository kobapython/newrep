# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите ip сеть: ')

redip = ip[0:ip.find('/')].split('.')
mask = ip[ip.find('/')+1:]

mone = int(mask)
mzero = 32 - mone
mline = '1'*mone + '0'*mzero
moct1, moct2, moct3, moct4 = mline[0:8], mline[8:16], mline[16:24], mline[24:32]
ipbin = '{:08b}{:08b}{:08b}{:08b}'.format(int(redip[0]), int(redip[1]),int(redip[2]), int(redip[3]))
ipnet = ipbin[0:mone] + '0'*mzero

ipoct1, ipoct2 = int(ipnet[0:8], 2), int(ipnet[8:16], 2), 
ipoct3, ipoct4 = int(ipnet[16:24], 2), int(ipnet[24:32], 2)

template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{fm}
{4:<10}{5:<10}{6:<10}{7:<10}
{4:08b}  {5:08b}  {6:08b}  {7:08b}
    '''
resalt = template.format(ipoct1, ipoct2, ipoct3, ipoct4, int(moct1, 2), int(moct2, 2), int(moct3, 2), int(moct4, 2), fm=mask)
print (resalt)
