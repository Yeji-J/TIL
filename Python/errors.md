# Errors and Exceptions
## Errors
### 문법 에러(Syntax Error)
- `SyntaxError` 발생 시 프로그램이 실행되지 않음
- 파일이름, 줄번호, `^`문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 **가장 앞의 위치**를 가리키는 캐럿(caret) 기호 `^` 표시

`Invalid syntax` 문법 오류

`assing to literal` 잘못된 할당

`EOL` (End of Line) 

```python
print('hello
# SyntaxError: EOL while scanning string literal
```

`EOF` (End of File)

```python
print(
# SyntaxError: unexpected EOF while parsing
```

## 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면 **프로그램 실행을 멈춤**
- 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- `NameError` `TypeError` 등이 있음
- 모든 내장 예외는 `Exception Class` 를 상속 받아 이뤄짐
- 사용자 정의 예외를 만들어 관리 가능

`ZeroDivisonError` 0으로 나누려고 할 때

`NameError` namespace 상에 이름이 없는 경우

`TypeError`

```python
1 + '1' # 타입 불일치

divmod() # argument 누락

divmod(1, 2, 3) # argument 개수 초과

import random
random.sample(1,2) # argument type 불일치
```

`ValueError`

```python
int('3.5') # 타입은 올바르나 값이 적절하지 않는 경우
```

`IndexError` 인덱스가 존재하지 않거나 범위를 벗어나는 경우

`KeyError` 해당 키가 존재하지 않는 경우

`ModuleNotFoundError` import할 모듈이 존재하지 않는 경우

`ImportError` 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

`KeyboardInterrupt` 임의로 프로그램을 종료했을 때

- ex. 무한으로 도는 반복문의 경우 임의로 종료했을 때 뜸..!

`IndentationError` 들여쓰기가 적절하지 않은 경우

### 파이썬 내장 예외 (built-in-exceptions)

![](python.assets/exceptions)

### 예외 처리

`try` (statement)

- 오류가 발생할 가능성이 있는 코드 실행
- 예외가 발생되지 않으면,  except 없이 실행 종료

`except` (clause)

- 예외가 발생하면 except 절이 실행
- 예외 상황을 처리하느 코드르 받아서 적절한 조치를 취함

`else`

- try 문에서 예외가 발생하지 않으면 실행

`finally`

- 예외 발생 여부와 관계없이 항상 실행

```python
try:
	num = input('give me a number: ')
	print(int(num))
except ValueError: # 숫자를 입력하지 않았을 때
	print('I said a NUMBER!!!')

```

`as` 예외를 다른 이름에 대입

```python
try:
	num = input('give me a number: ')
	print(int(num))
except ValueError as err: # 숫자를 입력하지 않았을 때
	print(f'{err}, I said NUMBER!!!') 
# ValueError, I said NUMBER!!!
```

### 복수 예외 처리

```python
try:
	num = input('100으로 나눌 값 주렴 : ')
	print(100/int(num))
except (ValueError, ZeroDivisionError): # 숫자를 입력하지 않았을 때, 0을 입력했을 때
	print('제대로 입력해줘.') # 발생 가능한 에러를 모두 명시 

```

순차적으로 수행되기 때문에, **가장 작은 범주부터** 예외 처리를 해야함
#### `BaseExceiption`으로 처리를 해버리면 가장 큰 범주이기 때문에 어떤 에러가 발생했는지 알 수 없음