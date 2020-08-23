def largestRectangle(h):
    s = []
    ans = len(h) #initial value
    h.append(0)
    
    for i in range(len(h)):
        left_index = i
        while s and s[-1][0] >= h[i]: # when the next building is not taller than the previous
            prev = s.pop()
            left_index = prev[1]
            ans = max(ans, h[i] * (i - left_index +1)) # to the left
            ans = max(ans, prev[0] * (i - left_index)) # to the right
        s.append((h[i], left_index))
    
    return ans

if __name__ == "__main__":
    h = [2, 5, 7, 6, 3, 4]
    ans = largestRectangle(h)
    print(ans)
