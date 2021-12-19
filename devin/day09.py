test_data = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

individual_number_list = []

with open('input9.txt', 'r') as f:
    data = f.read().split("\n")

data.pop()

for i in data:
    x_len = int(len(i))
    print(x_len)
    for char in i:
        individual_number_list.append(char)

count = 0
block_length = int(len(individual_number_list))
#print(individual_number_list, block_length, x_len)
for i in range(block_length):
    for num in individual_number_list[i]:
        if i == 0: 
            if num < individual_number_list[i+1] and num < individual_number_list[i+x_len]:
                #print(num)
                count += int(num) + 1
        elif i == x_len - 1:
            if num < individual_number_list[i-1] and num < individual_number_list[i+int(x_len)]:
                #print(num)
                count += int(num) + 1
        elif i == 100 or i == 200 or i == 300 or i == 500 or i == 600 or i == 700 or i == 800 or i == 900:
            if num < individual_number_list[i+1] and num < individual_number_list[i+int(x_len)] and num < individual_number_list[i-int(x_len)]:
                #print(num)
                count += int(num) + 1
        elif i == 199 or i == 299 or i == 399 or i == 599 or i == 699 or i == 799 or i == 899:
            if num < individual_number_list[i-1] and num < individual_number_list[i+int(x_len)] and num < individual_number_list[i-int(x_len)]:
                #print(num)
                count += int(num) + 1
        elif i == 999:
            if num < individual_number_list[i-1] and num < individual_number_list[i-x_len]:
                count += int(num) + 1
        elif 0 < i < int(x_len):
            if num < individual_number_list[i+1] and num < individual_number_list[i+int(x_len)] and num < individual_number_list[i-1]:
                #print(num)
                count += int(num) + 1
        elif 999> i > 900:
            if num < individual_number_list[i+1] and num < individual_number_list[i-int(x_len)] and num < individual_number_list[i-1]:
                #print(num)
                count += int(num) + 1
        else:
            if num < individual_number_list[i+1] and num < individual_number_list[i+x_len] and num < individual_number_list[i-1] and num < individual_number_list[i-x_len]:
                #print(num)
                count += int(num) + 1
print(count)
#print(x_len, individual_number_list)
#print(individual_number_list, block_length, x_len)
