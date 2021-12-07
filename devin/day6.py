lanternfish = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]


"""for i in range(80):
    for item in range(len(lanternfish)):
        number = int(lanternfish[item])
        if number != 0:
            lanternfish[item] = number - 1
        else:
            lanternfish[item] = 6
            lanternfish.append(8)

answer = len(lanternfish)
#print("The answer is", answer)"""
#Answer 1 is 386640

"""part 2 is the same but with 256 days"""    
#This was my original thought. It is wrong.


def part2(data: [int], days: int) -> int:
    fish_per_life: [] = [data.count(span) for span in range(9)]
    for day in range(days):
        zeroes = fish_per_life[0]  # count 0 life guys
        fish_per_life[:-1] = fish_per_life[1:]  # decrement fish with 1
        fish_per_life[6] += zeroes  # make another from 0 life fishies
        fish_per_life[8] = zeroes  # new boy
    return sum(fish_per_life)


fishies: [] = [int(i) for i in lanternfish]

print(part2(fishies, 256))
#Answer two is 1733403626279
