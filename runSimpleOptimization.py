import simpleOptimization as simple_opt
import random
import numpy

# This file generates csv files for each of the plots of the appropriate data,
# to allow for easy plot creating in Excel.

max_iter = 200
trials = 30

rw_solutions = []
rs_solutions = []
gd_solutions = []
gs_solutions = []

for i in range(trials):
    s_initial = random.randint(0, 500)
    rw_solutions.append(simple_opt.random_walk(s_initial, max_iter))
    rs_solutions.append(simple_opt.random_sample(s_initial, max_iter))
    gd_solutions.append(simple_opt.greedy_deterministic(s_initial, max_iter))
    gs_solutions.append(simple_opt.greedy_stochastic(s_initial, max_iter))

# Generate CSV for Random walk, first part of part f
(rows, cols) = rw_solutions[0].shape
with open("RW-solution1.csv", 'w') as rw_file:
    for i in range(rows):
        rw_file.write("%d, %d, %d\n" % (rw_solutions[0][i][0],
                                        rw_solutions[0][i][1],
                                        rw_solutions[0][i][2]))


# Second plot of part f
with open("RW-average.csv", 'w') as rw_average_file:
    for i in range(rows):
        total_cost_current = 0
        total_cost_best = 0
        for sol in range(trials):
            total_cost_current += rw_solutions[sol][i][3]
            total_cost_best += rw_solutions[sol][i][4]

        iteration = rw_solutions[0][i][0]
        avg_cost_current = total_cost_current / trials
        avg_cost_best = total_cost_best / trials

        rw_average_file.write("%d, %f, %f\n" % (iteration,
                                                avg_cost_current,
                                                avg_cost_best))


# Third plot of part f - average of the best costs after each iteration
with open("average-cost-best.csv", 'w') as best_file:
    for i in range(rows):
        total_bests = [0, 0, 0, 0]
        for sol in range(trials):
            total_bests[0] += rw_solutions[sol][i][4]
            total_bests[1] += rs_solutions[sol][i][4]
            total_bests[2] += gd_solutions[sol][i][4]
            total_bests[3] += gs_solutions[sol][i][4]

        iteration = rw_solutions[0][i][0]

        # Calculating averages in place
        best_file.write("%d, %f, %f, %f, %f\n" % (iteration,
                                                  total_bests[0] / trials,
                                                  total_bests[1] / trials,
                                                  total_bests[2] / trials,
                                                  total_bests[3] / trials))

# Fourth part: calculations
iteration = 100

rw_at_iteration = numpy.zeros([trials, 1])
rs_at_iteration = numpy.zeros([trials, 1])
gd_at_iteration = numpy.zeros([trials, 1])
gs_at_iteration = numpy.zeros([trials, 1])

for sol in range(trials):
    rw_at_iteration[sol] = rw_solutions[sol][iteration][4]
    rs_at_iteration[sol] = rs_solutions[sol][iteration][4]
    gd_at_iteration[sol] = gd_solutions[sol][iteration][4]
    gs_at_iteration[sol] = gs_solutions[sol][iteration][4]

print "Average and Std Dev of Cost Best After 100 Iterations:"

rw_avg = numpy.mean(rw_at_iteration)
rw_std = numpy.std(rw_at_iteration)
print "RW - Average: %f, Std Dev: %f" % (rw_avg, rw_std)

rs_avg = numpy.mean(rs_at_iteration)
rs_std = numpy.std(rs_at_iteration)
print "RS - Average: %f, Std Dev: %f" % (rs_avg, rs_std)

gd_avg = numpy.mean(gd_at_iteration)
gd_std = numpy.std(gd_at_iteration)
print "GD - Average: %f, Std Dev: %f" % (gd_avg, gd_std)

gs_avg = numpy.mean(gs_at_iteration)
gs_std = numpy.std(gs_at_iteration)
print "GS - Average: %f, Std Dev: %f" % (gs_avg, gs_std)
