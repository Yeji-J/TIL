# 함수

특정 기능을 하는 코드의 조각(묶음) ⇒ 필요시 호출하여 간편히 사용 가능

## 함수 종류

- 내장함수 : 파이썬에 기본적으로 포함된 함수
- 외장함수 : `import` 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
- 사용자 정의 함수 : 직접 사용자가 만드는 함수

## 함수 기본 구조

### 선언과 호출 (Define & Call)

- 선언은 `def` 키워드 활용
- `함수명()` 호출
  - parameter가 있는 경우 `함수명(parameter)`
- 함수는 parameter을 넘겨줄 수 있음
- 동작 후에 `return` 을 통해 결과값 전달

```python
def first_function(parameter):
	# code block
	return returning_value
```

- 문서화 (Docstring)
- 범위 ( Scope)

### 결과값 (Output)

- Void function : 명시적인 return 값이 없는 경우, `None` 을 반환하고 종료
  ```python
  print('hello python')
  ```
- Value returning function : 값 반환 후 함수 종료
  ```python
  foat('3.21')
  ```

---

**주의! print | return**

- print 함수와 return의 차이점

  - print를 사용하면 호출될 때마다 값이 출력됨 (주로 테스트를 위해 사용)
  - 데이터 처리를 위해서는 return 사용

  ```python
  # Void Function
  def void_product(x, y):
  	print(x*y)

  ans = void_product(3, 5):
  print(ans) # None
  ```

  ```python
  # Value Returning Function
  def value_returning_product(x, y):
  	return x * y

  ans = void_product(3, 5):
  print(ans) # 15
  ```

⇒ `Jupyte`r와 같은 REPL(Read-Eval_Loop) 환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 **같은 동작을 하는 것을 착가할 수 있으니 주의** !!

---

### Q. 두 개 이상의 값을 반환하려면?

: return은 항상 하나의 값 만을 반환 → 두 개의 값을 반환하고 싶을 땐?

- **튜플을 활용해 두 개 이상의 값 반환**

```python
def minus_and_product(x, y):
	return x-y, x * y

y = minus_and_product(4, 5)
print(y) # (-1, 20)
print(type(y)) <class 'tuple'>
```

---

**To sum up …**

- `return` X → `None`
- `return` 0 → **하나를 반환**

                       → **여러 개**를 원하면 **튜플 혹은 리스트와 같은 컨테이너 활용**

---

### 함수의 입력 Input

`Parameter` : 함수를 **정의**할 때 함수 내부에서 사용되는 변수

`Argument` : 함수를 **호출**할 때 넣어주는 값

- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argument는 소괄호 안에 할당 `function(argument)`
  - 필수 Argument : 반드시 전달되어야 하는 값
  - 선택 Argumetnt : 값을 전달하지 않아도 되는 경우는 기본값이 전달됨
- **Positional Arguments : 기본!!**
  : **기본적으로** 함수 호출 시 Argument는 **위치에 따라 함수 내에 전달**됨

  ```python
  def add(x, y):
  	 return x + y

  add(2, 3) # x = 2, y = 3
  ```

- **Keyword Arguments**
  : 직접 변수의 이름으로 특정 Argument 전달 가능
  : **Keyword Argument 다음에 Positional Arugment를 활용할 수 없음**

  ```python
  def add(x, y):
  	return x + y

  add(x = 2, y = 5)
  add(2, y = 5)
  **add (x, y = 5) # Error !!**
  ```

- **Default Arguments Values**
  : **기본값을 지정**하여 함수 호출 시 Argument 값을 설정하지 않도록 함
  : 정의된 것보다 더 적은 개수의 Argument로 호출될 수 있음

  ```python
  def add(x, y = 0):
  	return x + y

  add(2) # y는 미리 지정됨
  ```

- 정해지지 않은 여러개의 Arguments 처리

  - `**print()` : `애스터리스크(Asterisk)` 혹은 언패킹 연산자로 불리는 `*` 덕분 !\*\*
  - 가변 인자 만들기 가능

  ```python
  print('you', 'are', 'cute')
  # youarecute

  def func(*args):
  	print(args)

  func(1, 2, 3, 'a') # (1, 2, 3, 'a') # 튜플로 반환
  # 언패킹시 리스트로 반환
  ```

- **가변인자 `*args`**
  : 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  : 몇 개의 Pisitional Argument를 받을지 모르는 함수를 정의할 때 유용
  ***
  **To understand what 가변인자 is …**
  - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
  ```python
  numbers = (1, 2, 3, 4, 5)
  print(numbers)
  ```
  - 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
    - 언패킹시 변수의 개수와 할당하고자 하는 요소의 개수가 동일해야 함
    - **언패킹시 왼쪽의 변수에 `asterisk(*)` 를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음**
  ```python
  numbers = (1, 2, 3, 4, 5)
  a, b, c, d, e = numbers # 언패킹
  print(a, b, c, d, e)
  ```
  ```python
  numbers = (1, 2, 3, 4, 5)
  **a, *rest, b = numbers # asterisk(*)**
  # a = 1 b = 5 rest = [2, 3, 4]
  ```
  ***
- 가변인자 예시

  ```python
  def sum_all(*nums):
  	result = 0
  	for num in nums:
  		result += num
  	return result

  print(sum_all(1,2,3)) # 6
  ```

  ```python
  def print_family_name(father, mother, *pets): # father, mother는 필수 입력
  	print(father)
  	print(mother)
  	for name in pets:
  		print(name)

  print_family_name('아부지', '어무니', '멍멍이', '냥냥이')
  ```

