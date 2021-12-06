"""
4 11 15 1
8 9 2 3
6 13 10 12
7 x 5 14


"""
from collections import deque

def minSwaps(grid):
    init = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']]
    init_loc = {}

    off_index = {}
    swaps = 0

    rows = len(grid)
    cols = len(grid[0])

    x_loc = (rows-1,cols-1)

    for i in range(rows):
        for j in range(cols):
            init_loc[init[i][j]] = (i,j)
            if grid[i][j] != init[i][j]:               
                off_index[(i,j)] = grid[i][j]


    # move from init to curr grid
    for loc, val in off_index.items():
        if init[loc[0]][loc[1]] == val:
            continue

        #1. swap X and val
        print("Init: swap X with {}".format(init[loc[0]][loc[1]]))
        init[loc[0]][loc[1]], init[x_loc[0]][x_loc[1]] = init[x_loc[0]][x_loc[1]], init[loc[0]][loc[1]]
        init_loc[init[x_loc[0]][x_loc[1]]] = x_loc
        x_loc = loc
        init_loc['X'] = x_loc
        swaps +=1


        while init[x_loc[0]][x_loc[1]] != grid[x_loc[0]][x_loc[1]]:
            #swap X with the value that should be in current X position
            target_val = off_index[x_loc]
            target_val_loc = init_loc[target_val]

            print("swap X with {}".format(target_val))
            init[x_loc[0]][x_loc[1]], init[target_val_loc[0]][target_val_loc[1]] = init[target_val_loc[0]][target_val_loc[1]], init[x_loc[0]][x_loc[1]]
            init_loc[target_val] = x_loc
            x_loc = target_val_loc
            init_loc['X'] = x_loc
            swaps +=1


    #print(init)
    return swaps



#grid = [[4,11,15,1],[8,9,2,3],[6,13,10,12],[7,'X',5,14]]
#grid = [[1,2,3,4],[5,6,15,8],[9,14,11,12],[13,10,7,'X']]
grid = [[9,2,10,4],[5,6,13,8],[1,3,11,12],[14,7,15,'X']]
print(minSwaps(grid))