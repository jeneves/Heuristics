import GA as GenAlgo
import random


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
for pop in initial_populations:
    results.append(GenAlgo.GA(pop, pop_size, max_gen, p_crossover, p_mutation))

# Compute average best fitness, for each generation, averaging over 30 trials
with open("fitness_vs_gen.csv", 'w') as output:
    for i in range(max_gen):
        sum_fitness = 0
        for j in range(total_iterations):
            sum_fitness += results[j][0][i][2]
        output.write("%d,%.2f\n" % (i, (sum_fitness / total_iterations)))
