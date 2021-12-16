import numpy as np

f = open('16_ex.txt','r').read().rstrip()
print(f)

def find_tot(code, ver):
    ver = ver + find_ver(code[0:3])
    typ = isoperator(code[3:6])
    if typ == True:
        length, cut = find_length(code[6:])
        subcode = code[cut:cut + length]
        lims = read_sub(subcode)
    return ver

def find_ver(code):
    return 4*code[0] + 2*code[1] + code[2]

def isoperator(code):
    if 4*code[0] + 2*code[1] + code[2] != 4:
        return True
    else:
        return False

def find_length(code):
    length = 0
    if code[0] == 0:
        cut = 22
        for i in range(15):
            length = length + code[1+i]*2**(14-i)
    return length, cut

def read_sub(subcode):
    count = 0
    while count < len(subcode):
        typ = isoperator
    print(subcode)

exa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
bin = ['0000','0001','0010','0011','0100','0101','0110','0111',
       '1000','1001','1010','1011','1100','1101','1110','1111']

totver = 0
binstr = ''
for i in range(len(f)):
    index = exa.index(f[i])
    binstr = binstr + bin[index]
code = list(map(int, binstr))
ver = 0
ver = find_tot(code,ver)
print(ver)
