with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()


item_types = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_priority(item_type):
    return item_types.find(item_type) + 1


total_priority = 0

for input_str in input_txt.split('\n'):
    if input_str:
        items = list(input_str)
        count = len(items) // 2
        a, b = sorted(items[:count]), sorted(items[count:])
        for i in a:
            if i in b:
                total_priority += get_priority(i)
                break


print('Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?')
print(f'The sum of the priorities is {total_priority}')


group = []
total_priority = 0

for input_str in input_txt.split('\n'):
    if input_str:
        group.append(list(input_str))
        if len(group) == 3:
            a, b, c = sorted(group[0]), sorted(group[1]), sorted(group[2])
            for i in a:
                if i in b and i in c:
                    total_priority += get_priority(i)
                    break
            group = []


print('Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?')
print(f'The sum of the priorities is {total_priority}')
