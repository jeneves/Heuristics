import random


# Generates a random allocation with m rows, n columns, and a number of 1
# values per row defined by the traffic vector
def generateRandomAllocation(m=7, n=50, traffic=[32, 26, 14, 32, 18, 20, 24]):
    s = []
    for row in range(m):
        s_row = [0] * n
        ones = random.sample(range(n), traffic[row])
        for one in ones:
            s_row[one] = 1
        s.append(s_row)
    return s
