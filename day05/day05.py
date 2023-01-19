import pprint
import re


MOVE_EXPR = re.compile('move (\d+) from (\d+) to (\d+)')


with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()



stacks = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


def move1(cnt, src, dst):
    def _move1():
        c = stacks[src].pop()
        stacks[dst].append(c)
    [_move1() for i in range(cnt)]


def move2(cnt, src, dst):
    a, b = stacks[src][:-cnt], stacks[src][-cnt:]
    stacks[src] = a
    stacks[dst].extend(b)


for input_str in input_txt.split('\n'):
    if not input_str or input_str.strip() == '1   2   3   4   5   6   7   8   9':
        break
    for i in range(9):
        val, input_str = input_str[:3].strip(), input_str[4:]
        if val != '':
            stacks[i].insert(0, val[1])


#pprint.pprint(stacks)


for input_str in input_txt.split('\n'):
    matches = re.search(MOVE_EXPR, input_str)
    if matches:
        cnt, src, dst = map(int, matches.groups())
        move2(cnt, src - 1, dst - 1)


#pprint.pprint(stacks)

top_crates = ''.join(map(lambda s: s[len(s) - 1], stacks))


print('After the rearrangement procedure completes, what crate ends up on top of each stack?')
print(top_crates)
