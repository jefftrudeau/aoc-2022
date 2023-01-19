PACKET_MARKER_LEN = 4
MESSAGE_MARKER_LEN = 14


SEARCH_MODE = 1


if SEARCH_MODE == 0:
    BUF_LEN = PACKET_MARKER_LEN
    MARKER_TYPE = 'start-of-packet'
else:
    BUF_LEN = MESSAGE_MARKER_LEN
    MARKER_TYPE = 'start-of-message'


with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()


buf = []


def add_char(char):
    buf.append(char)
    if len(buf) > BUF_LEN:
        buf.pop(0)


def is_unique():
    for i, x in enumerate(buf):
        for y in buf[(i + 1):]:
            if x == y:
                return False
    return True


marker = -1


for i, c in enumerate(list(input_txt)):
    add_char(c)
    if len(buf) == BUF_LEN:
        if is_unique():
            marker = i
            break


print(f'How many characters need to be processed before the first {MARKER_TYPE} marker is detected?')
print(f'{marker + 1} characters')
