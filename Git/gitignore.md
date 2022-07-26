# Git Ignore
##### 이 파일만 빼고 git에 commit 해줘 !

#### Q. What if... password와 같이 중요한 데이터가 들어간 파일이 있으면 ?

`.gitignore` 에 해당 파일명을 작성하면 자동으로 git에서 제외하고 commit

1. 개별 파일 ignore 가능

![Untitled](GIT.assets/ignore1)

2. `*.확장자` 로 해당 파일 종류 모두 ignore

![Untitled](GIT.assets/ignore2)

3. 특정 파일 하위 목록 모두 ignore
![Untitled](GIT.assets/ignore8)
---

#### Q. 파일의 하위 항목이 모두 ignore되어 파일 자체가 안 올라갈 때?

`*.txt` 파일을 ignore했기 때문에 `.txt` 만 들어있는 ignore 폴더 자체도 git에 commit되지 않음

![Untitled](GIT.assets/ignore3)

1. `.gitkeep` 을 사용하면 `.txt` 는 제외하고 ignore 파일은 올라갈 수 있음
2. 아래와 같이 empty 폴더도 올라감

![Untitled](GIT.assets/ignore4)

---

#### Q. 운영체제, 언어, framework에서 부산물로 나오는 파일을 일일이 ignore 해줘야 하나 ?

### NO!! Visit  [gitignore.io](http://gitignore.io/) 

1. 본인이 사용하는 운영체제, 언어, framework 검색후  `생성` 을 누르면

![Untitled](GIT.assets/ignore5)

2. 아래와 같이 소스코드를 모두 복사해

![Untitled](GIT.assets/ignore6)

```python
/생략/
```

3. `.gitignore` 에 붙여주면 끝 - !

![Untitled](GIT.assets/ignore7)

```python
/생략/
```

---

#### 위 모든 과정이 프로젝트 시작 전 `Initial Commit`