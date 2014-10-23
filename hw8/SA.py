import math
import random
from cost import cost

# peturb s according to neighbor definition
def neighbor(s):
    update_index = random.randint(0, len(s) - 1)
    neighbor_s = [i for i in s]
    change = random.gauss(0.0, math.sqrt(5.0))
    while (neighbor_s[update_index] + change > 10.0
            or neighbor_s[update_index] + change < 0.0):
        change = random.gauss(0.0, math.sqrt(5.0))
    neighbor_s[update_index] += change
    return neighbor_s


# main algorithm for SA
def simulated_annealing(s_initial, t_initial, alpha, beta, m_initial, maxtime):
    t = t_initial
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
            metropolis(current_s, current_cost, best_s, best_cost, t, m)
        time += m
        t *= alpha
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
        if d_cost > 0:
            current_s = new_s
            current_cost = new_cost
            if new_cost > best_cost:
                best_s = new_s
                best_cost = new_cost
        elif random.random() < math.e ** (d_cost / t):
            current_s = new_s
            current_cost = new_cost
        m -= 1
    return current_s, current_cost, best_s, best_cost
