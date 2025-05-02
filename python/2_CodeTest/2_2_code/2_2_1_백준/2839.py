def min_sugar_bags(N):
    for five_bags in range(N // 5, -1, -1):
        remaining = N - (5 * five_bags)
        if remaining % 3 == 0:
            three_bags = remaining // 3
            return five_bags + three_bags
    return -1

N = int(input())
print(min_sugar_bags(N))