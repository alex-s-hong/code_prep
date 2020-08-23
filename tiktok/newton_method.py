#! usr/bin/env python3

def sqrt(a, k=1):
    x0 = a
    x1 = (x0 + a/x0)/2

    while abs(x1-x0) > k:
        x0 = x1
        x1 = (x0 + a/x0)/2

    return x1

def cubic_root(a, k=0.1):
    x0 = a
    x1 = (a/x0**2 + 2 * x0)/3

    while abs(x1 - x0) > k:
        x0 = x1
        x1 = (a/x0**2 + 2 * x0)/3
    return x1

def newton(nth, a, k):
    x0 = a
    x1 = ((nth-1) * x0 + a/x0**(nth-1))/nth

    while abs(x1 - x0) > k:
        x0 = x1
        x1 = ((nth-1)*x0 + a/x0**(nth-1))/nth
    return x1

if __name__ == "__main__":
    ans = sqrt(16, 0.001)
    print(ans)

    ans2 = cubic_root(81)
    print(ans2)

    ans3 = newton(3, 81, 0.1)
    print(ans3)