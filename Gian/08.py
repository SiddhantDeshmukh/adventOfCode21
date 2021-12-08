import numpy as np

f = open('08.txt').read().splitlines()
count = 0
mylist = [2,3,4,7]
for line in f:
    words = line.split(' ')
    for j in range(11, 15):
        if len(words[j]) in mylist:
            count = count + 1
print(count)

tot = 0
easy  = [2,3,4,7]
nume  = [1,7,4,8]
right = [0,0,0,0,0,0,0,0,0,0]
for line in f:

    num6 = []
    num5 = []
    words = line.split(' ')
    for i in range(0,10):
        att = len(words[i])
        if att in easy:
            right[nume[easy.index(len(words[i]))]] = sorted(words[i])
        elif att == 6:
            num6.append(words[i])
        elif att == 5:
            num5.append(words[i])
    for i in num6:
        up = list(set(right[8]) - set(right[4]) - set(i))
        cn = list(set(right[8]) - set(right[7]) - set(i))
        if len(up) + len(cn) == 2:
            right[9] = sorted(i)
        if len(up) + len(cn) == 1:
            right[0] = sorted(i)
        if len(up) + len(cn) == 0:
            right[6] = sorted(i)
    for i in num5:
        ul = list(set(right[6]) - set(i))
        dl = list(set(right[9]) - set(i))
        if len(ul) + len(dl) == 2:
            right[5] = sorted(i)
        if len(ul) + len(dl) == 4:
            right[2] = sorted(i)
        if len(ul) + len(dl) == 3:
            right[3] = sorted(i)

    sinnum = 0
    for j in range(11, 15):
        if sorted(words[j]) in right:
            sinnum = sinnum + int(right.index(sorted(words[j])))*10**(14-j)
    right = [0,0,0,0,0,0,0,0,0,0]
    tot = tot + sinnum
print(tot)
