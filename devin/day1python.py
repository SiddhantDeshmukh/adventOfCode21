test_depth_list = raw_input_2.split("\n")
depth_list = raw_input.split("\n")
def check_greater_part_1(list_item):
    answer = 1
    for x, y in zip(list_item, list_item[1:]): #This gives item and adjacent
        if y > x:
            answer += 1
    print(answer)
    return(answer)
#check_greater_part_1(depth_list)

#Try 1 gave me 1447, not the answer, but 1448 is, so maybe answer starts at 1?

#Trying part 2
def check_increase_part_2(list_item):
    answer = 0
    for w, x, y, z in zip(list_item, list_item[1:], list_item[2:], list_item[3:]):
        #print(w, x, y, z) # Trying to see where my answer went wrong
        #print(int(w) + int(x) + int(y)) #This is where I realized I need to int them
        #print(x + y + z) #This was just concatenating the numbers
        if (int(x) + int(y) + int(z)) > (int(w) + int(x) + int(y)):
            answer += 1
    print(answer)
    return(answer)
check_increase_part_2(depth_list)

#first try gave me 1446
#Correct answer is 1471

