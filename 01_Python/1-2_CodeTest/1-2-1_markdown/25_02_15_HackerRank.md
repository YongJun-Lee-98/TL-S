## 문항
[Probem Solving](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)

---
## 문제 요약

대학 등급 정책  
grade 는 0~100까지를 포함한다.  
- 84 round to 85 (5 단위로 반올림을 한다.)  
- 38보다 작으면 반올림하지 않는다.

---
## 문제 풀이
```python
def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade >= 38 and (grade//5) > 3:
            grade += grade//5
            result.append(grade)
        else:
            result.append(grade)
```

## 오류 사항

- 결과값(result)를 반환하는 return을 작성하지 않았음
- python의 사칙연산 // (몫) 의미하는데 
	%(나머지)를 사용해야 했음
	따라서 두가지의 조건이 충족한다면  
	5 단위 반올림을 한다.
- grade % 5를 하더라도 grade 변수에 더 해주는 것은 5단위의 나머지 값이여야 하므로 위의 풀이는 잘못 작성하였다.

### 해결 풀이
```python
def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade >= 38 and (grade % 5) >= 3:
            grade += 5 - grade % 5
            result.append(grade)
        else:
            result.append(grade)
    return result
            
```
- 문제풀이 단계에서 잘못 작성한 부분들을 수정하였음

### 개선 풀이(GPT 참조)
더 나은 풀이를 생각해보려 했지만 좋은 방법이 떠오르지 않을 경우  
ChatGPT에게 추천받은 내용을 입력하고  
해당 내용을 확인 및 다음 내 코드에도 적용시키려 합니다.
```python
def gradingStudents(grades):
	return [
		grade + (5 - grade % 5) if grade >= 38 and (grade % 5) >= 3 else grade
	for grade in grades
	]
```

#### ChatGPT가 최적화한 방향

> 리스트 컴프리헨션

기본 형태
```
[표현식 for 항목 in 반복가능한객체 if 조건문]
```
기본적인 리스트 생성
```python
numbers = [x for x in range(5)]
```

if 조건문 추가
```python
# 0을 포함한 짝수만 출력됨
even_number = [x for x in range(10) if x % 2 == 0]
```
