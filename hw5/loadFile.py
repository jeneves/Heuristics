
def load_file(file_name):
    m = []
    with open(file_name, 'r') as input:
        for line in input.readlines():
            if len(line) > 10:
                t = []
                t.append(get_digit_from_string(line[1:16]))
                t.append(get_digit_from_string(line[17:32]))
                t.append(get_digit_from_string(line[33:48]))
                m.append(t)

    return m


def get_digit_from_string(s):

    d = 1
    if s[0] == '-':
        d = -1

    if s[14] == '1':
        d = d * (int(s[1]) * 10 + int(s[3]))
    else:
        d = d * (int(s[1]))

    return d
