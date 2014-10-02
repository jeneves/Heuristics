import random

def costSAT(s, sat_matrix):
    cost = 0

    for clause in sat_matrix:
        correct = False
        for var in clause:
            binVal = s[abs(var) - 1]

            if (var < 0 and binVal == '0') or (var > 0 and binVal == '1'):
                correct = True
        if correct:
            cost += 1

    return cost


# Returns the neighborhood for the binary string s
# Neighborhood is a list of 3-tuples where first element is index
# second element is the actual binary string
# third element is the cost
def neighborhood(s, sat_matrix):
    neighbors = []
    for index, bit in enumerate(s):
        if bit == '1':
            flipped_bit = '0'
        else:
            flipped_bit = '1'
        new_string = s[0:index] + flipped_bit + s[index + 1:]
        c = costSAT(s, sat_matrix)
        neighbors.append((index, new_string, c))
    random.shuffle(neighbors)
    return neighbors


# Returns the index of the best neighbor in the neighbors list
def best_neighbor_index(neighbors):
    best_index = -1
    best_cost = float('-inf')
    for index, (flipped_bit, string, cost) in enumerate(neighbors):
        if cost > best_cost:
            best_cost = cost
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


# Returns (solution, aspiration_level, evaluations_before_aspiration)
# solution is the best solution found
# aspiration_level is the cost of the best solution
# evaluations_before_aspiration is the number of cost evaluations before
# that aspiration_level was found. This should be useful to find the average
# number of evaluations before the satisfying solution is found.
#
# s_initial is the initial binary string
# sat_matrix is the satisfiability matrix loaded from the file
# k is |K|, the tenure length
# iterations is the number of iterations to compute (not cost evals)
def tabu_search(s_initial, sat_matrix, k, iterations):
    tabu_map = {}
    aspiration_level = costSAT(s_initial, sat_matrix)
    s_current = s_initial
    solution = s_current
    cost_evals = 0
    evaluations_before_aspiration = 0

    for i in range(iterations):
        neighbors = neighborhood(s_current, sat_matrix)
        # Cost is evaluated for every neighbor, so increment here
        cost_evals += len(neighbors)
        best_solution_index = best_neighbor_index(neighbors)
        flipped_bit = neighbors[best_solution_index][0]
        best_solution_cost = neighbors[best_solution_index][2]
        if (flipped_bit not in tabu_map
           or best_solution_cost > aspiration_level):
            s_current = neighbors[best_solution_index][1]
            update_tabu_map(tabu_map)
            tabu_map[flipped_bit] = k
            if best_solution_cost > aspiration_level:
                aspiration_level = best_solution_cost
                evaluations_before_aspiration = cost_evals
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
                    tabu_map[flipped_bit] = k

    return (solution, aspiration_level, evaluations_before_aspiration)
