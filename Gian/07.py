import numpy as np

f = open('07.txt','r').read().rstrip().split(',')
f = np.array(list(map(int, f)))

mm = min(f)
mx = max(f)

for i in range(mm, mx+1):
    tot = np.sum(np.abs(f - i))
    try:
        if tot < low1:
            low1 = tot
            ind1 = i
    except:
        low1 = tot
        ind1 = i

print(ind1,low1)

for i in range(mm, mx+1):
    print(i)
    tot = 0
    for j in f:
        tot = tot + np.sum(range(np.abs(j - i) + 1))
    try:
        if tot < low2:
            low2 = tot
            ind2 = i
    except:
        low2 = tot
        ind2 = i

print(ind2,low2)
