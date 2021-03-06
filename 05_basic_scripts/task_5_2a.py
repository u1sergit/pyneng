# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('ввод IP-сети в формате: 10.1.1.0/24\n')
print()
ip = ip.split('/')
ip[0] = ip[0].split('.')
print('{:<8}  {:<8}  {:<8}  {:<8}'.format(
    ip[0][0], ip[0][1], ip[0][2], ip[0][3]))
print('{:08b}  {:08b}  {:08b}  {:08b}'.format(
    int(ip[0][0]), int(ip[0][1]), int(ip[0][2]), int(ip[0][3])))

try:
    mask = int(ip[1])
except IndexError:
    if (len(ip) == 1 ): print('Вы не указали маску. Она будет вычислена из ip адреса')
    mask = 


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
