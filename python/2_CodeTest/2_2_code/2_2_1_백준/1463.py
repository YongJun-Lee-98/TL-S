# x = int(input())

# d = [0] * 10 ** 6

# for i in range(2, x + 1):
#     d[i] = d[i - 1] + 1
    
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[x])

from collections import deque

x = int(input())
visited = [0] * (x + 1)

queue = deque()
print(queue)
queue.append(x)

while queue:
    n = queue.popleft()

    if n == 1:
        print(visited[n])
        break

    for next_n in [n - 1, n // 2 if n % 2 == 0 else 0, n // 3 if n % 3 == 0 else 0]:
        if next_n > 0 and visited[next_n] == 0: # next_n이 존재하고, visited가 초기화된 상태인 0을 유지한다면
            visited[next_n] = visited[n] + 1 # visited에 next_n번에 visited[n]+1을 추가한다.
            queue.append(next_n)
