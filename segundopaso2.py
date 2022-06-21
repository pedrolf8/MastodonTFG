import csv
import json
import sys
from subprocess import call
import os

if(len(sys.argv)>2):
    if(sys.argv[2] == "hora"):
        y = sys.argv[1] + '/Degree'
        print(y)
        os.chdir(str(y))
        os.system('ls > lista.txt')
        h3 = open('lista.txt', 'r')
        carpeta = ''
        for row in h3:
            if 'Degree' in row:
                carpeta = row
        w = str(carpeta)
        w = w.replace("\n", "")
        os.chdir(w)
        call(['mv', 'partition-0', '../partition-0-hora'])
        call(['mv', 'partition-1', '../partition-1-hora'])
        call(['mv', 'partition-2', '../partition-2-hora'])
        call(['mv', 'partition-3', '../partition-3-hora'])
        call(['mv', 'partition-4', '../partition-4-hora'])
        call(['mv', 'partition-5', '../partition-5-hora'])
        call(['mv', 'partition-6', '../partition-6-hora'])
        call(['mv', 'partition-7', '../partition-7-hora'])

        os.chdir('..')
        call(['rm', '-r', w])
        a = open('partition-0-hora', 'r')
        b = open('partition-1-hora', 'r')
        c = open('partition-2-hora', 'r')
        d = open('partition-3-hora', 'r')
        e = open('partition-4-hora', 'r')
        f = open('partition-5-hora', 'r')
        g = open('partition-6-hora', 'r')
        h = open('partition-7-hora', 'r')
        i = open('dathora.csv', 'a')

        i.write('date,window,userid,in-degree,out-degree,degree\n')
        for line in a:
            i.write(line)
        for line in b:
            i.write(line)
        for line in c:
            i.write(line)
        for line in d:
            i.write(line)
        for line in e:
            i.write(line)
        for line in f:
            i.write(line)
        for line in g:
            i.write(line)
        for line in h:
            i.write(line)

        a.close()
        b.close()
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()
    if(sys.argv[2] == "dia"):
        y = sys.argv[1] + '/Degree'
        print(y)
        os.chdir(str(y))
        os.system('ls > lista.txt')
        h3 = open('lista.txt', 'r')
        carpeta = ''
        for row in h3:
            if 'Degree' in row:
                carpeta = row
        w = str(carpeta)
        w = w.replace("\n", "")
        os.chdir(w)
        call(['mv', 'partition-0', '../partition-0-dia'])
        call(['mv', 'partition-1', '../partition-1-dia'])
        call(['mv', 'partition-2', '../partition-2-dia'])
        call(['mv', 'partition-3', '../partition-3-dia'])
        call(['mv', 'partition-4', '../partition-4-dia'])
        call(['mv', 'partition-5', '../partition-5-dia'])
        call(['mv', 'partition-6', '../partition-6-dia'])
        call(['mv', 'partition-7', '../partition-7-dia'])

        os.chdir('..')
        call(['rm', '-r', w])
        a = open('partition-0-dia', 'r')
        b = open('partition-1-dia', 'r')
        c = open('partition-2-dia', 'r')
        d = open('partition-3-dia', 'r')
        e = open('partition-4-dia', 'r')
        f = open('partition-5-dia', 'r')
        g = open('partition-6-dia', 'r')
        h = open('partition-7-dia', 'r')
        i = open('datdia.csv', 'a')

        i.write('date,window,userid,in-degree,out-degree,degree\n')
        for line in a:
            i.write(line)
        for line in b:
            i.write(line)
        for line in c:
            i.write(line)
        for line in d:
            i.write(line)
        for line in e:
            i.write(line)
        for line in f:
            i.write(line)
        for line in g:
            i.write(line)
        for line in h:
            i.write(line)

        a.close()
        b.close()
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()
    if(sys.argv[2] == "semana"):
        y = sys.argv[1] + '/Degree'
        print(y)
        os.chdir(str(y))
        os.system('ls > lista.txt')
        h3 = open('lista.txt', 'r')
        carpeta = ''
        for row in h3:
            if 'Degree' in row:
                carpeta = row
        w = str(carpeta)
        w = w.replace("\n", "")
        os.chdir(w)
        call(['mv', 'partition-0', '../partition-0-semana'])
        call(['mv', 'partition-1', '../partition-1-semana'])
        call(['mv', 'partition-2', '../partition-2-semana'])
        call(['mv', 'partition-3', '../partition-3-semana'])
        call(['mv', 'partition-4', '../partition-4-semana'])
        call(['mv', 'partition-5', '../partition-5-semana'])
        call(['mv', 'partition-6', '../partition-6-semana'])
        call(['mv', 'partition-7', '../partition-7-semana'])

        os.chdir('..')
        call(['rm', '-r', w])
        a = open('partition-0-semana', 'r')
        b = open('partition-1-semana', 'r')
        c = open('partition-2-semana', 'r')
        d = open('partition-3-semana', 'r')
        e = open('partition-4-semana', 'r')
        f = open('partition-5-semana', 'r')
        g = open('partition-6-semana', 'r')
        h = open('partition-7-semana', 'r')
        i = open('datsemana.csv', 'a')

        i.write('date,window,userid,in-degree,out-degree,degree\n')
        for line in a:
            i.write(line)
        for line in b:
            i.write(line)
        for line in c:
            i.write(line)
        for line in d:
            i.write(line)
        for line in e:
            i.write(line)
        for line in f:
            i.write(line)
        for line in g:
            i.write(line)
        for line in h:
            i.write(line)

        a.close()
        b.close()
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()

    if(sys.argv[2] == "mes"):
        y = sys.argv[1] + '/Degree'
        print(y)
        os.chdir(str(y))
        os.system('ls > lista.txt')
        h3 = open('lista.txt', 'r')
        carpeta = ''
        for row in h3:
            if 'Degree' in row:
                carpeta = row
        w = str(carpeta)
        w = w.replace("\n", "")
        os.chdir(w)
        call(['mv', 'partition-0', '../partition-0-mes'])
        call(['mv', 'partition-1', '../partition-1-mes'])
        call(['mv', 'partition-2', '../partition-2-mes'])
        call(['mv', 'partition-3', '../partition-3-mes'])
        call(['mv', 'partition-4', '../partition-4-mes'])
        call(['mv', 'partition-5', '../partition-5-mes'])
        call(['mv', 'partition-6', '../partition-6-mes'])
        call(['mv', 'partition-7', '../partition-7-mes'])

        os.chdir('..')
        call(['rm', '-r', w])
        a = open('partition-0-mes', 'r')
        b = open('partition-1-mes', 'r')
        c = open('partition-2-mes', 'r')
        d = open('partition-3-mes', 'r')
        e = open('partition-4-mes', 'r')
        f = open('partition-5-mes', 'r')
        g = open('partition-6-mes', 'r')
        h = open('partition-7-mes', 'r')
        i = open('datmes.csv', 'a')

        i.write('date,window,userid,in-degree,out-degree,degree\n')
        for line in a:
            i.write(line)
        for line in b:
            i.write(line)
        for line in c:
            i.write(line)
        for line in d:
            i.write(line)
        for line in e:
            i.write(line)
        for line in f:
            i.write(line)
        for line in g:
            i.write(line)
        for line in h:
            i.write(line)

        a.close()
        b.close()
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()

    if(sys.argv[2] == "año"):
        y = sys.argv[1] + '/Degree'
        print(y)
        os.chdir(str(y))
        os.system('ls > lista.txt')
        h3 = open('lista.txt', 'r')
        carpeta = ''
        for row in h3:
            if 'Degree' in row:
                carpeta = row
        w = str(carpeta)
        w = w.replace("\n", "")
        os.chdir(w)
        call(['mv', 'partition-0', '../partition-0-año'])
        call(['mv', 'partition-1', '../partition-1-año'])
        call(['mv', 'partition-2', '../partition-2-año'])
        call(['mv', 'partition-3', '../partition-3-año'])
        call(['mv', 'partition-4', '../partition-4-año'])
        call(['mv', 'partition-5', '../partition-5-año'])
        call(['mv', 'partition-6', '../partition-6-año'])
        call(['mv', 'partition-7', '../partition-7-año'])

        os.chdir('..')
        call(['rm', '-r', w])
        a = open('partition-0-año', 'r')
        b = open('partition-1-año', 'r')
        c = open('partition-2-año', 'r')
        d = open('partition-3-año', 'r')
        e = open('partition-4-año', 'r')
        f = open('partition-5-año', 'r')
        g = open('partition-6-año', 'r')
        h = open('partition-7-año', 'r')
        i = open('dataño.csv', 'a')

        i.write('date,window,userid,in-degree,out-degree,degree\n')
        for line in a:
            i.write(line)
        for line in b:
            i.write(line)
        for line in c:
            i.write(line)
        for line in d:
            i.write(line)
        for line in e:
            i.write(line)
        for line in f:
            i.write(line)
        for line in g:
            i.write(line)
        for line in h:
            i.write(line)

        a.close()
        b.close()
        c.close()
        d.close()
        e.close()
        f.close()
        g.close()
        h.close()
        i.close()
