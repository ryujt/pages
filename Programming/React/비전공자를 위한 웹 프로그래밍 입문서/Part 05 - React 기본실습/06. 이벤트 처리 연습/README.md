## **이미지 슬라이더 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const images = [
    'https://via.placeholder.com/300x200?text=Image+1',
    'https://via.placeholder.com/300x200?text=Image+2',
    'https://via.placeholder.com/300x200?text=Image+3'
  ];

  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    console.log('이전', currentIndex);
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    console.log('다음', currentIndex);
    setCurrentIndex((prevIndex) => (prevIndex === images.length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div>
      <h1>이미지 슬라이더</h1>
      <img
        src={images[currentIndex]}
        alt={`Slide ${currentIndex + 1}`}
        style={{ width: '300px', height: '200px' }}
      />
      <div>
        <button onClick={handlePrev}>이전</button>
        <button onClick={handleNext}>다음</button>
      </div>
    </div>
  );
}

export default App;
```

---

## **키보드 이벤트 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      setMessage('Enter 키가 눌렸습니다!');
    } else {
      setMessage(`"${e.key}" 키가 눌렸습니다.`);
    }
  };

  return (
    <div>
      <h1>키보드 이벤트</h1>
      <input
        type="text"
        onKeyDown={handleKeyPress}
        placeholder="키를 입력하세요"
      />
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
```

---

## **마우스 오버 효과 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [hover, setHover] = useState(false);

  const buttonStyle = {
    padding: '10px 20px',
    fontSize: '16px',
    backgroundColor: hover ? '#f0a500' : '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer'
  };

  return (
    <div>
      <h1>마우스 오버 효과</h1>
      <button
        style={buttonStyle}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
      >
        마우스를 올려보세요
      </button>
    </div>
  );
}

export default App;
```