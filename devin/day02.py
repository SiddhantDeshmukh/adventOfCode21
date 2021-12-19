"""At first, I was trying to split my big list into two parts, 
but couldn't get that to work today due to addled brain.
Thus, I just went for indexes of the string and got it to work that way!"""

def find_coordinates_part_1(directions):
    depth = 0
    horizontal = 0
    for item in directions:
        if item[0] == 'f':
            horizontal += int(item[-1])
        elif item[0] == 'd':
            depth += int(int(item[-1]))
        else:
            depth -= int(int(item[-1]))
    print(horizontal,depth)
    print(horizontal*depth)
    return(horizontal,depth)

#find_coordinates_part_1(raw_input)

"""Part two adds a third variable to account for, aim, 
which is the only way to modify depth. 
I changed my if statements accordingly and got the answer in one shot"""

def find_coordinates_part_2(directions):
    depth = 0
    horizontal = 0
    aim = 0
    for item in directions:
        if item[0] == 'f':
            horizontal += int(item[-1])
            depth += (aim * int(item[-1]))
        elif item[0] == 'd':
            aim += int(int(item[-1]))
        else:
            aim -= int(int(item[-1]))
    print(horizontal,depth)
    print(horizontal*depth)
    return(horizontal,depth)

find_coordinates_part_2(raw_input)

