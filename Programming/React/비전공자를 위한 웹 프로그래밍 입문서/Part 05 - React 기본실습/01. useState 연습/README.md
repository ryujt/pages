## **카운터 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    setCount(count - 1);
  };

  const handleReset = () => {
    setCount(0);
  };

  return (
    <div>
      <h1>카운터: {count}</h1>
      <button onClick={handleIncrement}>증가</button>
      <button onClick={handleDecrement}>감소</button>
      <button onClick={handleReset}>초기화</button>
    </div>
  );
}

export default App;
```

---

## **좋아요 버튼 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [liked, setLiked] = useState(false);

  const toggleLike = () => {
    setLiked(!liked);
  };

  return (
    <div>
      <h1>{liked ? '❤️' : '🤍'}</h1>
      <button onClick={toggleLike}>좋아요 토글</button>
    </div>
  );
}

export default App;
```