웹 페이지에 동적인 기능을 부여하기 위해서는 JavaScript 언어 자체에 대한 이해가 필요합니다. 이번 장에서는 변수를 선언하고, 연산자를 사용하고, 조건문과 반복문을 작성하는 등 JavaScript의 기초 문법 전반을 간단히 살펴봅니다.

---

## 1. 변수와 상수

### 1.1 변수 선언

- **`var`**: 함수 스코프(function scope)를 가지며, 호이스팅(hoisting)의 영향을 크게 받습니다.  
- **`let`**: 블록 스코프(block scope)를 가지며, 재할당이 가능합니다.  
- **`const`**: 블록 스코프를 가지며, 재할당이 불가능합니다.  

아래 예제는 변수를 선언하고 값을 할당해보는 간단한 코드입니다.

```javascript
var oldStyle = "var 키워드로 선언";
let modernStyle = "let 키워드로 선언";
const fixedValue = "const 키워드로 선언";
console.log(oldStyle);
console.log(modernStyle);
console.log(fixedValue);
```

- **설명**  
  - `var oldStyle`: 기존 방식이지만, 블록 스코프를 지원하지 않아 의도치 않은 버그를 유발할 수 있습니다.  
  - `let modernStyle`: 블록 스코프를 지원해 좀 더 안전하게 사용할 수 있습니다.  
  - `const fixedValue`: 재할당할 수 없는 상수 변수입니다.

### 1.2 변수 스코프와 호이스팅

- **스코프(Scope)**: 변수가 접근할 수 있는 범위를 의미합니다.  
- **호이스팅(Hoisting)**: 변수 선언이 스코프 최상단으로 끌어올려지는 동작을 말합니다(`var`만 해당).  

이로 인해 `var` 키워드는 예기치 않은 동작이 발생할 수 있으므로, 일반적으로는 `let`과 `const`를 권장합니다.

---

## 2. 자료형(Data Types)

JavaScript는 동적 타이핑 언어로, 변수에 다양한 자료형의 값을 유연하게 담을 수 있습니다. 대표적인 자료형은 다음과 같습니다.

1. **Number**: 정수, 실수 등 모든 숫자를 표현  
2. **String**: 문자열  
3. **Boolean**: `true`와 `false`  
4. **Null**: 의도적으로 값이 없음을 표현  
5. **Undefined**: 값이 할당되지 않은 상태  
6. **Object**: 객체, 배열, 함수 등 복합 자료형을 표현  

```javascript
let age = 30;
let name = "Alice";
let isStudent = false;
let emptyValue = null;
let notDefined;
let user = { name: "Bob", age: 25 };
let numbers = [10, 20, 30];
console.log(typeof age);
console.log(typeof name);
console.log(typeof isStudent);
console.log(typeof emptyValue);
console.log(typeof notDefined);
console.log(typeof user);
console.log(typeof numbers);
```

- **설명**  
  - `typeof` 연산자를 통해 변수의 자료형을 확인할 수 있습니다.  
  - `null`은 `object`로 표시되는데, 이는 JavaScript 언어의 역사적 설계 이슈로 인한 결과입니다.

---

## 3. 연산자(Operators)

### 3.1 산술 연산자

- `+` (덧셈), `-` (뺄셈), `*` (곱셈), `/` (나눗셈), `%` (나머지), `**` (거듭제곱)

```javascript
let x = 10;
let y = 3;
console.log(x + y);
console.log(x - y);
console.log(x * y);
console.log(x / y);
console.log(x % y);
console.log(x ** y);
```

### 3.2 대입 연산자

- `=` (대입), `+=`, `-=`, `*=`, `/=`, `%=` 등

```javascript
let a = 5;
a += 2;
a *= 3;
console.log(a);
```

### 3.3 비교 연산자

- `==` (값만 비교), `===` (값과 타입 모두 비교), `!=`, `!==`, `<`, `>`, `<=`, `>=`

```javascript
console.log(1 == "1");
console.log(1 === "1");
console.log(5 > 3);
console.log(5 !== 4);
```

### 3.4 논리 연산자

- `&&` (AND), `||` (OR), `!` (NOT)

```javascript
let conditionA = true;
let conditionB = false;
console.log(conditionA && conditionB);
console.log(conditionA || conditionB);
console.log(!conditionA);
```

---

## 4. 제어 구조(Control Structures)

JavaScript에서는 조건문과 반복문을 통해 프로그램의 흐름을 제어할 수 있습니다.

