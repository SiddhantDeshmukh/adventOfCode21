.split("\n")
gamma = []
epsilon = []
zero = []
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []
ninth = []
tenth = []
eleventh = []
#This is going to be very messy code. 
def separate_string(item):
    for i in item:
        if i[0] == "1":
            zero.append(i[0])
    for i in item:
        if i[1] == "1":
            first.append(i[1])
    for i in item:
        if i[2] == "1":
            second.append(i[2])
    for i in item:
        if i[3] == "1":
            third.append(i[3])
    for i in item:
        if i[4] == "1":
            fourth.append(i[4])
    for i in item:
        if i[5] == "1":
            fifth.append(i[5])
    for i in item:
        if i[6] == "1":
            sixth.append(i[6])
    for i in item:
        if i[7] == "1":
            seventh.append(i[7])
    for i in item:
        if i[8] == "1":
            eighth.append(i[8])
    for i in item:
        if i[9] == "1":
            ninth.append(i[9])
    for i in item:
        if i[10] == "1":
            tenth.append(i[10])
    for i in item:
        if i[11] == "1":
            eleventh.append(i[11])

def find_gamma_epsilon(item):
#I can probably make this call the previous function if I use for i in...
    if len(item) < 500:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

def convert_to_number(item):
#Once again, I can probably make this call the previous functions
    string = [str(i) for i in item]
    combined = "".join(string)
    number = int(combined, 2)
    print(number)
    return number
    
        
"""separate_string(raw_input)
find_gamma_epsilon(zero)
find_gamma_epsilon(first)
find_gamma_epsilon(second)
find_gamma_epsilon(third)
find_gamma_epsilon(fourth)
find_gamma_epsilon(fifth)
find_gamma_epsilon(sixth)
find_gamma_epsilon(seventh)
find_gamma_epsilon(eighth)
find_gamma_epsilon(ninth)
find_gamma_epsilon(tenth)
find_gamma_epsilon(eleventh)
convert_to_number(gamma)
convert_to_number(epsilon)"""
"""I was given 654 and 3441, multiplied = 2250414, it's correct.
I can clean this up later so it actually stores the values then multiplies
them for me, instead of me doing so, but I'm tired and not caffienated."""

nice_input = dict(zip(range(len(raw_input)), raw_input))
def find_ox(dct):
    count = 0
    for i in range(len(dct)):
        #print(dct[i][0]) #This was to test to see if I could get just the first index to print
        if dct[i][0] == 1:
            count += 1 #for some reason my count won't increase here. I can get it to print every value, and every [0], but it still won't add to count. 
        else:
            None
    print(count)
    return(count)
    """for i in range(len(dct)):
        if count >= 500 and dct[i][0] == 0:
            dct.remove(dct[i])
        elif count < 500 and dct[i][0] ==1:
            dct.remove(dct[i])
    print(dct)
    return(dct)
    This is all theoretical code that I'll use once I get the count to work"""
            
find_ox(nice_input)
oxygen = []
cotwo = []
def find_ox_cotwo(item):
#This is an adaptation of my find_gamma_epsilon from above. I don't think I'll need it. Originally I had the wrong understanding of what I was doing.
    if len(item) >= 500:
        oxygen.append(1)
        cotwo.append(0)
    else:
        oxygen.append(0)
        cotwo.append(1)
