import random
import numpy
from time import time
from Tabu import TabuSearch
from allocation import generateRandomAllocation


trials = 5
max_iter = 500
k = 3

def run_trials(out_avg_file):
    solution_sets = []
    best_s_sets = []

    total_cpu_time = time()

    for i in range(trials):
        (solution, best_s) = TabuSearch(generateRandomAllocation(), k, max_iter)
        solution_sets.append(solution)
        best_s_sets.append(best_s)
        print("trial complete")

    total_cpu_time = time() - total_cpu_time

    with open(out_avg_file, 'w') as out_file:
        for i in range(max_iter):
            total_cost_best = 0

            for sol in range(trials):
                total_cost_best += solution_sets[sol][i]

            avg_cost_best = total_cost_best / trials

            out_file.write("%d, %f\n" % (i + 1, avg_cost_best))

    # Avg and Std deviation
    best_costs = numpy.zeros([trials, 1])
    for sol in range(trials):
        best_costs[sol] = solution_sets[sol][max_iter - 1]

    avg_cost = numpy.mean(best_costs)
    std_cost = numpy.std(best_costs)

    print("Average best cost: %f, Std Dev: %f" % (avg_cost, std_cost))

    # Avg CPU Time
    avg_cpu_time = total_cpu_time / trials
    print("Average CPU time: %f" % avg_cpu_time)

    with open("best_solutions_TS.txt", 'w') as output:
        output.write('TS = [')
        for best_cost in best_costs:
            output.write(str(best_cost[0]) + ' ')
        output.write('];')


run_trials("TS.csv")
