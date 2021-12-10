import numpy as np

file  = open('10.txt', 'r')
lines = file.readlines()
grid  = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)
lf    = ['(','[','{','<']
rg    = [')',']','}','>']
sc    = [3,57,1197,25137]
err   = 0

for i in range(len(lines)):
    exp   = []
    call  = lines[i].rstrip()

    ind = lf.index(call[0])
    exp.append(rg[ind])
    for count, value in enumerate(call, start=1):
        if value in lf:
            ind = lf.index(value)
            exp.append(rg[ind])
        else:
            if value != exp[-1]:
                ind = rg.index(value)
                err = err + sc[ind]
                break
            else:
                exp.pop(-1)
print(err)

scs = []
for i in range(len(lines)):
    fail  = 0
    exp   = []
    call  = lines[i].rstrip()

    for count, value in enumerate(call):
        if value in lf:
            ind = lf.index(value)
            exp.append(rg[ind])
        else:
            if value != exp[-1]:
                fail = 1
                break
            else:
                exp.pop(-1)
    if fail == 0:
        num = 0
        exp = exp[::-1]
        for count, value in enumerate(exp):
            ind = rg.index(value)
            num = 5*num + ind + 1
        scs.append(num)

scs = np.sort(scs)
print(scs[len(scs)/2])
