import math
import random

# s = [s1, s2], 0 <= s1, s2 <= 127
def cost(s):
    return (
        10**9
        - (625 - (s[0] - 25)**2)
        * (1600 - (s[1] - 10)**2)
        * math.sin(s[0] * math.pi / 10)
        * math.sin(s[1] * math.pi / 10)
    )

# peturb s according to neighbor definition
def neighbor(s):
    if random.random() > 0.5:
        new_max = min(s[0] + 25, 127)
        new_min = max(s[0] - 25, 0)
        diff = random.randint(new_min, new_max - 1) - s[0]
        return [s[0] + diff + 1, s[1]] if diff >=0 else [s[0] + diff, s[1]]
    else:
        new_max = min(s[1] + 25, 127)
        new_min = max(s[1] - 25, 0)
        diff = random.randint(new_min, new_max - 1) - s[1]
        return [s[0], s[1] + diff + 1] if diff >=0 else [s[0], s[1] + diff]

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
    return solution

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
        elif random.random() < math.e**(-d_cost / t):
            current_s = new_s
            current_cost = new_cost
        m -= 1
    return current_s, current_cost, best_s, best_cost


# main script
with open("SA.csv", 'w') as results:
    for row in simulated_annealing([50.0, 100.0], 200.0, 0.9, 1.0, 30.0, 6000):
        for field in row:
            results.write("%.1f," % field)
        results.write("\n")
