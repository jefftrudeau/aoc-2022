with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()


elf = []
elves = []

for calories in input_txt.split('\n'):
    if calories == '':
        elves.append(elf)
        elf = []
    else:
        elf.append(int(calories))

if len(elf):
    elves.append(elf)
    elf = []

elf_index = None
max_total = 0

for index, elf in enumerate(elves):
    total = sum(elf)
    if total > max_total:
        max_total = total
        elf_index = index

print('Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?')
print(f'The {elf_index}th elf is carrying {max_total} calories')

totals = sorted([sum(elf) for elf in elves], reverse=True)

print('Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?')
print(sum(totals[:3]))
