## 객체지향 프로그래밍 OOP

#### **Object-Oriented Programming**

- 컴퓨터 프로그래밍 방법론(패러다임) 중 하나
- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위, 객체 간의 상호작용으로 파악

### Object

#### 과거 | 절차지향 프로그래밍

- 하나를 바꾸면 연달아서 바꿔야 해서 문제가 많이 발생

#### 현재 | 객체지향 프로그래밍

- Object 간 상호작용
  - data → methods
- 장점
  - 클래스 단위로 모듈화시켜 개발 가능 ⇒ 대규모 소프트웨어 개발에 적합
  - 필요한 부분만 수정 가능 ⇒ 프로그램 유지보수 용이
- 단점
  - 설계시 많은 시간과 노력 필요
    - 다양한 객체의 상호 작용 구조를 만들어야 하기 때문에
  - 실행 속도가 상대적으로 느림
    - 절차 지향 프로그래밍이 컴퓨터의 처리 구조와 비슷해 실행 속도가 빠름

### 객체(컴퓨터 과학)

: 속성과 행동으로 구성된 모든 것

속성(정보) + 행동(동작)

변수 + 함수-메서드

변수, 자료 구조, 함수, 메서드가 될 수 있다

### 객체와 인스턴스

: 클래스로 만든 객체를 인스턴스라고도 함

- 객체는 **특정 타입/특정 클래스**의 인스턴스

- **클래스**(가수라는 개념)와 **객체**(실제 사례)

```python
[3,2,1].sort() == 객체.행동()
```

```python
[1,2,3], [1], [], ['hi']
# 모두 리스트 타입(클래스)의 객체

", 'hi', '파이썬'
# 모두 문자열 타입(클래스)의 객체
```

### 객체(Object)

- 타입(Type) : 어떤 연산자(operator)와 조작(method)이 가능한다?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
- **객체 = 속성(attribute) + 기능(method)**

```python
123, 900, 5는 int의 인스턴스
'hello', 'bye'는 모두 string의 인스턴스
[2322, 89, 1], []은 모두 list의 인스턴스
```

---

### 기본 문법

- 클래스 정의 `Class MyClass:`
- 인스턴스 생성 `my_instance = MyClass()`
- 메서드 호출 `my_instance.my_method()`
- 속성 `my_instance.my_attribute`

### 클래스와 인스턴스

- 객체의 설계도(클래스)를 가지고, 객체(인스턴스)를 생성
- 클래스 : 객체의 분류, 설계도, **클래스 이름은 반드시 대문자로 시작**
- 인스턴스 : 하나하나의 실체, 예

### 객체 비교하기

#### `==`

- `equal`
- **값이 같은 경우** `True`
- 같아 보이지만 실제로 동일한 대상을 가리키고 있는 것은 아님

#### `is`

- `identical`
- **같은 메모리 주소를 share하는 경우** `True`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a==b, a is b) # True False

a = [1, 2, 3]
b = a
print( a==b, a is b) #  True True
```

### OOP 속성

- 특정 데이터 타입/클래스 객체들이 가지게 될 상태/데이터를 의미
- **클래스 변수** : 공유하는 성질
- **인스턴스 변수** : 각자 unique한 성질(ex. 이름)

```python
class Person:
	blood_color = 'red' # 클래스 변수
	population = 100 # 클래스 변수

	def __init__(self, name):
		self.name = name # 인스턴스 변수

person1 = Person('지민')
print(person1.name) # 지민
```

### 인스턴스 변수

- **각 인스턴스가 가지는 변수**
- 생성자 메서드 `__init__` 에서 `self.<name>` 으로 정의
- 인스턴스가 생성된 이후 `<instance>.<name>` 으로 접근 및 할당

```python
class Person:

	def __init__(self, name):
		self.name = name # 인스턴스 변수

john = Person('지민') # 인스턴스 변수 접근 및 할당
print(person1.name) # 지민
```

⇒`self`는 자동으로 들어가서 name하나만 넣어도 됨

### 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값
- ex. 사용자가 몇 명인지 확인하고 싶을 때
- `<classname>.<name>` 으로 접근 및 할당

```python
class Circle():
	pi = 3.14 # 클래스 변수 정의

	def __init__(self, name):
		self.name = name # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 3.14

