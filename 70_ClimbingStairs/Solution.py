from array import array
def dp(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
