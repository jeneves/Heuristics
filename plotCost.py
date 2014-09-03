# Creates a csv of the cost function to plot in Excel
import simpleOptimization as simple_opt

with open('costPlot.csv', 'w') as cost_file:
    for s in range(500 + 1):
        cost_file.write('{0},{1}\n'.format(s, simple_opt.cost(s)))
