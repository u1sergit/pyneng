# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

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
                print('Неправильный IP-адрес')
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