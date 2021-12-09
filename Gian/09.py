import numpy as np

file  = open('09_ex.txt', 'r')
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
gridtest = np.zeros((len(lines) + 2,len(lines[0].rstrip()) + 2))

sizes = []
for i in range(1,len(lines) + 1):
    call  = lines[i-1].rstrip()
    for j in range(1,len(call) + 1):
        grid[i,j] = call[j-1]

for i in range(len(low)):
    size  = 1
    found9 = 1
    x9 = x[i] + 1
    y9 = y[i] + 1
    xmin = x[i] + 1
    xmax = x[i] + 1
    ymin = y[i] + 1
    ymax = y[i] + 1
    gridtest[x9,y9] = 1
    checkl = 1
    checkr = 1
    checku = 1
    checkd = 1
    while checkl == 1:
        ymin = ymin - 1
        if grid[x9,ymin] < 9:
            size = size + 1
            gridtest[x9,ymin] = 1
        else:
            checkl = 0
    while checkr == 1:
        ymax = ymax + 1
        if grid[x9,ymax] < 9:
            size = size + 1
            gridtest[x9,ymax] = 1
        else:
            checkr = 0
    print(size)        


print(grid)
print(gridtest)
