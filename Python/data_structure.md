# Data Structure

- 데이터 구조를 활용하기 위해 `메서드(method)` 활용

- 메서드는 클래스 내부에 정의한 함수

**`데이터구조`.`메서드()`** 형태로 활용!

`str.replace`(**old** , **new** , **[count]**)
=> old, new는 필수 count는 선택전 인자 의미

### 순서가 있는 데이터 구조

#### 문자열(String)

모든 문자는 `immutable`

#### `.find(x)`

: x의 **첫 번째 위치**를 반환, 없으면 -1을 반환 (오류가 나지 않음)

⇒ **프로그램 그대로 진행**

```python
print('apple'.find('p')) # 1
print('apple'.find('k')) # -1
```

#### `.index(x)`

: x의 첫번째 위치를 반환, **없으면 오류 발생**

⇒ **프로그램 멈춤**

```python
print('apple'.index('p')) # 1
print('apple'.index('k')) # ValueError: substring not found
```

#### `.isalpha()`

: 알파벳 문자 여부 (단순 알파벳이 아닌 유니코드 상 letter) **숫자냐 문자냐의 차이**

```python
print('abc'.isalpha()) # True
```

#### `.isupper()`

: 대문자 여부

```python
print('Ab'.isupper()) # False
```

#### `.islower()`

: 소문자 여부

```python
print('ab'.islower()) # True
```

#### `.istitle()`

: 타이틀 형식 여부
: to check if each word starts with an upper case letter

```python
print('Title Title!'.istitle()) # True
```

---

### 문자열 관련 검증 메서드

#### `.isdecimal()`

: 문자열이 `int`로 반환 가능한지

#### `.isdigit()`

: 숫자처럼 생긴 모든 글자에 `True` 반환

#### `.isnumeric()`

: 숫자값 표현에 해당하는 문자열 인정. 분수, 거듭제곱, 특수문자 `True` 반환

---

### 문자열 변경 메서드

#### Q. 문자열은 `immutable`인데, 문자열 변경이 돼?

- 기존 문자열을 변경하는 것이 아니라, **변경된 문자열을 새롭게 만들어서 반환**하는 것 !

#### `.replace(old, new [,count])`

: 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
: count 지정 시 해당 갯수만큼만 시행

```python
print('coone'.replace('o','a')) # caane
print('woowoo'.replace('o','!',2)) # w!!woo
```

#### `.strip([chars])`

: 공백이나 특정 문자를 제거

- `strip` 양쪽 제거
- `lstrip` 왼쪽 제거
- `rstrip` 오른쪽 제거
  : 문자열을 지정하지 않을 시 공백을 제거

```python
print('    WOW!'.strip()) # 'WOW!'
print('    WOW!'.rstrip()) # '    WOW!'
print('WOW!!!!!'.strip('!')) # 'WOW'
```

#### `.split(sep=None, maxsplit=-1)`

: 문자열을 특정 단위로 나눠 리스트로 반환

- sep = None 혹은 지정되지 않을 시 연속된 공백문자를 단일한 공백문자로 간주하고 선행/후행 공백은 빈 문자열에 포함시키지 않음
- maxsplit이 -1인 경우에는 제한이 없음

```python
print('a,b,c'.split('_')) # ['a,b,c']
print('a,b,c'.split()) # ['a', 'b', 'c']
```

#### `'separator'.join([iterable])`

: 반복가능한 요소를 separator로 합쳐 문자열 반환
: iterable에 문자열이 아닌 값이 있으면 `TypeError` 발생

```python
print('!'.joing('yeji')) # 'y!e!j!i!'
```

#### `.capitalize()`

: 가장 첫 번째 글자를 대문자로 변경

#### `.title()`

: 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자, 나머지는 소문자로 변환

#### `.upper()`

: 대문자로 변환

#### `.lower()`

: 소문자로 변환

#### `.swapcase()`

: 대문자와 소문자 서로 변환

