from math import cos, sqrt


def constraints_valid(values):
    product = 1
    for x in values:
        if x < 0.0 or x > 10.0:
            return False
        product *= x
    if product < 0.75:
        return False
    else:
        return True


def bump(values):
    if not constraints_valid(values):
        return 0.0
    numerator_sum = 0.0
    numerator_product = 1.0
    denominator_sum = 0.0
    for i, x in enumerate(values):
        numerator_sum += cos(x) ** 4
        numerator_product *= cos(x) ** 2
        # Need i+1 below because Matlab is 1 indexed (ugh)
        denominator_sum += (i + 1) * x ** 2
    fraction = (numerator_sum - 2 * numerator_product) / sqrt(denominator_sum)
    return abs(fraction)

# Testing that bump returns correct value!
print(bump([0.99] * 20))
