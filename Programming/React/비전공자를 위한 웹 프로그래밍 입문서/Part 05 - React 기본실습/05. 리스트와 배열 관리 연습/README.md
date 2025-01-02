## **할 일 목록 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  const addTodo = () => {
    if (newTodo.trim()) {
      setTodos([...todos, { text: newTodo, completed: false }]);
      setNewTodo('');
    }
  };

  const toggleTodo = (index) => {
    setTodos(
      todos.map((todo, i) =>
        i === index ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  const deleteTodo = (index) => {
    setTodos(todos.filter((_, i) => i !== index));
  };

  return (
    <div>
      <h1>할 일 목록</h1>
      <input
        type="text"
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="할 일을 입력하세요"
      />
      <button onClick={addTodo}>추가</button>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            <span
              style={{
                textDecoration: todo.completed ? 'line-through' : 'none',
                cursor: 'pointer'
              }}
              onClick={() => toggleTodo(index)}
            >
              {todo.text}
            </span>
            <button onClick={() => deleteTodo(index)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

## **즐겨찾기 기능 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [items, setItems] = useState([
    { text: '아이템 1', favorite: false },
    { text: '아이템 2', favorite: false },
    { text: '아이템 3', favorite: false }
  ]);

  const toggleFavorite = (index) => {
    setItems(
      items.map((item, i) =>
        i === index ? { ...item, favorite: !item.favorite } : item
      )
    );
  };

  return (
    <div>
      <h1>즐겨찾기 기능</h1>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            {item.text}{' '}
            <button onClick={() => toggleFavorite(index)}>
              {item.favorite ? '⭐' : '☆'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

## **드롭다운 메뉴 예제**

```javascript
import React, { useState } from 'react';

function App() {
  const [selected, setSelected] = useState('');
  const [isOpen, setIsOpen] = useState(false);

  const options = ['옵션 1', '옵션 2', '옵션 3'];

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const selectOption = (option) => {
    setSelected(option);
    setIsOpen(false);
  };

  return (
    <div>
      <h1>드롭다운 메뉴</h1>
      <button onClick={toggleDropdown}>
        {selected || '항목을 선택하세요'}
      </button>
      {isOpen && (
        <ul>
          {options.map((option, index) => (
            <li key={index} onClick={() => selectOption(option)}>
              {option}
            </li>
          ))}
        </ul>
      )}
      {selected && <p>선택한 항목: {selected}</p>}
    </div>
  );
}

export default App;
```