# n = 배열의 크기 , m = 숫자가 더해지는 횟수, k = k번 이상 더해질 수 없는 조건

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k + m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)