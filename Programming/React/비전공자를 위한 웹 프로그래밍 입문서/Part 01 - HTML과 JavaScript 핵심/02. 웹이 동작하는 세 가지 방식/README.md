## **1. 정적 웹(Static Web)**

서버에 미리 만들어진 HTML 파일이 저장되어 있고, 사용자가 페이지를 요청하면 해당 HTML 파일이 그대로 전송됩니다.

- 별도의 서버 로직이나 데이터베이스 연결 없이, 고정된 웹 문서만 전달  
- 간단한 회사 소개 사이트처럼 내용 변화가 없는 웹사이트에 적합  

## **2. 서버 사이드 렌더링(Server-Side Rendering, SSR)**

사용자가 웹 페이지를 요청할 때, 서버 쪽에서 HTML 결과를 만들어(“렌더링”) 클라이언트(브라우저)에게 전달하는 방식입니다.  

``` jobflow
master: WebServer
Object: Browser, WebServer, Database

Browser.OnPageRequest --> WebServer.HandleRequest
WebServer.HandleRequest --> Database.LoadData
Database.data.result --> WebServer.GenerateHTML
WebServer.GenerateHTML --> Browser.data.RenderPage
```

1. 브라우저가 서버에 “페이지를 달라”고 요청  
2. 서버는 내부 로직(데이터베이스 조회 등)을 수행한 뒤 HTML 형태로 완성된 결과물을 생성  
3. 서버가 생성한 HTML을 브라우저에 전송  
4. 브라우저는 HTML을 그대로 화면에 표시

## **3. 프론트엔드와 백엔드로 나눠서 처리**

 화면을 표시하는 것과 데이터와 논리적인 처리를 나눠서 처리하는 방식입니다.
 최근에 가장많이 사용하는 방식입니다.

- 프론트엔드와 백엔드 개발을 독립적으로 진행할 수 있어 개발 효율성 증가
- 서버 부하를 분산시킬 수 있으며, 확장성이 좋음

### **화면을 만드는 프론트엔드 (Frontend)**  

- 웹 브라우저에서 사용자에게 보이는 화면과 그 화면에서 일어나는 모든 상호작용을 담당하는 영역  
- 일반적으로 HTML, CSS, JavaScript를 사용하며, 최근에는 React, Vue, Angular 등 다양한 라이브러리와 프레임워크가 활용됨  

### **뒤에서 일하는 백엔드 (Backend)**  

- 서버 측에서 데이터베이스와 비즈니스 로직을 처리하는 영역  
- Node.js, Python(Django, Flask), Java(Spring), PHP(Laravel) 등 다양한 언어와 프레임워크를 사용  
- API(서버와 클라이언트 간의 데이터 전달 방식) 및 데이터베이스 연동 등을 담당  

