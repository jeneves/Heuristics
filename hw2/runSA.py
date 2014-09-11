import SA
import random
import numpy
from time import time

min_s = 0
max_s = 127
Z = []

while len(Z) != 30:
    solution_sets = []
    best_s_sets = []
    s = [random.randint(min_s, max_s), random.randint(min_s, max_s)]
    if not s in Z:
        Z.append(s)


def run_trials(T0, alpha, out_avg_file):
    beta = 1
    m_initial = 1
    max_time = 1100

    trials = 30

    total_cpu_time = 0

    for i in range(trials):
        t = time()
        (solution, best_s) = SA.simulated_annealing(Z[i], T0, alpha,
                                                    beta, m_initial, max_time)
        total_cpu_time += (time() - t)

        solution_sets.append(solution)
        best_s_sets.append(best_s)

    # Best vs. Cur Cost
    with open(out_avg_file, 'w') as out_file:
        for i in range(max_time):
            total_cost_current = 0
            total_cost_best = 0
            for sol in range(trials):
                total_cost_current += solution_sets[sol][i][1]
                total_cost_best += solution_sets[sol][i][2]
            iteration = solution_sets[sol][i][0]

            avg_cost_current = total_cost_current / trials
            avg_cost_best = total_cost_best / trials

            out_file.write("%d, %f, %f\n" % (iteration,
                                             avg_cost_current,
                                             avg_cost_best))

    # Avg and Std deviation
    G = 1000
    best_costs = numpy.zeros([trials, 1])
    for sol in range(trials):
        best_costs[sol] = solution_sets[sol][G][2]

    avg_cost = numpy.mean(best_costs)
    std_cost = numpy.std(best_costs)

    print "Average best cost: %f, Std Dev: %f" % (avg_cost, std_cost)

    # Avg CPU Time
    avg_cpu_time = total_cpu_time / trials
    print "Average CPU time: %f" % avg_cpu_time

# P1 = 0.9
# Calculated from SAParamter.py
T0 = 152934534.3
alpha = 0.996658

run_trials(T0, alpha, "p1_0.9.csv")

# P1 = 0.7
T0 = 45176320.0
alpha = 0.997874

run_trials(T0, alpha, "p1_0.7.csv")
