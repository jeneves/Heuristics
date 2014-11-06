import numpy as np
from time import time
from cost import cost
from random import randint


def neighbor_classic(sCur, tenure, tabu_map):
    best_cost = float("inf")
    tabu_index = None
    rows, cols = len(sCur), len(sCur[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(j, cols):
                if sCur[i,j] != sCur[i,k] and (i,j,k) not in tabu_map:
                    temp = sCur[i,j]
                    sCur[i,j] = sCur[i,k]
                    sCur[i,k] = temp
                    new_cost = cost(sCur)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        tabu_index = (i,j,k)
                    sCur[i,k] = sCur[i,j]
                    sCur[i,j] = temp

    tabu_map = { k:(v - 1) for k,v in tabu_map.items() if k != 0 }
    best_neighbor = sCur[:,:]
    i,j,k = tabu_index
    temp = best_neighbor[i,j]
    best_neighbor[i,j] = best_neighbor[i,k]
    best_neighbor[i,k] = temp
    tabu_map[tabu_index] = tenure
    return best_neighbor


def shuffle_cell(cell_vector, num_swaps):
    cell = list(cell_vector)
    for i in range(num_swaps):
        first = randint(0, len(cell) - 1)
        second = randint(0, len(cell) - 1)
        temp = cell[first]
        cell[first] = cell[second]
        cell[second] = temp
    return cell

def neighbor(sCur, tenure, tabu_map, num_cell_neighbors=2, cell_variance=5):
    best_cost = float("inf")
    tabu_cell = -1
    best_neighbor = None
    rows, cols = len(sCur), len(sCur[0])
    for i in range(rows):
        if i not in tabu_map:
            for j in range(num_cell_neighbors):
                temp = sCur[i,:]
                sCur[i,:] = shuffle_cell(sCur[i,:], cell_variance)
                new_cost = cost(sCur)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_neighbor = sCur[:,:]
                    tabu_cell = i
                sCur[i,:] = temp
    tabu_map = { k:(v - 1) for k,v in tabu_map.items() if k != 0 }
    tabu_map[tabu_cell] = tenure
    return best_neighbor


def TabuSearch(s0, k, max_iter):
    tabu_map = {}
    m = len(s0)
    n = len(s0[0])
    sCur = np.zeros([max_iter, m, n])
    sBest = np.zeros([max_iter, m, n])
    solution = np.zeros(max_iter)
    sCur[0,:,:] = s0
    sBest[0,:,:] = s0
    bestCost = cost(sBest[0,:,:])
    solution[0] = bestCost

    for i in range(max_iter-1):
        start_time = time()

        sCur[i+1,:,:] = neighbor(sBest[i,:,:], k, tabu_map)

        #evaluate the cost of the new solution
        curCost = cost(sCur[i+1,:,:])

        #update the best cost and best solution
        if curCost < bestCost:
            sBest[i+1,:] = sCur[i+1,:,:]
            bestCost = curCost
        else:
            sBest[i+1,:] = sBest[i,:,:]

        #update the solution matrix
        solution[i+1] = bestCost
        # print("iteration complete %.2f" % (time() - start_time))

    return solution, sBest[max_iter-1,:,:]
