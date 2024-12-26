# 자바스크립트 입문서 - 요약편

## 시작하기

### 자바스크립트의 소개

자바스크립트는 웹 브라우저에서 동작하는 스크립트 언어로 시작했지만, 현재는 Node.js 환경에서도 사용할 수 있는 범용 프로그래밍 언어로 발전했습니다. 자바스크립트는 객체 지향 프로그래밍과 함수형 프로그래밍 패러다임을 모두 지원하며, 동적 타입 언어입니다.

### 개발환경 설치

Node.js를 설치하려면 공식 웹사이트(https://nodejs.org)에서 LTS 버전을 다운로드하고 설치 마법사의 지시에 따라 설치 과정을 완료합니다. 설치가 완료되면 터미널에서 `node --version` 명령어를 실행하여 Node.js가 정상적으로 설치되었는지 확인할 수 있습니다.

Visual Studio Code는 마이크로소프트에서 개발한 오픈 소스 코드 에디터입니다. 공식 웹사이트(https://code.visualstudio.com)에서 다운로드하고 설치할 수 있습니다. Visual Studio Code는 다양한 확장 기능을 제공하여 자바스크립트 개발에 유용한 도구로 사용됩니다.

### 첫 번째 프로그램 실행

첫 번째 자바스크립트 프로그램을 실행하려면 다음 단계를 따르세요:

1. Visual Studio Code를 열고 새 파일을 생성합니다.
2. 파일에 다음 코드를 입력합니다:

```javascript
console.log("Hello, World!");
```

3. 파일을 `hello.js`로 저장합니다.
4. 터미널을 열고 `hello.js` 파일이 있는 디렉토리로 이동합니다.
5. 다음 명령어를 실행하여 프로그램을 실행합니다:

```
node hello.js
```

6. 터미널에 "Hello, World!"가 출력되는 것을 확인할 수 있습니다.

이제 자바스크립트 개발 환경 설정이 완료되었으며, 첫 번째 프로그램을 성공적으로 실행했습니다. 이를 기반으로 자바스크립트 문법과 기능을 학습하고 더 복잡한 프로그램을 작성할 수 있습니다.

## 자료와 변수

자바스크립트에서 자료와 변수는 프로그램의 기본 구성 요소입니다. 자료는 프로그램에서 처리할 데이터를 의미하며, 변수는 이러한 자료를 저장하는 메모리 공간을 나타냅니다.

### 기본 자료형

자바스크립트에는 다음과 같은 기본 자료형이 있습니다:

1. 숫자형 (Number): 정수와 실수를 표현할 수 있습니다.
   예) `let age = 25;`

2. 문자열 (String): 문자의 나열을 표현합니다. 작은따옴표('') 또는 큰따옴표("")로 묶어 표현합니다.
   예) `let name = "John Doe";`

3. 불리언 (Boolean): 참(true)과 거짓(false)의 두 가지 값을 가집니다.
   예) `let isStudent = true;`

4. undefined: 변수가 선언되었지만, 값이 할당되지 않은 상태를 나타냅니다.
   예) `let count;`

5. null: 변수에 의도적으로 빈 값을 할당할 때 사용합니다.
   예) `let obj = null;`

### 상수와 변수

상수(const)와 변수(let)는 자료를 저장하는 메모리 공간을 나타내는 식별자입니다.

- 상수(const): 한 번 값을 할당하면 변경할 수 없는 메모리 공간입니다. 상수는 선언과 동시에 초기화해야 합니다.
  예) `const PI = 3.14159;`

- 변수(let): 값을 변경할 수 있는 메모리 공간입니다. 변수는 선언 후에 값을 할당하거나 변경할 수 있습니다.
  예) `let score = 80; score = 90;`

### 자료형 변환

자바스크립트에서는 필요에 따라 자료형을 변환할 수 있습니다. 주요 자료형 변환 방법은 다음과 같습니다:

1. 문자열로 변환:
   - `String(value)` 함수 사용
   - `value.toString()` 메서드 사용
   - 빈 문자열과 더하기 연산자 사용 (`"" + value`)

2. 숫자형으로 변환:
   - `Number(value)` 함수 사용
   - `parseInt(value)` 함수 사용 (정수로 변환)
   - `parseFloat(value)` 함수 사용 (실수로 변환)

