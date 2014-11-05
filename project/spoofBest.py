
from cost import cost


def spoofBest():

    #interference_matrix=[[2, 1, 0, 0, 0, 0, 0],
    #                     [1, 2, 1, 1, 1, 0, 0],
    #                     [0, 1, 2, 0, 1, 0, 0],
    #                     [0, 1, 0, 2, 1, 1, 0],
    #                     [0, 1, 1, 1, 2, 1, 1],
    #                     [0, 0, 0, 1, 1, 2, 1],
    #                     [0, 0, 0, 0, 1, 1, 2]]

    traffic = [32, 26, 14, 32, 18, 20, 24]

    s = []
    for i in range(7):
        s.append([0] * 50)

    # Set first row
    for i in range(25):
        s[0][i * 2] = 1

    for i in range(7):
        s[0][i * 2 + 1] = 1

    assert(sum(s[0]) == traffic[0])

    # Set second row
    for i in range(25):
        s[1][i * 2 + 1] = 1
    s[1][48] = 1

    assert(sum(s[1]) == traffic[1])

    # Set third row
    for i in range(14):
        s[2][i * 2] = 1

    assert(sum(s[2]) == traffic[2])

    # Set fourth row
    for i in range(25):
        s[3][i * 2] = 1

    for i in range(7):
        s[3][i * 2 + 1] = 1

    assert(sum(s[3]) == traffic[3])

    # Set fifth row
    for i in range(18):
        s[4][i * 2 + 15] = 1

    assert(sum(s[4]) == traffic[4])

    # Set sixth row
    for i in range(20):
        s[5][i * 2 + 1] = 1

    assert(sum(s[5]) == traffic[5])

    # Set seventh row
    for i in range(24):
        s[6][i * 2] = 1

    assert (sum(s[6]) == traffic[6])

    return (s, cost(s))


def sperlingAllocation():
    s, cost = spoofBest()
    return s
