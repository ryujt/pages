# 자바스크립트 입문서

## 시작하기

### 자바스크립트의 소개

자바스크립트는 웹 브라우저에서 동작하는 스크립트 언어로 시작했지만, 현재는 Node.js 환경에서도 널리 사용되고 있는 범용 프로그래밍 언어입니다. 자바스크립트는 객체 지향 프로그래밍과 함수형 프로그래밍 패러다임을 모두 지원하며, 동적 타입 언어로 분류됩니다.

Node.js 환경에서 자바스크립트를 사용하면 서버 사이드 애플리케이션을 개발할 수 있습니다. 이는 자바스크립트가 백엔드 개발에도 활용될 수 있음을 의미합니다. Node.js는 Chrome V8 자바스크립트 엔진을 기반으로 하며, 이벤트 기반 비동기 I/O 모델을 사용하여 높은 성능과 확장성을 제공합니다.

자바스크립트는 다음과 같은 특징을 가지고 있습니다:

1. 동적 타입 언어: 변수의 타입을 미리 선언할 필요가 없으며, 런타임에 타입이 결정됩니다.
2. 객체 지향 프로그래밍: 자바스크립트는 프로토타입 기반의 객체 지향 프로그래밍을 지원합니다.
3. 함수형 프로그래밍: 자바스크립트에서 함수는 일급 객체로 취급되며, 함수형 프로그래밍 기법을 활용할 수 있습니다.
4. 이벤트 기반 프로그래밍: 자바스크립트는 이벤트 기반 프로그래밍 모델을 사용하여 비동기 작업을 처리할 수 있습니다.
5. 풍부한 생태계: 자바스크립트는 대규모 개발자 커뮤니티와 다양한 라이브러리, 프레임워크를 가지고 있어 개발 생산성을 높일 수 있습니다.

Node.js 환경에서 자바스크립트를 사용하면 다음과 같은 작업을 수행할 수 있습니다:

1. 서버 사이드 애플리케이션 개발
2. 명령줄 도구 개발
3. 데스크톱 애플리케이션 개발 (Electron 등을 활용)
4. 실시간 애플리케이션 개발 (채팅, 게임 등)

자바스크립트는 배우기 쉬우면서도 강력한 기능을 제공하는 언어로, 웹 개발뿐만 아니라 다양한 분야에서 활용되고 있습니다. Node.js와 함께 사용함으로써 자바스크립트의 활용 범위는 더욱 확대되었으며, 풀스택 개발을 가능하게 해주는 언어로 자리잡았습니다.

### 개발환경 설치

Node.js는 자바스크립트를 브라우저 외부에서 실행할 수 있는 런타임 환경입니다. 이를 통해 자바스크립트로 서버를 구축하거나 데스크톱 애플리케이션을 개발할 수 있습니다.