# 인스턴스가 안에 없으면 위로 올라감 ⇒ 그래서 pi 출력 가능한 것
```

- 클래스 변수를 변경할 때는 `클래스.클래스변수` 형식으로 변경

```python
c2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi) # 3.14 클래스 변수
print(c1.pi) # 3.14 클래스 변수
print(c2.pi) # 5 새로운 인스턴스 변수 생성
```
---
## OOP 메서드

- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 클래스 안에 있는 함수

`인스턴스 메서드` : 인스턴스 처리

`@클래스메서드` : 클래스 처리

`@정적메서드`: 나머지 처리

```python
class Person:
	def talk(self):
		print('안녕')

	def talk(self, food):
		print(f'{food}를 냠냠')

person1 = Person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
```

### 인스턴스 메서드

- **호출 시 ,첫번 째 인자로 인스턴스 자기자신 `self` 전달**
- `self` 가 있으면 인스턴스 메서드
  - `self` : 인스턴스 자기 자신
  - 인스턴스 메서드 호출 시 매개변수 이름으로 `self` 를 첫 번째 인자로 정의
    - 파이썬 암묵적 규칙

### 생성자(constructor) 메서드

- 인스턴스 객체가 **생성**될 때 자동으로 호출되는 메서드
  - 인스턴스 생성
  - `__init__` 메서드 자동 호출

```python
class Person:

	def __init__(self, name):
		print('인스턴스가 생성되었습니다.')

person1 = Person() # 인스턴스가 생성되었습니다.
```

### 매직 메서드

- Double underscore `__` 가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에서 자동으로 불리는 메서드
- 예시
  - `__str__` 클래스를 출력했을 때 `return`할 값 지정
	- 어떤 인스턴스를 출력하면 `__str__` 의 `return` 값이 출력
  - `__gt__` 부등호 연산자(>, greater than)

```python
class Circle:

	def __init__(self, r): # self에는 인스턴스 변수 자체가 넘어감
		self.r = r 

	def area(self):
		return 3.14 * self * self.r

	def __str__(self):
		return f'[원] radius: {self.r}'

	def __gt__(self, other):
		return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

print(c1) # [원] radius : 10
print(c2) # [원] radius : 1
print(c1 > c2) # True
```

#### `__str__`

- 해당 객체의 출력 형태를 임의로 지정하고 싶을 때
- 프린트 함수를 호출할 때, `__str__`의 `return` 값 출력

```python
class Frozen:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'{self.name} says \'I like warm hugs:)\''

olaf = Frozen('Olaf')
print(olaf) # Olaf says 'I like warm hugs:_'
```

#### `__repr__`

- 어떤 객체의 pintable representation을 문자열의 형태로 반환

```python
import math

repr(3) # '3'
repr(math) #"<module 'math' from ...>"
```

##### 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드

```python
class Person:

	def __del__(self):
		print('인스턴스가 사라졌습니다.')

person1 = Person()
del person1 # 인스턴스가 사라졌습니다.
```

### 클래스 메서드

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터 사용해 정의
- 호출 시, 첫 번째 인자로 클래스 `cls`가 전달
- `cls` 매개 변수를 통해 클래스 조작

```python
class Person:
	count = 0 # 클래스 변수
	def __init__(self): # 인스턴스 변수 설정
		self.name = name
		Person.count += 1

	@classmethod
	def number_of_population(cls): # 클래스 자체가 넘어옴
		print(f'인구수 {cls.count}입니다.')

person1 = Person('아이유')
print(Person.count) # 인구수 1입니다.

```

---

### 데코레이터

- 함수를 어떤 함수로 꾸며서 `return`
- `@데코레이터(함수명)` 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요
- 데코리이터를 활용하면 쉽게 여러 함수를 원하는대로 변경할 수 있음

```python
def add_print(original): # 파라미터로 함수 받기
	def wrapper(): # 들어온 함수 꾸며주는 함수
		print('start') # 부가기능 -> original을 꾸민다
		original()
		print('end') # 부가기능 -> original을 꾸민다
	return wrapper # wrapper 함수 리턴

