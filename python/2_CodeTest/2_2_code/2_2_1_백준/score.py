# score = int(input())
# if  90 <= score <= 100:
#     print("A")
# elif 80 <= score <= 89:
#     print("B")
# elif 70 <= score <= 79:
#     print("C")
# elif 60 <= score <= 69:
#     print("D")
# else:
#     print("F")

### gpt 제안
score = int(input())
grades = {
    9: "A",
    8: "B",
    7: "C",
    6: "D",
}
print(grades.get(min(score // 10, 9), "F"))