1. Node.js 설치
   - Node.js 공식 웹사이트(https://nodejs.org)에 접속합니다.
   - 최신 LTS 버전을 다운로드하여 설치합니다.
   - 설치 과정에서 기본 설정을 유지하면 됩니다.

2. Node.js 설치 확인
   - 명령 프롬프트(Windows) 또는 터미널(macOS, Linux)을 엽니다.
   - 다음 명령어를 입력하여 Node.js의 버전을 확인합니다.
     ```
     node -v
     ```
   - 설치된 Node.js의 버전이 출력되면 정상적으로 설치된 것입니다.

3. Visual Studio Code 설치
   - Visual Studio Code는 마이크로소프트에서 개발한 무료 텍스트 에디터입니다.
   - 공식 웹사이트(https://code.visualstudio.com)에 접속하여 다운로드 페이지로 이동합니다.
   - 자신의 운영체제에 맞는 버전을 다운로드하여 설치합니다.

4. 자바스크립트 파일 생성
   - Visual Studio Code를 실행합니다.
   - 새로운 파일을 생성하고 확장자를 `.js`로 지정합니다. (예: `app.js`)

5. 자바스크립트 코드 작성
   - 생성한 `.js` 파일에 자바스크립트 코드를 작성합니다.
   - 예를 들어, 다음과 같이 간단한 코드를 작성할 수 있습니다.
     ```javascript
     console.log("Hello, JavaScript!");
     ```

6. 자바스크립트 파일 실행
   - Visual Studio Code의 터미널을 엽니다. (View > Terminal)
   - 터미널에서 자바스크립트 파일이 있는 디렉토리로 이동합니다.
   - 다음 명령어를 입력하여 자바스크립트 파일을 실행합니다.
     ```
     node app.js
     ```
   - 콘솔에 "Hello, JavaScript!"가 출력되면 정상적으로 실행된 것입니다.

이제 Node.js와 Visual Studio Code를 사용하여 자바스크립트 개발 환경을 설치하고 첫 번째 프로그램을 실행해보았습니다. 이를 기반으로 자바스크립트 문법과 기능을 학습하고 다양한 프로그램을 작성할 수 있습니다.

### 첫 번째 프로그램 실행

Node.js 환경에서 자바스크립트 프로그램을 실행하는 것은 매우 간단합니다. 다음 단계를 따라 첫 번째 프로그램을 실행해보겠습니다.

1. 새로운 디렉토리를 생성하고, 해당 디렉토리로 이동합니다.
   ```
   mkdir my-first-program
   cd my-first-program
   ```

2. 선호하는 텍스트 에디터 (예: Visual Studio Code)를 사용하여 `index.js` 파일을 생성합니다.

3. `index.js` 파일에 다음 코드를 입력합니다.
   ```javascript
   console.log("Hello, World!");
   ```

4. 터미널에서 다음 명령을 실행하여 프로그램을 실행합니다.
   ```
   node index.js
   ```

5. 터미널에 "Hello, World!"가 출력되는 것을 확인할 수 있습니다.

축하합니다! 첫 번째 자바스크립트 프로그램을 성공적으로 실행했습니다.

`console.log()`는 자바스크립트에서 가장 기본적인 출력 함수 중 하나입니다. 이 함수는 괄호 안에 전달된 값을 콘솔에 출력합니다. 문자열, 숫자, 불리언, 객체 등 다양한 값을 출력할 수 있습니다.

이제 `index.js` 파일에 더 많은 코드를 추가하고 프로그램을 확장할 수 있습니다. 예를 들어, 변수를 선언하고 연산을 수행한 후 결과를 출력할 수 있습니다.

```javascript
let name = "John";
let age = 25;

console.log("My name is " + name + " and I am " + age + " years old.");
```

위 코드를 `index.js`에 추가하고 다시 `node index.js`를 실행하면, 콘솔에 "My name is John and I am 25 years old."가 출력됩니다.

이렇게 Node.js 환경에서 자바스크립트 파일을 생성하고 실행하는 기본적인 과정을 알아보았습니다. 이제 더 복잡한 프로그램을 작성하고 실행할 준비가 되었습니다.

## 자료와 변수

자바스크립트에서 자료와 변수는 프로그램의 기본 구성 요소입니다. 자료는 프로그램에서 처리할 데이터를 의미하며, 변수는 이러한 자료를 저장하는 메모리 공간을 나타냅니다.

### 기본 자료형

자바스크립트에는 다음과 같은 기본 자료형이 있습니다.

1. 숫자 (Number)
   - 정수와 실수를 모두 포함하는 자료형입니다.
   - 예: `let num = 10;`, `let pi = 3.14;`

2. 문자열 (String)
   - 문자의 나열을 표현하는 자료형입니다.
   - 작은따옴표('') 또는 큰따옴표("")로 감싸서 표현합니다.
   - 예: `let str = "Hello, World!";`, `let name = 'John';`

3. 불리언 (Boolean)
   - 참(true)과 거짓(false)을 나타내는 자료형입니다.
   - 조건문이나 반복문에서 주로 사용됩니다.
   - 예: `let isTrue = true;`, `let isFalse = false;`

4. undefined
   - 변수가 선언되었지만 값이 할당되지 않은 상태를 나타내는 자료형입니다.
   - 예: `let undef;`, `console.log(undef); // undefined`

5. null
   - 변수에 의도적으로 빈 값을 할당할 때 사용되는 자료형입니다.
   - 예: `let nullValue = null;`

6. 심볼 (Symbol)
   - ES6에서 새로 추가된 자료형으로, 고유한 식별자를 생성할 때 사용됩니다.
   - 예: `let sym = Symbol("description");`

자바스크립트에서는 변수를 선언할 때 자료형을 명시하지 않습니다. 변수에 할당되는 값에 따라 자료형이 동적으로 결정됩니다. 이를 동적 타이핑(dynamic typing)이라고 합니다.

```javascript
let num = 10;
console.log(typeof num); // "number"

let str = "Hello";
console.log(typeof str); // "string"

let bool = true;
console.log(typeof bool); // "boolean"
```

`typeof` 연산자를 사용하여 변수의 자료형을 확인할 수 있습니다.

자바스크립트에서는 변수의 자료형이 동적으로 변할 수 있기 때문에 주의해야 합니다. 예를 들어, 숫자 변수에 문자열을 할당하면 자료형이 문자열로 변경됩니다.

```javascript
let num = 10;
console.log(typeof num); // "number"

num = "Hello";
console.log(typeof num); // "string"
```

이러한 동적 타이핑은 유연성을 제공하지만, 코드의 예측 가능성을 떨어뜨릴 수 있으므로 적절한 변수 이름과 일관된 자료형 사용이 중요합니다.

### 상수와 변수

자바스크립트에서 상수와 변수는 데이터를 저장하고 참조하는 데 사용됩니다. 상수는 한 번 할당된 값을 변경할 수 없는 반면, 변수는 값을 변경할 수 있습니다.

1. 상수 선언
   - 상수를 선언할 때는 `const` 키워드를 사용합니다.
   - 상수는 선언과 동시에 값을 할당해야 합니다.
   - 상수의 이름은 일반적으로 대문자로 작성하며, 여러 단어로 이루어진 경우 언더스코어(_)로 구분합니다.

   ```javascript
   const PI = 3.14;
   const MAX_VALUE = 100;
   ```

2. 변수 선언
   - 변수를 선언할 때는 `let` 키워드를 사용합니다.
   - 변수는 선언과 동시에 값을 할당할 수도 있고, 나중에 값을 할당할 수도 있습니다.
   - 변수의 이름은 일반적으로 카멜 케이스(camelCase)로 작성합니다.

   ```javascript
   let count = 0;
   let userName = "John";
   let isLoggedIn = false;
   ```

3. 변수 값 변경
   - 변수는 `=` 연산자를 사용하여 값을 변경할 수 있습니다.
   - 변수에 새로운 값을 할당하면 이전 값은 덮어씌워집니다.

   ```javascript
   let count = 0;
   count = 5;
   count = count + 1;
   ```

4. 변수 범위(스코프)
   - `let`과 `const`로 선언한 변수는 블록 범위(block scope)를 가집니다.
   - 블록(`{}`) 내부에서 선언된 변수는 해당 블록 내에서만 접근할 수 있습니다.

   ```javascript
   let x = 10;

   if (true) {
     let y = 20;
     console.log(x); // 10
     console.log(y); // 20
   }

   console.log(x); // 10
   console.log(y); // ReferenceError: y is not defined
   ```

5. 변수 호이스팅(Variable Hoisting)
   - 자바스크립트에서는 변수 선언이 해당 스코프의 맨 위로 끌어올려지는 현상이 있습니다.
   - `let`과 `const`로 선언한 변수는 호이스팅되지만, 초기화는 되지 않습니다.
   - 변수를 선언하기 전에 접근하려고 하면 `ReferenceError`가 발생합니다.

   ```javascript
   console.log(x); // ReferenceError: Cannot access 'x' before initialization
   let x = 10;
   ```

상수와 변수를 적절히 사용하여 코드의 가독성과 유지보수성을 높일 수 있습니다. 상수는 값이 변경되지 않는 경우에 사용하고, 변수는 값이 변경될 수 있는 경우에 사용합니다.

### 자료형 변환

자바스크립트에서는 자료형 변환이 자주 사용됩니다. 자료형 변환은 값의 타입을 다른 타입으로 변환하는 것을 의미합니다. 자바스크립트에서는 암시적 변환과 명시적 변환, 두 가지 방법으로 자료형을 변환할 수 있습니다.

1. 암시적 변환 (Implicit Conversion)
   - 자바스크립트 엔진이 자동으로 자료형을 변환하는 것을 말합니다.
   - 예를 들어, 문자열과 숫자를 더하면 숫자가 문자열로 변환되어 연결됩니다.
     ```javascript
     console.log("10" + 20); // 출력: "1020"
     ```

2. 명시적 변환 (Explicit Conversion)
   - 개발자가 직접 자료형을 변환하는 것을 말합니다.
   - 주로 사용되는 명시적 변환 방법은 다음과 같습니다.

     - 문자열로 변환:
       - `String()` 함수 또는 `toString()` 메서드를 사용합니다.
         ```javascript
         console.log(String(123)); // 출력: "123"
         console.log((123).toString()); // 출력: "123"
         ```

     - 숫자로 변환:
       - `Number()` 함수 또는 `parseInt()`, `parseFloat()` 함수를 사용합니다.
         ```javascript
         console.log(Number("123")); // 출력: 123
         console.log(parseInt("123")); // 출력: 123
         console.log(parseFloat("123.45")); // 출력: 123.45
         ```

     - 불리언으로 변환:
       - `Boolean()` 함수를 사용합니다.
         ```javascript
         console.log(Boolean(0)); // 출력: false
         console.log(Boolean("")); // 출력: false
         console.log(Boolean(null)); // 출력: false
         console.log(Boolean(undefined)); // 출력: false
         console.log(Boolean(NaN)); // 출력: false
         console.log(Boolean(1)); // 출력: true
         console.log(Boolean("hello")); // 출력: true
         ```

자료형 변환은 자바스크립트에서 매우 중요한 개념입니다. 암시적 변환은 편리하지만 예상치 못한 결과를 초래할 수 있으므로 주의해야 합니다. 명시적 변환을 사용하면 코드의 의도를 명확히 할 수 있습니다.

예를 들어, 사용자로부터 입력받은 값은 문자열 형태이므로 숫자로 변환해야 할 때가 있습니다. 이때 `Number()` 함수나 `parseInt()`, `parseFloat()` 함수를 사용하여 명시적으로 변환할 수 있습니다.

자료형 변환을 적절히 사용하면 코드의 가독성과 안정성을 높일 수 있습니다.

## 배열

배열은 여러 개의 값을 순차적으로 저장할 수 있는 자료구조입니다. 자바스크립트에서 배열은 동적으로 크기가 변경될 수 있으며, 다양한 데이터 타입을 함께 저장할 수 있습니다.

1. 배열 선언 및 초기화
   - 배열을 선언할 때는 대괄호([])를 사용합니다.
   - 배열 내부의 요소는 쉼표(,)로 구분합니다.
   - 예시:
     ```javascript
     let arr = [1, 2, 3, 4, 5];
     ```

2. 배열 요소 접근
   - 배열의 각 요소에는 인덱스를 통해 접근할 수 있습니다.
   - 인덱스는 0부터 시작하며, 배열의 길이보다 1 작은 값까지 사용할 수 있습니다.
   - 예시:
     ```javascript
     let arr = [1, 2, 3, 4, 5];
     console.log(arr[0]); // 1
     console.log(arr[2]); // 3
     ```

3. 배열 길이
   - 배열의 길이는 `length` 속성을 통해 확인할 수 있습니다.
   - 예시:
     ```javascript
     let arr = [1, 2, 3, 4, 5];
     console.log(arr.length); // 5
     ```

4. 배열 메서드
   - 자바스크립트는 배열을 다루기 위한 다양한 내장 메서드를 제공합니다.
   - `push()`: 배열의 끝에 새로운 요소를 추가합니다.
   - `pop()`: 배열의 마지막 요소를 제거하고 반환합니다.
   - `shift()`: 배열의 첫 번째 요소를 제거하고 반환합니다.
   - `unshift()`: 배열의 시작 부분에 새로운 요소를 추가합니다.
   - `slice()`: 배열의 일부분을 새로운 배열로 반환합니다.
   - `splice()`: 배열의 요소를 추가, 제거 또는 교체합니다.
   - 예시:
     ```javascript
     let arr = [1, 2, 3];
     arr.push(4);
     console.log(arr); // [1, 2, 3, 4]

     let lastElement = arr.pop();
     console.log(lastElement); // 4
     console.log(arr); // [1, 2, 3]

     let firstElement = arr.shift();
     console.log(firstElement); // 1
     console.log(arr); // [2, 3]

     arr.unshift(0);
     console.log(arr); // [0, 2, 3]

     let slicedArr = arr.slice(1, 3);
     console.log(slicedArr); // [2, 3]

     arr.splice(1, 1, 'a', 'b');
     console.log(arr); // [0, 'a', 'b', 3]
     ```

5. 배열 순회
   - 배열의 각 요소를 순회하기 위해 `for` 반복문이나 `forEach()` 메서드를 사용할 수 있습니다.
   - 예시:
     ```javascript
     let arr = [1, 2, 3, 4, 5];

     for (let i = 0; i < arr.length; i++) {
       console.log(arr[i]);
     }

     arr.forEach(function(element) {
       console.log(element);
     });
     ```

배열은 자바스크립트에서 매우 유용하고 자주 사용되는 자료구조입니다. 배열을 활용하면 여러 개의 값을 효율적으로 저장하고 처리할 수 있습니다.

## 연산자

연산자는 값을 조작하고 결합하는 데 사용되는 기호입니다. 자바스크립트에는 다양한 유형의 연산자가 있습니다.

### 기본 연산자

자바스크립트에서는 다양한 기본 연산자를 제공합니다. 기본 연산자는 산술 연산자, 할당 연산자, 비교 연산자 등이 있습니다.

1. 산술 연산자
   - 더하기 연산자 (`+`): 두 개의 피연산자를 더합니다.
     ```javascript
     let result = 5 + 3; // 결과: 8
     ```
   - 빼기 연산자 (`-`): 첫 번째 피연산자에서 두 번째 피연산자를 뺍니다.
     ```javascript
     let result = 5 - 3; // 결과: 2
     ```
   - 곱하기 연산자 (`*`): 두 개의 피연산자를 곱합니다.
     ```javascript
     let result = 5 * 3; // 결과: 15
     ```
   - 나누기 연산자 (`/`): 첫 번째 피연산자를 두 번째 피연산자로 나눕니다.
     ```javascript
     let result = 10 / 2; // 결과: 5
     ```
   - 나머지 연산자 (`%`): 첫 번째 피연산자를 두 번째 피연산자로 나눈 후 나머지를 반환합니다.
     ```javascript
     let result = 10 % 3; // 결과: 1
     ```

2. 할당 연산자
   - 등호 연산자 (`=`): 변수에 값을 할당합니다.
     ```javascript
     let x = 5;
     ```
   - 더하기 등호 연산자 (`+=`): 변수에 값을 더한 후 결과를 다시 변수에 할당합니다.
     ```javascript
     let x = 5;
     x += 3; // x = x + 3과 동일
     console.log(x); // 결과: 8
     ```
   - 빼기 등호 연산자 (`-=`): 변수에서 값을 뺀 후 결과를 다시 변수에 할당합니다.
     ```javascript
     let x = 5;
     x -= 3; // x = x - 3과 동일
     console.log(x); // 결과: 2
     ```
   - 곱하기 등호 연산자 (`*=`): 변수에 값을 곱한 후 결과를 다시 변수에 할당합니다.
     ```javascript
     let x = 5;
     x *= 3; // x = x * 3과 동일
     console.log(x); // 결과: 15
     ```
   - 나누기 등호 연산자 (`/=`): 변수를 값으로 나눈 후 결과를 다시 변수에 할당합니다.
     ```javascript
     let x = 10;
     x /= 2; // x = x / 2와 동일
     console.log(x); // 결과: 5
     ```

3. 비교 연산자
   - 동등 연산자 (`==`): 두 값이 같은지 비교합니다. (타입은 고려하지 않음)
     ```javascript
     console.log(5 == "5"); // 결과: true
     ```
   - 일치 연산자 (`===`): 두 값과 타입이 모두 같은지 비교합니다.
     ```javascript
     console.log(5 === "5"); // 결과: false
     ```
   - 부등 연산자 (`!=`): 두 값이 다른지 비교합니다. (타입은 고려하지 않음)
     ```javascript
     console.log(5 != "5"); // 결과: false
     ```
   - 불일치 연산자 (`!==`): 두 값 또는 타입이 다른지 비교합니다.
     ```javascript
     console.log(5 !== "5"); // 결과: true
     ```
   - 크다 연산자 (`>`): 첫 번째 피연산자가 두 번째 피연산자보다 큰지 비교합니다.
     ```javascript
     console.log(5 > 3); // 결과: true
     ```
   - 크거나 같다 연산자 (`>=`): 첫 번째 피연산자가 두 번째 피연산자보다 크거나 같은지 비교합니다.
     ```javascript
     console.log(5 >= 5); // 결과: true
     ```
   - 작다 연산자 (`<`): 첫 번째 피연산자가 두 번째 피연산자보다 작은지 비교합니다.
     ```javascript
     console.log(5 < 3); // 결과: false
     ```
   - 작거나 같다 연산자 (`<=`): 첫 번째 피연산자가 두 번째 피연산자보다 작거나 같은지 비교합니다.
     ```javascript
     console.log(5 <= 5); // 결과: true
     ```

이러한 기본 연산자를 사용하여 자바스크립트에서 다양한 연산을 수행할 수 있습니다. 연산자의 우선순위에 유의하면서 필요에 따라 괄호를 사용하여 연산 순서를 명확히 할 수 있습니다.

### 논리 연산자

논리 연산자는 주어진 조건들을 논리적으로 결합하여 참(true) 또는 거짓(false)을 판단하는 데 사용됩니다. 자바스크립트에서는 세 가지 주요 논리 연산자가 있습니다: AND(&&), OR(||), NOT(!).

1. AND 연산자 (&&)
   - AND 연산자는 두 개의 조건이 모두 참일 때만 true를 반환합니다.
   - 예시:
     ```javascript
     let x = 5;
     let y = 10;
     console.log(x > 0 && y > 0); // true
     console.log(x > 0 && y < 0); // false
     ```

2. OR 연산자 (||)
   - OR 연산자는 두 개의 조건 중 하나 이상이 참이면 true를 반환합니다.
   - 예시:
     ```javascript
     let x = 5;
     let y = -10;
     console.log(x > 0 || y > 0); // true
     console.log(x < 0 || y < 0); // true
     console.log(x < 0 || y > 0); // false
     ```

3. NOT 연산자 (!)
   - NOT 연산자는 조건의 반대 값을 반환합니다. 즉, 조건이 true이면 false를, false이면 true를 반환합니다.
   - 예시:
     ```javascript
     let x = 5;
     console.log(!(x > 0)); // false
     console.log(!(x < 0)); // true
     ```

논리 연산자는 조건문과 함께 자주 사용됩니다. 예를 들어, if 문에서 여러 조건을 결합할 때 논리 연산자를 사용할 수 있습니다.

```javascript
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
  console.log("운전할 수 있습니다.");
} else {
  console.log("운전할 수 없습니다.");
}
```

위의 예시에서는 AND 연산자를 사용하여 두 가지 조건(나이가 18세 이상이고 운전면허증이 있는지)을 확인합니다. 두 조건이 모두 참이면 "운전할 수 있습니다."가 출력되고, 그렇지 않으면 "운전할 수 없습니다."가 출력됩니다.

논리 연산자를 적절히 사용하면 코드의 가독성과 효율성을 높일 수 있습니다.

### 삼항 연산자

삼항 연산자는 조건에 따라 값을 선택할 수 있는 간단한 조건 연산자입니다. 삼항 연산자의 기본 형태는 다음과 같습니다.

```javascript
조건식 ? 값1 : 값2
```

삼항 연산자는 먼저 조건식을 평가합니다. 조건식이 참(true)이면 값1이 선택되고, 거짓(false)이면 값2가 선택됩니다.

예를 들어, 다음 코드에서는 age 변수의 값에 따라 메시지를 다르게 출력합니다.

```javascript
const age = 20;
const message = age >= 18 ? "성인입니다." : "미성년자입니다.";
console.log(message);
```

위 코드에서 age가 18 이상이면 "성인입니다."가 message 변수에 할당되고, 18 미만이면 "미성년자입니다."가 할당됩니다. 따라서 콘솔에는 "성인입니다."가 출력됩니다.

삼항 연산자는 if 조건문을 간단하게 표현할 수 있어 코드의 가독성을 높일 수 있습니다. 하지만 너무 복잡한 조건식을 사용하면 오히려 가독성이 떨어질 수 있으므로 주의해야 합니다.

삼항 연산자는 중첩해서 사용할 수도 있습니다. 다음은 중첩된 삼항 연산자의 예시입니다.

```javascript
const score = 85;
const grade = score >= 90 ? "A" :
              score >= 80 ? "B" :
              score >= 70 ? "C" :
              score >= 60 ? "D" : "F";
console.log(`당신의 학점은 ${grade}입니다.`);
```

위 코드에서는 score 변수의 값에 따라 학점을 출력합니다. 첫 번째 조건식에서 score가 90 이상인지 확인하고, 90 이상이면 "A"를 grade 변수에 할당합니다. 90 미만이면 다음 조건식으로 넘어가서 score가 80 이상인지 확인하고, 80 이상이면 "B"를 할당합니다. 이런 식으로 계속 조건식을 평가하여 학점을 결정합니다.

삼항 연산자를 사용할 때는 가독성을 고려하여 적절히 사용해야 합니다. 간단한 조건식에는 삼항 연산자를 사용하고, 복잡한 조건식에는 if 조건문을 사용하는 것이 좋습니다.

## 조건문

자바스크립트에서 조건문은 특정 조건에 따라 코드의 실행 여부를 결정하는 구문입니다. 조건문을 사용하면 프로그램의 흐름을 제어할 수 있습니다. 자바스크립트에는 두 가지 주요 조건문이 있습니다: `if` 조건문과 `switch` 조건문입니다.

### if 조건문

if 조건문은 주어진 조건식이 참(true)인 경우에만 특정 코드 블록을 실행하는 데 사용됩니다. 조건식이 거짓(false)인 경우에는 해당 코드 블록을 건너뜁니다.

기본 구문은 다음과 같습니다:

```javascript
if (조건식) {
  // 조건식이 참인 경우 실행할 코드
}
```

예를 들어, 숫자가 양수인지 확인하는 if 조건문은 다음과 같이 작성할 수 있습니다:

```javascript
const number = 5;

if (number > 0) {
  console.log("숫자는 양수입니다.");
}
```

위의 예시에서 `number`가 0보다 크기 때문에 조건식이 참이 되어 `"숫자는 양수입니다."`가 콘솔에 출력됩니다.

if 조건문은 `else` 절과 함께 사용하여 조건식이 거짓인 경우에 실행할 코드를 지정할 수도 있습니다.

```javascript
const number = -3;

if (number > 0) {
  console.log("숫자는 양수입니다.");
} else {
  console.log("숫자는 양수가 아닙니다.");
}
```

위의 예시에서 `number`가 0보다 작기 때문에 조건식이 거짓이 되어 `else` 절의 코드 블록이 실행되고 `"숫자는 양수가 아닙니다."`가 콘솔에 출력됩니다.

여러 개의 조건을 확인해야 하는 경우에는 `else if` 절을 사용할 수 있습니다.

```javascript
const number = 0;

if (number > 0) {
  console.log("숫자는 양수입니다.");
} else if (number < 0) {
  console.log("숫자는 음수입니다.");
} else {
  console.log("숫자는 0입니다.");
}
```

위의 예시에서 `number`가 0이기 때문에 첫 번째 조건식과 두 번째 조건식이 모두 거짓이 되어 마지막 `else` 절의 코드 블록이 실행되고 `"숫자는 0입니다."`가 콘솔에 출력됩니다.

if 조건문은 다양한 조건식을 사용할 수 있으며, 논리 연산자(`&&`, `||`, `!`)를 사용하여 복잡한 조건을 표현할 수도 있습니다.

이렇게 if 조건문을 사용하면 프로그램의 흐름을 제어하고 조건에 따라 다른 동작을 수행할 수 있습니다.

### switch 조건문

switch 조건문은 특정 변수의 값에 따라 다른 코드 블록을 실행할 수 있게 해주는 조건문입니다. 여러 가지 경우 중 하나를 선택하여 실행할 때 유용합니다.

switch 조건문의 기본 구조는 다음과 같습니다:

```javascript
switch (변수) {
  case 값1:
    // 변수가 값1과 일치할 때 실행할 코드
    break;
  case 값2:
    // 변수가 값2와 일치할 때 실행할 코드
    break;
  ...
  default:
    // 변수가 어떤 case와도 일치하지 않을 때 실행할 코드
}
```

switch 키워드 다음에 괄호 안에 조건을 판별할 변수를 지정합니다. 그 다음에는 중괄호 안에 case 키워드와 함께 변수가 가질 수 있는 값들을 지정합니다. 각 case 블록 끝에는 break 키워드를 사용하여 switch 조건문을 빠져나갑니다. 만약 변수의 값이 어떤 case와도 일치하지 않으면 default 블록이 실행됩니다.

예를 들어, 요일을 나타내는 숫자가 주어졌을 때 해당 요일의 이름을 출력하는 코드를 switch 조건문으로 작성할 수 있습니다:

```javascript
const dayNumber = 3;

switch (dayNumber) {
  case 0:
    console.log("일요일");
    break;
  case 1:
    console.log("월요일");
    break;
  case 2:
    console.log("화요일");
    break;
  case 3:
    console.log("수요일");
    break;
  case 4:
    console.log("목요일");
    break;
  case 5:
    console.log("금요일");
    break;
  case 6:
    console.log("토요일");
    break;
  default:
    console.log("잘못된 요일 번호입니다.");
}
```

위 코드에서 dayNumber 변수의 값이 3이므로 "수요일"이 출력됩니다.

switch 조건문은 if-else if-else 조건문과 비슷한 역할을 하지만, 코드의 가독성과 성능 면에서 장점이 있습니다. 특히 조건이 많고 각 조건에 따라 실행할 코드 블록이 간단할 때 switch 조건문을 사용하면 코드를 더 깔끔하게 작성할 수 있습니다.

## 반복문

반복문은 특정 코드 블록을 여러 번 반복하여 실행할 수 있게 해주는 제어 구조입니다. 자바스크립트에서는 주로 `for`문과 `while`문을 사용하여 반복문을 구현합니다.

### for 반복문

for 반복문은 자바스크립트에서 가장 많이 사용되는 반복문 중 하나입니다. for 반복문은 주어진 조건이 참인 동안 코드 블록을 반복 실행합니다.

for 반복문의 기본 구조는 다음과 같습니다:

```javascript
for (초기화; 조건; 증감) {
  // 실행할 코드
}
```

- 초기화: 반복문이 시작될 때 한 번만 실행되는 부분입니다. 주로 반복문에서 사용될 변수를 초기화합니다.
- 조건: 반복문이 계속 실행되기 위한 조건입니다. 이 조건이 참인 동안 반복문이 계속 실행됩니다.
- 증감: 반복문이 한 번 실행된 후에 수행되는 부분입니다. 주로 초기화에서 선언한 변수의 값을 변경하는 데 사용됩니다.

예를 들어, 1부터 10까지의 숫자를 출력하는 for 반복문은 다음과 같이 작성할 수 있습니다:

```javascript
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

위 코드에서:
- 초기화 부분에서 변수 `i`를 1로 초기화합니다.
- 조건 부분에서 `i`가 10보다 작거나 같은지 확인합니다.
- 증감 부분에서 `i`를 1씩 증가시킵니다.

따라서 이 코드는 1부터 10까지의 숫자를 차례대로 출력합니다.

for 반복문은 배열과 함께 자주 사용됩니다. 배열의 각 요소에 접근하기 위해 for 반복문을 사용할 수 있습니다.

```javascript
const fruits = ['apple', 'banana', 'orange'];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

위 코드는 `fruits` 배열의 각 요소를 차례대로 출력합니다.

for 반복문은 중첩될 수 있습니다. 즉, for 반복문 내부에 다른 for 반복문을 사용할 수 있습니다. 이는 2차원 배열을 다룰 때 유용합니다.

```javascript
const matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

for (let i = 0; i < matrix.length; i++) {
  for (let j = 0; j < matrix[i].length; j++) {
    console.log(matrix[i][j]);
  }
}
```

위 코드는 2차원 배열 `matrix`의 모든 요소를 출력합니다.

이 외에도 for 반복문은 다양한 상황에서 사용될 수 있습니다. 조건과 증감 부분을 적절히 조정하여 필요한 반복 동작을 구현할 수 있습니다.

### while 반복문

while 반복문은 주어진 조건이 참(true)인 동안 반복해서 코드 블록을 실행합니다. 조건이 거짓(false)이 되면 반복문을 종료하고 다음 코드로 넘어갑니다.

while 반복문의 기본 구조는 다음과 같습니다:

```javascript
while (조건) {
  // 조건이 참인 동안 반복 실행될 코드
}
```

예를 들어, 1부터 5까지의 숫자를 출력하는 while 반복문은 다음과 같이 작성할 수 있습니다:

```javascript
let i = 1;

while (i <= 5) {
  console.log(i);
  i++;
}
```

위 코드에서는 변수 `i`를 1로 초기화하고, `i`가 5 이하일 때까지 반복문을 실행합니다. 반복문 내부에서는 `console.log()`를 사용하여 `i`의 값을 출력하고, `i`를 1씩 증가시킵니다.

실행 결과:
```
1
2
3
4
5
```

while 반복문은 조건이 항상 참이 되도록 작성하면 무한 반복문이 될 수 있으므로 주의해야 합니다. 무한 반복문은 프로그램을 종료할 수 없는 상태가 되므로 의도적으로 사용하는 경우가 아니라면 피해야 합니다.

```javascript
while (true) {
  // 무한 반복문
}
```

while 반복문 내부에서 `break` 키워드를 사용하면 반복문을 즉시 종료할 수 있습니다. 또한, `continue` 키워드를 사용하면 해당 반복을 건너뛰고 다음 반복으로 넘어갈 수 있습니다.

```javascript
let i = 0;

while (i < 10) {
  i++;
  if (i === 5) {
    continue;
  }
  console.log(i);
  if (i === 8) {
    break;
  }
}
```

위 코드에서는 `i`가 5일 때는 `continue`를 만나 해당 반복을 건너뛰고, `i`가 8일 때는 `break`를 만나 반복문을 종료합니다.

실행 결과:
```
1
2
3
4
6
7
8
```

이렇게 while 반복문을 사용하여 조건에 따라 코드 블록을 반복 실행할 수 있습니다. 조건을 적절히 설정하고, 반복문 내부에서 변수를 갱신하는 것이 중요합니다.

## 함수

함수는 특정 작업을 수행하는 코드 블록입니다. 함수를 사용하면 코드를 더 구조적으로 작성할 수 있고, 코드의 재사용성을 높일 수 있습니다.

### 함수의 기본 형태

함수는 특정 작업을 수행하는 코드 블록으로, 필요할 때마다 호출하여 사용할 수 있습니다. 함수를 사용하면 코드의 재사용성과 가독성을 높일 수 있습니다.

함수의 기본 형태는 다음과 같습니다:

```javascript
function 함수명(매개변수1, 매개변수2, ...) {
  // 함수 내부에서 실행될 코드
  return 반환값;
}
```

- `function` 키워드를 사용하여 함수를 선언합니다.
- 함수명은 함수를 식별하는 이름으로, 함수를 호출할 때 사용됩니다.
- 매개변수는 함수에 전달할 값을 받는 변수입니다. 필요에 따라 여러 개의 매개변수를 선언할 수 있습니다.
- 함수 내부에는 실행될 코드를 작성합니다.
- `return` 키워드를 사용하여 함수의 실행 결과를 반환할 수 있습니다.

예를 들어, 두 수를 더하는 함수를 다음과 같이 작성할 수 있습니다:

```javascript
function add(a, b) {
  return a + b;
}
```

함수를 호출할 때는 함수명 뒤에 괄호를 붙이고, 필요한 인자를 전달합니다.

```javascript
const result = add(3, 5);
console.log(result); // 8
```

위 코드에서 `add` 함수를 호출하면서 인자로 `3`과 `5`를 전달하였습니다. 함수 내부에서 `a`와 `b`는 각각 `3`과 `5`로 초기화되고, 두 값을 더한 결과인 `8`이 반환됩니다.

함수는 매개변수를 받지 않을 수도 있고, 반환값이 없을 수도 있습니다. 또한, 함수를 변수에 할당하거나 다른 함수의 인자로 전달할 수도 있습니다.

```javascript
function greet() {
  console.log("Hello, World!");
}

greet(); // "Hello, World!" 출력
```

위 코드에서 `greet` 함수는 매개변수와 반환값이 없는 함수입니다. 함수를 호출하면 "Hello, World!"가 출력됩니다.

함수는 자바스크립트에서 매우 중요한 역할을 하며, 코드의 구조를 개선하고 재사용성을 높이는 데 도움을 줍니다.

### 함수 고급

함수는 자바스크립트에서 매우 중요한 개념입니다. 함수를 더 깊이 이해하고 활용하기 위해 다음과 같은 내용을 알아보겠습니다.

1. 함수 표현식 (Function Expression)
   - 함수 선언문 (Function Declaration)과 달리, 함수 표현식은 변수에 함수를 할당하는 방식입니다.
   - 예시:
     ```javascript
     const add = function(a, b) {
       return a + b;
     };
     ```

2. 화살표 함수 (Arrow Function)
   - ES6에 도입된 화살표 함수는 함수를 더 간결하게 작성할 수 있게 해줍니다.
   - 예시:
     ```javascript
     const multiply = (a, b) => a * b;
     ```

3. 고차 함수 (Higher-Order Function)
   - 고차 함수는 함수를 인자로 받거나 함수를 반환하는 함수입니다.
   - 예시:
     ```javascript
     function applyOperation(a, b, operation) {
       return operation(a, b);
     }

     const result = applyOperation(3, 4, (a, b) => a + b);
     ```

4. 콜백 함수 (Callback Function)
   - 콜백 함수는 다른 함수의 인자로 전달되어 특정 시점에 호출되는 함수입니다.
   - 예시:
     ```javascript
     function fetchData(callback) {
       // 데이터를 가져오는 로직
       const data = [1, 2, 3, 4, 5];
       callback(data);
     }

     fetchData(function(data) {
       console.log(data);
     });
     ```

5. 클로저 (Closure)
   - 클로저는 함수가 생성될 때의 환경을 기억하고, 해당 환경에 접근할 수 있는 함수입니다.
   - 예시:
     ```javascript
     function outerFunction(x) {
       return function innerFunction(y) {
         return x + y;
       };
     }

     const addFive = outerFunction(5);
     console.log(addFive(3)); // 8
     ```

6. 재귀 함수 (Recursive Function)
   - 재귀 함수는 자기 자신을 호출하는 함수입니다.
   - 예시 (팩토리얼 계산):
     ```javascript
     function factorial(n) {
       if (n === 0) {
         return 1;
       }
       return n * factorial(n - 1);
     }

     console.log(factorial(5)); // 120
     ```

이러한 함수의 고급 개념을 이해하고 활용함으로써, 더 효율적이고 가독성 높은 코드를 작성할 수 있습니다. 함수는 자바스크립트에서 매우 유연하고 강력한 도구이므로, 다양한 상황에서 적절히 사용할 수 있도록 연습하는 것이 중요합니다.

### 함수의 기본 파라미터

함수를 정의할 때, 파라미터에 기본값을 설정할 수 있습니다. 이를 기본 파라미터(default parameter)라고 합니다. 기본 파라미터를 사용하면 함수 호출 시 해당 파라미터를 전달하지 않았을 때 기본값이 자동으로 할당됩니다.

기본 파라미터는 다음과 같이 정의할 수 있습니다:

```javascript
function greet(name = 'Anonymous') {
  console.log(`Hello, ${name}!`);
}
```

위 예시에서 `name` 파라미터의 기본값은 `'Anonymous'`로 설정되어 있습니다. 따라서 `greet()` 함수를 파라미터 없이 호출하면 `'Anonymous'`가 `name`의 값으로 사용됩니다.

```javascript
greet(); // "Hello, Anonymous!" 출력
greet('John'); // "Hello, John!" 출력
```

기본 파라미터는 여러 개 설정할 수 있으며, 필요에 따라 일부 파라미터만 기본값을 지정할 수도 있습니다.

```javascript
function introduce(name, age = 25, job = 'Developer') {
  console.log(`My name is ${name}, I'm ${age} years old, and I work as a ${job}.`);
}

introduce('Alice'); // "My name is Alice, I'm 25 years old, and I work as a Developer." 출력
introduce('Bob', 30); // "My name is Bob, I'm 30 years old, and I work as a Developer." 출력
introduce('Charlie', 35, 'Designer'); // "My name is Charlie, I'm 35 years old, and I work as a Designer." 출력
```

위 예시에서 `age`와 `job` 파라미터는 기본값이 설정되어 있습니다. 함수 호출 시 해당 파라미터를 전달하지 않으면 기본값이 사용됩니다.

기본 파라미터를 사용하면 함수 호출 시 파라미터 전달을 유연하게 할 수 있으며, 코드의 가독성과 유지보수성을 높일 수 있습니다. 또한 파라미터 개수가 많은 함수에서 일부 파라미터를 생략할 수 있어 편리합니다.

## 비동기 처리

자바스크립트에서 비동기 처리는 코드의 실행 순서를 제어하고, 블로킹 없이 작업을 수행할 수 있게 해주는 중요한 개념입니다. 비동기 처리를 사용하면 시간이 오래 걸리는 작업을 수행하는 동안에도 다른 작업을 계속 진행할 수 있습니다.

자바스크립트에서 비동기 처리를 다루는 대표적인 방법으로는 콜백 함수, Promise, async/await 등이 있습니다.

### 콜백 함수
콜백 함수는 다른 함수의 인자로 전달되는 함수를 말합니다. 비동기 작업이 완료되면 콜백 함수가 호출되어 결과를 처리합니다.

```javascript
function asyncOperation(callback) {
  setTimeout(() => {
    const result = 'Async operation completed';
    callback(result);
  }, 1000);
}

asyncOperation((result) => {
  console.log(result);
});
```

위 예제에서 `asyncOperation` 함수는 1초 후에 콜백 함수를 호출하여 결과를 전달합니다.

### Promise

Promise는 비동기 작업의 최종 완료 또는 실패를 나타내는 객체입니다. 주로 서버에서 데이터를 받아오거나, 파일을 읽어들이는 등의 비동기 작업을 처리할 때 사용됩니다.

Promise는 다음과 같은 세 가지 상태를 가집니다:

1. Pending(대기): 비동기 처리가 아직 완료되지 않은 상태
2. Fulfilled(이행): 비동기 처리가 완료되어 Promise가 결과 값을 반환한 상태
3. Rejected(실패): 비동기 처리가 실패하거나 오류가 발생한 상태

Promise는 `new Promise()` 생성자 함수를 사용하여 생성할 수 있습니다. 생성자 함수는 `resolve`와 `reject` 두 개의 매개변수를 갖는 콜백 함수를 인자로 받습니다.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // 비동기 작업을 수행하는 코드
  // ...
  if (/* 비동기 작업 성공 */) {
    resolve(result); // 성공한 경우 resolve() 호출
  } else {
    reject(error); // 실패한 경우 reject() 호출
  }
});
```

Promise 객체가 생성되면 `then()`과 `catch()` 메서드를 사용하여 비동기 작업의 결과를 처리할 수 있습니다.

```javascript
myPromise
  .then((result) => {
    console.log(result); // 비동기 작업이 성공한 경우 결과 값을 받아 처리
  })
  .catch((error) => {
    console.error(error); // 비동기 작업이 실패한 경우 에러를 받아 처리
  });
```

여러 개의 Promise를 연결하여 순차적으로 실행할 수도 있습니다. 이를 Promise chaining이라고 합니다.

```javascript
myPromise
  .then((result) => {
    // 첫 번째 비동기 작업 결과 처리
    return anotherPromise; // 다른 Promise 반환
  })
  .then((result) => {
    // 두 번째 비동기 작업 결과 처리
  })
  .catch((error) => {
    // 에러 처리
  });
```

Promise를 사용하면 비동기 작업을 보다 깔끔하고 읽기 쉽게 처리할 수 있습니다. 콜백 지옥(callback hell)에 빠지지 않고 비동기 작업을 순차적으로 처리할 수 있습니다.

Promise는 현대 자바스크립트에서 비동기 처리를 다루는 표준적인 방법으로 자리잡았습니다. Node.js에서도 많은 비동기 작업이 Promise를 기반으로 이루어집니다.

### async/await

async/await는 비동기 처리를 더욱 쉽게 작성할 수 있도록 도와주는 자바스크립트의 문법입니다. 이는 Promise를 기반으로 동작하며, 코드의 가독성을 높이고 비동기 처리를 동기 처리처럼 작성할 수 있게 해줍니다.

1. async 함수 선언
   - 함수 앞에 `async` 키워드를 붙여 해당 함수가 비동기 함수임을 나타냅니다.
   - async 함수는 항상 Promise를 반환합니다.

```javascript
async function 함수명() {
  // 비동기 처리 로직
}
```

2. await 키워드
   - `await` 키워드는 Promise가 완료될 때까지 대기하도록 합니다.
   - await은 async 함수 내에서만 사용할 수 있습니다.
   - Promise가 완료되면 해당 Promise의 결과값을 반환합니다.

```javascript
async function 함수명() {
  const 결과 = await Promise;
  // Promise가 완료된 후 결과값을 사용하여 추가 작업 수행
}
```

3. 예외 처리
   - async/await에서 예외 처리는 try/catch 문을 사용합니다.
   - 비동기 작업 중 발생한 예외를 catch 블록에서 처리할 수 있습니다.

```javascript
async function 함수명() {
  try {
    const 결과 = await Promise;
    // 비동기 작업이 성공한 경우 처리
  } catch (예외) {
    // 비동기 작업 중 예외가 발생한 경우 처리
  }
}
```

4. 병렬 처리
   - 여러 개의 비동기 작업을 병렬로 처리하기 위해 `Promise.all()`을 사용할 수 있습니다.
   - Promise.all()은 주어진 Promise들이 모두 완료될 때까지 기다린 후 결과를 배열로 반환합니다.

```javascript
async function 함수명() {
  const [결과1, 결과2] = await Promise.all([Promise1, Promise2]);
  // 모든 Promise가 완료된 후 결과값들을 사용하여 추가 작업 수행
}
```

async/await를 사용하면 비동기 처리를 마치 동기 처리처럼 작성할 수 있어 코드의 가독성과 유지보수성이 향상됩니다. 하지만 과도한 사용은 성능에 영향을 줄 수 있으므로 적절히 사용하는 것이 중요합니다.

## 기타

### 객체

자바스크립트에서 객체는 키(key)와 값(value)의 쌍으로 이루어진 속성(property)들의 집합입니다. 객체는 중괄호 {}를 사용하여 정의하며, 속성은 키: 값 형식으로 표현합니다.

객체 생성 방법:
```javascript
const person = {
  name: "John",
  age: 30,
  city: "New York"
};
```

객체의 속성에 접근하는 방법은 두 가지가 있습니다:
1. 점 표기법(Dot notation): 객체 이름 뒤에 점(.)을 붙이고 속성 이름을 지정합니다.
```javascript
console.log(person.name); // "John"
console.log(person.age); // 30
```

2. 대괄호 표기법(Bracket notation): 객체 이름 뒤에 대괄호 []를 붙이고 속성 이름을 문자열로 지정합니다.
```javascript
console.log(person["city"]); // "New York"
```

객체의 속성은 동적으로 추가, 수정, 삭제할 수 있습니다.
```javascript
person.email = "john@example.com"; // 속성 추가
person.age = 31; // 속성 수정
delete person.city; // 속성 삭제
```

객체는 다른 객체나 함수를 속성으로 가질 수 있습니다.
```javascript
const student = {
  name: "Alice",
  grades: {
    math: 90,
    science: 85
  },
  getAverage: function() {
    return (this.grades.math + this.grades.science) / 2;
  }
};

console.log(student.grades.math); // 90
console.log(student.getAverage()); // 87.5
```

객체는 참조 타입(reference type)입니다. 즉, 객체를 변수에 할당하면 해당 변수는 객체의 참조(메모리 주소)를 저장합니다.
```javascript
const person1 = { name: "John" };
const person2 = person1;
person2.name = "Jane";
console.log(person1.name); // "Jane"
```

위의 예제에서 person1과 person2는 동일한 객체를 참조하므로, person2를 통해 객체를 수정하면 person1에도 영향을 줍니다.

객체는 자바스크립트에서 매우 중요한 개념이며, 데이터와 관련 기능을 그룹화하여 코드의 구조를 개선하고 유지보수성을 높이는 데 사용됩니다.

### 예외 처리

자바스크립트에서 예외 처리는 `try`, `catch`, `finally` 키워드를 사용하여 이루어집니다. 예외 처리는 프로그램 실행 중에 발생할 수 있는 예외 상황을 처리하고, 프로그램의 비정상적인 종료를 막는 데 사용됩니다.

예외 처리의 기본 구조는 다음과 같습니다:

```javascript
try {
  // 예외가 발생할 가능성이 있는 코드
} catch (error) {
  // 예외가 발생했을 때 실행될 코드
} finally {
  // 예외 발생 여부와 상관없이 항상 실행될 코드
}
```

- `try` 블록 내부에는 예외가 발생할 가능성이 있는 코드를 작성합니다.
- `catch` 블록은 `try` 블록에서 예외가 발생했을 때 실행되는 코드를 포함합니다. `catch` 블록은 예외 객체를 인자로 받아 예외 정보에 접근할 수 있습니다.
- `finally` 블록은 선택적으로 사용되며, 예외 발생 여부와 상관없이 항상 실행되는 코드를 포함합니다. 주로 자원을 정리하는 등의 작업에 사용됩니다.

예외를 직접 발생시키려면 `throw` 키워드를 사용합니다. `throw` 키워드 뒤에는 예외 객체를 지정할 수 있습니다. 예외 객체는 주로 `Error` 클래스의 인스턴스이지만, 다른 값도 사용 가능합니다.

```javascript
throw new Error('예외 발생!');
```

예외 처리의 실제 사용 예시는 다음과 같습니다:

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error('0으로 나눌 수 없습니다.');
  }
  return a / b;
}