3. 불리언으로 변환:
   - `Boolean(value)` 함수 사용

예)
```javascript
let num = 10;
let str = String(num);
console.log(typeof str); // "string"

let boolValue = Boolean(0);
console.log(boolValue); // false
```

이렇게 자바스크립트에서는 자료와 변수를 사용하여 데이터를 저장하고 처리할 수 있습니다. 기본 자료형, 상수와 변수, 그리고 자료형 변환에 대한 이해는 프로그래밍의 기초가 됩니다.

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

1. 산술 연산자
   - 덧셈 연산자 (`+`): 두 값을 더합니다.
   - 뺄셈 연산자 (`-`): 한 값에서 다른 값을 뺍니다.
   - 곱셈 연산자 (`*`): 두 값을 곱합니다.
   - 나눗셈 연산자 (`/`): 한 값을 다른 값으로 나눕니다.
   - 나머지 연산자 (`%`): 한 값을 다른 값으로 나눈 후 나머지를 반환합니다.

예제:
```javascript
let a = 10;
let b = 3;

console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.3333333333333335
console.log(a % b); // 1
```

2. 할당 연산자
   - 할당 연산자 (`=`): 변수에 값을 할당합니다.
   - 더하기 할당 연산자 (`+=`): 변수에 값을 더한 후 결과를 변수에 할당합니다.
   - 빼기 할당 연산자 (`-=`): 변수에서 값을 뺀 후 결과를 변수에 할당합니다.
   - 곱하기 할당 연산자 (`*=`): 변수에 값을 곱한 후 결과를 변수에 할당합니다.
   - 나누기 할당 연산자 (`/=`): 변수를 값으로 나눈 후 결과를 변수에 할당합니다.

예제:
```javascript
let x = 5;
x += 3; // x = x + 3
console.log(x); // 8

let y = 10;
y -= 2; // y = y - 2
console.log(y); // 8

let z = 4;
z *= 2; // z = z * 2
console.log(z); // 8

let w = 20;
w /= 4; // w = w / 4
console.log(w); // 5
```

3. 비교 연산자
   - 동등 연산자 (`==`): 두 값이 같은지 비교합니다.
   - 일치 연산자 (`===`): 두 값과 데이터 유형이 모두 같은지 비교합니다.
   - 부등 연산자 (`!=`): 두 값이 다른지 비교합니다.
   - 불일치 연산자 (`!==`): 두 값 또는 데이터 유형이 다른지 비교합니다.
   - 큼 연산자 (`>`): 한 값이 다른 값보다 큰지 비교합니다.
   - 작음 연산자 (`<`): 한 값이 다른 값보다 작은지 비교합니다.
   - 크거나 같음 연산자 (`>=`): 한 값이 다른 값보다 크거나 같은지 비교합니다.
   - 작거나 같음 연산자 (`<=`): 한 값이 다른 값보다 작거나 같은지 비교합니다.

예제:
```javascript
let num1 = 5;
let num2 = "5";
let num3 = 10;

console.log(num1 == num2); // true
console.log(num1 === num2); // false
console.log(num1 != num3); // true
console.log(num1 !== num2); // true
console.log(num1 > num3); // false
console.log(num1 < num3); // true
console.log(num1 >= num2); // true
console.log(num1 <= num3); // true
```

### 논리 연산자

1. 논리 AND 연산자 (`&&`): 두 조건이 모두 참인 경우 `true`를 반환합니다.
2. 논리 OR 연산자 (`||`): 두 조건 중 하나 이상이 참인 경우 `true`를 반환합니다.
3. 논리 NOT 연산자 (`!`): 조건의 반대 값을 반환합니다.

예제:
```javascript
let age = 25;
let isStudent = true;

console.log(age > 18 && isStudent); // true
console.log(age > 30 || isStudent); // true
console.log(!isStudent); // false
```

### 삼항 연산자

삼항 연산자 (`?:`)는 조건에 따라 값을 선택할 수 있는 간단한 방법을 제공합니다.

구문: `조건 ? 값1 : 값2`

- 조건이 참이면 `값1`이 반환되고, 거짓이면 `값2`가 반환됩니다.

예제:
```javascript
let score = 85;
let result = score >= 60 ? "합격" : "불합격";
console.log(result); // "합격"
```

