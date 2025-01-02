## **탭 UI 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [activeTab, setActiveTab] = useState('Tab1');

  const tabs = {
    Tab1: '탭 1의 내용입니다.',
    Tab2: '탭 2의 내용입니다.',
    Tab3: '탭 3의 내용입니다.'
  };

  return (
    <div>
      <h1>탭 UI</h1>
      <div>
        {Object.keys(tabs).map((tab) => (
          <button key={tab} onClick={() => setActiveTab(tab)}>
            {tab}
          </button>
        ))}
      </div>
      <div>
        <p>{tabs[activeTab]}</p>
      </div>
    </div>
  );
}

export default App;
```

---

## **다크 모드 토글 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  const appStyle = {
    backgroundColor: isDarkMode ? '#333' : '#fff',
    color: isDarkMode ? '#fff' : '#000',
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center'
  };

  return (
    <div style={appStyle}>
      <h1>다크 모드 {isDarkMode ? '켜짐' : '꺼짐'}</h1>
      <button onClick={toggleDarkMode}>다크 모드 토글</button>
    </div>
  );
}

export default App;
```

---

## **더보기 버튼 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [isExpanded, setIsExpanded] = useState(false);

  const content = '이것은 아주 긴 텍스트 예제입니다. 더보기를 눌러서 전체 내용을 확인하세요.';
  const preview = content.slice(0, 20);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div>
      <h1>더보기 버튼</h1>
      <p>{isExpanded ? content : `${preview}...`}</p>
      <button onClick={toggleExpand}>{isExpanded ? '접기' : '더보기'}</button>
    </div>
  );
}

export default App;
```