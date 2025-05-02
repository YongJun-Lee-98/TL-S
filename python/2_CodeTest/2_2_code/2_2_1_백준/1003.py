# def count_fibonacci(n: int, result_list: list) -> int:
#     if n == 0:
#         result_list[0] += 1
#         return 0
#     elif n == 1:
#         result_list[1] += 1
#         return 1
#     else:
#         return count_fibonacci(n - 1, result_list) + count_fibonacci(n - 2, result_list)
# # 몇 개를 구할것인가
# count = int(input())
# # 구할 정수들 개수만큼 초기화
# n_list = [0] * count

# for i in range(count):
#     n_list[i] = int(input())


# for n in n_list:
#     result_list = [0, 0]
#     count_fibonacci(n, result_list)
#     for i in result_list:
#         print(i, end=' ')
#     print(end='\n')

def fibo_count(n_list):
    max_n = max(n_list)
    dp=[[0, 0] for _ in range(max_n + 1)]
    # 초기 조건
    dp[0] = [1, 0]
    if max_n >= 1:
        dp[1] = [0, 1]
    # DP 테이블 채우기
    for i in range(2, max_n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    for n in n_list:
        for i in dp[n]:
            print(i, end=' ')
        print(end='\n')

count = int(input())
n_list = [int(input()) for _ in range(count)]

fibo_count(n_list)