이상으로 자바스크립트의 연산자에 대해 알아보았습니다. 연산자는 값을 조작하고 결합하는 데 사용되며, 프로그램의 논리를 구성하는 데 필수적입니다.

## 조건문

자바스크립트에서 조건문은 특정 조건에 따라 코드의 실행 여부를 결정하는 구문입니다. 조건문을 사용하면 프로그램의 흐름을 제어할 수 있습니다. 자바스크립트에는 두 가지 주요 조건문이 있습니다: `if` 조건문과 `switch` 조건문입니다.

### if 조건문

`if` 조건문은 주어진 조건이 참(`true`)인 경우에만 코드 블록을 실행합니다. 조건이 거짓(`false`)이면 코드 블록은 건너뜁니다. `if` 조건문의 기본 구조는 다음과 같습니다:

```javascript
if (조건) {
  // 조건이 참일 때 실행되는 코드
}
```

예를 들어:

```javascript
let age = 20;

if (age >= 18) {
  console.log("성인입니다.");
}
```

위의 예시에서는 `age`가 18 이상이면 "성인입니다."라는 메시지가 출력됩니다.

`if` 조건문은 `else` 절과 함께 사용할 수 있습니다. `else` 절은 조건이 거짓일 때 실행되는 코드 블록을 정의합니다.

```javascript
let age = 15;

if (age >= 18) {
  console.log("성인입니다.");
} else {
  console.log("미성년자입니다.");
}
```

위의 예시에서는 `age`가 18 미만이므로 "미성년자입니다."라는 메시지가 출력됩니다.

여러 조건을 확인해야 할 때는 `else if` 절을 사용할 수 있습니다.

```javascript
let score = 85;

if (score >= 90) {
  console.log("A 등급");
} else if (score >= 80) {
  console.log("B 등급");
} else if (score >= 70) {
  console.log("C 등급");
} else {
  console.log("D 등급");
}
```

위의 예시에서는 `score`가 85이므로 "B 등급"이 출력됩니다.

### switch 조건문

`switch` 조건문은 여러 가지 경우 중 하나를 선택하여 실행할 수 있습니다. `switch` 조건문은 표현식의 값과 일치하는 `case` 절을 찾아 해당 코드 블록을 실행합니다. `switch` 조건문의 기본 구조는 다음과 같습니다:

```javascript
switch (표현식) {
  case 값1:
    // 값1과 일치할 때 실행되는 코드
    break;
  case 값2:
    // 값2와 일치할 때 실행되는 코드
    break;
  default:
    // 일치하는 값이 없을 때 실행되는 코드
}
```

예를 들어:

```javascript
let fruit = "apple";

switch (fruit) {
  case "apple":
    console.log("사과입니다.");
    break;
  case "banana":
    console.log("바나나입니다.");
    break;
  default:
    console.log("알 수 없는 과일입니다.");
}
```

위의 예시에서는 `fruit`가 "apple"이므로 "사과입니다."라는 메시지가 출력됩니다.

`switch` 조건문에서 `break` 문을 사용하여 각 `case` 절의 끝을 나타냅니다. `break` 문이 없으면 일치하는 `case` 절 이후의 모든 `case` 절이 실행됩니다.

이렇게 자바스크립트에서는 `if`와 `switch` 조건문을 사용하여 프로그램의 흐름을 제어할 수 있습니다. 조건에 따라 적절한 조건문을 선택하여 사용할 수 있습니다.

## 반복문

반복문은 특정 코드 블록을 여러 번 반복하여 실행할 수 있게 해주는 제어 구조입니다. 자바스크립트에서는 주로 `for`문과 `while`문을 사용하여 반복문을 구현합니다.

### for 반복문

`for`문은 가장 일반적인 반복문으로, 초기값, 조건식, 증감식을 사용하여 반복을 제어합니다. 구문은 다음과 같습니다.

```javascript
for (초기값; 조건식; 증감식) {
  // 반복할 코드 블록
}
```

예를 들어, 1부터 10까지의 숫자를 출력하는 `for`문은 다음과 같이 작성할 수 있습니다.

