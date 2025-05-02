n, k = map(int, input().split())

# 나눴을때 나머지가 0이면 나눈고 아니면 1을 뺀다.
number = 0
while True:
    if n == 1:
        break
    elif (n % k == 0):
        n = int(n/k)
    else:
        n -= 1
    print(n)
    number += 1

print(number)