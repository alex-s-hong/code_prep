import math

def racing_car(obstacle_lanes):

    prev = [math.inf, 0, math.inf]
    next = [None, None, None]

    for block in obstacle_lanes:
        block -= 1

        for i in range(3):
            next[i] = min(prev[0]+1, prev[1]+1, prev[2]+1) if i != block else math.inf

            if i != block and prev[i] < next[i]:
                next[i] = prev[i]

        prev, next = next, prev
        #print(prev)

    print(min(prev))
    return min(prev)

racing_car([2,1,2])
racing_car([2,1,3,2])
racing_car([2,2,2,2,2,2,2,2,2,2])