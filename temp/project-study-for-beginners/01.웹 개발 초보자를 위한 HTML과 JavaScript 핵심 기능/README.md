# 웹 개발 초보자를 위한 HTML과 JavaScript 핵심 기능

## HTML 기초

### HTML 문서 구조 이해하기

HTML 문서는 웹 페이지의 뼈대를 구성하는 기본 요소입니다. HTML 문서의 구조를 이해하는 것은 웹 개발의 첫 걸음이라고 할 수 있습니다.

HTML 문서는 크게 두 부분으로 나뉩니다: 헤드(head)와 바디(body)입니다.

1. 헤드(head):
   - 문서의 메타데이터(metadata)를 포함하는 부분입니다.
   - 웹 페이지의 제목(title), 문자 인코딩 정보, 스타일시트 링크, 자바스크립트 파일 링크 등이 여기에 들어갑니다.
   - 헤드 안의 내용은 웹 페이지에 직접 표시되지 않습니다.

2. 바디(body):
   - 실제로 웹 페이지에 표시되는 내용을 담고 있는 부분입니다.
   - 텍스트, 이미지, 비디오, 링크, 버튼 등 다양한 요소들이 바디 안에 위치합니다.
   - 바디 안의 내용은 웹 브라우저에 의해 렌더링되어 사용자에게 보여집니다.

HTML 문서의 기본 구조는 다음과 같습니다:

```html
<!DOCTYPE html>
<html>
<head>
  <title>웹 페이지 제목</title>
</head>
<body>
  <h1>큰 제목</h1>
  <p>단락 내용</p>
</body>
</html>
```

- `<!DOCTYPE html>`: 문서 유형을 정의하는 선언문입니다. 현재 문서가 HTML5 문서임을 나타냅니다.
- `<html>`: HTML 문서의 루트(root) 요소입니다. 모든 다른 요소들은 이 요소 안에 위치합니다.
- `<head>`: 문서의 메타데이터를 포함하는 헤드 부분입니다.
- `<title>`: 웹 페이지의 제목을 나타내는 요소입니다. 브라우저 탭이나 즐겨찾기에 표시됩니다.
- `<body>`: 웹 페이지에 표시되는 내용을 담고 있는 바디 부분입니다.
- `<h1>`: 큰 제목을 나타내는 요소입니다. 제목의 크기와 중요도에 따라 `<h1>`부터 `<h6>`까지 사용할 수 있습니다.
- `<p>`: 단락을 나타내는 요소입니다.

이렇게 HTML 문서의 구조를 이해하면, 웹 페이지를 만들 때 각 요소들을 적절한 위치에 배치할 수 있게 됩니다. 헤드 부분에는 문서의 메타데이터를, 바디 부분에는 실제 내용을 담으면 됩니다. 이를 바탕으로 다양한 HTML 태그를 사용하여 웹 페이지를 구성할 수 있습니다.

### 주요 HTML 태그 사용하기

HTML에는 다양한 태그들이 있습니다. 이 태그들을 사용하여 웹 페이지의 구조와 내용을 작성할 수 있습니다. 여기에서는 초보자가 자주 사용하는 주요 HTML 태그들에 대해 알아보겠습니다.

1. 제목 태그 (Heading Tags):
   - `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>` 태그를 사용하여 제목을 나타냅니다.
   - `<h1>`이 가장 큰 제목이고, `<h6>`이 가장 작은 제목입니다.
   - 예: `<h1>큰 제목</h1>`, `<h2>작은 제목</h2>`

2. 단락 태그 (Paragraph Tag):
   - `<p>` 태그를 사용하여 문단을 나타냅니다.
   - 예: `<p>이것은 하나의 문단입니다.</p>`

3. 목록 태그 (List Tags):
   - 순서 있는 목록 (Ordered List)은 `<ol>` 태그를 사용하고, 순서 없는 목록 (Unordered List)은 `<ul>` 태그를 사용합니다.
   - 목록의 각 항목은 `<li>` 태그로 표시합니다.
   - 예: `<ul><li>항목 1</li><li>항목 2</li></ul>`

4. 링크 태그 (Anchor Tag):
   - `<a>` 태그를 사용하여 다른 웹 페이지나 웹 사이트로 연결하는 링크를 만듭니다.
   - `href` 속성을 사용하여 링크의 목적지를 지정합니다.
   - 예: `<a href="https://www.example.com">링크 텍스트</a>`

5. 이미지 태그 (Image Tag):
   - `<img>` 태그를 사용하여 이미지를 삽입합니다.
   - `src` 속성을 사용하여 이미지 파일의 경로를 지정합니다.
   - `alt` 속성을 사용하여 이미지에 대한 대체 텍스트를 제공합니다.
   - 예: `<img src="image.jpg" alt="이미지 설명">`

