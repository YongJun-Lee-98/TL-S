n, k = map(int, input().split())

count = 0
while True:
    # 나머지 수는 -1횟수와 나누는 동작 횟수로 +1을 해줌 
    count += n % k + 1
    n = n // k
    if n < k:
        # 1까지 빼야하니까 횟수는 1개가 적게해줌
        count += n - 1
        break

print(count)