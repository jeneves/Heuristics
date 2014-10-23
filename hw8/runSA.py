import SA
import random
import numpy
from time import time

min_s = 0.0
max_s = 10.0
Z = []
trials = 20
beta = 1
m_initial = 1
max_time = 10000

while len(Z) != 30:
    s = []
    for i in range(20):
        s.append(random.uniform(min_s, max_s))
    Z.append(s)


def run_trials(T0, alpha, out_avg_file):
    solution_sets = []
    best_s_sets = []

    total_cpu_time = time()

    for i in range(trials):
        (solution, best_s) = SA.simulated_annealing(Z[i], T0, alpha,
                                                    beta, m_initial, max_time)
        solution_sets.append(solution)
        best_s_sets.append(best_s)

    total_cpu_time = time() - total_cpu_time

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
    best_costs = numpy.zeros([trials, 1])
    for sol in range(trials):
        best_costs[sol] = solution_sets[sol][max_time - 1][2]

    avg_cost = numpy.mean(best_costs)
    std_cost = numpy.std(best_costs)

    print("Average best cost: %f, Std Dev: %f" % (avg_cost, std_cost))

    # Avg CPU Time
    avg_cpu_time = total_cpu_time / trials
    print("Average CPU time: %f" % avg_cpu_time)

    with open("best_solutions_SA.txt", 'w') as output:
        output.write('SA = [')
        for best_cost in best_costs:
            output.write(str(best_cost[0]) + ' ')
        output.write('];')

T0 = 152934534.3
alpha = 0.996658

run_trials(T0, alpha, "SA.csv")
