import math

def constraints_valid(values):
    product = 1
    for x in values:
        if x < 0.0 or x > 10.0:
            return False
        product *= x
    return product >= 0.75


def cost(values):
    if not constraints_valid(values):
        return 0.0
    numerator_sum = 0.0
    numerator_product = 1.0
    denominator_sum = 0.0
    for i, x in enumerate(values):
        numerator_sum += math.cos(x) ** 4
        numerator_product *= math.cos(x) ** 2
        # Need i+1 below because Matlab is 1 indexed (ugh)
        denominator_sum += (i + 1) * (x ** 2)
    fraction = \
        (numerator_sum - 2 * numerator_product) / math.sqrt(denominator_sum)
    return abs(fraction)
