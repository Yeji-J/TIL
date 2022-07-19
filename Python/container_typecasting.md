## 컨테이너 (자료구조)

: 데이터 여러개 저장할 수 있고 서로 다른 자료형을 저장할 수 있음 like `list`

- 순서가 있는 데이터(ordered) vs 순서가 없는 데이터(unordered)
    - **순서가 있다 ≠ 정렬되어 있다.**
- 시퀀스형 == 반복가능한 개체..?
    - 리스트 *(mutable)*
    - 튜플 (immutable)
    - 레인지 (immutable)
- 비시퀀스형
    - 세트 *(mutable)*
    - 딕셔너리 (mutable)

---

### 리스트

: 여러 개의 값을 **순서가 있는 구조로 저장**하고 싶을 때 사용

- 리스트는 대괄호 `[]` 혹은 `list()` 를 통해 생성
    - 어떠한 자료형도 저장 가능, 리스트 중첩 가능
    - 생성된 이후 내용 변경 가능
    - 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
        - `list[index]` : **index 0부터 시작**

---

### 튜플

: 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

⇒ 리스트와 차이점: **생성 후, 담고 있는 값 변경 불가**

- 소괄호 형태로 사용 `()` or `tuple()`
    - 수정 불가능한 시퀀스로 인덱스 통해 접근 가능
        - `my_tuble[i]`
- 튜플 생성 주의사항
    - 단일 항목의 경우
        - 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 함
    - 복수 항목의 경우,
        - 마지막 항목에 붙은 쉼표는 없어도 되지만, 넣는 것 권장(Traling comma)
    
    ```python
    tuple_a = (1, 2, 3,)
    print(tuple_b) # (1, 2, 3)
    print(type(tuple_b)) # <class 'tuple'>
    ```
    
- 튜플대입(Tuple Assignment)

: 우변의 값을 좌변의 변수에 한 번에 할당하는 과정

- 추후 함수에서 복수의 값을 반환할 때에도 활용

```python
x, y = 1, 2
print(x, y) # 1 2 

x, y = (1, 2)
print(x, y) # 1 2
```

---

### Range

: 숫자의 시퀀스를 나태내기 위해 사용

: 주로 반복문과 함께 사용

`range(숫자)` : 0부터 숫자-1 까지

`range(start, stop, step)` : step에 음수도 가능 range(6, 1, -1)

```python
print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
print(list(range(6, 1, 2))) # [6, 4, 2]
print(list(range(6, 1, 1))) # [] null
```

---

### 슬라이싱 연산자

- 시퀀스르 특정 단위로 슬라이싱

`[index start : index stop]` : `start` ~ `stop-1`까지

- 시퀀스를 K 간격으로 슬라이싱

`[index start : index stop : index step]`

```python
print([1, 2, 3][:2]) # [1, 2]
print('abcd'[2:4]) # 'cd'
print(range(10)[1:5:3]) # range(1, 5, 3)
```

- `[::-1]` : 거꾸로 나열
- `[:]` : 전체

---

### Set 셋 : 집합

: 중복되는 요소 업이 순서에 상관 없는 데이터들의 묶음

- **순서가 없어 인덱스를 이욯나 접근 불가**
- 집합 연산 가능
- 중복된 값 존재하지 않음
- *mutable* 자료형
- `set()` or `{}`
    
    : 빈 Set을 만드려면 `set()`을 활용해야 함
    
- 연산자
    - `|` 합집합
    - `&` 교집합
    - `-` 차집합
    - `^` 대칭차집합 : 합집합 - 교집합

---

### 딕셔너리

: `키(key)-값(value)` 쌍으로 이뤄진 자료형

: 3.7 이상부터 ordered로 바뀜 !

`ordered dict` : 확실하게 순서 보장받고 싶을 때 쓰는 자료형

- `Key`는 변경 불가능한 데이터만 활용 가능
    - string, integer, float, boolean, tuple, range
- 각 키의 값 `values`
    - 어떤 형태든 노상관
- `{key : value}` or `dict(key : value)` 로 생성
- **key 를 통해 value에 접근**
    - `.keys()`
    - `.values()`
    - `.items()`

---

### 형변환(Typecasting)

- 암시적 형 변환(Implicit) **BUT 반드시 명시적 형 변환으로 작성해야함 !!**
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형 변환
        - bool
        - Numeric type(int, float)
        
        ```python
        print(True + 3) # 4
        print(3 + 5.0) # 8.0
        ```
        
- 명시적 형 변환(Explicit)
    - 사용자가 특정 함수를 활용해 의도적으로 자료형 변환
        - `int()`
        - `str()` int, float, list, tuple, dict ⇒ str
        - `float()` **float 형식이 아닌 경우 타입 변환 불가** ex) 3/4