with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()


contained = 0

for input_str in input_txt.split('\n'):
    if input_str:
        pair = input_str.split(',')
        a = range(*map(int, pair[0].split('-')))
        b = range(*map(int, pair[1].split('-')))
        if (a.start <= b.start and b.stop <= a.stop) or (a.start >= b.start and b.stop >= a.stop):
            contained += 1

print('In how many assignment pairs does one range fully contain the other?')
print(contained)


overlapped = 0

for input_str in input_txt.split('\n'):
    if input_str:
        pair = input_str.split(',')
        a = range(*map(int, pair[0].split('-')))
        b = range(*map(int, pair[1].split('-')))
        if (a.start <= b.start <= a.stop) or (a.start <= b.stop <= a.stop) or (b.start <= a.start <= b.stop) or (b.start <= a.stop <= b.stop):
            overlapped += 1

print('In how many assignment pairs do the ranges overlap?')
print(overlapped)
