import loadFile
import Tabu
import random

def rand_bin_string(len):
    vector = []
    for i in range(len):
        vector.append(str(random.randint(0,1)))
    return "".join(vector)

sat_matrix = loadFile.load_file("uf20_01.txt")
iterations = 100

for k in range(1, 20):
    sum_evals = 0
    sum_aspirations = 0
    for i in range(30):
        s_initial = rand_bin_string(20);
        (sol, aspiration, evals) = Tabu.tabu_search(
            s_initial, sat_matrix, k, iterations)
        sum_evals += evals
        sum_aspirations += aspiration
    print("avg %.2f evals, %.2f aspire for k = %d " %
        (float(sum_evals) / 30, float(sum_aspirations) / 30, k))
