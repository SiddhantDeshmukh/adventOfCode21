import numpy as np

file  = open('04.txt', 'r')
lines = file.readlines()
call  = lines[0].rstrip().split(',')

count = 0
found = 0
last  = 0
tot   = 0
tab   = 0
d = {}
for i in range(2,len(lines)):
    if (i - 2)%6 == 0:
        d[str(count)]      = np.ndarray(shape=(5,5), dtype=int)
        d[str(count)+'_o'] = np.ones((5,5))
        count = count + 1
    if (i - 1)%6 != 0:
        nums = str(lines[i].rstrip()).split()
        for j in range(len(nums)):
            d[str(count-1)][(i - 2)%6][j]      = nums[j]

for i in range(len(call)):
    for j in range(count):
        if int(call[i]) in d[str(j)]:
            aaa = np.where(d[str(j)] == int(call[i]))
            d[str(j)+'_o'][aaa[0],aaa[1]] = 0
            if np.sum(d[str(j)+'_o'][aaa[0],:]) == 0 or np.sum(d[str(j)+'_o'][:,aaa[1]]) == 0:
                last = call[i]
                tab = j
                found = 1
                break
    if found == 1:
        break

for j in range(len(d[str(tab)+'_o'])):
    for k in range(len(d[str(tab)+'_o'][j,:])):
        tot = tot + d[str(tab)+'_o'][j,k]*d[str(tab)][j,k]

print(int(tot)*int(last))

for j in range(count):
    d[str(j)+'_o'] = np.ones((5,5))

tot  = 0
nwin = count
for i in range(len(call)):
    for j in range(count):
        try:
            if int(call[i]) in d[str(j)]:
                aaa = np.where(d[str(j)] == int(call[i]))
                d[str(j)+'_o'][aaa[0],aaa[1]] = 0
                if np.sum(d[str(j)+'_o'][aaa[0],:]) == 0 or np.sum(d[str(j)+'_o'][:,aaa[1]]) == 0:
                    last  = int(call[i])
                    tab   = d[str(j)]
                    tab_o = d[str(j)+'_o']
                    nwin  = nwin - 1
                    d.pop(str(j))
                    d.pop(str(j)+'_o')
                if nwin == 1:
                    found == 2
        except:
            None
    if found == 2:
        break

for j in range(len(tab)):
    for k in range(len(tab[j,:])):
        tot = tot + tab[j,k]*tab_o[j,k]

print(int(tot)*int(last))
