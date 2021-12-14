import numpy as np

file  = open('14.txt', 'r')
lines = file.readlines()
call  = lines[0].rstrip().split()

listo = []
listn = []
start = []
react = []
elnum = []
for i in range(len(call[0])):
    listo.append(call[0][i])
    listn.append(call[0][i])
    if call[0][i] not in elnum:
        elnum.append(call[0][i])

for i in range(2,len(lines)):
    call0 = lines[i].rstrip().split()
    start.append(call0[0])
    react.append(call0[2])

for i in range(10):
    for j in range(len(listo)-1):
        index = start.index(listo[j]+listo[j+1])
        listn.insert(2*j+1,react[index])
        if react[index] not in elnum:
            elnum.append(react[index])
    listo = listn.copy()

count = np.zeros(len(elnum))

for i in range(len(listo)):
    index = elnum.index(listo[i])
    count[index] = count[index] + 1

sort = np.sort(count)

print(int(sort[-1] - sort[0]))

numro = np.zeros(len(react))
listo = []

for i in range(len(call[0])):
    listo.append(call[0][i])

for j in range(len(listo)-1):
    index = start.index(listo[j]+listo[j+1])
    numro[index] = numro[index] + 1

for i in range(40):
    numrn = np.zeros(len(react))
    for j in range(len(numro)):
        indexl = start.index(start[j][0] + react[j])
        indexr = start.index(react[j] + start[j][1])
        numrn[indexl] = numrn[indexl] + numro[j]
        numrn[indexr] = numrn[indexr] + numro[j]
    numro = np.copy(numrn)

count = np.zeros(len(elnum))
for i in range(len(numrn)):
    index = elnum.index(start[i][0])
    count[index] = count[index] + numrn[i]
index = elnum.index(call[0][-1])
count[index] = count[index] + 1

sort = np.sort(count)

print(int(sort[-1] - sort[0]))
