with open('input7.txt', 'r') as f:
    crab_pos_x = f.read().strip().split(",")

#print(crab_pos_x) trying to see what my list looks like
#print(sorted(int(crab_pos_x))) #This didn't work

int_crab_pos = []
for i in crab_pos_x:
    int_crab_pos.append(int(i))

#print(sorted(int_crab_pos)) checking to see if it sorts correctly

#print(len(crab_pos_x)) debugging trying to see why my median wasn't working correctly
#print(crab_pos_x[500], crab_pos_x[499])
#print(crab_pos_x)
fuel_use = 0
test_list = [16,1,2,0,4,2,7,1,2,14]

def average_x(crabs_list):
    summ = 0
    for i in crabs_list:
        summ = summ + int(i)
        average_x = (summ)/(len(crabs_list))
        rounded_average = int(average_x) + ((int(average_x) - average_x) != 0)
    print(summ, len(crabs_list), rounded_average)
    return rounded_average

def median_x(crabs_list):
    crabs_list = sorted(crabs_list)
    item_1 = crabs_list[len(crabs_list)//2]
    item_2 = crabs_list[(len(crabs_list)//2)-1]
    #print(item_1, item_2)
    median = (int(item_1) + int(item_2))/2
    #print(median)
    return median

"""My original thought was that I could use the average x position,
maybe it's just median?"""
#average_x(crab_pos_x)

def change_in_x(crabs):
    desired_x_pos = median_x(crabs)
    #print(desired_x_pos)
    fuel_use = 0
    for i in crabs:
        if int(i) < desired_x_pos:
            fuel_use += desired_x_pos - int(i)
        elif int(i) > desired_x_pos:
            fuel_use += int(i) - desired_x_pos
        else:
            fuel_use += 0
    print("Total fuel use: ", fuel_use)
    return fuel_use

change_in_x(int_crab_pos)

"""Attempt 1 returned 361145, which was too high"""
"""Attempt 2 using median instead, still too high 348001.
Got the example answer via median though,
so maybe my code needs refined"""
"""Going through my elements, I realized that the
sorted function isn't working on my crab_list. That's my issue"""
"""Attempt 3 success! 347449 was my answer. My list was reading as strings rather than integers, causing the issue."""


def change_in_x_p2(crabs):
    desired_x_pos = (average_x(crabs)-1)
    fuel_use = 0
    for i in crabs:
        if int(i) < desired_x_pos:
            j = int(desired_x_pos) - int(i)
            fuel_use += int((j*(j+1))/2)
        elif int(i) > desired_x_pos:
            j = int(i) - int(desired_x_pos)
            fuel_use += int((j*(j+1))/2)
        else:
            fuel_use += 0
    print("Total fuel use: ", fuel_use)
    return fuel_use

change_in_x_p2(int_crab_pos)

"""Attempt 1 returned 97678470 which was too low.
Time to fix my formula?"""
"""Attempt 2 worked for the example. 98039615 was too high though, so failed"""
"""Attempt 3, instead of rounding average up,
I rounded down and got the right answer: 98039527"""
