## HTML 태그란 무엇인가?
- **HTML 태그**는 웹 페이지를 구성하는 기본 단위입니다.  
- 텍스트, 이미지, 동영상 등 다양한 요소를 웹 문서에 삽입하고 구조화하기 위해 사용됩니다.  
- 예: `<p>`(문단), `<img>`(이미지), `<a>`(링크)

## HTML 태그의 간단한 예제
- 다음 예시는 가장 간단한 HTML 코드의 형태입니다.
- 브라우저에서 파일을 열면 “Hello World!” 문장이 화면에 표시됩니다.

```
<!DOCTYPE html>
<html>
<head>
<title>HTML Test</title>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
```

## HTML 문서 구조 이해하기
- **`<!DOCTYPE html>`**  
  HTML5 문서임을 선언하는 구문입니다.  
- **`<html>` ~ `</html>`**  
  전체 HTML 문서를 감싸는 루트(root) 태그입니다.  
- **`<head>` ~ `</head>`**  
  웹 브라우저에는 직접 보이지 않지만, 문서 정보(메타데이터), 외부 파일(CSS, JS) 연결, `<title>` 등을 정의합니다.  
- **`<body>` ~ `</body>`**  
  사용자가 실제로 보는 화면(텍스트, 이미지, 동영상 등)이 들어가는 영역입니다.

## 주요 HTML 태그 사용하기
- **텍스트 관련 태그**
  - `<p>`: 문단을 표현합니다.  
  - `<h1> ~ <h6>`: 제목(Heading) 태그로, 숫자가 낮을수록 글자 크기가 커집니다.  
  - `<span>`: 인라인 요소를 구분할 때 사용합니다.
- **링크와 이미지**
  - `<a href="URL">`: 다른 페이지나 리소스(이미지, 파일 등)로 이동할 수 있는 하이퍼링크  
  - `<img src="이미지 파일 경로" alt="대체 텍스트">`: 이미지를 삽입합니다.  
- **목록**
  - `<ul>`: 순서가 없는 목록(불릿 리스트)  
  - `<ol>`: 순서가 있는 목록(숫자 리스트)
- **표**
  - `<table>`, `<tr>`, `<td>` 등을 사용해 표를 구성합니다.
- **폼(form)**
  - `<form>`으로 감싸진 영역 안에 `<input>`, `<button>`, `<select>` 등 입력 요소를 배치해 데이터를 전송할 수 있습니다.

## CSS란 무엇인가?
- **CSS(Cascading Style Sheets)**는 HTML로 작성된 구조(문서)에 디자인(색상, 폰트, 여백 등)을 입히는 언어입니다.
- HTML이 ‘내용’과 ‘구조’를 담당한다면, CSS는 ‘디자인’과 ‘레이아웃’을 담당합니다.
- 예: 글자 크기, 색상, 배경, 화면 레이아웃 등을 지정

## 간단한 예제
- 아래 예제는 HTML 문서에 간단한 CSS를 `<style>` 태그를 통해 직접 추가한 것입니다.
- 결과 화면은 “Hello HTML & CSS”라는 큰 제목과 붉은색 문단 텍스트가 표시됩니다.

```
<!DOCTYPE html>
<html>
<head>
<title>HTML and CSS Example</title>
<style>
h1 {
  color: blue;
  text-align: center;
}
p {
  color: red;
  font-size: 18px;
}
</style>
</head>
<body>
<h1>Hello HTML & CSS</h1>
<p>이 문장은 빨간색으로 표시됩니다.</p>
</body>
</html>
```
