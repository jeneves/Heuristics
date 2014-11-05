from copy import deepcopy
import math
import random
from cost import cost


def neighbor(s):
    new_s = deepcopy(s)
    cell_to_change = random.choice(new_s)
    channel_to_invert = random.randint(0, len(cell_to_change) - 1)
    if cell_to_change[channel_to_invert] == 1:
        old_value = 1
        new_value = 0
    else:
        old_value = 0
        new_value = 1
    potential_to_invert = []
    for index, value in enumerate(cell_to_change):
        if value == new_value:
            potential_to_invert.append(index)
    other_to_invert = random.choice(potential_to_invert)
    cell_to_change[channel_to_invert] = new_value
    cell_to_change[other_to_invert] = old_value
    return new_s


# main algorithm for SA
def simulated_annealing(s_initial, t_initial, alpha, beta, m_initial, maxtime):
    temp = t_initial
    current_s = s_initial
    best_s = current_s
    current_cost = cost(current_s)
    best_cost = current_cost
    time = 0
    m = m_initial

    solution = []
    best_s_vals = []

    iter_num = 0
    while time < maxtime:
        iter_num += 1
        current_s, current_cost, best_s, best_cost = \
            metropolis(current_s, current_cost, best_s, best_cost, temp, m)
        time += m
        if temp > 0.1:  # Preventing divide by zero on line 68
            temp *= alpha
        m *= beta
        result = [iter_num, current_cost, best_cost]
        solution.append(result)
        best_s_vals.append(best_s)
    return (solution, best_s)


# help function for updating current_s, current_cost, best_s, best_cost
def metropolis(current_s, current_cost, best_s, best_cost, t, m_current):
    m = m_current
    while m > 0:
        new_s = neighbor(current_s)
        new_cost = cost(new_s)
        d_cost = new_cost - current_cost
        if d_cost < 0:
            current_s = new_s
            current_cost = new_cost
            if new_cost < best_cost:
                best_s = new_s
                best_cost = new_cost
        elif random.random() < math.e ** (-d_cost / t):
            current_s = new_s
            current_cost = new_cost
        m -= 1
    return current_s, current_cost, best_s, best_cost
