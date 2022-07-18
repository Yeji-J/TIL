### CLI ; Command Line Interface

- **명령어를 통해** 사용자와 컴퓨터가 상호 작용
- 컴퓨터에게 명령을 내리는 방법 두 가지 → GUI, CLI
  - CLI는 GUI(; Graphic User Interface)와 똑같은 작업을 한 줄에 끝냄
  - GUI로 못하는 것 CLI로 가능 → 굳이 그래픽으로 나태날 필요가 없기 때문

### Q. Why CLI?

- 컴퓨터 리소스 절약 (명령 한 줄로 끝)

- 수 많은 서버 / 개발 시스템이 CLI 통한 조작 환경을 제공

### 기본 명령어

- `touch` 파일생성
- `Mkdir` 새폴더 생성
- `rm` 파일 삭제 | `-r` (recursive)옵션을 주면 폴더 삭제 가능
- `ls` 현재 작업중인 디렉토리의 폴더 / 파일 목록 보여줌
- `cd` + `이동하고 싶은 dir` 현재 작업 중인 디렉토리 변경
- `start, open` 폴더 / 파일을 여는 명령어 (Window `start` / Mac `open`)
- `clear` 화면 지우기

---

### 참조

`git status`

뭐가 잘못됐는지, 어떻게 해야되는지도 알려줌

`git log`

commit 히스토리

![Untitled](README.assets/Untitled-16578586579955.png)

commit 78d1bb86~ 커밋 고유 아이디 (앞의 네자리만 적어줘도 commit 구분 가능)

`git diff 커밋고유아이디네자리` : 앞을 기준으로 뒤가 어떻게 됐는지 history 보여줌 → 보기 불편해서 다른 프로그램 사용 ~

`ctrl shift +` ` : 터미널 실행

`ctrl ,` : 설정

`code .` : 그 자리에서 vsc열기

---

**CLI로 파일 수정**

`vi 파일명`

_`i`_ ; insert 입력

`esc` : 입력모드 해제

`:wq` : write quit 파일 쓰기 그만

`:q` : 파일 수정모드 나오기

---

![image-20220715133050387](CLI/CLI.assets/image-20220715133050387.png)

### 절대경로 VS 상대경로

- 절대경로

  - **루트 디렉토리부터** 목적 지점까지 거치는 모든 경로
  - **C:\Users\multicampus\desktop**

- 상대경로

  - **현재 작업하고 있는 디렉토리를 기준**으로 계산된 상대적 위치를 작성한 것

  - 현재 작업하고 있는 디렉토리가

    C:\Users

    일 때

    - 윈도우 바탕화면으로의 상대 경로는 **multicampus\desktop**

  - `./` 현재 작업하고 있는 폴더

  - `../` 현재 작업하고 있는 폴더의 부모 폴더
