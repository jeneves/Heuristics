

# s is a  a matrix with m rows (one for each cell) and n columns
# (one for each channel) concatenated together. Each value in the
# matrix should be a binary 0 or 1.
# interference_matrix is an (m x m) matrix of interference values
#
# for this particular project, m = 7, n = 50.
def cost(s, interference_matrix=[[2, 1, 0, 0, 0, 0, 0],
                                 [1, 2, 1, 1, 1, 0, 0],
                                 [0, 1, 2, 0, 1, 0, 0],
                                 [0, 1, 0, 2, 1, 1, 0],
                                 [0, 1, 1, 1, 2, 1, 1],
                                 [0, 0, 0, 1, 1, 2, 1],
                                 [0, 0, 0, 0, 1, 1, 2]]):

    num_cells = len(interference_matrix)
    num_channels = len(s[0])

    total_interference = 0
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
                                total_interference += 1

    return total_interference


def get_value(s, cell, channel):
    return s[cell][channel]
