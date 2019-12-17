# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
l1 = ospf_route.split(' ')
fstroka = """
Protocol:              OSPF
Prefix:                {4}
AD/Metric:             {3}
Next-Hop:              {2}
Last update:           {1}
Outbound Interface     {0}
"""
print(fstroka.format(l1[-1], l1[-2].strip(','), l1[-3].strip(','), l1[-5].strip('[]'), l1[-6]))