6. 입력 양식 태그 (Form Tags):
   - `<form>` 태그를 사용하여 사용자로부터 입력을 받는 양식을 만듭니다.
   - `<input>` 태그를 사용하여 다양한 유형의 입력 필드를 만듭니다 (텍스트, 비밀번호, 체크박스, 라디오 버튼 등).
   - `<textarea>` 태그를 사용하여 여러 줄의 텍스트를 입력받을 수 있습니다.
   - `<select>` 태그와 `<option>` 태그를 사용하여 드롭다운 목록을 만듭니다.
   - 예: `<form><input type="text" name="username"><input type="password" name="password"></form>`

이러한 기본적인 HTML 태그들을 사용하여 웹 페이지의 구조와 내용을 작성할 수 있습니다. 태그들을 적절히 조합하고 내용을 채워넣으면 원하는 모양의 웹 페이지를 만들 수 있습니다. 초보자라도 이러한 태그들을 연습하고 익히면 점차 더 복잡하고 다양한 웹 페이지를 만들 수 있게 될 것입니다.

### 스타일 꾸미기 및 CSS

웹 페이지를 보다 아름답고 보기 좋게 만들기 위해서는 HTML 태그들에 스타일을 적용해야 합니다. 이때 사용하는 것이 바로 CSS(Cascading Style Sheets)입니다.

CSS는 HTML 문서의 스타일을 정의하는 언어로, HTML 태그들의 색상, 크기, 위치, 배경 등을 지정할 수 있습니다. CSS를 사용하면 웹 페이지의 디자인을 일관성 있게 유지할 수 있고, HTML 코드와 스타일을 분리할 수 있어 코드의 가독성과 유지보수성이 향상됩니다.

CSS를 적용하는 방법에는 세 가지가 있습니다:

1. 인라인 스타일(Inline Style): HTML 태그 내부에 style 속성을 사용하여 직접 스타일을 지정하는 방법입니다.
예) `<p style="color: blue; font-size: 16px;">이것은 파란색 16px 크기의 문단입니다.</p>`

2. 내부 스타일시트(Internal Stylesheet): HTML 문서의 `<head>` 태그 내부에 `<style>` 태그를 사용하여 스타일을 정의하는 방법입니다.
예)
```html
<head>
  <style>
    p {
      color: blue;
      font-size: 16px;
    }
  </style>
</head>
```

3. 외부 스타일시트(External Stylesheet): 별도의 CSS 파일을 만들어 HTML 문서에 연결하는 방법입니다. 이 방법이 가장 권장되는 방식입니다.
예) style.css 파일을 만들어 스타일을 정의하고, HTML 문서의 `<head>` 태그 내부에 `<link>` 태그를 사용하여 CSS 파일을 연결합니다.
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

CSS에서는 선택자(Selector)를 사용하여 스타일을 적용할 HTML 요소를 선택합니다. 선택자에는 태그 이름, 클래스(class), 아이디(id) 등이 사용될 수 있습니다. 선택자를 사용하여 특정 요소나 요소 그룹에 스타일을 적용할 수 있습니다.

예를 들어, 모든 `<p>` 태그에 빨간색 텍스트 색상을 적용하고 싶다면 다음과 같이 CSS 코드를 작성할 수 있습니다:

```css
p {
  color: red;
}
```

이처럼 CSS를 사용하면 웹 페이지의 디자인을 보다 아름답고 일관성 있게 만들 수 있습니다. 초보자라도 CSS의 기본 개념과 문법을 이해한다면 쉽게 스타일을 적용할 수 있습니다.

## 버튼 클릭 이벤트 처리

### 버튼 클릭 시 alert 창 표시하기

웹 페이지에서 버튼을 클릭했을 때, 작은 창이 나타나면서 메시지를 보여주는 기능을 구현해보겠습니다. 이 작은 창을 "alert 창"이라고 부릅니다.

먼저, HTML에서 버튼을 만들어야 합니다. 다음과 같이 `<button>` 태그를 사용하면 됩니다.

```html
<button id="myButton">클릭해 주세요!</button>
```

버튼에는 "클릭해 주세요!"라는 텍스트가 표시됩니다. 그리고 버튼을 구분할 수 있는 `id`라는 속성을 "myButton"으로 지정했습니다.

다음으로, JavaScript 코드를 작성해야 합니다. `<script>` 태그 안에 다음 코드를 추가합니다.

```javascript
<script>
  document.getElementById("myButton").addEventListener("click", function() {
    alert("버튼을 클릭했습니다!");
  });
</script>
```

