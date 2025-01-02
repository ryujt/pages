## JavaScript 기초 예제

### 1) 간단한 경고창 띄우기

```html
<!DOCTYPE html>
<html>
<head>
  <title>JavaScript Alert</title>
</head>
<body>
  <!-- 자바스크립트 코드가 HTML 내에서 직접 실행 -->
  <script>
    alert('Hello, JavaScript!');
  </script>
</body>
</html>
```

- **설명**  
  - `<script>` 태그 안에 작성된 코드는 브라우저에서 실행됩니다.  
  - `alert()` 함수는 작은 팝업 창(경고창)을 띄우는 기능을 합니다.  
  - 페이지가 로드되자마자 “Hello, JavaScript!” 메시지를 띄워줍니다.

### 2) 버튼 클릭 시 메시지 띄우기

```html
<!DOCTYPE html>
<html>
<head>
  <title>Button Click</title>
</head>
<body>
  <input type="button" value="Click" onclick="buttonClick()">

  <script>
    function buttonClick() {
      alert('Button Clicked!');
    }
  </script>
</body>
</html>
```

- **설명**  
  - `onclick="buttonClick()"` 속성은 사용자가 버튼을 클릭했을 때 `buttonClick()` 함수를 호출하도록 만듭니다.  
  - `<script>` 태그 안에서 정의된 `buttonClick()` 함수가 실행되며, 경고창에 “Button Clicked!” 메시지를 표시합니다.  
  - 이처럼 JavaScript는 HTML의 이벤트(`onclick`, `onmouseover`, `onchange` 등)와 연계되어 상호작용을 제어합니다.

---

## DOM 조작 예제

HTML 문서가 브라우저에 로드되면, 브라우저는 문서를 **DOM(Document Object Model)**이라는 트리 형태로 이해합니다. JavaScript로 **DOM**에 접근해 다양한 요소를 수정하고, 동적으로 페이지의 내용을 바꿀 수 있습니다.

### 3) 텍스트 변경하기

```html
<!DOCTYPE html>
<html>
<head>
  <title>Change Text</title>
</head>
<body>

<h1 id="title">원래 제목</h1>
<button onclick="changeTitle()">제목 바꾸기</button>

<script>
function changeTitle() {
  const titleElement = document.getElementById("title");
  titleElement.textContent = "바뀐 제목";
}
</script>

</body>
</html>
```

- **설명**  
  - `document.getElementById("title")`를 통해 `<h1 id="title">` 요소를 가져옵니다.  
  - `textContent` 속성을 수정하면, 해당 요소의 텍스트를 실시간으로 변경할 수 있습니다.  
  - 버튼을 클릭할 때마다 “원래 제목”이 “바뀐 제목”으로 교체됩니다.

### 4) 요소 생성 및 추가

```html
<!DOCTYPE html>
<html>
<head>
  <title>Create Element</title>
</head>
<body>

<button onclick="addParagraph()">문단 추가</button>
<div id="content">
  <p>이미 있는 문단입니다.</p>
</div>

<script>
function addParagraph() {
  const newP = document.createElement("p");
  newP.textContent = "새로 추가된 문단입니다.";

  const contentDiv = document.getElementById("content");
  contentDiv.appendChild(newP);
}
</script>

</body>
</html>
```

- **설명**  
  - `document.createElement("p")`를 통해 새로운 `<p>` 요소를 생성합니다.  
  - `appendChild()`를 사용해 `<div id="content">` 내부에 새 요소를 추가합니다.  
  - 버튼을 클릭할 때마다 문단이 계속해서 추가됩니다.

---

## 이벤트 예제

JavaScript는 마우스 클릭, 폼 제출, 키보드 입력 등 다양한 이벤트를 감지하고 처리할 수 있습니다.

### 5) 마우스 오버 이벤트

```html
<!DOCTYPE html>
<html>
<head>
  <title>Mouse Over Example</title>
</head>
<body>

<p onmouseover="mouseOverHandler()" onmouseout="mouseOutHandler()" id="hoverText">
  여기에 마우스를 올려보세요
</p>

<script>
function mouseOverHandler() {
  const text = document.getElementById("hoverText");
  text.style.color = "blue";
  text.textContent = "마우스가 올라갔습니다!";
}

function mouseOutHandler() {
  const text = document.getElementById("hoverText");
  text.style.color = "black";
  text.textContent = "여기에 마우스를 올려보세요";
}
</script>

</body>
</html>
```

- **설명**  
  - `onmouseover` 이벤트는 요소 위에 마우스가 올라갔을 때, `onmouseout`은 빠져나갔을 때 각각 함수를 실행합니다.  
  - 텍스트 색상과 문구가 동적으로 변경되어 사용자에게 상호작용 경험을 제공합니다.

---

## 폼과 사용자 입력 처리 예제

사용자가 입력한 정보를 처리하고, 그 결과를 화면에 표시하는 것은 웹 애플리케이션의 중요한 기능 중 하나입니다.

### 6) 간단한 폼 유효성 검사

```html
<!DOCTYPE html>
<html>
<head>
  <title>Form Validation</title>
</head>
<body>

<form onsubmit="return checkForm()">
  <label for="username">이름:</label>
  <input type="text" id="username" name="username">
  <br><br>
  <input type="submit" value="제출">
</form>

<script>
function checkForm() {
  const usernameInput = document.getElementById("username").value;
  if (usernameInput === "") {
    alert("이름을 입력해주세요.");
    return false; // 폼 제출 취소
  }
  return true; // 폼 제출 진행
}
</script>

</body>
</html>
```

- **설명**  
  - `onsubmit` 이벤트를 통해 폼이 제출되기 전에 `checkForm()` 함수를 호출합니다.  
  - 이름 입력값이 비어 있으면 경고창을 띄우고, `return false;`로 폼 제출을 취소합니다.  
  - 정상적으로 입력됐다면 폼 제출을 진행(`return true;`)합니다.

## 동적 이벤트 연결

아래 예시는 버튼 요소를 찾아서(`document.getElementById`) 이벤트 리스너(`addEventListener`)를 연결하고, 클릭 시 경고창을 띄우는 간단한 코드입니다.

```html
<!DOCTYPE html>
<html>
<head>
<title>Find Element and Add Event</title>
</head>
<body>
<button id="myButton">Click Me</button>

<script>
const btn = document.getElementById("myButton");
btn.addEventListener("click", function() {
  alert("Button was clicked!");
});
</script>
</body>
</html>
```

- **설명**  
  - `<button id="myButton">`: 버튼 요소에 고유한 `id`를 부여했습니다.  
  - `document.getElementById("myButton")`: HTML 문서에서 `id`가 "myButton"인 요소를 찾아 변수 `btn`에 할당합니다.  
  - `btn.addEventListener("click", function() { ... })`: 버튼에 클릭 이벤트를 연결하여, 버튼이 클릭될 때마다 해당 함수를 실행합니다.
