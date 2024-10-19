# 나이트 이동 방식
# 수평으로 두 칸 이동 후 수직으로 한 칸
# 수직으로 두 칸 이동 후 수평으로 한 칸

# 나이트가 이동 가능한 경우의 수를 출력하는 프로그램을 작성하기
# a1에 있을 때 이동할 수 있는 경우는 다음 두가지임 c2, b3

# 입력조건 8*8로 평면상 두 문자로 구성된 문자열이 입력된다.

# 열 a ~ h
# 행 1 ~ 8

input_data = list(input())

row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)