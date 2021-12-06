import numpy as np

f = open('06.txt','r').read().rstrip().split(',')
f = list(map(int, f))
for i in range(80):
    for j in range(len(f)):
        num = int(f[j])
        if num != 0:
            f[j] = num - 1
        else:
            f[j] = 6
            f.append(8)
print(len(f))

f = open('06.txt','r').read().rstrip().split(',')
f = list(map(int, f))
arr = np.zeros(9)
for i in f:
    arr[i] = arr[i] + 1

for i in range(256):
    arr_n = np.copy(arr)
    for i in range(len(arr)):
        arr_n[i] = arr[(i+1)%len(arr)]
    arr_n[6] = arr_n[6] + arr_n[8]
    arr = arr_n

print(int(np.sum(arr)))
