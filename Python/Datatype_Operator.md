## 자료형(Datatype) & 연산자(Operator)

### 문자열 자료형

- 모든 문자는 str 타입
- 문자열은 작은 따옴표나`'` 큰따옴표`"` 활용해 표기
    - 문자열을 묶을 때 동일한 문장부호 활용

---

1. 중첩 따옴표
    - 따옴표 안 따옴표를 표현할 때
2. 삼중 따옴표
    - 여러 줄 나눠 입력할 때
    - 따옴표 안에 따옴표를 넣을 때

### Escape sequence

:역슬래시(backslash)뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합

![Untitled](python.assets/Untitled2)

### 문자열 연산

1. 덧셈, 곱셈
    - **String Concatenation** : 문자열을 연결
    
    ```python
    print('Hello' + 'World') # HelloWorld
    print('Python' * 3) # PythonPythonPython
    ```
    
2. **String Interpolation** : 문자열을 변수를 활용하여 만드는 법
    - `%` formatting
    
    ```python
    name = 'Kim'
    score = 4.5
    print('Hello, %s' % name) # Hello, Kim
    print('내 성적은 %d' % score) # 내 성적은 4
    ```
    
    - `.format()`
    
    ```python
    name = 'Kim'
    score = 4.5
    print('Hello, {}! Your score is {}' .format(name, score))
    ```
    
    - **`f`-strings**: python 3.6+ (형식 지정 가능)
    
    ```python
    print(f'Hello, {name}! Your score is {score}')
    
    print(f'오늘은 {today $y}년 {today %m}월 {today %d}일')
    #오늘은 22년 07월 18일
    ```
    

---

### None

: 파이썬 자료형 중 하나

: **값이 없음을 표현**하기 위해 None 타입이 존재

: 일반적으로 반환 값이 없는 함수에 사용하기도 함

---

### 불린형(Boolean)

: 논리 자료형으로 **참과 거짓을 표현**하는 자료형

: True`1` 또는 False`0`를 값으로 가짐

: 비교 / 논리 연산에서 활용

---

### 비교 연산자

- 수학에서 등호, 부등호와 동일한 개념
- 주로 조건문에 사용되며 값을 비교할 때 사용
- 결과는 True / False 리턴
- 종류
    - `<` 미만
    - `<=` 이해
    - `>` 초과
    - `>=` 이상
    - `==` 같음
    - `!=` 같지 않음
    - `is` 객체 아이덴티티(OOP)
    - `is not` 객체 아이덴티티가 아닌 경우

```python
print(3 > 6) # False
print(3.0 == 3) # True
print ( 2 >= 0) # True
print('3' != 3) # True
print('Hi' == 'hi') # False
```

---

### 논리연산자

- 여러 가지 조건이 있을 때

`A and B` : A와 B 모두 True ⇒ True

`A or B` : A와 B 모두 False ⇒ False

`Not` : True ⇒ False, False ⇒ True

- **논리연산자 주의할 점** : **not 연산자**
    - Falsy: False는 아니지만 False로 취급되는 다양한 값
        - `()`, `[]`, `{}`, `0`, `0.0`, `“”`(빈 문자열)
        - Falsy가 아닌 모든 값은 True
            
            → False로 평가되는 것만 기억하자!
            
- 논리 연산자도 우선 순위가 존재
    
    `not` >`and` >`or`
    
- 논리 연산자의 단축 평가
    - 결과가 확실한 경우 두 번째는 확인하지 않고 첫 번째 값 반환
    - `and` 연산에서 **첫 번째가 False**인 경우
    - `or` 연산에서 **첫 번째가 True**인 경우
    - `0은 False, 1은 True`

```python
print(3 and 5) # 5 : 5 때문에 true라 평가를 받음
print(3 and 0) # 0
print(0 and 3) # 0
```