@add_print
def print_hello():
	print('hello') # print 함수 original로 넘어감

print_hello() # wrapper가 실행됨
# start
# hello
# end
```

### 클래스 메서드와 인스턴스 메서드

- 클래스 메서드 ⇒ 클래스 변수 사용
- 인스턴스 메서드 ⇒ 인스턴스 변수 사용
- What if 클래스 변수, 인스턴스 변수 모두 사용하고 싶을 때?
  - **인스턴스 메서드는 둘 다 사용 가능!**

### 스태틱 메서드

- 인스턴스 변수, 클래식 변수를 다루지 않는 메서드
- 언제 사용?
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용
  - 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우
    - **객체 상태나 클래스 상태를 수정할 수 없음**
- `@staticmethod` 데코레이터를 사용해 정의
- 일반 함수처럼 동작하지만 클래스 이름 공간에 귀속
  - 주로 해당 클래스로 한정하는 용도로 사용

```python
class Person:

	def __init__(self,name):
		self.name = name
		Person.count += 1

@staticmethod
def check_rich(money) # 스태틱은 cls, self 사용 X
	return money > 10000

person1 = Person('아이유')
# 하나의 클래스에 종속시키고 싶을 때 이용
print(Person.check_rich(1000000)) # True : 스태틱은 클래스로 접근 가능
print(person1.check_rich(200000)) # True : 스태틱은 인스턴스로 접근 가능
```

### 인스턴스와 클래스 간의 이름공간(namespace)

- 클래스 정의 시 클래스와 해당하는 이름 공간 생성
- 인스턴스 만들면 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면 인스턴스-클래스 순으로 탐색

```python
class Person:
	name = 'unknown'

	def talk(self):
		print(self.name)

p1 = Person()
p1.talk() # unknown
# p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수 unknown이 출력됨

p2 = Person()
p2.name = 'Kim'
p2.talk() # Kim
# p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)가 출력됨

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim
```

## 객체지향 핵심 4가지

### 추상화 (변수, 함수, 클래스)

- 현실 세계를 프로그램 세계에 반영
- 복잡한 것은 숨기고, 필요한 것만 드러내기

### 상속

- 두 클래스 사이 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능함
  - 모든 파이썬 클래스는 object를 상속 받음

```python
class ChildClass(ParentClass):
```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성 증가

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self): # 메서드 재사용
		print('반갑습니다. {self.name}입니다.')

class Professor(Person): # Person 클래스 상속
	def __init__(self, name, age, department):
		self.name = name
		self.age = age
		self.department = department

class Student(Person):
	def __init__(self, name, age, gpa):
			self.name = name
			self.age = age
			self.gpa = gpa

p1 = Professor('Lee', 45, 'Computer Science')
s1 = Student('Kim', 23, 3.5)

# 부모 Person 클래스의 talk 메서드 활용
p1.talk() # 반갑습니다. Lee입니다.
s1.talk() # 반갑습니다. Kim입니다.
```

#### `isinstance(object, classinfo)`
  - classinfo의 instance거나 **subclass**인 경우 `True`

```python
class Person:
	pass

class Professor:
	pass

class Student:
	pass

p1.Professor()
s1.Student()

print(isinstance(p1, Person)) # Fasle
print(isinstance(s1, Person)) # False
```

```python
class Person:
	pass

class Professor(Person):
	pass

class Student(Person):
	pass

print(isinstance(p1, Person)) # True
print(isinstance(s1, Person)) # True
```

#### `issubclass(class, classinfo)`
  - class가 classinfo의 subclass면 `True`
#### `super()`
  - 자식 클래스에서 상속 받은 부모 클래스를 사용하고 싶은 경우

