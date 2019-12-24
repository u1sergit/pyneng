# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import sys

print(len(sys.argv))


ip = sys.argv[1].split('/')
ip[0] = ip[0].split('.')
print('{:<8}  {:<8}  {:<8}  {:<8}'.format(
    ip[0][0], ip[0][1], ip[0][2], ip[0][3]))
print('{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}'.format(
    int(ip[0][0]), int(ip[0][1]), int(ip[0][2]), int(ip[0][3])))

try:
    mask = int(ip[1])
except IndexError:
    mask = 24


print('/' + str(mask))

if ((mask - 8) > 0):
    oct1 = '1'*8
    mask = mask - 8
    if ((mask - 8) > 0):
        oct2 = '1'*8
        mask = mask - 8
        if ((mask - 8) > 0):
            oct3 = '1'*8
            oct4 = '1' * (mask - 8)
            print('{:<8}  {:<8}  {:<8}  {:<8}'.format(
                int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)))
            print('{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}'.format(
                int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)))

        else:
            oct3 = '1'*mask
            print('{:<8}  {:<8}  {:<8}  {:<8}'.format(
                int(oct1, 2), int(oct2, 2), int(oct3, 2), 0))
            print('{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}'.format(
                int(oct1, 2), int(oct2, 2), int(oct3, 2), 0))

    else:
        oct2 = '1'*mask
        print('{:<8}  {:<8}  {:<8}  {:<8}'.format(
            int(oct1, 2), int(oct2, 2), 0, 0))
        print('{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}'.format(
            int(oct1, 2), int(oct2, 2), 0, 0))


else:
    oct1 = '1'*mask
    print('{:<8}  {:<8}  {:<8}  {:<8}'.format(int(oct1, 2), 0, 0, 0))
    print('{:0>8b}  {:0>8b}  {:0>8b}  {:0>8b}'.format(int(oct1, 2), 0, 0, 0))
