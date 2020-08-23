#! /usr/bin/env python
import random
def empty_boxes(balls= 10, boxes= [0]*12):
    for _ in range(balls):
        idx = random.randint(0,11)
        boxes[idx] +=1
    return boxes

def naive_simulation():
    total_tests = 100000
    ten_empty = 0
    for _ in range(total_tests):
        if empty_boxes().count(0) == 10:
            ten_empty +=1
    
    return ten_empty / total_tests

# P(B): 5 out of the 10 balls are randomly distributed, results in 10 or more boxes are empty
def ten_or_more_prob(number):
    ten_empty = 0
    states = []
    for i in range(number):
        box = empty_boxes(5, [0]*12)
        if box.count(0) >= 10:
            ten_empty +=1
            states.append(box)

    return ten_empty / number, states

# P(A|B): 10 boxes are empty, given 10 or more boxes are empty with 5 balls
def cond_prob(number, states):
    exact_ten = 0
    for _ in range(number):
        idx = random.randint(0, len(states)-1)
        state = states[idx][:]
        # put the other 5 balls in it, and evaluate whether 10 boxes are empty
        if empty_boxes(5, state).count(0) == 10:
            exact_ten +=1
    
    return exact_ten / number

if __name__ == "__main__":
    pb, states = ten_or_more_prob(10000)
    cond = cond_prob(50000, states)
    print(pb, cond)
    print(pb*cond)