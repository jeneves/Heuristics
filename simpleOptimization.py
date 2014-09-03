
import math
import random
import numpy


# Calculates and returns the cost function
def cost(s):
    return (400 - (s - 21) ** 2) * math.sin(s * math.pi / 6)


# Uses a neighborhood of max(scurrent -25,0) <= s <= min(scurrent +25, 500)
#
# returns snews, a random value in the neighborhood of s
def neighbor(s):
    min_val = max(s - 25, 0)
    max_val = min(s + 25, 500)

    s_new = random.randint(min_val, max_val)
    while s_new == s:
        s_new = random.randint(min_val, max_val)
    return s_new


# Random Walk
def random_walk(s_initial, max_iter):
    s_current = s_initial
    s_best = s_current
    cost_current = cost(s_initial)
    cost_best = cost_current

    solution = numpy.zeros([max_iter + 1, 5])
    solution[0] = [0, s_current, s_best, cost_current, cost_best]

    for i in range(max_iter):
        s_current = neighbor(s_current)
        cost_current = cost(s_current)
        if cost_current < cost_best:
            cost_best = cost_current
            s_best = s_current
        solution[i + 1] = [i + 1, s_current, s_best, cost_current, cost_best]

    return solution


# Random Sampling
# New neighbor function
def random_sample_neighbor(s):
    s_new = random.randint(0, 500)
    while s_new == s:
        s_new = random.randint(0, 500)
    return s_new


def random_sample(s_initial, max_iter):
    s_current = s_initial
    s_best = s_current
    cost_current = cost(s_initial)
    cost_best = cost_current

    solution = numpy.zeros([max_iter + 1, 5])
    solution[0] = [0, s_current, s_best, cost_current, cost_best]

    for i in range(max_iter):
        s_current = random_sample_neighbor(s_current)
        cost_current = cost(s_current)
        if cost_current < cost_best:
            cost_best = cost_current
            s_best = s_current
        solution[i + 1] = [i + 1, s_current, s_best, cost_current, cost_best]

    return solution


# Deterministic neighborhood


# Greedy Deterministic
def gd_neighborhood(s):
    min_val = max(s - 10, 0)
    max_val = min(s + 10, 500)
    return [neighbor for neighbor in range(min_val, max_val) if neighbor != s]


def greedy_deterministic(s_initial, max_iter):
    cost_best = cost(s_initial)
    s_best = s_initial

    solution = numpy.zeros([max_iter + 1, 5])
    solution[0] = [0, s_initial, s_best, cost_best, cost_best]

    for i in range(max_iter):
        neighborhood = gd_neighborhood(s_best)
        for s_current in neighborhood:
            cost_current = cost(s_current)
            if cost_current < cost_best:
                cost_best = cost_current
                s_best = s_current
        solution[i + 1] = [i + 1, s_best, s_best, cost_best, cost_best]
    return solution


# Greedy Stochastic
def greedy_stochastic(s_initial, max_iter):
    s_current = s_initial
    s_best = s_initial
    cost_current = cost(s_initial)
    cost_best = cost_current

    solution = numpy.zeros([max_iter + 1, 5])
    solution[0] = [0, s_current, s_best, cost_current, cost_best]

    for i in range(max_iter):
        s_current = neighbor(s_best)
        cost_current = cost(s_current)
        if cost_current < cost_best:
            cost_best = cost_current
            s_best = s_current
        solution[i + 1] = [i + 1, s_current, s_best, cost_current, cost_best]
    return solution