try {
  const result = divide(10, 0);
  console.log(result);
} catch (error) {
  console.error('예외 발생:', error.message);
} finally {
  console.log('예외 처리 완료');
}
```

위의 예시에서 `divide` 함수는 두 수를 나누는 함수입니다. 만약 두 번째 인자가 0이면 예외를 발생시킵니다. `try` 블록에서 `divide` 함수를 호출하고, 예외가 발생하면 `catch` 블록에서 예외를 처리합니다. `finally` 블록은 예외 발생 여부와 상관없이 항상 실행됩니다.

예외 처리를 사용하면 예외 상황에 대한 적절한 처리를 통해 프로그램의 안정성과 가독성을 높일 수 있습니다. 또한, 예외 처리를 통해 예외 정보를 기록하거나 사용자에게 알려주는 등의 추가 작업을 수행할 수 있습니다.

### 프로토타입과 클래스

자바스크립트에서 객체 지향 프로그래밍을 구현하는 방법에는 프로토타입과 클래스가 있습니다.

#### 프로토타입

프로토타입은 자바스크립트에서 객체 간 상속을 구현하는 메커니즘입니다. 모든 객체는 `[[Prototype]]`이라는 내부 슬롯을 가지고 있으며, 이를 통해 다른 객체의 프로퍼티와 메서드를 상속받을 수 있습니다.

프로토타입 객체를 생성하는 방법은 다음과 같습니다:

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHello = function() {
  console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
};

const person1 = new Person('John', 30);
const person2 = new Person('Jane', 25);

person1.sayHello(); // Hello, my name is John and I'm 30 years old.
person2.sayHello(); // Hello, my name is Jane and I'm 25 years old.
```