- **가변 키워드 인자 `(**kwargs)`\*\*

  - **딕셔너리**로 묶여 처리되며, parameter에 `**` 를 붙여 표현

  ```python
  def family(**kwargs):
  	for key, value in kwargs.items():
  		print(key, value)

  family(father = '아부지', mother='어무니', baby ='아기')
  # 문자열로 쓰면 안됨!
  ```

  ```python
  def print_family_name(father, mother, **pets):
  	print('father :', father)
  	print('mother :', mother)
  	if pets: # pet 의 값이 있다면 (없으면empty로 Falsy 처리 되니까 실행 X)
  		print('pets :')
  		for species, name in pets.items():
  			print(f'{species} : {name}')

  print_family_name('john', 'daisy', dog = 'tom', cat = 'cathy')
  ```

- **가변 인자 `(*args)`와* 가변 키워드`*(**kwargs)` 인자 동시 사용 가능\*\*

  ```python
  def print_family_name(*parents, **pets):
  	print('father :', parents[0])
  	print('mother :', parents[1])
  	if pets:
  		print('pets :')
  		for species, name in pets.items():
  			print(f'{species} : {name}')

  print_family_name('john', 'daisy', dog = 'tom', cat = 'cathy')
  ```

---

### Python의 범위 (Scope)

함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

### 변수 수명 주기(Life Cyle)

: 변수는 각자 수명주기가 존재

- built-in- scope
  - 파이썬이 실행된 이후부터 영원히 유지
- global scope
  - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
- local scope
  - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution) - `LEGB Rule`

- `Local Scope` : 현재 작업 중인 범위
- `Enclosed Scope`
- `Global Scope` : 최상단에 위치한 범위
- `Built-in Scope` : 정의하지 않고 사용할 수 있는 모든 것 ex) `print()`

⇒ 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음 !

![Untitled](python.assets/scope)

```python
a = 0
b = 1
def enclsoed():
	a = 10
	c = 3
	def local(c):
		print(a, b, c) # 10 1 300
	local(300)
	print(a, b, c) # 10 1 3

enclosed()
print(a, b) # 0 1
```

1. `Global Scope` : 현재 코드 블록 전체에 적용

```python
a = 10
def func1():
	global a
	a = 3 # Local Scope에서 Global 변수 값 변경

print(a) # 10
func1()
print(a) # 3
```

```python
# Global 관련 Error
a = 10
def func1():
	print(a) # global a 선언 전에 사용
	global a
	a = 3

# SyntaxError: name 'a' is used prior to global declaration
```

1. `nonlocal` : global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함

   - global과 달리 이미 존재하는 이름과의 연결만 가능

   ```python
   x = 0
   def func1():
   	x = 1
   	def func2():
   		nonlocal x
   		x = 2
   	func2()
   	print(x) # 2

   func1()
   print(x) # 0
   ```

---

**함수의 범위** **주의 !**

1. 해당 scope에 변수가 없는 경우 LEGB Rule에 의해 이름 검색
   1. 변수 접근은 가능 but 해당 변수 수정 불가
   2. 값을 할당하는 경우 해당 scope의 이름 공간에 새롭게 생성되기 때문
   3. **함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것!**
2. 상위 scope에 있는 변수를 수정하고 싶다면 `gloabl` `nonlocal` 키워드 활용
   1. 코드가 복잡해지면 변수 변경 추척이 어렵고 오류 발생 가능성 상승
   2. 사용을 지양하는 것을 권장, **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하기**

## 함수 응용

### 내장함수 (Built-in Functions)

`map(function, iterable)`

: 순회 가능한 데이터 구조의 모든 요소에 함수 적용 ⇒ 결과 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(list(result)) # ['1', '2', '3']
```

`filter(function, iterable)`

: 결과가 True인 것을 filter object로 반환

```python
def odd(n):
	return n % 2

numbers = [1, 2, 3]
result = filter(odd, numbers)
print(list(result)) # [1, 3]
```

`zip(*iterables)`

: 복수의 iterable을 모야 **튜플**을 원소로 하는 zip object 반환

```python
girls = ['yeji', 'jane']
boys = ['david', 'ross']
pair = zip(girls, boys)
print(list(pair)) # [('yeji', 'david'), ('ashely', 'eric')]
```

`lambda[parameter]:표현식`

: 표현식을 계산한 결과값 반환, 이름이 없는 익명 함수

- return 문을 가질 수 없음
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 함수를 정의해 사용하는 것보다 간결함
- `def` 를 사용할 수 없는 곳에서도 사용 가능

```python
def triangle(b, h):
	return 0.5 * b * h

triangle = lambda b, h : 0.5 * b * h
print(triangle(5,6)) # 15.0
```

`recursive function` : 재귀함수

: 자기 자신을 호출하는 함수

- 무한한 호출이 목표가 아님
  - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음
  - 변수의 사용이 줄어들고 코드 가독성 증가
- 1개 이상의 base case (종료되는 상황)이 존재, 수렴하도록 작성

```python
# Factorial

def factorial(n):
	if n == 0 or n ==1:
		return 1 # f(1) base case
	else:
		return n * factorial(n-1)

print(factorial(4)) $ 24
```

- 메모리 스택이 넘치게 되면 프로그램 동작 불가
- 파이썬의 최대 재귀 깊이는 1000번으로, 호출 횟수가 이를 넘어가면 `Recursion Error` 발생
