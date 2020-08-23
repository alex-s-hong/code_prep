#!/usr/bin/env python3

# new character in any position not only at the end. Return the construction path of the longest word.

# should fix to keep the ordinal information (ace /= cea)
def longest_word_path(input: list) -> list:
    dic = {}
    for i in input:
        n = len(i)
        if n in dic:
            dic[n].append(i)
        else:
            dic[n] = [i]

    res = []
    for i in dic[1]:
        for elem in i:
            tmp = dfs([elem], elem, 1, dic)
            #print(tmp)
            if len(tmp) > len(res):
                res = tmp

    return res


def dfs(tmp_l: list, curr: str, length: int, dic: dict):
    if length + 1 not in dic:
        return tmp_l
    candidate = []
    c_leng = 0
    for elem in dic[length + 1]:
        if set(curr).issubset(set(elem)):
            tmp_l.append(elem)
            curr_res = dfs(tmp_l, elem, length + 1, dic)
            if len(curr_res) > c_leng:
                candidate = curr_res
                c_leng = len(curr_res)

    return candidate


def longest_word(self, input: list) -> str:
    pass


if __name__ == "__main__":
    # path
    #one = longest_word_path(["o", "or", "ord", "word", "world"])
    #print(one)
    trace = longest_word_path(["o", "or", "ord", "word", "world", "p", "ap", "ape", "appe", "apple", "apples", "r", "ry", "ryp", "rypt", "crypt", "ncrypt", "encrypt"])
    print(trace)
