## 문항
피보나치 수열을 구현 하라.
fibo = 1, 1, 2, 3, 5, 8, ...

---
## 문제 요약

방식 1 Top-Down(탑다운 방식)
방식 2 메모지제이션으로 개선
방식 3 Bottom-Up보텀업

---
## 문제 풀이

### Top-Down

```python
def fibo(x):
	# 종료 조건
	if x == 1 or x == 2:
		return 1
	# 맨 위에서 아래로 계산하여 Top-Down 방식
	# 재귀적으로 표현한다.
	return fibo(x - 1) + fibo(x - 2)

print(fibo(99))
```

### Memozation

```python
def fibo(x, _cache):
	# 종료 조건
	if x == 1 or x == 2:
		return 1
	if _cache[x - 1] != 0:
		return _cache[x - 1]
	return fibo(x - 1) + fibo(x - 2)

def main():
	x = int(input())
	_cache = [0] * x
	print(fibo(x, _cache))

main()
```
## 오류 사항
```bash

```

### 해결 풀이
```python

```

### 개선 풀이
```python

```