위 예제에서 `Person` 생성자 함수를 정의하고, `Person.prototype`에 `sayHello` 메서드를 추가했습니다. 이렇게 하면 `Person` 생성자 함수로 생성된 모든 객체는 `sayHello` 메서드를 상속받게 됩니다.

#### 클래스

ES6부터는 클래스 문법이 도입되었습니다. 클래스는 프로토타입 기반 상속을 보다 깔끔하고 직관적인 문법으로 구현할 수 있게 해줍니다.

클래스를 정의하는 방법은 다음과 같습니다:

```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

const person1 = new Person('John', 30);
const person2 = new Person('Jane', 25);

person1.sayHello(); // Hello, my name is John and I'm 30 years old.
person2.sayHello(); // Hello, my name is Jane and I'm 25 years old.
```

위 예제에서 `Person` 클래스를 정의하고, 생성자 함수와 `sayHello` 메서드를 추가했습니다. 클래스를 사용하면 프로토타입 기반 상속을 보다 명확하고 간결하게 표현할 수 있습니다.

클래스는 상속도 지원합니다. `extends` 키워드를 사용하여 다른 클래스를 상속받을 수 있습니다:

```javascript
class Student extends Person {
  constructor(name, age, major) {
    super(name, age);
    this.major = major;
  }

  sayMajor() {
    console.log(`I'm studying ${this.major}.`);
  }
}

const student1 = new Student('Mike', 22, 'Computer Science');
student1.sayHello(); // Hello, my name is Mike and I'm 22 years old.
student1.sayMajor(); // I'm studying Computer Science.
```

위 예제에서 `Student` 클래스는 `Person` 클래스를 상속받습니다. `super` 키워드를 사용하여 부모 클래스의 생성자 함수를 호출하고, `sayMajor` 메서드를 추가로 정의했습니다.

프로토타입과 클래스는 자바스크립트에서 객체 지향 프로그래밍을 구현하는 핵심 개념입니다. 프로토타입은 객체 간 상속을 구현하는 메커니즘이며, 클래스는 프로토타입 기반 상속을 보다 명확하고 간결한 문법으로 표현할 수 있게 해줍니다.