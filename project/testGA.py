import GA as GenAlgo
from allocation import generateRandomAllocation


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

trials = 10
pop_size = 10
max_gen = 20

# generate initial populations
initial_populations = []
for i in range(trials):
    population = []
    for j in range(pop_size):
        population.append(generateRandomAllocation())
    initial_populations.append(population)

# Run genetic algorithm for parameters, using roulette algorithm
best_score = float("inf")
best_p_crossover = 0
best_p_mutation = 0


# Go for a number of reasonably small steps
for p_crossover in frange(0.8, 1, 0.01):
    for p_mutation in frange(0.01, 0.1, 0.01):
        score = 0
        for pop in initial_populations:
            sol = GenAlgo.GA(pop, pop_size, max_gen, p_crossover, p_mutation)
            score += sol[0][max_gen - 1][2]
        print('%f, %f, %d' % (p_crossover, p_mutation, score))
        if score < best_score:
            best_score = score
            best_p_crossover = p_crossover
            best_p_mutation = p_mutation

print("Best p mutation: %f, Best p crossover: %f" % (best_p_mutation,
                                                     best_p_crossover))
# Do more, smaller steps around the best
prev_best_c = best_p_crossover
prev_best_m = best_p_mutation
for p_crossover in frange(prev_best_c - 0.02, prev_best_c + 0.02, 0.002):
    for p_mutation in frange(prev_best_m - 0.02, prev_best_m + 0.02, 0.002):
        score = 0
        for pop in initial_populations:
            sol = GenAlgo.GA(pop, pop_size, max_gen, p_crossover, p_mutation)
            score += sol[0][max_gen - 1][2]
        print('%f, %f, %d' % (p_crossover, p_mutation, score))
        if score < best_score:
            best_score = score
            best_p_crossover = p_crossover
            best_p_mutation = p_mutation

print("Best p mutation: %f, Best p crossover: %f" % (best_p_mutation,
                                                     best_p_crossover))
