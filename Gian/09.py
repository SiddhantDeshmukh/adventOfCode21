import numpy as np

file  = open('09.txt', 'r')
lines = file.readlines()
grid = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = call[j]
count = 0
low = []
x = []
y = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        check = 0
        if j > 0:
            left = grid[i,j-1]
            if grid[i,j] >= left:
                check = 1
        if j < len(grid[i]) - 1:
            right = grid[i,j+1]
            if grid[i,j] >= right:
                check = 1
        if i > 0:
            up = grid[i-1,j]
            if grid[i,j] >= up:
                check = 1
        if i < len(grid) - 1:
            down = grid[i+1,j]
            if grid[i,j] >= down:
                check = 1
        if check == 0:
            low.append(grid[i,j])
            x.append(i)
            y.append(j)
            count = count + 1 + grid[i,j]
print(count)

grid = np.ones((len(lines) + 2,len(lines[0].rstrip()) + 2))*9

sizes = []
for i in range(1,len(lines) + 1):
    call  = lines[i-1].rstrip()
    for j in range(1,len(call) + 1):
        grid[i,j] = call[j-1]

sizes  = []
for i in range(len(low)):
    gridtest = np.zeros((len(lines) + 2,len(lines[0].rstrip()) + 2))
    zoneso = []
    zonesn = []
    x9 = x[i] + 1
    y9 = y[i] + 1
    gridtest[x9,y9] = 1
    zoneso.append([x9,y9])
    zonesn.append([x9,y9])
    while len(zoneso) > 0:
        for j in zoneso:
            scrh1 = grid[j[0],j[1]+1]
            scrh2 = gridtest[j[0],j[1]+1]
            if scrh1 < 9 and scrh2 < 1:
                zonesn.append([j[0],j[1]+1])
                gridtest[j[0],j[1]+1] = 1
            scrh1 = grid[j[0],j[1]-1]
            scrh2 = gridtest[j[0],j[1]-1]
            if scrh1 < 9 and scrh2 < 1:
                zonesn.append([j[0],j[1]-1])
                gridtest[j[0],j[1]-1] = 1
            scrh1 = grid[j[0]+1,j[1]]
            scrh2 = gridtest[j[0]+1,j[1]]
            if scrh1 < 9 and scrh2 < 1:
                zonesn.append([j[0]+1,j[1]])
                gridtest[j[0]+1,j[1]] = 1
            scrh1 = grid[j[0]-1,j[1]]
            scrh2 = gridtest[j[0]-1,j[1]]
            if scrh1 < 9 and scrh2 < 1:
                zonesn.append([j[0]-1,j[1]])
                gridtest[j[0]-1,j[1]] = 1

        zonesn.remove(j)
        zoneso = zonesn
    sizes.append(np.sum(gridtest))

size = np.sort(sizes)
print(int(size[-1]*size[-2]*size[-3]))
