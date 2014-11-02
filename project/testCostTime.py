import time
from cost import cost
from allocation import generateRandomAllocation

# Timing the execution of 10,000 random allocations + cost evaluations
numEvals = 10000
start_time = time.time()
for i in range(numEvals):
    cost(generateRandomAllocation())

print("%d evals take %s seconds." % (numEvals, (time.time() - start_time)))
