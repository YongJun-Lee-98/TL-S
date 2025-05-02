n = int(input())

x, y = 1, 1
plans = input().split()

move_map = [[0,-1],[0,1],[-1,0],[1,0]]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + move_map[i][0]
            ny = y + move_map[i][1]
    # 공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)