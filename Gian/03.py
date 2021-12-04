import numpy as np

with open("03.txt", "r") as datafile:
    x = datafile.read().split()
    l = len(x[0])
    gam = 0
    eps = 0
    ox2 = 0
    co2 = 0
    c_0 = np.zeros(l)
    c_1 = np.zeros(l)
    for j in range(l):
        for i in x:
            if int(i[j]) == 0:
                c_0[j] = c_0[j] + 1
            if int(i[j]) == 1:
                c_1[j] = c_1[j] + 1
        if c_1[j]> c_0[j]:
            gam = gam + 2**(l - j - 1)
        else:
            eps = eps + 2**(l - j - 1)
    print(gam*eps)

    c_0 = np.zeros(l)
    c_1 = np.zeros(l)
    sub_0o = x.copy()
    sub_0n = sub_0o.copy()
    for j in range(l):
        for i in sub_0o:
            if int(i[j]) == 0:
                c_0[j] = c_0[j] + 1
            if int(i[j]) == 1:
                c_1[j] = c_1[j] + 1
        if c_1[j] >= c_0[j]:
            ind = 1
        else:
            ind = 0
        for i in sub_0o:
            if i[j] != str(ind):
                sub_0n.remove(i)
        sub_0o = sub_0n.copy()
        if len(sub_0o) < 2:
            break
    for j in range(l):
        ox2 = ox2 + int(sub_0o[0][j])*(2**(l - j - 1))
    c_0 = np.zeros(l)
    c_1 = np.zeros(l)
    sub_0o = x.copy()
    sub_0n = sub_0o.copy()
    for j in range(l):
        for i in sub_0o:
            if int(i[j]) == 0:
                c_0[j] = c_0[j] + 1
            if int(i[j]) == 1:
                c_1[j] = c_1[j] + 1
        if c_1[j] >= c_0[j]:
            ind = 1
        else:
            ind = 0
        for i in sub_0o:
            if i[j] == str(ind):
                sub_0n.remove(i)
        sub_0o = sub_0n.copy()
        if len(sub_0o) < 2:
            break
    for j in range(l):
        co2 = co2 + int(sub_0o[0][j])*(2**(l - j - 1))
    print(ox2*co2)
