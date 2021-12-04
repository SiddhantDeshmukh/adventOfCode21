with open("02.txt", "r") as datafile:
    x = datafile.read().split()[0::2]
with open("02.txt", "r") as datafile:
    y = datafile.read().split()[1::2]

hor = 0
dep = 0

for i in range(len(y)):
    if x[i] == 'forward':
        hor = hor + int(y[i])
    if x[i] == 'up':
        dep = dep - int(y[i])
    if x[i] == 'down':
        dep = dep + int(y[i])

print(hor*dep)

hor = 0
dep = 0
aim = 0

for i in range(len(y)):
    if x[i] == 'forward':
        hor = hor + int(y[i])
        dep = dep + aim*int(y[i])
    if x[i] == 'up':
        aim = aim - int(y[i])
    if x[i] == 'down':
        aim = aim + int(y[i])

print(hor*dep)
