def fibo(x, _cache):
	# 종료 조건
    if x == 1 or x == 2:
        return 1
    if _cache[x - 1] != 0:
        return _cache[x - 1]
    _cache[x - 1] = fibo(x - 1, _cache) + fibo(x - 2, _cache)
    return _cache[x-1]



def main():
	x = int(input())
	_cache = [0] * x
	print(fibo(x, _cache))

main()