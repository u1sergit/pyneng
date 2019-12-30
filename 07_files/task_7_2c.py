# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

ignore = ['duplex', 'alias', 'Current configuration', '!', 'switchport']
import sys
print(sys.argv[1] + " ~~~> " + sys.argv[2])


try:
    with open(sys.argv[1]) as file:
        with open(sys.argv[2], 'w') as f:
            for line in file:
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