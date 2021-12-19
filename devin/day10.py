with open('input10.txt', 'r') as f:
    data = f.readlines()

open_char = list('([{<')
closed_char = list(')]}>')

illegal_character_count = {")": 0, "]": 0, "}": 0, ">": 0}
point_value = [1, 2, 3, 4]

valid = []
total_points = []

for line in data:
    valid.clear()
    flag = True
    for char in line:
        if char in open_char:
            valid.append(char)
        elif char in closed_char:
            if valid.pop() != open_char[closed_char.index(char)]:
                illegal_character_count[char] += 1
                flag = False
                break
    if flag:
        total = 0
        while len(valid) != 0:
            t = valid.pop()
            c = closed_char[open_char.index(t)]
            total *= 5
            total += point_value[closed_char.index(c)]
        total_points.append(total)

syntax_error = [3, 57, 1197, 25137]
print(f'Syntax error score: {sum([a * b  for a,b in zip(syntax_error, list(illegal_character_count.values()))])}')

total_points.sort()
middle = int((len(total_points) - 1) / 2)
print(f'Middle score is: {total_points[middle]}')