### 4.1 조건문(If, Else If, Else)

```javascript
let score = 85;
if (score >= 90) {
  console.log("A 학점");
} else if (score >= 80) {
  console.log("B 학점");
} else {
  console.log("C 학점 이하");
}
```

- **설명**  
  - `if`와 `else if`를 사용해 여러 조건을 순차적으로 확인합니다.  
  - 조건을 만족하지 않으면 `else` 블록이 실행됩니다.

### 4.2 switch문

```javascript
let day = 2;
switch (day) {
  case 0:
    console.log("일요일");
    break;
  case 1:
    console.log("월요일");
    break;
  case 2:
    console.log("화요일");
    break;
  default:
    console.log("수요일 이후");
}
```

- **설명**  
  - 변수(`day`)의 값에 따라 여러 경우 중 하나를 처리합니다.  
  - `break`를 사용해 각 분기 처리를 마친 뒤 빠져나옵니다.

### 4.3 반복문(For, While, Do While)

```javascript
// For 문
for (let i = 0; i < 3; i++) {
  console.log("For 문:", i);
}

// While 문
let count = 0;
while (count < 3) {
  console.log("While 문:", count);
  count++;
}

// Do While 문
let num = 0;
do {
  console.log("Do While 문:", num);
  num++;
} while (num < 3);
```

- **설명**  
  - `for` 문: 반복 횟수가 정해져 있을 때 유용  
  - `while` 문: 조건이 참인 동안 반복  
  - `do while` 문: 최소 한 번은 무조건 실행

---

## 5. 함수(Function)

### 5.1 함수 선언문

```javascript
function greet(name) {
  return "Hello, " + name;
}
console.log(greet("Alice"));
```

- **설명**  
  - 함수를 선언하고, 호출 시 인자를 전달하여 원하는 값을 반환받습니다.

### 5.2 함수 표현식

```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
```

- **설명**  
  - 변수에 익명 함수를 할당하는 방식입니다.  
  - 함수 자체도 하나의 값으로 취급됩니다.

### 5.3 화살표 함수

```javascript
const multiply = (a, b) => a * b;
console.log(multiply(4, 5));
```

- **설명**  
  - ES6에서 도입된 간결한 함수 표기법입니다.  
  - 함수 내부가 한 줄일 경우 `{}`와 `return`을 생략할 수 있습니다.

---

## 6. 배열(Array)과 반복 메서드

### 6.1 배열 선언 및 접근

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);
```

- **설명**  
  - 배열 요소는 인덱스(0부터 시작)를 이용해 접근합니다.

### 6.2 배열 반복 메서드

```javascript
let numbers = [1, 2, 3, 4, 5];
numbers.forEach(num => console.log(num));
let squared = numbers.map(num => num * num);
let evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(squared);
console.log(evenNumbers);
```

- **설명**  
  - `forEach()`: 배열의 모든 요소에 대해 콜백 함수를 실행  
  - `map()`: 배열의 각 요소를 변환한 새로운 배열을 반환  
  - `filter()`: 조건을 만족하는 요소만 모아 새로운 배열을 반환

---

## 7. 객체(Object) 기초

### 7.1 객체 생성

```javascript
let person = {
  name: "Alice",
  age: 25,
  greet: function() {
    return "Hello, I'm " + this.name;
  }
};
console.log(person.name);
console.log(person.greet());
```

- **설명**  
  - 중괄호 `{}` 안에 키-값 쌍을 정의합니다.  
  - `this` 키워드는 현재 객체를 가리킵니다.

### 7.2 프로퍼티 추가 및 삭제

```javascript
person.job = "Developer";
delete person.age;
console.log(person);
```

- **설명**  
  - 점 표기법 또는 대괄호 표기법을 사용해 동적으로 프로퍼티를 추가/삭제할 수 있습니다.

---

## 8. 예외 처리(Exception Handling)

오류가 발생했을 때 프로그램이 중단되지 않고, 예외 상황을 적절히 처리할 수 있습니다.

```javascript
try {
  let result = someUndefinedFunction();
  console.log(result);
} catch (error) {
  console.log("에러 발생:", error.message);
} finally {
  console.log("에러 발생 여부와 상관없이 실행");
}
```

- **설명**  
  - `try` 블록에서 오류가 발생하면 `catch` 블록으로 흐름이 넘어갑니다.  
  - `finally` 블록은 오류 발생 여부와 관계없이 항상 실행됩니다.