```javascript
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

이 코드는 `i`라는 변수를 1로 초기화하고, `i`가 10 이하일 때까지 반복하면서 `i`를 1씩 증가시킵니다. 반복할 코드 블록에서는 `console.log()`를 사용하여 `i`의 값을 출력합니다.

### while 반복문

`while`문은 조건식이 참인 동안 반복을 수행합니다. 구문은 다음과 같습니다.

```javascript
while (조건식) {
  // 반복할 코드 블록
}
```

예를 들어, 1부터 10까지의 숫자를 출력하는 `while`문은 다음과 같이 작성할 수 있습니다.

```javascript
let i = 1;
while (i <= 10) {
  console.log(i);
  i++;
}
```

이 코드는 `i`라는 변수를 1로 초기화하고, `i`가 10 이하일 때까지 반복하면서 `console.log()`를 사용하여 `i`의 값을 출력하고, `i`를 1씩 증가시킵니다.

반복문은 배열이나 객체의 요소를 순회할 때 자주 사용됩니다. 예를 들어, 배열의 모든 요소를 출력하는 코드는 다음과 같이 작성할 수 있습니다.

```javascript
const fruits = ['apple', 'banana', 'orange'];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

이 코드는 `fruits` 배열의 길이만큼 반복하면서, 각 요소를 `console.log()`를 사용하여 출력합니다.

이 외에도 `for...in`문과 `for...of`문 등 다양한 반복문이 있습니다. 상황에 맞는 적절한 반복문을 선택하여 사용하면 효율적인 코드를 작성할 수 있습니다.

## 함수

함수는 특정 작업을 수행하는 코드 블록입니다. 함수를 사용하면 코드를 더 구조적으로 작성할 수 있고, 코드의 재사용성을 높일 수 있습니다.

### 함수의 기본 형태

함수의 기본 형태는 다음과 같습니다.

```javascript
function 함수명(매개변수1, 매개변수2, ...) {
  // 함수 내부에서 실행될 코드
  return 반환값;
}
```

- `function` 키워드를 사용하여 함수를 선언합니다.
- 함수명은 함수를 식별하는 이름입니다.
- 매개변수는 함수 호출 시 전달되는 값을 받아오는 변수입니다. 매개변수는 0개 이상 사용할 수 있습니다.
- 함수 내부에는 실행될 코드를 작성합니다.
- `return` 키워드를 사용하여 함수의 실행 결과를 반환할 수 있습니다.

예를 들어, 두 수를 더하는 함수는 다음과 같이 작성할 수 있습니다.

```javascript
function add(a, b) {
  return a + b;
}
```

함수를 호출할 때는 함수명 뒤에 괄호를 붙이고, 괄호 안에 매개변수에 해당하는 값을 전달합니다.

```javascript
let result = add(3, 5);
console.log(result); // 출력 결과: 8
```

### 함수 고급

함수는 일급 객체(First-class Object)로 취급됩니다. 즉, 함수를 변수에 할당하거나 다른 함수의 매개변수로 전달할 수 있으며, 함수 자체를 반환할 수도 있습니다.

예를 들어, 함수를 변수에 할당하는 경우는 다음과 같습니다.

```javascript
const multiply = function(a, b) {
  return a * b;
};

console.log(multiply(3, 4)); // 출력 결과: 12
```

함수를 다른 함수의 매개변수로 전달하는 경우는 다음과 같습니다.

```javascript
function calculate(operation, a, b) {
  return operation(a, b);
}

const result1 = calculate(add, 3, 5);
console.log(result1); // 출력 결과: 8

const result2 = calculate(multiply, 3, 4);
console.log(result2); // 출력 결과: 12
```

### 함수의 기본 파라미터

함수의 매개변수에 기본값을 설정할 수 있습니다. 기본값을 설정하면 함수 호출 시 해당 매개변수에 값이 전달되지 않았을 때 기본값이 사용됩니다.

```javascript
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}

greet(); // 출력 결과: Hello, Guest!
greet("John"); // 출력 결과: Hello, John!
```

위의 예시에서 `name` 매개변수의 기본값은 "Guest"로 설정되어 있습니다. 함수 호출 시 `name` 값을 전달하지 않으면 기본값인 "Guest"가 사용됩니다.