위 코드의 의미를 하나씩 살펴보겠습니다.
- `document.getElementById("myButton")`은 HTML에서 `id`가 "myButton"인 요소를 찾습니다. 여기서는 우리가 만든 버튼을 찾는 것입니다.
- `.addEventListener("click", function() { ... })`은 찾은 버튼에 클릭 이벤트를 추가합니다. 클릭 이벤트가 발생하면, `function() { ... }` 안에 있는 코드가 실행됩니다.
- `alert("버튼을 클릭했습니다!")`은 alert 창을 띄우고, 안에 "버튼을 클릭했습니다!"라는 메시지를 표시합니다.

이제 웹 페이지에서 버튼을 클릭하면, "버튼을 클릭했습니다!"라는 메시지가 담긴 alert 창이 나타날 것입니다.

이렇게 간단한 코드로 버튼 클릭 시 alert 창을 표시하는 기능을 구현할 수 있습니다. 버튼과 메시지 내용은 여러분이 원하는 대로 바꿀 수 있습니다. 이 기능을 응용하면 더 다양한 상호작용을 만들어낼 수 있을 것입니다.

### 버튼 클릭 시 텍스트 변경하기

웹 페이지에서 버튼을 클릭했을 때 특정 텍스트를 변경하는 기능을 구현해보겠습니다. 이를 위해 HTML과 JavaScript를 사용할 것입니다.

먼저, HTML 문서에 버튼과 변경할 텍스트를 포함하는 요소를 추가합니다.

```html
<button id="myButton">클릭하세요!</button>
<p id="myText">안녕하세요!</p>
```

위 코드에서 `<button>` 태그는 클릭할 수 있는 버튼을 생성하고, `id` 속성을 사용하여 고유한 이름을 부여했습니다. `<p>` 태그는 변경할 텍스트를 포함하는 단락을 나타내며, 역시 `id` 속성을 사용하여 식별할 수 있도록 했습니다.

다음으로, JavaScript 코드를 작성하여 버튼 클릭 이벤트를 처리하고 텍스트를 변경하는 기능을 구현합니다.

```javascript
document.getElementById("myButton").addEventListener("click", function() {
  document.getElementById("myText").textContent = "버튼이 클릭되었습니다!";
});
```

위 코드를 하나씩 살펴보겠습니다.

1. `document.getElementById("myButton")`은 HTML 문서에서 `id`가 "myButton"인 요소를 찾습니다. 여기서는 버튼을 나타냅니다.

2. `.addEventListener("click", function() { ... })`은 찾은 버튼 요소에 클릭 이벤트 리스너를 추가합니다. 버튼이 클릭되면 함수 내부의 코드가 실행됩니다.

3. `document.getElementById("myText")`는 `id`가 "myText"인 요소, 즉 변경할 텍스트를 포함하는 단락을 찾습니다.

4. `.textContent = "버튼이 클릭되었습니다!"`는 찾은 단락 요소의 텍스트 내용을 "버튼이 클릭되었습니다!"로 변경합니다.

이제 웹 페이지에서 버튼을 클릭하면 단락의 텍스트가 "안녕하세요!"에서 "버튼이 클릭되었습니다!"로 변경될 것입니다.

이 예제를 통해 버튼 클릭 이벤트를 처리하고 텍스트를 동적으로 변경하는 방법을 배웠습니다. 이 개념을 응용하여 다양한 상호작용을 구현할 수 있습니다. 예를 들어, 버튼 클릭 시 이미지를 변경하거나 스타일을 변경하는 등의 기능을 추가할 수 있습니다.

### 버튼 클릭 시 이미지 변경하기

웹 페이지에서 버튼을 클릭했을 때 이미지를 변경하는 기능을 구현하는 것은 JavaScript를 사용하여 쉽게 할 수 있습니다. 아래 단계를 따라하면 버튼 클릭 시 이미지를 변경할 수 있습니다.

1. HTML 문서에 버튼과 이미지를 추가합니다. 버튼에는 고유한 아이디(id)를 지정하고, 이미지에는 고유한 아이디와 초기 이미지 경로를 지정합니다.

```html
<button id="changeImageBtn">이미지 변경</button>
<img id="myImage" src="image1.jpg" alt="초기 이미지">
```

2. JavaScript 코드를 작성합니다. 버튼과 이미지 요소를 선택하기 위해 `document.getElementById()`를 사용합니다.

```javascript
// 버튼과 이미지 요소 선택
var button = document.getElementById("changeImageBtn");
var image = document.getElementById("myImage");
```