```python
class Person:
	def __init__(self, name, age, number, email):
		self.name = name
		self.age = age
		self.number = number
		self.email = email

class Student(Person):
	def __init__(self, name, age, number, email, student_id):
		# Person 클래스
		# 보통 생성자 안에 많이 적음
		super().__init__(name, age, number, email)
		self.student_id = student_id
```

---

### 상속 정리

- 부모 클래스의 모든 요소가 상속
- `super()` 를 통해 부모 클래스의 요소 사용 가능
- `메서드 오버라이딩`을 통해 자식 클래스에 재정의 가능
- 상속 관계에서 이름 공간은 `인스턴스 > 자식 클래스 > 부모 클래스` 순으로 탐색
- `mro` 메서드 (Method Resolution Order)
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는 확인
  - `인스턴스 > 자식 클래스 > 부모 클래스`로 확장

---

### 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소 활용 가능
- 중복된 속성이나 매서드가 있는 경우 **상속 순서에 의해 결정**

```python
class Person:

	def __init__(self,name):
		self.name = name

	def greeting(self):
		return f'Hi, {self.name}'

class Mom(Person):
	gene = 'XX'

	def swim(self):
		return 'Mom is swimming'

class Dad(Person):
	gene = 'XY'

	def walk(self):
		return 'Dad is walking'

class FirstChild(Dad, Mom):
# Dad 클래스가 먼저 상속되었으므로
# font-family 같이 선례한 클래스에 없으면 다음으로, 그 다음으로
	def swim(self):
		return 'FirstChild is swimming' # Mom 메서드 오버라이딩

	def cry(self):
		return 'FirstChild is crying'

baby1 = FirstChild('baby')
print(baby1.cry()) # FirstChild is crying
print(baby1.swim()) # FirstChild is swimming
# Dad 클래스의 속성 출력
print(baby.walk()) # Dad is walking
print(baby.gene) # XY
```

---

### 다형성 (Polymorphism)

- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음
- 서로 다른 클래스에 속하는 객체들이 **동일한 메세지에 대해 다른 방식으로 응답**할 수 있음

#### 매서드 오버라이딩

- 상속받은 메서드를 `재정의`
- 부모 클래스 메서드의 이름과 기본 기능은 그대로 사용하지만, **특정 기능을 바꾸고 싶을 때** 사용
  - 상속 받은 클래스에서 같은 이름의 메서드로 덮어씀
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 `super` 활용

---

### 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스를 차단 == 민감한 정보 숨기는 것
  - ex. 주민번호
- 공식적으로는 존재하지 않음, 암묵적으로 존재
#### **Public Access Modifier**
  - 언더바 없이 시작하는 메서드나 속성
  - 클래서 외부에서 언제, 누구든 호출이 가능, 하위 클래스 오버라이딩 허용
  
#### **Protected Access Modifier**
  - 언더바 1개로 시작하는 메서드나 속성
  - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
  - 하위클래스 override 허용
	- 클래스 외부에서 수정 불가(하지만 python에서는 로직상 문제X)

#### **Private Access Modifier**
  - 언더바 2개로 시작하는 메서드나 속성
  - 본 클래스 내부에서만 사용 가능 **외부에서 접근 및 수정 절대 불가**
  - 하위클래스 상속 및 호출 불가능 `오류`
  - 외부 호출 불가능 `오류`
	
#### `getter` `setter` 메서드 (다이렉트로 데이터에 접근하는 것을 막기위해)
  - 변수에 접근할 수 있는 메서드 별도 생성
    - `getter` 변수 값을 읽는 메서드
      - `@property` 데코레이터 사용
    - `setter` 변수 값 설정
      - `@변수.setter` 사용

```python
class Person:
	def __init__(self, age):
		self.age_age = age # Protected Access Modifier

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, new_age):
		if new_age <= 19:
			raise ValueError('Too Young!!')
			return

		self._age = new_age

p1 = Person(20)
print(p1.age) # 20

p1.age = 33
print(p1.age) # 33

p1.age = 19
print(p1.age) # ValueError : Too Young!!

# 나이가 19 이하면 안된다는 조건이 하나 걸려있기 때문에
# 19이하인 값으로 변경하면 오류 발생
```