함수는 자바스크립트에서 매우 중요한 역할을 합니다. 함수를 활용하여 코드를 모듈화하고 재사용성을 높일 수 있습니다. 함수의 기본 형태와 고급 기능을 이해하고 활용하면 더 효율적이고 가독성 높은 코드를 작성할 수 있습니다.

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
Promise는 비동기 작업의 최종 완료 또는 실패를 나타내는 객체입니다. Promise를 사용하면 콜백 지옥(callback hell)을 피하고 더 깔끔한 코드를 작성할 수 있습니다.

```javascript
function asyncOperation() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const result = 'Async operation completed';
      resolve(result);
    }, 1000);
  });
}

asyncOperation()
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });
```

위 예제에서 `asyncOperation` 함수는 Promise를 반환합니다. Promise의 `resolve` 함수를 호출하여 비동기 작업이 성공적으로 완료되었음을 알리고, `then` 메서드를 사용하여 결과를 처리합니다. 만약 비동기 작업 중 오류가 발생하면 `reject` 함수를 호출하고, `catch` 메서드를 사용하여 오류를 처리합니다.

### async/await
async/await는 Promise를 더 간편하게 사용할 수 있도록 도와주는 문법입니다. async 함수 내에서 await 키워드를 사용하여 Promise의 완료를 기다릴 수 있습니다.

```javascript
async function asyncOperation() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const result = 'Async operation completed';
      resolve(result);
    }, 1000);
  });
}

async function main() {
  try {
    const result = await asyncOperation();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

main();
```

위 예제에서 `asyncOperation` 함수는 Promise를 반환합니다. `main` 함수는 async 함수로 선언되었으며, await 키워드를 사용하여 `asyncOperation` 함수의 완료를 기다립니다. 비동기 작업이 완료되면 결과를 변수에 할당하고 사용할 수 있습니다. 오류 처리는 try/catch 블록을 사용하여 수행됩니다.

비동기 처리는 자바스크립트에서 매우 중요한 개념이며, 서버와의 통신, 파일 읽기/쓰기, 타이머 등 다양한 상황에서 사용됩니다. 콜백 함수, Promise, async/await를 적절히 활용하여 비동기 작업을 효과적으로 처리할 수 있습니다.

## 기타

### 객체

자바스크립트에서 객체는 키-값 쌍으로 이루어진 데이터 구조입니다. 객체를 생성하는 방법에는 객체 리터럴 표기법과 생성자 함수를 사용하는 방법이 있습니다.

```javascript
// 객체 리터럴 표기법
const person = {
  name: 'John',
  age: 30,
  sayHello: function() {
    console.log('Hello, my name is ' + this.name);
  }
};

// 생성자 함수
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sayHello = function() {
    console.log('Hello, my name is ' + this.name);
  };
}

const john = new Person('John', 30);
```

객체의 속성에 접근하거나 값을 할당할 때는 점 표기법 또는 대괄호 표기법을 사용합니다.

```javascript
console.log(person.name); // 'John'
person.age = 31;
console.log(person['age']); // 31
```

### 예외 처리

자바스크립트에서 예외 처리는 try-catch 문을 사용하여 처리합니다. try 블록 내에서 예외가 발생하면 catch 블록에서 해당 예외를 처리합니다.

```javascript
try {
  // 예외가 발생할 수 있는 코드
  throw new Error('예외 발생');
} catch (error) {
  // 예외 처리 코드
  console.log(error.message);
}
```

### 프로토타입과 클래스

자바스크립트는 프로토타입 기반 언어입니다. 모든 객체는 프로토타입 객체를 가지고 있으며, 프로토타입을 통해 상속과 메서드 공유가 이루어집니다.

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.sayHello = function() {
  console.log('Hello, my name is ' + this.name);
};

const john = new Person('John');
john.sayHello(); // 'Hello, my name is John'
```

ES6부터는 클래스 문법이 도입되었습니다. 클래스는 프로토타입 기반 상속을 더 간결하고 명확한 문법으로 표현할 수 있게 해줍니다.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

  sayHello() {
    console.log('Hello, my name is ' + this.name);
  }
}

const john = new Person('John');
john.sayHello(); // 'Hello, my name is John'
```

위의 내용은 node.js 환경에서 순수 자바스크립트로 객체, 예외 처리, 프로토타입과 클래스에 대해 설명한 것입니다. HTML과 CSS는 사용하지 않았습니다.
