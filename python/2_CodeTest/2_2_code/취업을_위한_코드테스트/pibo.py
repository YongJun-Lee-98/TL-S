
def pibo0(x):
    if x == 1 or x == 2:
        return 1
    return pibo0(x - 1) + pibo0(x - 2)

def pibo1(x, _cache):
    if x == 1 or x == 2:
        return 1
    if _cache[x] != 0:
        return _cache[x]
    _cache[x] = pibo1(x - 1, _cache) + pibo1(x - 2, _cache)
    print(x)
    return _cache[x]

def pibo2(x):
    if x == 1 or x == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, x + 1):
        a, b = b, a + b
    return b

def main():
    x = int(input())
    _cache = [0] * (x + 1)
    
    print(pibo1(x, _cache))
    print(pibo2(x))
    
main()