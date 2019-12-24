# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_ok = False
try_again_flag = True

octets = []
while ( len(octets) != 4 or try_again_flag):
    ip_addr = input("Введите IP-адреса в формате 10.0.1.1:\n")
    ip_addr_int = []
    octets = ip_addr.split('.')
    if (''.join(octets).isdigit()):
        try_again_flag = False
        for octet in octets:
            if int(octet) > 255 or int(octet) < 0:
                try_again_flag = True
            else:
                ip_addr_int.append(int(octet))
                
    
if ip_addr_int[0] <= 223:
    print('unicast')
elif ip_addr_int[0] >= 224 and ip_addr_int[0] <= 239:
    print('multicast')
else:
    is_local_broadcast = False
    for octet in ip_addr_int:
        if octet == 255:
            is_local_broadcast = True
        else:
            is_local_broadcast = False
    if is_local_broadcast:
        print('is_local_broadcast')
    else:
        print('unused')