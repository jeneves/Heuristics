
import SA
import random

ap = 20
min_s = 0
max_s = 127
s_values = []
cost_values = []

#Set initial values
s = [random.randint(min_s, max_s), random.randint(min_s, max_s)]
cost_s = SA.cost(s)

s_values.append(s)
cost_values.append(cost_s)
best_s = s
best_cost = cost_s

# Find other s_values and calculate their costs
while len(s_values) != 20:
    s = [random.randint(min_s, max_s), random.randint(min_s, max_s)]
    if s not in s_values:
        cost_s = SA.cost(s)
        if cost_s < best_cost:
            best_s = s
            best_cost = cost_s
        s_values.append(s)
        cost_values.append(cost_s)


# Find s values in range of the best and calculate the average change in cost
neighbor_range = 25
neighbors = 0
neighbor_total_cost = 0

for (s, cost_s) in zip(s_values, cost_values):
    if s != best_s and abs(s[0] - best_s[0]) <= neighbor_range and \
            abs(s[1] - best_s[1]) <= neighbor_range:
        neighbors += 1
        neighbor_total_cost += (cost_s - best_cost)

avg_delta_cost = 0
if neighbors > 0:
    avg_delta_cost = neighbor_total_cost / neighbors

print "AvgDeltaCost = %f" % avg_delta_cost
