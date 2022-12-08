"""
Write a function to crush candy in one dimensional board. 
In candy crushing games, groups of like items are removed from the board. 
In this problem, any sequence of 3 or more like items should be removed and 
any items adjacent to that sequence should now be considered adjacent to each other. 
This process should be repeated as many time as possible. 
You should greedily remove characters from left to right.


aabbbacccd -> d


"""


def candyCrush(string: str) -> str:
    stack = [] # ("char", num)

    for char in string + "#":
        if stack and char != stack[-1][-1] and len(stack[-1]) >= 3:
            stack.pop()

        if stack and stack[-1][-1] == char:
            stack[-1] += char
        else:
            stack.append(char)

    res = "".join(stack[:-1])
    print(res)
    return res


if __name__ == "__main__":
    assert candyCrush("aabbbacccd") == "d"
    assert candyCrush("aabbbacd") == "cd"
    assert candyCrush("aabbccddeeedcba") == ""

