import simpleOptimization as simple_opt
import random

max_iter = 200
rw_solutions = []
rs_solutions = []
gd_solutions = []
gs_solutions = []

for i in range(30):
    s_initial = random.randint(0, 500)
    rw_solutions.append(simple_opt.random_walk(s_initial, max_iter))
    rs_solutions.append(simple_opt.random_sample(s_initial, max_iter))
    gd_solutions.append(simple_opt.greedy_deterministic(s_initial, max_iter))
    gs_solutions.append(simple_opt.greedy_stochastic(s_initial, max_iter))

# generate CSV for Random walk
(rows, cols) = rw_solutions[0].shape
with open("RW-solution1.csv", 'w') as rw_file:
    for i in range(rows):
        rw_file.write("%d, %d, %d\n" % (rw_solutions[0][i][0],
                                        rw_solutions[0][i][1],
                                        rw_solutions[0][i][2]))
