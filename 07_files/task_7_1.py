# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

result = '''
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''


with open('ospf.txt') as f:
    
    for line in f:
        param_list = []
        params = line.rstrip().split(" ")        
        for param in params:
            if (param):
                param_list.append(param.strip(',[]'))
        print(result.format(param_list[1],
        param_list[2],
        param_list[4],
        param_list[5],
        param_list[6]
        
        ))
    
