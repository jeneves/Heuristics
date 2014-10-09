from math import cos, sqrt
from InitialPopulations import initial_populations
import random
from numpy import mean, std


def constraints_valid(values):
    product = 1
    for x in values:
        if x < 0.0 or x > 10.0:
            return False
        product *= x
    if product < 0.75:
        return False
    else:
        return True


def bump(values):
    if not constraints_valid(values):
        return 0.0
    numerator_sum = 0.0
    numerator_product = 1.0
    denominator_sum = 0.0
    for i, x in enumerate(values):
        numerator_sum += cos(x) ** 4
        numerator_product *= cos(x) ** 2
        # Need i+1 below because Matlab is 1 indexed (ugh)
        denominator_sum += (i + 1) * x ** 2
    fraction = (numerator_sum - 2 * numerator_product) / sqrt(denominator_sum)
    return abs(fraction)


# Selects the best pop_size population from the parents and children, using
# elitism with m = 1.
def select(pop_size, parent_fitness, offspring_fitness, parents, offspring):

    # Sorting the indices by best fitness in the list
    parent_fitness_indices = sorted(range(len(parent_fitness)),
                                    key=lambda k: parent_fitness[k])
    offspring_fitness_indices = sorted(range(len(offspring_fitness)),
                                       key=lambda k: offspring_fitness[k])

    # Following elitism with m = 1 - take last parent and last n - 1 children
    best_parent_index = parent_fitness_indices[-1]
    best_offspring_indices = offspring_fitness_indices[-(pop_size - 1):]

    parent = parents[best_parent_index]
    fitness_of_parent = parent_fitness[best_parent_index]
    children = list(offspring[i] for i in best_offspring_indices)
    fitness_of_children = list(offspring_fitness[i]
                               for i in best_offspring_indices)

    population = [parent] + children
    fitness_values = [fitness_of_parent] + fitness_of_children

    return (population, fitness_values)


# Tournament Selection genetic algorithm function
# Only difference is selection_T is called instead of selection_R
def GA_T(X_initial, pop_size, max_gen, p_crossover, p_mutation, variance):
    convert_to_min = False
    use_tournament = True
    return GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
                      convert_to_min, use_tournament, variance)


# Primary genetic algorithm function
def GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
               convert_to_min, use_tournament, variance):
    fitness_values = []
    best_s = X_initial[0]
    best_fitness = bump(best_s)

    # Initial fitness of population
    for s in X_initial:
        fitness_s = bump(s)
        if (fitness_s > best_fitness):
            best_s = s
            best_fitness = fitness_s
        fitness_values.append(fitness_s)
    average_fitness = sum(fitness_values) / pop_size

    solution = []
    solution.append([0, average_fitness, best_fitness])
    population = X_initial

    # Go through all generations
    for i in range(1, max_gen + 1):

        # Generate children from crossover
        children = []
        while len(children) < pop_size:
            parents = []
            parents = selection_T(population, fitness_values)
            children += crossover(parents, p_crossover)

        # Mutate the offspring and evaluate their fitness
        offspring = []
        offspring_fitness = []
        for child in children:
            mutated = mutation(child, p_mutation, variance)
            offspring.append(mutated)
            offspring_fitness.append(bump(mutated))

        # Select the top children, plus the one top parent
        population, fitness_values = select(pop_size, fitness_values,
                                            offspring_fitness, population,
                                            offspring)

        # Produce relevant solution code
        generation = i
        best_fitness = max(fitness_values)
        best_index = fitness_values.index(best_fitness)
        best_s = population[best_index]

        average_fitness = sum(fitness_values) / pop_size

        result = [generation, average_fitness, best_fitness]
        solution.append(result)

    return (solution, best_s)


# Selects a pair of parents using tournament selection based on their fitness
# values.
def selection_T(population, fitness_values):
    parents = []
    for i in range(2):

        # Pick two random indices
        x = range(0, len(population))
        random.shuffle(x)
        indices = x[0:2]
        if fitness_values[indices[0]] > fitness_values[indices[1]]:
            parents.append(population[indices[0]])
        else:
            parents.append(population[indices[1]])

    return parents


