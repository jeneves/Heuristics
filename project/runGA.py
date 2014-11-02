import GA as GenAlgo
import numpy
from time import time
from allocation import generateRandomAllocation


trials = 30
pop_size = 50
max_gen = 50
p_crossover = 0.9
p_mutation = 0.01

# generate initial populations
initial_populations = []
for i in range(trials):
    population = []
    for j in range(pop_size):
        population.append(generateRandomAllocation())
    initial_populations.append(population)

# Run genetic algorithm and time it - using roulette selection
total_cpu_time = time()
results = []
num_global_max = 0
for pop in initial_populations:
    sol = GenAlgo.GA(pop, pop_size, max_gen, p_crossover, p_mutation)
    results.append(sol)

total_cpu_time = time() - total_cpu_time


# Run genetic algorithm with tournament selection
total_cpu_time_t = time()
results_t = []
for pop in initial_populations:
    results_t.append(
        GenAlgo.GA_T(pop, pop_size, max_gen, p_crossover, p_mutation))

total_cpu_time_t = time() - total_cpu_time_t


# Compute average best fitness, for each generation, averaging over 30 trials
with open("GA.csv", 'w') as output:
    output.write('Generation,Roulette,Tournament\n')
    for i in range(max_gen):
        sum_fitness_roulette = 0
        sum_fitness_tourney = 0
        for j in range(trials):
            sum_fitness_roulette += results[j][0][i][2]
            sum_fitness_tourney += results_t[j][0][i][2]
        output.write("%d,%.2f,%.2f\n" %
                    (i,
                     (sum_fitness_roulette / float(trials)),
                     (sum_fitness_tourney / float(trials))))

# Avg and Std deviation
best_costs = numpy.zeros([trials, 1])
best_costs_t = numpy.zeros([trials, 1])
for sol in range(trials):
    best_costs[sol] = results[sol][0][max_gen - 1][2]
    best_costs_t[sol] = results_t[sol][0][max_gen - 1][2]

avg_cost = numpy.mean(best_costs)
std_cost = numpy.std(best_costs)
print("Roulette: Average best cost: %f, Std Dev: %f" % (avg_cost, std_cost))

avg_cpu_time = total_cpu_time / trials
print("Average CPU time: %f" % avg_cpu_time)


avg_cost_t = numpy.mean(best_costs_t)
std_cost_t = numpy.std(best_costs_t)
print("Tournament: Average best cost: %f, Std Dev: %f" % (avg_cost_t,
                                                          std_cost_t))

avg_cpu_time_t = total_cpu_time_t / trials
print("Average CPU time tournament: %f" % avg_cpu_time_t)

with open("best_solutions_GA.txt", 'w') as output:
    output.write('GA = [')
    for best_cost in best_costs:
        output.write(str(best_cost) + ' ')
    output.write('];\n')

    output.write('GA_T = [')
    for best_cost_t in best_costs_t:
        output.write(str(best_cost_t) + ' ')
    output.write('];')
