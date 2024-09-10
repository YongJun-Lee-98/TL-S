N,M = map(int, input().split())
value = []
for i in range(N):
    a,b,c = map(int, input().split())
    min_value = min(a, b, c)
    value.append(min_value)

print(max(value))