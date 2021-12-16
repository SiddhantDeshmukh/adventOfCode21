import numpy as np

file  = open('11.txt', 'r')
lines = file.readlines()
grid = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = call[j]

count = 0
for i in range(100):
    grid = grid + 1
    flasho = []
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            if grid[j,k] > 9:
                flasho.append([j,k])
    flashn = flasho.copy()
    ccc = 0
    while len(flasho) > 0:

        count = count + len(flasho)
        for j in range(len(flasho)):
            grid[flasho[j][0],flasho[j][1]] = 0
            flashn.remove(flasho[j])
            for k in range(flasho[j][0]-1,flasho[j][0] + 2):
                for l in range(flasho[j][1]-1,flasho[j][1] + 2):
                    if 0 <= k < len(grid) and 0 <= l < len(grid):
                        if 0 < grid[k][l] < 10:
                            grid[k][l] = grid[k][l] + 1
        for j in range(len(grid)):
            for k in range(len(grid[j])):
                if grid[j,k] > 9:
                    flashn.append([j,k])
        flasho = flashn.copy()

print(count)

grid = np.ndarray(shape=(len(lines),len(lines[0].rstrip())), dtype=int)

for i in range(len(lines)):
    call  = lines[i].rstrip()
    for j in range(len(call)):
        grid[i,j] = call[j]

step = 0
fff  = 0
while fff == 0:
    step = step + 1
    grid = grid + 1
    flasho = []
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            if grid[j,k] > 9:
                flasho.append([j,k])
    flashn = flasho.copy()
    ccc = 0
    while len(flasho) > 0:
        count = count + len(flasho)
        for j in range(len(flasho)):
            grid[flasho[j][0],flasho[j][1]] = 0
            flashn.remove(flasho[j])
            for k in range(flasho[j][0]-1,flasho[j][0] + 2):
                for l in range(flasho[j][1]-1,flasho[j][1] + 2):
                    if 0 <= k < len(grid) and 0 <= l < len(grid):
                        if 0 < grid[k][l] < 10:
                            grid[k][l] = grid[k][l] + 1
        for j in range(len(grid)):
            for k in range(len(grid[j])):
                if grid[j,k] > 9:
                    flashn.append([j,k])
        flasho = flashn.copy()
    if np.sum(grid) < 1:
        fff = 1

print(step)
