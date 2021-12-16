import numpy as np

file  = open('15_ex.txt', 'r')
lines = file.readlines()
'''
grid = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = call[j]

time = grid.copy()*np.Infinity
vis  = grid.copy()*0
time[0][0] = 0
found = 0
coord = [0,0]
iter = 0
while found == 0:
    iter = iter + 1
    vis[coord[0],coord[1]] = 1
    va = time[coord[0],coord[1]]
    cx = coord[0]
    cy = coord[1]
    up = coord[0] - 1
    dn = coord[0] + 1
    sx = coord[1] - 1
    dx = coord[1] + 1

    if 0 < up < len(grid) and vis[up,cy] == 0:
        time[up,cy] = min(time[up,cy],va + grid[up,cy])
    if 0 < dn < len(grid) and vis[dn,cy] == 0:
        time[dn,cy] = min(time[dn,cy],va + grid[dn,cy])
    if 0 < dx < len(grid) and vis[cx,dx] == 0:
        time[cx,dx] = min(time[cx,dx],va + grid[cx,dx])
    if 0 < sx < len(grid) and vis[cx,sx] == 0:
        time[cx,sx] = min(time[cx,sx],va + grid[cx,sx])
    newval = np.Infinity
    for i in range(len(grid)):
        for j in range(len(grid)):
            if time[i][j] < newval and vis[i,j] == 0:
                coord[0] = i
                coord[1] = j
                newval = time[i][j]
    if coord[0] == len(grid) - 1 and coord[1] == len(grid) - 1:
        found = 1

print(int(time[len(grid)-1][len(grid)-1]))


grid = np.ndarray(shape=(len(lines)*5,len(lines[0].rstrip())*5), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = (call[j])
        for k in range(0,5):
            for l in range(0,5):
                val = int(call[j]) + k + l
                if val > 9:
                    val = val - 9
                grid[i + k*len(call),j + l*len(call)] = val

print('Grid created')

time = grid.copy()*np.Infinity
time[0][0] = 0
coord = [0,0]

for i in range(1,2*len(grid)-1):
    if i < len(grid):
        xs = 0
        ys = i
    else:
        xs = i%len(grid) + 1
        ys = len(grid) - 1
    for j in range(abs(xs-ys) + 1):
        if xs > 0:
            up = time[xs-1][ys]
        else:
            up = np.Infinity
        if ys > 0:
            sx = time[xs][ys-1]
        else:
            sx = np.Infinity
        time[xs,ys] = min(up,sx) + grid[xs][ys]
        xs = xs + 1
        ys = ys - 1

print(grid, time)
#print(int(time[len(grid)-1][len(grid)-1]))
'''

grid = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = call[j]

l = [[],[],[],[]]
for i in range(2,len(grid)):
    for j in range(2,len(grid)):
        l[0].append(i)
        l[1].append(j)
        l[2].append(grid[i,j])
        l[3].append(grid[i,j])

print(l[0])
print(l[1])
print(l[2])
ind = l[2].index(min(l[2]))
print(ind)
print(l[0][ind],l[1][ind])
