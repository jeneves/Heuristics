
import math
import random

# Calculates and returns the cost function
def cost(s):
    return (400 - (s-21) ** 2)  * math.sin(s * math.pi/6)

# Uses a neighborhood of max(scurrent -25,0) <= s <= min(scurrent +25, 500)
#
# returns snews, a random value in the neighborhood of s
def neighbor(s):
    minVal = max(s - 25, 0)
    maxVal = min(s + 25, 500)
    snew = random.randint(minVal, maxVal)
    return snew

# Random Walk



# Random Sampling



# Deterministic neighborhood



# Greedy Deterministic



# Greedy Stochastic


