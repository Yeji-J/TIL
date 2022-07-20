## 제어문

- 특정 상황에 따라 코드를 선택적으로 실행
- 제어문은 순서도(flowchart)로 표현이 가능

---

### 조건문 `if/else`

: 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본 형식
  - 조건에는 `참/거짓`에 대한 조건식
  - 조건이 참일 경우 들여쓰기 되어 있는 코드 블록 실행
  - 이외 경우 `else` 이후 들여쓰기 되어 있는 코드 블록 실행
    - `else`는 선택적으로 활용할 수 있음!

```python
num = int(input())
if num % 2 == 0:
	print('짝수')
else:
	print('홀수')
```

### 복수 조건문 `elif`

```python
dust = 80
if dust > 150:
	print('매우 나쁨')
elif dust > 80:
	print('나쁨')
elif dust > 30:
	print('보통')
else:
	print('좋음')

# 보통
```

### 중첩 조건문

- 조건문은 다른 조건문에 중첩해 사용할 수 있음
- 들여쓰기에 유의 !!

1. 미세먼지 농도가 300이 넘는 경우 ‘실외 활동을 자제하세요’ 추가 출력
2. 음수인 경우 ‘값이 잘못 되었스니다’ 출력

```python
dust = 80
if dust > 150:
	print('매우 나쁨')
	if dust > 300:
		print('실외 활동을 자제하세요.')
elif dust > 80:
	print('나쁨')
elif dust > 30:
	print('보통')
elif dust >= 0:
	print('좋음')
else:
	print('값이 잘못 되었습니다.')
```

### 조건 표현식(Conditional Expression)

- 일반적으로 조건에 따라 값을 정할 때 활용
- 삼항 연산자(Tenary Operator)로 부르기도 함

```python
|true 인경우값| if 조건 else |false인경우값|
```

실습 1 : 절댓값을 저장하기 위한 코드

```python
value = num if num >= 0 else -num
```

실습 2 : 홀짝 판별

```python
result ='짝수입니다.' if num % 2 == 0 else result='홀수입니다'
print(result)
```

---

### 반복문

: 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용

- `while` : 종료 조건에 해당하는 코드를 통해 반복문 종료
- `for` : 반복 가능한 객체를 모두 순회하면 종료 (별도의 종료 조건 필요 X)
- 반복 제어 : `break` `continue` `for-else`

### `While`

: 조건이 참인 경우 반복적으로 코드 실행

- 무한 루프를 하지 않도 **종료 조건이 반드시 필요**

```python
a = 0
while a < 3:
	print(a)
	a += 1

# a
# a
# a
```

### 복합 연산자(In-Place Operator)

: 연산과 할당을 합쳐 놓은 것

`+=` `-=` `*=` etc

### `for`

`for` 변수명 `in` iterable

: 시퀀스를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회

- 처음부터 끝까지 모두 순회하므로 별도의 조건 종료 필요 X
- Iterable
  - 순회할 수 있는 자료형 `string` `list` `tuple` `range`
  - 순회형 함수 `range` `enumerate`

```python
fruits= ['apple', 'mango', 'banana']
for fruit in fruits:
	print(fruit)

# 'apple'
# 'mango'
# 'banana'
```

- 딕셔너리 순회

  - **딕셔너리는 기본적으로 key를 순회**하며, key를 통해 값을 활용

  ```python
  grades = {'john': 90, 'eric':90}
  for student in grades:
  	print(student, grades[student])

  # john 90
  # eric 90
  ```

  - 추가 메서드를 활용해 순회 가능
    - `keys()` : key로 구성된 결과
    - `values()` : value로 구성된 결과
    - `items()` : (key, value)의 튜플로 구성도된 결과

  ```python
  grades = {'john': 90, 'eric':90}
  for student, grade in grades.items():
  	print(student, grade)

  # ('john', 80)
  # ('eric', 90)
  ```

- `enumerate()` 순회

  - 인덱스와 객체를 쌍으로 담은 열거형 객체 반환
  - (index, value) 형태의 tuple로 구성된 열거 객체 반환

  ```python
  members = ['minsu', 'yeji', 'hwan']
  for index, number in enumerate(members):
  	print(index, number)

  # (0, 'minsu')
  # (1, 'yeji')
  # (2, 'hwan')

  for index, number in enumerate(members, start=1):
  	print(index, number)

  # (1, 'minsu')
  # (2, 'yeji')
  # (3, 'hwan')

  ```

- List Comprehension
  : 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성
  [ code `for` 변수 `in` iterable ]

  ```python
  # 세제곱의 결과가 담긴 리스트

  num_list = []
  for number in range(1, 4):
  	num_list.append(number ** 3)
  print(num_list)

  # 위와 같은 것을 구현하는 코드

  num_list = [number ** 3 for number in range(1, 4)]
  print(num_list)
  ```

- Dictionary Comprehension
  : 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성

  ```python
  num_dict = {}
  for number in range(1, 4):
  	num_dict[number] = number ** 3
  print(num_dict)

  # 위와 같은 것을 구현하는 코드

  num_dict = {number: number ** 3 for number in range(1, 4)}
  print(num_dict)

  # {1:1, 2:8, 3:9}
  ```

### 반복문 제어

- `break` : 반복문 종료
- `continue` : `continue` 이후 코드 블록은 수행하지 않고 다음 반복을 수행
- `for-else` : 끝까지 반복문을 실행한 이후에 `else` 문 실행
  - `break` 를 통해 중간에 종료되는 경우 `else` 문은 실행되지 않음
- `pass` : 아무것도 하지 않음 (문법적으로 필요하지만 ,할 일이 없을 때 사용)
  - 특별히 할 일이 없을 때 자리를 채우는 용도로 사용
  - 반복문 아니어도 사용 가능
