import math

def cost(sinitial):
    ''' You need to define your own cost function, here is just an example
        '''
    s1 = sinitial[0]
    s2 = sinitial[1]

    costS = 10**9 - (625 - (s1 - 25)**2) * (1600 - (s2 - 10)**2) * math.sin(s1 * math.pi/10) * math.sin(s2 * math.pi/10)

    return costS
