# -*- coding: utf-8 -*-
'''
Задание 5.3

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk)
* номере интерфейса (тип и номер, вида Gi0/3)
* номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода,
должна возвращаться соответствующая конфигурация access или trunk
(шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса,
а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


work_mode = input('Введите режим работы интерфейса (access or trunk): ')
i_type = input('Введите тип и номер интерфейса например Fa0/6 : ')
vlan_numbers = input('Введите номер влан(ов)через запятую: ')

if (work_mode == 'access'):
    print('interface ' + i_type)
    print(access_template[0])
    print(access_template[1].format(vlan_numbers))
    print(access_template[2])
    print(access_template[3])
    print(access_template[4])
elif (work_mode == 'trunk'):
    print('interface ' + i_type)
    print(trunk_template[0])
    print(trunk_template[1])
    print(trunk_template[2].format(vlan_numbers))


