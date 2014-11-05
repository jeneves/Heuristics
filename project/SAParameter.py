from allocation import generateRandomAllocation
from cost import cost
from SA import neighbor

s_values = []
cost_values = []

#Set initial values
s = generateRandomAllocation()
cost_s = cost(s)

s_values.append(s)
cost_values.append(cost_s)
best_s = s
best_cost = cost_s

# Find other s_values and calculate their costs
while len(s_values) != 100:
    new_s = neighbor(s)
    cost_s = cost(new_s)
    if cost_s < best_cost:
        best_s = new_s
        best_cost = cost_s
    s_values.append(new_s)
    cost_values.append(cost_s)

neighbor_total_cost = 0

for (new_s, cost_s) in zip(s_values, cost_values):
    if new_s != best_s:
        neighbor_total_cost += (cost_s - best_cost)

avg_delta_cost = neighbor_total_cost / 100

print "AvgDeltaCost = %f" % avg_delta_cost
