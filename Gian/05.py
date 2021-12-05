import numpy as np

file  = open('05.txt', 'r')
lines = file.readlines()
land = np.zeros((1000,1000))
for line in lines:
    num = line.rstrip().split(' -> ')
    inv = num[0].split(',')
    fnv = num[1].split(',')
    if int(inv[0]) == int(fnv[0]):
        str = min(int(inv[1]),int(fnv[1]))
        fns = max(int(inv[1]),int(fnv[1]))
        for i in range(str,fns+1):
            land[i,int(inv[0])] = land[i,int(inv[0])] + 1
    elif int(inv[1]) == int(fnv[1]):
        str = min(int(inv[0]),int(fnv[0]))
        fns = max(int(inv[0]),int(fnv[0]))
        for i in range(str,fns+1):
            land[int(inv[1]),i] = land[int(inv[1]),i] + 1

count = 0
for i in land:
    for j in i:
        if j > 1:
            count = count + 1

print(count)

land = np.zeros((1000,1000))
for line in lines:
    num = line.rstrip().split(' -> ')
    inv = num[0].split(',')
    fnv = num[1].split(',')
    if int(inv[0]) == int(fnv[0]):
        str = min(int(inv[1]),int(fnv[1]))
        fns = max(int(inv[1]),int(fnv[1]))
        for i in range(str,fns+1):
            land[i,int(inv[0])] = land[i,int(inv[0])] + 1
    elif int(inv[1]) == int(fnv[1]):
        str = min(int(inv[0]),int(fnv[0]))
        fns = max(int(inv[0]),int(fnv[0]))
        for i in range(str,fns+1):
            land[int(inv[1]),i] = land[int(inv[1]),i] + 1
    else:
        incx = (int(fnv[0]) - int(inv[0]))/np.abs(int(fnv[0])- int(inv[0]))
        incy = (int(fnv[1]) - int(inv[1]))/np.abs(int(fnv[1])- int(inv[1]))
        delt = np.abs(int(fnv[0])- int(inv[0]))
        newx = int(inv[0])
        newy = int(inv[1])
        for i in range(delt + 1):
            land[int(newy),int(newx)] = land[int(newy),int(newx)] + 1
            newx = newx + incx
            newy = newy + incy

count = 0
for i in land:
    for j in i:
        if j > 1:
            count = count + 1

print(count)