3. 버튼에 클릭 이벤트 리스너를 추가합니다. 버튼이 클릭되면 실행될 함수를 지정합니다.

```javascript
// 버튼 클릭 이벤트 리스너 추가
button.addEventListener("click", function() {
  // 버튼 클릭 시 실행될 코드 작성
});
```

4. 버튼 클릭 시 실행될 코드를 작성합니다. 이미지의 `src` 속성을 변경하여 다른 이미지 파일 경로를 지정합니다.

```javascript
button.addEventListener("click", function() {
  // 이미지 변경
  image.src = "image2.jpg";
});
```

위의 코드에서는 버튼 클릭 시 이미지의 `src` 속성을 "image2.jpg"로 변경하였습니다. 원하는 이미지 파일 경로로 변경하면 됩니다.

5. 완성된 코드는 다음과 같습니다.

```html
<button id="changeImageBtn">이미지 변경</button>
<img id="myImage" src="image1.jpg" alt="초기 이미지">

<script>
  var button = document.getElementById("changeImageBtn");
  var image = document.getElementById("myImage");

  button.addEventListener("click", function() {
    image.src = "image2.jpg";
  });
</script>
```

이제 웹 페이지에서 "이미지 변경" 버튼을 클릭하면 이미지가 "image1.jpg"에서 "image2.jpg"로 변경됩니다.

이 코드를 응용하여 버튼을 여러 개 만들고 각 버튼 클릭 시 다른 이미지로 변경하는 등의 기능을 구현할 수 있습니다. 또한 이미지 파일 경로를 동적으로 생성하거나 서버에서 받아오는 등의 방법으로 확장할 수 있습니다.

## 입력 양식 다루기

### 입력 양식에 값 입력 시 실시간으로 출력하기

웹 페이지에서 사용자로부터 정보를 입력받는 방법 중 하나는 입력 양식(form)을 사용하는 것입니다. 입력 양식은 텍스트 입력 필드, 체크박스, 라디오 버튼 등 다양한 형태로 존재합니다. 이 중에서 텍스트 입력 필드에 사용자가 값을 입력할 때, 실시간으로 입력된 값을 화면에 출력하는 방법에 대해 알아보겠습니다.

먼저, HTML에서 입력 양식을 만들기 위해 `<input>` 태그를 사용합니다. 이 태그의 `type` 속성을 "text"로 설정하면 텍스트 입력 필드가 생성됩니다. 또한, 입력된 값을 실시간으로 출력할 HTML 요소를 만들어야 합니다. 이를 위해 `<p>` 태그나 `<div>` 태그를 사용할 수 있습니다.

다음으로, JavaScript를 사용하여 입력 필드의 값이 변경될 때마다 실행될 함수를 작성합니다. 이 함수는 입력 필드의 현재 값을 가져와서 출력할 HTML 요소의 내용을 업데이트합니다.

마지막으로, 입력 필드에 `oninput` 이벤트를 연결합니다. 이 이벤트는 입력 필드의 값이 변경될 때마다 발생하므로, 위에서 작성한 함수를 호출하도록 설정합니다.

아래는 이를 구현한 예시 코드입니다:

```html
<input type="text" id="inputField" oninput="updateOutput()">
<p id="outputText"></p>

<script>
function updateOutput() {
  var inputField = document.getElementById("inputField");
  var outputText = document.getElementById("outputText");
  outputText.innerHTML = "입력된 값: " + inputField.value;
}
</script>
```

위 코드에서 `<input>` 태그의 `id` 속성은 "inputField"로 설정되어 있고, `oninput` 속성은 "updateOutput()" 함수를 호출하도록 설정되어 있습니다. `<p>` 태그의 `id` 속성은 "outputText"로 설정되어 있습니다.

JavaScript 코드에서는 `getElementById()` 함수를 사용하여 "inputField"와 "outputText" 요소를 찾아 변수에 저장합니다. 그리고 `updateOutput()` 함수 내에서 입력 필드의 현재 값을 `value` 속성을 통해 가져와서, 출력 텍스트의 `innerHTML` 속성을 업데이트합니다.

이제 웹 페이지에서 입력 필드에 값을 입력하면, 실시간으로 입력된 값이 화면에 출력되는 것을 확인할 수 있습니다. 이를 통해 사용자는 입력한 값을 즉시 확인할 수 있으며, 필요한 경우 수정할 수 있습니다.

이 기능은 회원 가입 폼, 검색 폼 등 다양한 상황에서 유용하게 사용될 수 있습니다. 사용자 경험을 향상시키고, 입력 오류를 줄이는 데 도움이 됩니다.

### 라디오 버튼 선택 시 선택한 값 출력하기

