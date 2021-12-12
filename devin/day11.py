with open('input11.txt', 'r') as f:
    data = "".join(f.readlines())
    data = data.split()
    lst = []
    for i in data:
        print(i)
        for j in i:
            lst.append(int(j))
dic = dict(zip((i for i in range(1,101)), lst))

#print(lst)
#print(dic)

def run_flashes(octopus):
    count = 0
    step = 0
    while step < 100:
        for i in octopus:
            i = i + 1
            if i == 10:
                i = 0
                count = count + 1
        step = step + 1
    print(count)
    return count

run_flashes(lst)
"""I'm trying to build up on basic things to eventually get it to work. 
Granted, it's not working and I'm not sure why, 
but I'm gonna work on it more when I'm less beat to hell by the third vaccine."""
