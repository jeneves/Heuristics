import math
import random


# Maximum and minimum values of the cost function
max_cost = 1088359375
min_cost = 891015625


# s = [s1, s2], 0 <= s1, s2 <= 127
def cost(s):
    return (
        10 ** 9
        - (625 - (s[0] - 25) ** 2)
        * (1600 - (s[1] - 10) ** 2)
        * math.sin(s[0] * math.pi / 10)
        * math.sin(s[1] * math.pi / 10)
    )


# Calculates the decimal value of a binary string
def bin2dec(s):
    return int(s, 2)


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


# Primary genetic algorithm function - uses roulette selection and maximization
def GA(X_initial, pop_size, max_gen, p_crossover, p_mutation):

    convert_to_min = False
    use_tournament = False
    return GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
                      convert_to_min, use_tournament)


# Tournament Selection genetic algorithm function
# Only difference is selection_T is called instead of selection_R
def GA_T(X_initial, pop_size, max_gen, p_crossover, p_mutation):
    convert_to_min = False
    use_tournament = True
    return GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
                      convert_to_min, use_tournament)


# Minimization genetic algorithm function
# Only differences are True is used on fitness instead of false and generations
# are counted by number of calculations
def GA_min(X_initial, pop_size, max_gen, p_crossover, p_mutation):
    convert_to_min = True
    use_tournament = False
    return GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
                      convert_to_min, use_tournament)


# Primary genetic algorithm function
def GA_backend(X_initial, pop_size, max_gen, p_crossover, p_mutation,
               use_tournament, convert_to_min):

    fitness_values = []
    best_s = X_initial[0]
    best_fitness = fitness(best_s, convert_to_min)

    # Initial fitness of population
    for s in X_initial:
        fitness_s = fitness(s, convert_to_min)
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
            if use_tournament:
                parents = selection_T(population, fitness_values)
            else:
                parents = selection_R(population, fitness_values)
            children += crossover(parents, p_crossover)

        # Mutate the offspring and evaluate their fitness
        offspring = []
        offspring_fitness = []
        for child in children:
            mutated = mutation(child, p_mutation)
            offspring.append(mutated)
            offspring_fitness.append(fitness(mutated, convert_to_min))

        # Select the top children, plus the one top parent
        population, fitness_values = select(pop_size, fitness_values,
                                            offspring_fitness, population,
                                            offspring)

        # Produce relevant solution code
        generation = i
        if (convert_to_min):
            generation *= pop_size

        best_fitness = max(fitness_values)
        best_index = fitness_values.index(best_fitness)
        best_s = population[best_index]

        average_fitness = sum(fitness_values) / pop_size

        result = [generation, average_fitness, best_fitness]
        solution.append(result)

    s1 = best_s[0:7]
    s2 = best_s[7:14]
    s_vals = [bin2dec(s1), bin2dec(s2)]
    return (solution, s_vals)


# Calculates the fitness of solution s, and, if convert_to_min is True,
# converts to a minimization.
def fitness(s, convert_to_min):

    s1 = s[0:7]
    s2 = s[7:14]
    s_vals = [bin2dec(s1), bin2dec(s2)]
    fitness_s = cost(s_vals)

    # When converting to minimization, subtract from the maximum value and
    # add the minimum value to get the fitness
    if (convert_to_min):
        fitness_s = max_cost - fitness_s + min_cost
    return fitness_s


# Selects a pair of parents using roulette selection based on their fitness
# values.
def selection_R(population, fitness_values):
    total_fitness = sum(fitness_values)

    # Randomly choose two parents with probability based on their fitness
    parents = []
    for i in range(2):
        position = random.random() * total_fitness
        cur_fitness = 0
        for j in range(len(population)):
            if cur_fitness + fitness_values[j] >= position:
                parents.append(population[j])
                break
            cur_fitness += fitness_values[j]

    return parents


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

    offspring = []

    if p_crossover > random.random():
        crossover_point = random.randint(1, 13)
        child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
        child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
        offspring.append(child1)
        offspring.append(child2)
    else:
        offspring = parents

    return offspring


# Mutates the solution at each bit with probability p_mutation
def mutation(s, p_mutation):
    s_mutated = ''

    for i in range(len(s)):
        if p_mutation > random.random():
            if s[i] == '1':
                s_mutated += '0'
            else:
                s_mutated += '1'
        else:
            s_mutated += s[i]
    return s_mutated
