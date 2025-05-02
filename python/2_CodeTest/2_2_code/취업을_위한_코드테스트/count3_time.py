# 완전 탐색 문제
# 전체 개수를 먼저 파악하고 for문을 사용해도 되는지 확인
# 대략 100,000개가 되지 않으면 완전탐색을 허용함  2초 내외이기 땨문

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)