else:
    # os.mkdir('ConnectedComponents')
    # os.system('ls > listasss.txt')
    # h3 = open('listasss.txt', 'r')
    # carpeta = ''
    # for row in h3:
    #     if 'Connected' in row:
    #         print(row)
    #         carpeta = row
    # w = str(carpeta)
    # w = w.replace("\n", "")
    # os.chdir(w)    
    # call(['cp', 'partition-0', '../ConnectedComponents/partition-0'])
    # call(['cp', 'partition-1', '../ConnectedComponents/partition-1'])
    # call(['cp', 'partition-2', '../ConnectedComponents/partition-2'])
    # call(['cp', 'partition-3', '../ConnectedComponents/partition-3'])
    # call(['cp', 'partition-4', '../ConnectedComponents/partition-4'])
    # call(['cp', 'partition-5', '../ConnectedComponents/partition-5'])
    # call(['cp', 'partition-6', '../ConnectedComponents/partition-6'])
    # call(['cp', 'partition-7', '../ConnectedComponents/partition-7'])

    os.chdir('ConnectedComponents')
    a = open('partition-0', 'r')
    b = open('partition-1', 'r')
    c = open('partition-2', 'r')
    d = open('partition-3', 'r')
    e = open('partition-4', 'r')
    f = open('partition-5', 'r')
    g = open('partition-6', 'r')
    h = open('partition-7', 'r')
    i = open('dat.csv', 'a')

    i.write('date,window,userid,CCL\n')
    for line in a:
        i.write(line)
    for line in b:
        i.write(line)
    for line in c:
        i.write(line)
    for line in d:
        i.write(line)
    for line in e:
        i.write(line)
    for line in f:
        i.write(line)
    for line in g:
        i.write(line)
    for line in h:
        i.write(line)

    a.close()
    b.close()
    c.close()
    d.close()
    e.close()
    f.close()
    g.close()
    h.close()
    i.close()
