f = open('01.txt','r').read().split('\n')
f.pop()
count = 0
for i in range(len(f)-1):
    if int(f[i]) < int(f[i+1]):
        count = count + 1
print('N. count = '+str(count))

count = 0
for i in range(len(f)-3):
    if int(f[i]) < int(f[i+3]):
        count = count + 1
print('N. count = '+str(count))
