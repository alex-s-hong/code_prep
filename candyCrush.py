def crush1(candy):
    stack = []

    for char in candy:
        if not stack:
            stack.append((char,1))

        else:
            if char == stack[-1][0]:
                _, occur = stack.pop()
                stack.append((char, occur+1))
            
            else:
                if stack[-1][1] > 2:
                    stack.pop()
                    if stack and stack[-1][0] == char:
                        _, occur = stack.pop()
                        stack.append((char, occur+1))
                    else:
                        stack.append((char, 1))

                else:
                    stack.append((char,1))
    if stack[-1][1] > 2:
        stack.pop()
    res = ''
    for elem in stack:
        res += elem[0] * elem[1]

    return res

def crush(candy):
    if not candy:
        return candy
    stack =[]

    for elem in candy:

        if not stack:
            stack.append((elem, 1))

        else:
            if stack[-1][0] == elem:
                prev_occ = stack[-1][1]
                stack[-1] = (elem, prev_occ+1)
            else:
                if stack[-1][1] > 2:
                    stack.pop()
                
                if stack[-1][0] == elem:
                    stack[-1] = (stack[-1][0], stack[-1][1] + 1)
                
                else:
                    stack.append((elem, 1))
    
    if stack[-1][1] > 2:
        stack.pop()

    # representation

    res = ''

    for elem, occur in stack:
        res += elem * occur

    return res





if __name__ == "__main__":
    print(crush('ABBCCC'))
    print(crush('ABCDDDDCCBBDDA'))
    print(crush('ABCCCDDBBB'))
    print(crush('AAAAAA'))