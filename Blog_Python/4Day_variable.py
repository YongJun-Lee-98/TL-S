##이름 = 값

# james = 123456
# print(james)

## 변수 활용 세가지

# x = 3
# print("한변 길이 =", x)
# print("정사각형 둘레 =", 4 * x)
# print("정사각형 넓이 =" , x ** 2)

# # 숫자에서의 적용
# number = 10
# number += 20
# print(number) # 30이 예상됩니다.

# number = 10
# number -= 5
# print(number) # 5가 예상됩니다.

# number = 10
# number *= 2
# print(number) # 20이 예상됩니다.

# number = 10
# number /= 2
# print(number) # 5가 예상됩니다.

# number = 10
# number %= 3
# print(number) # 1이 예상됩니다.

# number = 10
# number **= 3
# print(number) # 1000이 예상됩니다.

# a = input("입력 : ")
# print("내용 : ", a)
# print("자료형 : ", type(a))

string_1 = input("1번 숫자 : ")

string_2 = input("2번 숫자: ")

int_1 = int(string_1)

int_2 = int(string_2)

print("문자열로 계산하면 : ", string_1 + string_2)

print("숫자로 계산하면 : ", int_1 + int_2)