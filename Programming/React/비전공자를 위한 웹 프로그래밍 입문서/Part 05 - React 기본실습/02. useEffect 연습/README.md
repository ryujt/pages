## **타이머 예제**

```javascript
import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    if (isRunning) {
      const timer = setInterval(() => {
        setCount((prevCount) => prevCount + 1);
      }, 1000);
      return () => clearInterval(timer); // Cleanup
    }
  }, [isRunning]);

  const toggleTimer = () => {
    setIsRunning(!isRunning);
  };

  return (
    <div>
      <h1>타이머: {count}</h1>
      <button onClick={toggleTimer}>{isRunning ? '정지' : '시작'}</button>
    </div>
  );
}

export default App;
```

---

## **검색창 예제**

```javascript
import React, { useState, useEffect } from 'react';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [debouncedValue, setDebouncedValue] = useState('');

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(inputValue);
      console.log(`검색값: ${inputValue}`);
    }, 500);

    return () => clearTimeout(handler); // Cleanup
  }, [inputValue]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <div>
      <h1>검색창</h1>
      <input type="text" value={inputValue} onChange={handleInputChange} placeholder="검색어를 입력하세요" />
      <p>현재 검색어: {debouncedValue}</p>
    </div>
  );
}

export default App;
```

---

## **윈도우 크기 감지 예제**

```javascript
import React, { useState, useEffect } from 'react';

function App() {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };

    window.addEventListener('resize', handleResize);

    return () => window.removeEventListener('resize', handleResize); // Cleanup
  }, []);

  return (
    <div>
      <h1>창 크기 감지</h1>
      <p>가로: {windowSize.width}px, 세로: {windowSize.height}px</p>
    </div>
  );
}

export default App;
```