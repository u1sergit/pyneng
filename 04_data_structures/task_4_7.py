# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
mac = mac.split(':')

mac[0] = int(mac[0],16)
mac[1] = int(mac[1],16)
mac[2] = int(mac[2],16)

print(bin(mac[0]) + bin(mac[1]) + bin(mac[2]))

