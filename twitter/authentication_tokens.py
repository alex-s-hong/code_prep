#! usr/bin/env python3

"""
given a sequence of commands with no pre-existing tokens, and these commands sorted ascending
by their T parameter, find the number of tokens that are active just after all commands have been executed

expiryLimit = 4
commands = [[0,1,1], [0,2,2], [1,1,5], [1,2,7]]
[0,1,1]: get a new token with token_id = 1 at time T=1, set its eL to 1+4 =5
[0,2,2]: token_id = 2, time T=2 -> eL to 2+4 = 6
[1,1,5]: reset id=1 at time 5, eL = 9
[1,2,7]: reset not valid as 7 > 6(eL)
"""
from collections import defaultdict

def numberOfTokens(expiryLimit:int, commands):
    tokens = {}
    clock = 0

    for action, id, time in commands:
        #set_token
        clock = time
        if action == 0:
            tokens[id] = expiryLimit + time
        else:
            if id in tokens and tokens[id] >= time:
                tokens[id] = expiryLimit + time

    return sum(1 for i in tokens.values() if i >= clock)

if __name__ == "__main__":
    expiryLimit = 4
    commands = [[0,1,1], [0,2,2], [1,1,5], [1,2,7]]
    print(numberOfTokens(expiryLimit, commands))