라디오 버튼은 여러 개의 선택 사항 중에서 하나만 선택할 수 있는 입력 양식입니다. 사용자가 라디오 버튼을 선택하면, 선택한 값을 실시간으로 출력할 수 있습니다.

1. HTML에서 라디오 버튼을 생성합니다.
   - `<input type="radio">`를 사용하여 라디오 버튼을 만듭니다.
   - 각 라디오 버튼에 `name` 속성을 설정하여 같은 그룹으로 묶습니다.
   - 각 라디오 버튼에 `value` 속성을 설정하여 선택 시 전달될 값을 지정합니다.

2. HTML에서 선택한 값을 출력할 영역을 생성합니다.
   - 선택한 값을 출력할 `<p>`, `<div>` 등의 태그를 만듭니다.
   - 출력 영역에 고유한 `id`를 부여합니다.

3. JavaScript에서 라디오 버튼의 변경 이벤트를 감지합니다.
   - `document.getElementsByName()`을 사용하여 라디오 버튼 그룹을 선택합니다.
   - 각 라디오 버튼에 `addEventListener()`를 사용하여 `change` 이벤트를 등록합니다.

4. 라디오 버튼 선택 시 선택한 값을 출력합니다.
   - 이벤트 핸들러 함수 내에서 `event.target.value`를 사용하여 선택한 라디오 버튼의 값을 가져옵니다.
   - `document.getElementById()`를 사용하여 출력 영역을 선택합니다.
   - 출력 영역의 `textContent` 속성에 선택한 값을 할당합니다.

예시 코드:
```html
<form>
  <input type="radio" name="fruit" value="apple"> 사과<br>
  <input type="radio" name="fruit" value="banana"> 바나나<br>
  <input type="radio" name="fruit" value="orange"> 오렌지<br>
</form>

<p id="result"></p>

<script>
  const radioButtons = document.getElementsByName('fruit');
  const resultElement = document.getElementById('result');

  radioButtons.forEach(radio => {
    radio.addEventListener('change', function(event) {
      const selectedValue = event.target.value;
      resultElement.textContent = `선택한 과일: ${selectedValue}`;
    });
  });
</script>
```

위 코드에서는 'fruit'이라는 `name` 속성으로 그룹화된 라디오 버튼을 생성하고, 각 라디오 버튼에는 'apple', 'banana', 'orange'라는 `value` 속성이 설정되어 있습니다. 사용자가 라디오 버튼을 선택하면, 선택한 값이 `<p>` 태그에 출력됩니다.

이렇게 라디오 버튼을 사용하면 사용자가 여러 개의 선택 사항 중 하나를 선택할 수 있으며, 선택한 값을 실시간으로 출력할 수 있습니다.

### 체크박스 선택 시 선택한 항목 출력하기

체크박스는 사용자가 여러 개의 옵션 중에서 원하는 것을 선택할 수 있게 해주는 HTML 요소입니다. 예를 들어, 설문조사에서 "좋아하는 과일을 모두 선택하세요"라는 질문에 사과, 바나나, 오렌지 등의 옵션이 제시되면, 사용자는 체크박스를 통해 자신이 좋아하는 과일을 복수로 선택할 수 있습니다.

이번에는 체크박스를 선택하면 선택한 항목을 화면에 출력하는 방법에 대해 알아보겠습니다.

먼저, HTML에서 체크박스를 만들기 위해서는 `<input>` 태그를 사용하고, `type` 속성 값을 `"checkbox"`로 설정합니다. 각 체크박스마다 `id`와 `value` 속성을 지정하여 고유한 식별자와 값을 부여합니다.

```html
<input type="checkbox" id="apple" value="사과">
<label for="apple">사과</label><br>
<input type="checkbox" id="banana" value="바나나">
<label for="banana">바나나</label><br>
<input type="checkbox" id="orange" value="오렌지">
<label for="orange">오렌지</label><br>
```

그 다음, JavaScript에서 체크박스의 선택 여부를 확인하고 선택된 항목을 출력하는 함수를 작성합니다. 함수 내부에서는 각 체크박스의 `checked` 속성을 확인하여 선택되었는지 판단하고, 선택된 체크박스의 `value` 값을 가져와서 문자열로 조합합니다. 최종적으로 조합된 문자열을 원하는 위치에 출력합니다.

```javascript
function printSelectedFruits() {
  var fruits = [];
  if (document.getElementById("apple").checked) {
    fruits.push(document.getElementById("apple").value);
  }
  if (document.getElementById("banana").checked) {
    fruits.push(document.getElementById("banana").value);
  }
  if (document.getElementById("orange").checked) {
    fruits.push(document.getElementById("orange").value);
  }

  var result = "선택한 과일: " + fruits.join(", ");
  document.getElementById("result").textContent = result;
}
```

