# x is an int 0 <= x <= 31
def cost(x):
    return x ** 3 - 60 * x ** 2 + 90 * x


# Calculates the decimal value of a binary string
def bin2dec(s):
    return int(s, 2)


# Returns the binary string representation of the integer x
# String is padded with 0s to be of length string_length
def dec2bin(x, string_length):
    binary_string = str(bin(x))[2:]
    while len(binary_string) < string_length:
        binary_string = '0' + binary_string
    return binary_string


# Returns the neighborhood for the binary string s
# Neighborhood is a list of 3-tuples where first element is index
# second element is the actual binary string
# third element is the cost
def neighborhood(s):
    neighbors = []
    for index, bit in enumerate(s):
        if bit == '1':
            flipped_bit = '0'
        else:
            flipped_bit = '1'
        new_string = s[0:index] + flipped_bit + s[index + 1:]
        c = cost(bin2dec(new_string))
        neighbors.append((index, new_string, c))
    return neighbors


# Returns the index of the best neighbor in the neighbors list
def best_neighbor_index(neighbors):
    best_index = -1
    best_cost = float('-inf')
    for index, (flipped_bit, string, cost) in enumerate(neighbors):
        if cost > best_cost:
            best_index = index
    return best_index


# Subtracts 1 iteration from every entry in the tabu map
def update_tabu_map(tabu_map):
    to_remove = []
    for bit in tabu_map:
        tabu_map[bit] -= 1
        if tabu_map[bit] == 0:
            to_remove.append(bit)
    for bit in to_remove:
        tabu_map.pop(bit)


def tabu_search(x=20, m=2, max_cost_evals=200):
    tabu_map = {}
    aspiration_level = cost(x)
    s_current = dec2bin(x, 5)
    solution = s_current
    cost_evals = 0
    while cost_evals < max_cost_evals:
        neighbors = neighborhood(s_current)
        # Cost is evaluated for every neighbor, so increment here
        cost_evals += len(neighbors)
        best_solution_index = best_neighbor_index(neighbors)
        flipped_bit = neighbors[best_solution_index][0]
        best_solution_cost = neighbors[best_solution_index][2]
        if (flipped_bit not in tabu_map
           or best_solution_cost > aspiration_level):
            s_current = neighbors[best_solution_index][1]
            update_tabu_map(tabu_map)
            tabu_map[flipped_bit] = m
            if best_solution_cost > aspiration_level:
                aspiration_level = best_solution_cost
                solution = s_current
        else:
            searching_for_non_tabu_solution = True
            while searching_for_non_tabu_solution:
                neighbors.pop(best_solution_index)
                best_solution_index = best_neighbor_index(neighbors)
                flipped_bit = neighbors[best_solution_index][0]
                if flipped_bit not in tabu_map:
                    searching_for_non_tabu_solution = False
                    s_current = neighbors[best_solution_index][1]
                    update_tabu_map(tabu_map)
                    tabu_map[flipped_bit] = m
    return bin2dec(solution)

print('Best solution from one trial: x = ' + str(tabu_search()))

# Sanity check for actual best solution
optimal_solution = -1
optimal_cost = float('-inf')
for x in range(32):
    print('x = ' + str(x) + ', ' + str(cost(x)))
    if cost(x) > optimal_cost:
        optimal_cost = cost(x)
        optimal_solution = x
print('Optimal solution is: x = ' + str(optimal_solution))