# Produces two children from the pair of parents, performing single-point
# crossover for each with probability p_crossover
def crossover(parents, p_crossover):
    if p_crossover > random.random():
        # We attempt to do crossover 6 times checking if constraints are obeyed
        attempts = 0
        while True:
            crossover_pt = random.randint(1, 19)
            child1 = parents[0][:crossover_pt] + parents[1][crossover_pt:]
            child2 = parents[1][:crossover_pt] + parents[0][crossover_pt:]
            if constraints_valid(child1) and constraints_valid(child2):
                return [child1, child2]
            else:
                attempts += 1
                if attempts > 5:
                    return parents
    else:
        return parents


# Mutates the solution at each bit with probability p_mutation
def mutation(s, p_mutation, variance):
    # We attempt to do mutation 6 times checking if constraints are obeyed
    attempts = 0
    while True:
        s_mutated = []
        for i in range(len(s)):
            if p_mutation > random.random():
                s_mutated.append(s[i] + random.gauss(0, sqrt(variance)))
            else:
                s_mutated.append(s[i])
        if constraints_valid(s_mutated):
            return s_mutated
        else:
            attempts += 1
            if attempts > 5:
                return s


# LET'S RUN THIS SHIT
def generate_initial_populations():
    print('[')
    for i in range(20):
        population = []
        for j in range(50):
            meep = []
            for k in range(20):
                meep.append(random.random() * 10)
            population.append(meep)
        if i == 19:
            print(population)
        else:
            print(str(population) + ',')
    print(']')


# Do not run this because it takes forever lolol
def find_best_parameters(pop_size, max_gen):
    possible_parameters = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    possible_variances = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    best_variance = 0
    best_mutation = 0
    best_crossover = 0
    best_average_elite_solution = 0
    populations = initial_populations()
    for p_mutation in possible_parameters:
        for p_crossover in possible_parameters:
            for variance in possible_variances:
                print('Trying: ' + str(variance) + ', ' +
                      str(p_crossover) + ', ' +
                      str(p_mutation))
                elite_solutions = []
                for i in range(3):
                    solution, elite = GA_T(populations[i], pop_size, max_gen,
                                           p_crossover, p_mutation, variance)
                    elite_solutions.append(bump(elite))
                average_elite_solution = mean(elite_solutions)
                print('Average elite solution: ' + str(average_elite_solution))
                if average_elite_solution > best_average_elite_solution:
                    print('Found new best values!')
                    best_average_elite_solution = average_elite_solution
                    best_variance = variance
                    best_crossover = p_crossover
                    best_mutation = p_mutation
    print('We found some great parameters!!')
    print('Variance: ' + str(best_variance))
    print('Probability Crossover: ' + str(best_crossover))
    print('Probability Mutation: ' + str(best_mutation))


pop_size = 50
max_gen = 200
p_crossover = 0.7
p_mutation = 0.1
variance = 2

elite_solutions = []
elite_solution_vals = []
all_solutions = []
for population in initial_populations():
    solution, elite = GA_T(population, pop_size, max_gen,
                           p_crossover, p_mutation, variance)
    elite_solutions.append(elite)
    elite_solution_vals.append(bump(elite))
    all_solutions.append(solution)

with open("problem2_results.txt", 'w') as output:
    output.write('Average: ' + str(mean(elite_solution_vals)))
    output.write('\nStandard deviation: ' + str(std(elite_solution_vals)))
    best_value = max(elite_solution_vals)
    output.write('\nBest value: ' + str(best_value))
    output.write('\nBest member: ' +
                 str(elite_solutions[elite_solution_vals.index(best_value)]))
    worst_value = min(elite_solution_vals)
    output.write('\Worst member: ' + str(worst_value))
    output.write('\nWorst value: ' +
                 str(elite_solutions[elite_solution_vals.index(worst_value)]))

with open("problem2_elitesolution_vs_evals.csv", 'w') as output:
    output.write('Function Evaluations,Average\n')
    for i in range(1, max_gen + 1):
        elite_solutions_at_i = []
        for solution in all_solutions:
            elite_solutions_at_i.append(solution[i][2])
        average_elite_solution = mean(elite_solutions_at_i)
        output.write(str(i * 20) + ',' + str(average_elite_solution) + '\n')
