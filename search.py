# -*- coding: utf-8 -*-
import stat, sys, os, string, commands
#Записываем в переменную шаблон поиска, введенный пользователем
try:
    pattern = raw_input("Введите шаблон поиска:\n")
    #запускаем команду 'find' и присваиваем результат переменной
    commandString = "find " + pattern
    commandOutput = commands.getoutput(commandString)
    findResults = string.split(commandOutput, "\n")
    #выводим найденные файлы вместе с правами доступа
    print "Файлы:"
    print commandOutput
    print "================================"
    for file in findResults:
        mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
        print "\nPermissions for file ", file, ":"
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
               if mode & getattr(stat,"S_I"+perm+level):
                   print level, " имеет ", perm, " права доступа"
               else:
                   print level, " не имеет ", perm, " прав доступа"
except:
    print "Возникла проблема! Проверьте сообщение выше."