# 모듈과 패키지

### 모듈

: 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

### 패키지

: 특정 기능과 관련된 여러 모듈의 집합

: 패키지 안에는 또 다른 서브 패키지 존재

#### 가상환경
: 버전 관리를 하는 곳
- 하나의 컴퓨터 안에 여러 공간을 만듦
  - A라면 => a, B라면 => b

### 모듈과 패키지 불러오기

- `import` module
  - `modle.var` `modul.function` 으로 사용
  - `import` module `as name`
    - 모듈 이름이 너무 길 경우 `as name` 처럼 임의로 이름을 붙여서 간단하게 콜
- `from` module `import` var, function, Class
  - `var()` `function()`로 사용
- `from` module `import*` : 모듈 내 모든 함수 (or 변수) 가져오기
  - `var()` `function()`로 사용
- `from` package `import` module
- `from` package.module `import` var, function, Class

### 파이썬 표준 라이브러리

파이썬에 기본적으로 설치된 모듈과 내장 함수

[https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

### 파이썬 패키지 관리자 (pip)

PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 최신 / 특정 / 최소 버전 명시하여 설치 가능
- 이미 설치 되어 있는 경우 설치됨을 알리고 아무 것도 하지 않음
  `$ pip install SomePackage`
  `$ pip install SomePackage==1.0.5`
  `$ pip install SomePackage>=1.0.4'`
- 패키지 삭제
  - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동으로 지워줌
    `$ pip uninstall SomePackage`
- 패키지 목록 및 특정 패키지 정보
  `$ pip list`
  `$ pip show SomePackage`
- 패키지 관리하기
  - 아래 명령어를 통해 패키지 목록을 관리(1)하고 설치(2)할 수 있음
  - 일반적으로 패키지를 기록하는 파일의 이름은 `requirements.txt` 로 정함
    `$ pip freeze > requirements.txt`
    `$ pip install -r requirements.txt`

### 사용자 패키지

`__init__.py` : 파이썬 3.3 부터는 없어도 자동으로 패키지로 인식하지만 하위버전 호환을 위해