마지막으로, 체크박스의 선택 상태가 변경될 때마다 `printSelectedFruits` 함수가 호출되도록 이벤트 리스너를 등록합니다.

```javascript
document.getElementById("apple").addEventListener("change", printSelectedFruits);
document.getElementById("banana").addEventListener("change", printSelectedFruits);
document.getElementById("orange").addEventListener("change", printSelectedFruits);
```

이제 사용자가 체크박스를 선택하거나 선택 해제할 때마다 선택한 과일의 목록이 실시간으로 화면에 출력됩니다. 이러한 방식으로 체크박스를 활용하면 사용자의 다중 선택을 처리하고 선택 결과를 동적으로 표시할 수 있습니다.

## 마우스 이벤트 처리

### 마우스 클릭한 위치 좌표 출력하기

웹 페이지에서 마우스를 클릭하면, 그 위치의 좌표를 알아내어 화면에 표시할 수 있습니다. 이를 위해서는 JavaScript의 도움이 필요합니다.

먼저, HTML 문서에 마우스 클릭 이벤트를 감지할 영역을 지정해야 합니다. 이는 `<div>` 태그를 사용하여 구현할 수 있습니다. 예를 들어, 다음과 같이 작성할 수 있습니다:

```html
<div id="clickArea">
  이 영역을 클릭해보세요!
</div>
```

이제 JavaScript 코드를 작성하여 마우스 클릭 이벤트를 처리해야 합니다. 다음 단계를 따라 작성해보세요:

1. `clickArea`라는 ID를 가진 요소를 찾아 변수에 저장합니다.
2. 해당 요소에 `click` 이벤트 리스너를 추가합니다.
3. 마우스 클릭 이벤트가 발생하면, 이벤트 객체에서 마우스 좌표를 가져옵니다.
4. 가져온 좌표를 화면에 표시할 요소를 찾아 변수에 저장합니다.
5. 좌표를 텍스트로 변환하여 해당 요소에 출력합니다.

아래는 위 단계를 구현한 JavaScript 코드 예시입니다:

```javascript
// 클릭 영역 요소 찾기
const clickArea = document.getElementById('clickArea');

// 클릭 이벤트 리스너 추가
clickArea.addEventListener('click', function(event) {
  // 마우스 좌표 가져오기
  const x = event.clientX;
  const y = event.clientY;

  // 좌표를 출력할 요소 찾기
  const output = document.getElementById('output');

  // 좌표를 텍스트로 변환하여 출력
  output.textContent = `마우스 클릭 좌표: (${x}, ${y})`;
});
```

위 코드에서 `event.clientX`와 `event.clientY`는 각각 마우스 클릭 위치의 가로 좌표와 세로 좌표를 나타냅니다. 이 값을 `output`이라는 ID를 가진 요소에 텍스트로 출력하게 됩니다.

마지막으로, 좌표를 출력할 요소를 HTML 문서에 추가해야 합니다. 예를 들면 다음과 같이 작성할 수 있습니다:

```html
<p id="output"></p>
```

이제 웹 페이지에서 마우스를 클릭하면, 클릭한 위치의 좌표가 화면에 표시될 것입니다. 이러한 기능은 인터랙티브한 웹 페이지를 만드는 데 유용하게 사용될 수 있습니다.

### 마우스 오버/아웃 시 요소 스타일 변경하기

웹 페이지에서 마우스를 특정 요소 위로 가져가거나(마우스 오버) 요소에서 벗어날 때(마우스 아웃) 해당 요소의 모양이나 스타일을 변경하는 것은 사용자와의 상호작용을 향상시키는 효과적인 방법입니다. 이를 통해 사용자는 요소와 상호작용할 수 있다는 것을 직관적으로 알 수 있습니다.

마우스 오버/아웃 시 요소의 스타일을 변경하는 방법은 다음과 같습니다:

1. HTML에서 스타일을 변경할 요소를 생성합니다. 예를 들어, 버튼이나 이미지 등이 될 수 있습니다.

2. CSS를 사용하여 요소의 기본 스타일을 지정합니다. 이는 마우스 오버/아웃 전의 상태를 나타냅니다.

3. JavaScript에서 해당 요소에 마우스 오버/아웃 이벤트 리스너를 추가합니다. 이는 마우스가 요소 위로 올라갈 때와 벗어날 때 특정 함수를 실행하도록 합니다.

4. 마우스 오버 시 실행될 함수에서는 요소의 스타일을 변경하는 코드를 작성합니다. 예를 들어, 배경색을 변경하거나 테두리를 추가하는 등의 작업을 할 수 있습니다.

