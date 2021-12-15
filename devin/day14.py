from collections import Counter

"""with open('input14.txt', 'r') as f:
    data = f.read()
    data = data.strip().split("\n")
    del data[1]
    polymer_template = data[0]
    insertion_rules = data[1:]"""
polymer_template = "NNCB"
insertion_rules = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")

def insert_polymer(template, rules, steps):
    for step_number in range(steps):
        for rule in rules:
            if rule[0:2] in template:
                index = template.find(rule[0:2])
                print(index)
                template = template[:index] + rule[6] + template[index:]
                print(template)
    #print(template)
    return template

#print(polymer_template)

#insert_polymer(polymer_template, insertion_rules, 10)

def find_most_least(template, rules, steps):
    polymer = insert_polymer(template, rules, steps)
    c = Counter(polymer)
    print(c.most_common(1))
    print(c.most_common()[:-1-1:-1])
    

find_most_least(polymer_template, insertion_rules, 10)
    

"""First try, got 66, which is clearly wrong. Can't get the example to work either, 
so I'm probably having an issue with my inserting of the letter"""
