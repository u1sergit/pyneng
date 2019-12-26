# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration', '!']
import sys

try:
    with open(sys.argv[1]) as file:
        for line in file:
          is_ignored = False


          for ignor in ignore:
            if line.find(ignor) != -1:
              is_ignored = True


          if not is_ignored:
            print(line.rstrip())
                       
except FileNotFoundError:
    print('File ' + sys.argv[1] + ' does not exist')
except IndexError:
    print("You didn't enter file name")