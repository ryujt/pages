## **로그인 폼 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('유효한 이메일을 입력하세요.');
      return;
    }
    if (password.length < 6) {
      setError('비밀번호는 6자 이상이어야 합니다.');
      return;
    }
    setError('');
    console.log('로그인 성공:', { email, password });
  };

  return (
    <div>
      <h1>로그인 폼</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
          placeholder="이메일" 
        />
        <input 
          type="password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
          placeholder="비밀번호" 
        />
        <button type="submit">로그인</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
```

---

## **간단한 계산기 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState(null);

  const handleAddition = () => {
    setResult(Number(num1) + Number(num2));
  };

  const handleSubtraction = () => {
    setResult(Number(num1) - Number(num2));
  };

  return (
    <div>
      <h1>간단한 계산기</h1>
      <input 
        type="number" 
        value={num1} 
        onChange={(e) => setNum1(e.target.value)} 
        placeholder="첫 번째 숫자" 
      />
      <input 
        type="number" 
        value={num2} 
        onChange={(e) => setNum2(e.target.value)} 
        placeholder="두 번째 숫자" 
      />
      <button onClick={handleAddition}>더하기</button>
      <button onClick={handleSubtraction}>빼기</button>
      {result !== null && <p>결과: {result}</p>}
    </div>
  );
}

export default App;
```

---

## **투표 기능 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [selectedOption, setSelectedOption] = useState('');
  const [submittedOption, setSubmittedOption] = useState(null);

  const options = ['항목 1', '항목 2', '항목 3'];

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmittedOption(selectedOption);
  };

  return (
    <div>
      <h1>투표</h1>
      <form onSubmit={handleSubmit}>
        {options.map((option) => (
          <div key={option}>
            <label>
              <input 
                type="radio" 
                name="vote" 
                value={option} 
                onChange={(e) => setSelectedOption(e.target.value)} 
              />
              {option}
            </label>
          </div>
        ))}
        <button type="submit">제출</button>
      </form>
      {submittedOption && <p>선택한 항목: {submittedOption}</p>}
    </div>
  );
}

export default App;
```