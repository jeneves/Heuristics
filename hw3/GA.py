import math


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


# Calculates the 7-bit binary value of a decimal number between 0 - 127
def dec2bin(s):
    b = bin(s)[2:]
    if len(b) < 7:
        b = '0' * (7 - len(b)) + b
    return b


# Primary genetic algorithm function
def GA(X_initial, pop_size, max_gen, p_crossover, p_mutation):
    return None


# Tournament Selection genetic algorithm function
def GA_T(X_initial, pop_size, max_gen, p_crossover, p_mutation):
    return None


# Minimization genetic algorithm function
def GA_min(X_initial, pop_size, max_gen, p_crossover, p_mutation):
    return None


# Calculates the fitness of solution s, and, if convert_to_max is True,
# converts to a maximization.
def fitness(s, convert_to_max):
    return None


# Selects a pair of parents using roulette selection based on their fitness
# values.
def selection_R(P, fitness_values):
    return None


# Selects a pair of parents using tournament selection based on their fitness
# values.
def selection_T(P, fitness_values):
    return None


# Produces two children from the pair of parents, performing single-point
# crossover for each with probability p_crossover
def crossover(parent_one, parent_two, p_crossover):
    return None


# Mutates the solution at each bit with probability p_mutation
def mutation(s, p_mutations):
    return None