5. 마우스 아웃 시 실행될 함수에서는 요소의 스타일을 원래대로 되돌리는 코드를 작성합니다.

이렇게 하면 마우스를 요소 위로 가져갈 때 지정한 스타일로 변경되고, 마우스를 요소에서 벗어나면 원래의 스타일로 돌아갑니다.

예를 들어, 버튼에 마우스를 올리면 배경색이 변경되고 마우스를 벗어나면 원래 배경색으로 돌아가도록 할 수 있습니다. 이는 사용자에게 버튼과 상호작용할 수 있다는 시각적인 피드백을 제공합니다.

마우스 오버/아웃을 사용하여 다양한 요소의 스타일을 변경할 수 있으며, 이를 통해 웹 페이지를 보다 역동적이고 인터랙티브하게 만들 수 있습니다. 초보자도 이해하기 쉬운 개념이므로, 웹 개발 학습 과정에서 유용하게 활용할 수 있습니다.

### 마우스 드래그 시 선택한 영역 강조하기

마우스로 드래그하여 선택한 영역을 강조하는 기능은 웹 페이지에서 유용하게 사용될 수 있습니다. 이를 구현하기 위해서는 HTML, CSS, JavaScript를 함께 사용해야 합니다.

먼저, HTML에서는 드래그 할 영역을 지정해야 합니다. 이는 `<div>` 태그를 사용하여 구현할 수 있습니다. 예를 들어, `<div id="draggable-area"></div>`와 같이 작성하면 됩니다.

다음으로, CSS에서는 드래그 영역의 스타일을 지정해야 합니다. 드래그 영역의 배경색, 크기, 테두리 등을 설정할 수 있습니다. 예를 들어, 다음과 같이 작성할 수 있습니다:

```css
#draggable-area {
  width: 400px;
  height: 200px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
}
```

마지막으로, JavaScript에서는 마우스 드래그 이벤트를 처리하여 선택한 영역을 강조하는 기능을 구현해야 합니다. 이를 위해 `mousedown`, `mousemove`, `mouseup` 이벤트를 사용합니다.

1. `mousedown` 이벤트: 마우스 버튼을 누를 때 발생하는 이벤트입니다. 이 이벤트에서는 드래그 시작 위치를 저장합니다.
2. `mousemove` 이벤트: 마우스를 움직일 때 발생하는 이벤트입니다. 이 이벤트에서는 드래그 중인 영역을 계산하고, 해당 영역을 강조합니다.
3. `mouseup` 이벤트: 마우스 버튼을 뗄 때 발생하는 이벤트입니다. 이 이벤트에서는 드래그가 종료되었음을 감지하고, 강조된 영역을 제거합니다.

JavaScript 코드 예시:

```javascript
const draggableArea = document.getElementById('draggable-area');
let isDragging = false;
let startX, startY, endX, endY;

draggableArea.addEventListener('mousedown', startDragging);
draggableArea.addEventListener('mousemove', drag);
draggableArea.addEventListener('mouseup', stopDragging);

function startDragging(event) {
  isDragging = true;
  startX = event.clientX;
  startY = event.clientY;
}

function drag(event) {
  if (!isDragging) return;

  endX = event.clientX;
  endY = event.clientY;

  // 선택한 영역 강조하기
  highlightSelectedArea();
}

function stopDragging() {
  isDragging = false;

  // 강조된 영역 제거하기
  removeHighlight();
}

function highlightSelectedArea() {
  // 선택한 영역을 계산하고 강조하는 로직 작성
  // 예: 선택한 영역에 반투명한 배경색 적용
}

function removeHighlight() {
  // 강조된 영역을 제거하는 로직 작성
  // 예: 선택한 영역의 반투명한 배경색 제거
}
```

위의 JavaScript 코드는 드래그 이벤트를 처리하여 선택한 영역을 강조하는 기본적인 로직을 보여줍니다. `startDragging` 함수에서는 드래그 시작 위치를 저장하고, `drag` 함수에서는 드래그 중인 영역을 계산하여 강조합니다. `stopDragging` 함수에서는 드래그가 종료되었을 때 강조된 영역을 제거합니다.

실제로 선택한 영역을 강조하려면 `highlightSelectedArea` 함수에서 선택한 영역의 좌표를 계산하고, 해당 영역에 스타일을 적용해야 합니다. 예를 들어, 선택한 영역에 반투명한 배경색을 적용하거나, 테두리를 그릴 수 있습니다.

