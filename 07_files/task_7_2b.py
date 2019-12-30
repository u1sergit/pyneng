# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


ignore = ['duplex', 'alias', 'Current configuration', '!', 'switchport']
import sys

try:
    with open(sys.argv[1]) as file:
        with open('config_sw1_cleared.txt', 'w') as f:
            for line in file:'config_sw1_cleared.txt'
                is_ignored = False


                for ignor in ignore:
                    if line.find(ignor) != -1:
                        is_ignored = True
                    
                if not is_ignored:
                    f.write(line)
                       
except FileNotFoundError:
    print('File ' + sys.argv[1] + ' does not exist')
except IndexError:
    print("You didn't enter file name")