```python
print('I Like Warm Hugs'.swapcase()) # i lIKE wARM hUGS
```

---

### 리스트 메서드

#### `.append(x)`

: 리스트 마지막에 항목 x 추가

#### `.insert(i, x)`

: 리스트 인덱스 i에 항목 x 삽입
: `i`가 리스트 길이보다 큰 경우 맨 뒤에 삽입

```python
InandOut = ['burger', 'coke', 'french fries']
InandOut.insert(0, 'sprite')
print(InandOut) # ['sprite', 'burger', 'coke', 'frech fries']
```

#### `.remove(x)`

: 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
: 항목이 존재하지 않을 경우, `ValueError`

```python
nums = [1, 2, 3, 'hi']
nums.remove('hi')
print(nums) # [1, 2, 3]

nums.remove('hi') # ValueError: list.remove('hi'): 'hi' not in list
```

#### `.clear()`

: 모든 값 삭제

#### `.pop(i)`

: 정해진 위치 `i`에 있는 값 삭제, 그 항목 반환
: `i`가 정해지지 않으면 마지막 항목 삭제 후 반환

```python
nums = ['hi', 1, 2, 3]
nums.pop()
print(nums) # ['hi',1,2]

nums.pop(0)
print(nums) # [1,2]
```

#### `.extend(m)`

: 리스트에 iterable 항목 추가 (+=)

```python
InandOut = ['burger', 'coke', 'french fries']
InandOut.extend(['bigMac'])
print(InandOut) # ['burger', 'coke', 'french fries', 'bigMac']

InandOut.extend('fanta')
print(InandOut) # ['burger', 'coke', 'french fries', 'bigMac', 'f', 'a', 'n', 't', 'a']
```

#### `.index(x)`

: x 값을 찾아 해당 index 값을 반환
: 없는 경우 `ValueError`

```python
nums = [1, 2, 3, 4]
print(nums.index(3)) # 2
print(nums.index(5)) # ValueError: 5 is not in list
```

#### `.reverse()`

: 순서를 반대로 뒤집음 (정렬 X)

```python
nums = [2,4,6,3]
new_nums = nums.reverse()
print(nums, new_nums) # [2,4,6,3] None
```

#### `.sort()`

: 리스트를 정렬, `None` 반환

```python
nums = [2,3,4,5]
new_nums = nums.sort()
print(nums, new_nums) # [2,3,4,5] None
```

#### `.sorted()`

: 리스트 정렬 후 반환

```python
nums = [2,3,6,1]
print(sorted(nums)) # [1,2,3,6]
```

#### `.count(x)`

: 리스트 내 x의 개수 반환

---

### 튜플 메서드

- 튜플은 값을 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원
- 리스트 메서드 중 항목을 변경하는 메서드를 제외하고 대부분 동일

---

## 비시퀀스형 데이터 구조

### 셋 메서드

- **순서가 없기 때문에 인덱스를 이용해 접근 불가**
- mutable

#### `.copy()`

셋의 얕은 복사본을 반환

#### `.add(x)`

: 셋에 값을 추가

#### `.pop()`

: 임의의 원소를 제거해 반환 (순서 x)
: set이 비어있을 경우, `Key Error`

```python
fruits = {'banana', 'apple', 'peach'}
fruits.pop()
print(fruits) # {'apple', 'banana'}
```

#### `.remove(x)`

: x를 셋에서 삭제
: x가 존재하지 않을 경우 `KeyError`

#### `.discard(x)`

: x가 셋에 있는 경우 x를 삭제
: x가 존재하지 않아도 에러가 발생하지 않음

#### `.update(*others)`

: 기존 셋에 없는 여러 값을 추가

```python
fruits = {'apple', 'banana', 'kiwi'}
fruits.update({'grape', 'strawberry'})
print(fruits) # {'apple', 'banana', 'grape', 'strawberry', 'kiwi}
```

#### `.clear()`