마우스 드래그 시 선택한 영역을 강조하는 기능은 위와 같은 과정을 통해 구현할 수 있습니다. 이해하기 쉽게 설명했지만, 실제로는 좀 더 복잡한 계산과 스타일 적용이 필요할 수 있습니다. 하지만 기본 개념을 이해하고 있다면 충분히 구현할 수 있을 것입니다.

## 키보드 이벤트 처리

### 키보드 입력 값 실시간으로 출력하기

웹 페이지에서 사용자가 키보드로 입력한 값을 실시간으로 화면에 보여주는 기능을 구현해보겠습니다. 이를 통해 사용자는 자신이 입력한 내용을 바로 확인할 수 있어 편리합니다.

먼저, HTML에서 입력 양식(input)과 입력 값을 출력할 영역(span)을 만듭니다.

```html
<input type="text" id="inputText">
<p>입력한 값: <span id="outputText"></span></p>
```

다음으로, JavaScript 코드를 작성합니다. 입력 양식에서 키보드 입력 이벤트(keyup)가 발생할 때마다 실행될 함수를 만듭니다.

```javascript
document.getElementById("inputText").addEventListener("keyup", function() {
  var inputValue = this.value;
  document.getElementById("outputText").textContent = inputValue;
});
```

위 코드의 동작 과정을 설명하면 다음과 같습니다.

1. `document.getElementById("inputText")`로 입력 양식을 선택합니다.
2. `addEventListener("keyup", function() { ... })`로 입력 양식에서 키보드 입력 이벤트(keyup)가 발생할 때마다 실행될 함수를 등록합니다.
3. 함수 내부에서 `this.value`로 입력 양식의 현재 값을 가져와 `inputValue` 변수에 저장합니다.
4. `document.getElementById("outputText")`로 입력 값을 출력할 영역을 선택합니다.
5. `textContent = inputValue`로 출력 영역의 텍스트 내용을 입력 값으로 변경합니다.

이제 웹 페이지에서 입력 양식에 키보드로 값을 입력하면, 입력한 값이 실시간으로 화면에 출력됩니다. 사용자는 자신이 입력한 내용을 즉시 확인할 수 있습니다.

이 기능은 검색어 입력, 양식 작성, 채팅 등 다양한 상황에서 유용하게 활용될 수 있습니다. 사용자의 입력 값을 실시간으로 처리하고 반영함으로써 더 나은 사용자 경험을 제공할 수 있습니다.

### 특정 키 입력 시 이벤트 발생시키기

웹 페이지에서 사용자가 키보드를 누를 때, 특정 키를 입력하면 원하는 동작을 수행하도록 만들 수 있습니다. 이를 위해 JavaScript에서는 키보드 이벤트를 활용합니다.

예를 들어, 사용자가 'Enter' 키를 누르면 폼을 제출하거나, 'Escape' 키를 누르면 팝업 창을 닫는 등의 기능을 구현할 수 있습니다.

이를 위해 다음과 같은 단계를 따릅니다:

1. 키보드 이벤트 리스너 등록하기
   - JavaScript에서 'keydown' 또는 'keyup' 이벤트를 사용하여 키보드 입력을 감지합니다.
   - 원하는 HTML 요소에 이벤트 리스너를 등록합니다.

2. 입력된 키 확인하기
   - 이벤트 객체의 'key' 또는 'keyCode' 속성을 사용하여 입력된 키를 확인합니다.
   - 'key' 속성은 키의 문자열 값을 반환하고, 'keyCode'는 키의 숫자 코드를 반환합니다.

3. 특정 키에 따른 동작 수행하기
   - 입력된 키가 원하는 키인지 확인하고, 해당 키에 맞는 동작을 수행합니다.
   - 예를 들어, 'Enter' 키라면 폼을 제출하고, 'Escape' 키라면 팝업 창을 닫는 등의 동작을 수행할 수 있습니다.

다음은 'Enter' 키를 누르면 메시지를 출력하는 예제 코드입니다:

```html
<input type="text" id="inputField">

<script>
  const inputField = document.getElementById('inputField');

  inputField.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      alert('Enter 키를 눌렀습니다!');
    }
  });
</script>
```

위 코드에서는 'inputField'라는 ID를 가진 입력 필드에 'keydown' 이벤트 리스너를 등록했습니다. 사용자가 키를 누를 때마다 이벤트 리스너 함수가 호출되고, 입력된 키가 'Enter'인지 확인합니다. 'Enter' 키라면 경고 메시지를 출력합니다.

이처럼 특정 키 입력 시 원하는 동작을 수행하도록 만들 수 있습니다. 이를 활용하여 사용자와의 상호작용을 향상시키고, 웹 페이지의 기능을 확장할 수 있습니다.
