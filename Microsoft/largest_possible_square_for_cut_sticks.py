

def square(A:int, B:int):
    if A == B:
        return A//2
    
    max_size = B // 4

    if A >= B //3:
        max_size = max(max_size, B //3)
    else:
        max_size = max(max_size, A)

    if A >= B:
        max_size = max(max_size, B // 2)
    else:
        max_size = max(max_size, A // 2)

    if B >= A // 3:
        max_size = max(max_size, A //3)
    else:
        max_size = max(max_size, B)

    max_size = max(max_size, A//4)
    
    
    print(max_size)
    return max_size




if __name__ == "__main__":
    assert square(13,11) == 5
    assert square(10,21) == 7
    assert square(2,1) == 0
    assert square(1,8) == 2
    assert square(4, 15) == 4
    assert square(16,18) == 8
    assert square(19,5) == 5