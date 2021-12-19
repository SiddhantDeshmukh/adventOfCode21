from collections import Counter

with open('input5.txt', 'r') as f:
    vents = [line.replace(' -> ', ',') for line in f.read().split('\n')]
    del vents[500]

def find_intersections(is_diagonal):
    straight, diagonal = [], []
    for i in vents:
        x1, y1, x2, y2 = map(int, i.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            straight += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        elif y1 < y2:
            diagonal += [(x, y1 + dx) for dx, x in enumerate(range(x1, x2 + 1))]
        else:
            diagonal += [(x, y1 - dx) for dx, x in enumerate(range(x1, x2 + 1))]
    position_counts = Counter(straight)
    if is_diagonal:
        position_counts += Counter(diagonal)
    return sum(value > 1 for value in position_counts.values())

print(find_intersections(is_diagonal=False))
print(find_intersections(is_diagonal=True))
