"""
You are given an array S consisting of N strings. 
Every string is of the same length M. Your task is to find a pair of strings in array S, 
such that there exists a position in which both of the strings have the same letter. 
Both the index in array S and the positions in the strings are numbered from zero.
"""
from collections import defaultdict

def find_pairs(S) -> list:
    # dict containing dict
    char2position = {}

    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] in char2position and j in char2position[S[i][j]]:
                return [char2position[S[i][j]][j], i, j]
            else:
                if not S[i][j] in char2position:
                    char2position[S[i][j]] = {}
                char2position[S[i][j]][j] = i
    
    return []


if __name__ == "__main__":
    S = ["abc", "bca", "dbe"]
    print(find_pairs(S))

    S = ["abc", "bca", "dda"]
    print(find_pairs(S))

    S = ['abc', 'cda', 'dab']
    print(find_pairs(S))