: 모든 항목을 제거

#### `set.isdisjoint(t)`

: 셋 set가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우 True 반환 **(서로소)**

#### `set.issubset(t)`

: 셋 set가 셋 t의 하위 셋인 경우 True 반환

#### `set.issuperset(t)`

: 셋 set가 셋 t의 상위 셋인 경우 True 반환

---

### 딕셔너리 메서드

#### `.clear()`

: 모든 항목 제거

#### `.copy()`

: 딕셔너리의 얕은 복사본을 반환

#### `.keys()`

: 딕셔너리의 모든 키를 담은 뷰 반환

#### `.values()`

: 딕셔너리의 모든 값을 담은 뷰 반환

#### `.items()`

: 딕셔너리의 모든 키-값 쌍을 담은 뷰 반환

#### `.get(k[,default])`

: 키 `k`의 값을 반환, 키 `k`가 딕셔너리에 없을 경우 `None`을 반환
: default 값 설정 가능(defaul = `None`)

```python
fruits = {'apple':'red', 'banana':'yellow'}
print(fruits.get('pineapple')) # None
print(fruits.get('peach', 'pink')) # pink
```

#### `.get(k, v)`

: 키 `k`의 값을 반환, 키 `k`가 딕셔너리에 없을 경우 `v`를 반환

#### `.pop(k[,default])`

: 키 `k` 값을 반환하고 `k` 항목을 딕셔너리에서 삭제,
: 키 `k`가 딕셔너리에 없을 경우 `KeyError` 발생

```python
fruits = {'apple':'red', 'banana':'yellow'}
print(fruits.pop('apple'), fruits) # red {'banana':'yellow'}
```

#### `.pop(k, v)`

: 키 `k` 값을 반환하고 `k` 항목을 딕셔너리에서 삭제,
: 키 `k`가 딕셔너리에 없을 경우 `v` 반환

#### `.update([other])`

: `key`, `value` 덮어쓰기

```python
fruits = {'apple':'red', 'banana':'yellow'}
fruits.update('apple'='green')
print(fruits) # {'apple':'green', 'banana':'yellow}
```

---

### 얕은 복사와 깊은 복사 (Shallow Copy & Deep Copy)

#### 할당(Assignment)

- 대입연산자 `=`
  - 대입 연산자를 통한 복사는 해당 객체에 대한 객체 참조를 복사
  - 값을 복사하는 것이 아니라 값을 담고 있는 주소를 share =>**같은 주소**
  - 따라서 원본의 값이 바뀌면 복사본의 값도 바뀜

```python
original = ['hi']
copied = original
print(original, copied) # ['hi'] ['hi']
```

#### 얕은 복사(Shallow Copy)

- `slice`연산자 활용
- 같은 원소를 가진 리스트지만 연산된 결과를 복사 => **다른 주소**
- 1차원 리스트에서만 적용

```python
original = [1,2,3,4]
copied = original[:]
print(original, copied) # [1,2,3,4] [1,2,3,4]
```

##### 얕은 복사 주의사항

- 복사하는 리스트의 원소가 주소를 참조하는 경우
- 2+ 차원 리스트를 `slice`한다면 원소가 리스트인 경우 다시 주소만을 참조 
=> 원본 값 변경시 복사본도 변경

```python
original = [[1,2],2,3,4]
copied = original[:]
original[0][0] = 3
print(original, copied) # [[3,2],2,3,4] [[3,2],2,3,4]
```

#### 깊은 복사 (Deep Copy)

- `copy` 모듈 사용

```python
import copy
original = [[1,2],2,3,4]
copied = copy.deepcopy(original)
original[0][0] = 3
print(original, copied) [[3,2],2,3,4] [[1,2],2,3,4]
```

- 데이터를 모아놓은 형태(ex. 리스트) => 데이터의 주소를 가리킴
- 일반적인 하나의 데이터 형태 => 값의 복사가 바로 일어남
