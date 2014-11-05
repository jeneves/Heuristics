from cost import cost


def find_cost_free_s(s):

    while cost(s) > 0:

        (cell, channel) = find_most_conflicts(s)
        s[cell][channel] = 0

    num_values = sum(sum(row) for row in s)
    return (s, num_values)


def find_most_conflicts(s, interference_matrix=[[2, 1, 0, 0, 0, 0, 0],
                                                [1, 2, 1, 1, 1, 0, 0],
                                                [0, 1, 2, 0, 1, 0, 0],
                                                [0, 1, 0, 2, 1, 1, 0],
                                                [0, 1, 1, 1, 2, 1, 1],
                                                [0, 0, 0, 1, 1, 2, 1],
                                                [0, 0, 0, 0, 1, 1, 2]]):

    num_cells = len(interference_matrix)
    num_channels = len(s[0])

    costs = []
    for i in range(7):
        costs.append([0] * 50)

    for cell in range(0, num_cells):
        for check_cell in range(cell, num_cells):
            distance = interference_matrix[cell][check_cell]

            # Perform checks when values need to be apart
            if distance > 0:
                # Only care about separation, so subtract 1 for check range
                distance -= 1
                for channel in range(0, num_channels):

                    # See if there's something to check
                    value = get_value(s, cell, channel)
                    if value == 1:

                        min_check = 0
                        max_check = min(channel + distance + 1, num_channels)

                        # Check subsequent channels on same cell
                        if cell == check_cell:
                            min_check = channel + 1
                        # Check below right/left channels on different cell
                        else:
                            min_check = max(channel - distance, 0)

                        # Actually perform the check
                        for check_channel in range(min_check, max_check):
                            if get_value(s, check_cell, check_channel) == 1:
                                costs[cell][channel] += 1
                                costs[check_cell][check_channel] += 1

    high_cost = 0
    high_cell = 0
    high_channel = 0

    for cell in range(7):
        for channel in range(50):
            if (costs[cell][channel] > high_cost):
                high_cost = costs[cell][channel]
                high_cell = cell
                high_channel = channel

    return (high_cell, high_channel)


def get_value(s, cell, channel):
    return s[cell][channel]
