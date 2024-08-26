# RAG를 활용한 프로젝트 분석 및 설계

이 발표에서는 RAG를 이용하여 기존의 프로젝트를 분석하거나 프로젝트를 수행하는 과정에 대해서 설명하겠습니다.
CodeSage라는 오픈 소스를 사용하여 발표를 진행하겠습니다.
또한 오픈소스 인공지능을 활용하여 개선된 부분에 대해서도 발표하겠습니다.

## Code Sage를 활용한 프로젝트 수행

### 설치 방법 

CodeSage의 소스코드는 아래의 링크에서 다운받을 수 있습니다.

* [https://github.com/ryujt/CodeSage](https://github.com/ryujt/CodeSage)

#### pip 사용

파이썬이 설치되어 있다면 아래의 스크립트로 간단하게 설치하여 사용하실 수 있습니다.

```
pip install -r requirements.txt
```

#### docker 사용

Docker를 사용하면 배포하고 실행할 수도 있습니다.

```
docker build -t codesage:latest .
docker run -d -p 8080:8080 --name codesage_container codesage:latest
```

### 동작확인

### 기존 프로젝트의 내용을 분석

```
IntKeyLinkedMap을 사용하는 코드를 중심으로 분석해서 굳이 linked list를 사용해야 하는 이유를 찾아줘.
http://127.0.0.1:8080/question/70
```

```
Status Code에 관한 설정을 모두 보여줘.
http://127.0.0.1:8080/question/71
```

```
오목 게임에 대한 시퀀스 다이어그램을 그려줘.
http://127.0.0.1:8080/question/83
```

```
오목 게임에 대한 job flow를 그려줘.
http://127.0.0.1:8080/question/82
```

### 프로젝트 전체 코드를 고려하여 기능 추가하기

```
userApi.js를 직접 호출하지 않고 user 스토어에서 userApi.js를 호출하는 방식으로 수정하려고 한다.
vue에서는 user 스토어를 통해서 signin, signup, signout 액션을 취하고 정보를 전달 받도록 코드를 수정해줘.
http://127.0.0.1:8080/question/76
```

```
오목게임에 결과 화면을 추가해줘.
수정해야할 파일들을 함께 표시해줘.
http://127.0.0.1:8080/question/59
```

### PR 전에 코드 분석 자동화

#### Git diff (recent)

http://127.0.0.1:8080/question/38

#### Git diff (main)

http://127.0.0.1:8080/question/37

### 기술문서 작성

위의 두 가지 RealChart 소스를 보고, 기존 영상 스크립트(scripts.md)를 참고하여.
영상 스크립트를 작성해줘.
http://127.0.0.1:8080/question/66

## 오픈소스 인공지능 활용

### 임베딩 모델의 한글 지원 이슈

### 입력 토큰 부족 이슈


