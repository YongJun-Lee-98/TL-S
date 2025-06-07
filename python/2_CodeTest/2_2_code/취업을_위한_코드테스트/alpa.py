def user_def(times, alpa):
    alpa = list(alpa)
    times = int(times)

    for i in alpa:
        result = i * times
    return result


if __name__ == "__main__":
    repeat = int(input())
    for i in range(repeat):
        times, alpa = map(str, input().split())
        print(user_def(times, alpa))
