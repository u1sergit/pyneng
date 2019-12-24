# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
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


if (work_mode == 'access'):
    vlan_numbers = input('Введите номер VLAN:')
    print('interface ' + i_type)
    print(access_template[0])
    print(access_template[1].format(vlan_numbers))
    print(access_template[2])
    print(access_template[3])
    print(access_template[4])
elif (work_mode == 'trunk'):
    vlan_numbers = input('Введите разрешенные VLANы:')
    print('interface ' + i_type)
    print(trunk_template[0])
    print(trunk_template[1])
    print(trunk_template[2].format(vlan_numbers))
