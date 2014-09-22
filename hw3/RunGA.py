import GA as GenAlgo
import random
import numpy


total_iterations = 30
pop_size = 20
entity_size = 14
max_gen = 50
p_crossover = 0.9
p_mutation = 0.05

# generate initial populations
initial_populations = []
for i in range(total_iterations):
    population = []
    for j in range(pop_size):
        entity = []
        for k in range(entity_size):
            entity.append(str(random.randint(0, 1)))
        population.append("".join(entity))
    initial_populations.append(population)

# Run genetic algorithm
results = []
num_global_max = 0
for pop in initial_populations:
    sol = GenAlgo.GA(pop, pop_size, max_gen, p_crossover, p_mutation)
    if sol[0][max_gen][2] == GenAlgo.max_cost:
        num_global_max += 1
    results.append(sol)
print 'Found global maximum %d times' % num_global_max

# Run genetic algorithm with tournament selection
results_t = []
for pop in initial_populations:
    results_t.append(
        GenAlgo.GA_T(pop, pop_size, max_gen, p_crossover, p_mutation))

# new populations for the minimization (homework requests it...)
initial_populations = []
for i in range(total_iterations):
    population = []
    for j in range(pop_size):
        entity = []
        for k in range(entity_size):
            entity.append(str(random.randint(0, 1)))
        population.append("".join(entity))
    initial_populations.append(population)


# One last time for the minimization problem
results_min = []
for pop in initial_populations:
    results_min.append(
        GenAlgo.GA_min(pop, pop_size, max_gen, p_crossover, p_mutation))

# Compute average best fitness, for each generation, averaging over 30 trials
with open("fitness_vs_gen.csv", 'w') as output:
    for i in range(max_gen):
        sum_fitness = 0
        for j in range(total_iterations):
            sum_fitness += results[j][0][i][2]
        output.write("%d,%.2f\n" % (i, (sum_fitness / total_iterations)))

with open("tournament_vs_roulette.csv", 'w') as output:
    output.write('Generation,Roulette,Tournament\n')
    for i in range(max_gen):
        sum_fitness_roulette = 0
        sum_fitness_tourney = 0
        for j in range(total_iterations):
            sum_fitness_roulette += results_t[j][0][i][2]
            sum_fitness_tourney += results[j][0][i][2]
        output.write("%d,%.2f,%.2f\n" %
                    (i,
                     (sum_fitness_roulette / total_iterations),
                     (sum_fitness_tourney / total_iterations)))

with open("minimized.csv", 'w') as output:
    for i in range(max_gen):
        sum_fitness = 0
        for j in range(total_iterations):
            sum_fitness += abs(results_min[j][0][i][2]
                               - GenAlgo.max_cost - GenAlgo.min_cost)
        output.write("%d,%.2f\n" % (i * 20, (sum_fitness / total_iterations)))

best_costs = numpy.zeros([total_iterations, 1])
num_global_min = 0
for j in range(total_iterations):
    best_costs[j] = abs(results_min[j][0][i][2]
                        - GenAlgo.max_cost - GenAlgo.min_cost)
    if best_costs[j] == GenAlgo.min_cost:
            num_global_min += 1

avg_cost = numpy.mean(best_costs)
std_cost = numpy.std(best_costs)
print "Average best cost: %f, Std Dev: %f" % (avg_cost, std_cost)
print "Number of global min: %d" % (num_global_min)
