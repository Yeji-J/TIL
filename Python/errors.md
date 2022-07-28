## 에러와 예외 처리

### 문법 에러(Syntax Error)

- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 **가장 앞의 위치**를 가리키는 캐럿(caret) 기호 `^` 표시

Invalid Syntax 문법 오류

assign to literal 잘못된 할당

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/616ef70d-54b6-4f0a-ae0e-dad313f0d8d5/Untitled.png)

### 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤
- 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 예외는 여러 타입을 ㅗ나타나고, 타입이 메세지으 ㅣ일부로 출력됨
  - Name Error, TypeError 등
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

except 가장 작은 수준의 error 부터
순
서
대
로
