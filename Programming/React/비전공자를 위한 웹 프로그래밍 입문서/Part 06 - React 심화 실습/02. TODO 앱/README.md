## **프로젝트 구조**

```
D:\Projects\TodoApp\
├── src\
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   ├── api\
│   │   ├── api.js
│   │   ├── todos.js
│   ├── stores\
│   │   ├── todoStore.js
│   ├── pages\
│   │   ├── HomePage.js
│   │   ├── TodoDetailPage.js
│   ├── components\
│   │   ├── Header.js
│   │   ├── Footer.js
```

---

## **1. API 통신 (`api`)**

### `api/api.js`

```javascript
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:3000',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default apiClient;
```

### `api/todos.js`

```javascript
import apiClient from './api';

export const fetchTodos = async () => {
  const response = await apiClient.get('/todo');
  return response.data;
};

export const fetchTodoById = async (id) => {
  const response = await apiClient.get(`/todo/${id}`);
  return response.data;
};

export const createTodo = async (data) => {
  const response = await apiClient.post('/todo', data);
  return response.data;
};

export const updateTodo = async (id, data) => {
  const response = await apiClient.put(`/todo/${id}`, data);
  return response.data;
};

export const patchTodo = async (id) => {
  const response = await apiClient.patch(`/todo/${id}`);
  return response.data;
};

export const deleteTodo = async (id) => {
  const response = await apiClient.delete(`/todo/${id}`);
  return response.data;
};
```

---

## **2. Zustand 스토어 (`stores`)**

### `stores/todoStore.js`

```javascript
import { create } from 'zustand';
import { fetchTodos, fetchTodoById, createTodo, updateTodo, patchTodo, deleteTodo } from '../api/todos';

const useTodoStore = create((set) => ({
  todos: [],
  selectedTodo: null,
  loading: false,
  error: null,
  fetchAllTodos: async () => {
    set({ loading: true, error: null });
    try {
      const todos = await fetchTodos();
      set({ todos, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  fetchTodoDetail: async (id) => {
    set({ loading: true, error: null });
    try {
      const todo = await fetchTodoById(id);
      set({ selectedTodo: todo, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  createNewTodo: async (data) => {
    set({ loading: true, error: null });
    try {
      await createTodo(data);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  updateExistingTodo: async (id, data) => {
    set({ loading: true, error: null });
    try {
      await updateTodo(id, data);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  patchExistingTodo: async (id) => {
    set({ loading: true, error: null });
    try {
      await patchTodo(id);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  deleteExistingTodo: async (id) => {
    set({ loading: true, error: null });
    try {
      await deleteTodo(id);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default useTodoStore;
```

---

## **3. 컴포넌트 페이지 (`pages`)**

### `pages/HomePage.js`

```javascript
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import useTodoStore from '../stores/todoStore';

function HomePage() {
  const { todos, fetchAllTodos, loading, error, createNewTodo, deleteExistingTodo } = useTodoStore();
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  useEffect(() => {
    fetchAllTodos();
  }, [fetchAllTodos]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createNewTodo({ title, description });
    await fetchAllTodos();
    setTitle('');
    setDescription('');
  };

  const handleDelete = async (id) => {
    await deleteExistingTodo(id);
    await fetchAllTodos();
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>Home</h1>
      <form onSubmit={handleSubmit}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
        />
        <input
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description"
        />
        <button type="submit">Create Todo</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <Link to={`/todos/${todo.id}`}>
              {todo.title} - {todo.description} - {todo.completed ? '완료' : '진행 중'}
            </Link>
            <button onClick={() => handleDelete(todo.id)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
```

### `pages/TodoDetailPage.js`

```javascript
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import useTodoStore from '../stores/todoStore';

function TodoDetailPage() {
  const { id } = useParams();
  const { selectedTodo, fetchTodoDetail, loading, error, patchExistingTodo, updateExistingTodo } = useTodoStore();

  useEffect(() => {
    fetchTodoDetail(id);
  }, [fetchTodoDetail, id]);

  const handleComplete = async () => {
    await patchExistingTodo(id);
    await fetchTodoDetail(id);
  };

  const handleUpdate = async () => {
    await updateExistingTodo(id, { title: selectedTodo.title + ' (수정)' });
    await fetchTodoDetail(id);
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  if (!selectedTodo) {
    return <p>Todo not found</p>;
  }

  return (
    <div>
      <h1>{selectedTodo.title}</h1>
      <p>{selectedTodo.description}</p>
      <p>상태: {selectedTodo.completed ? '완료' : '진행 중'}</p>
      <button onClick={handleComplete}>완료하기</button>
      <button onClick={handleUpdate}>제목 수정</button>
    </div>
  );
}

export default TodoDetailPage;
```

---

## **4. 컴포넌트 (`components`)**

### `components/Header.js`

```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="App-header">
      <nav>
        <Link to="/">Home</Link>
      </nav>
    </header>
  );
}

export default Header;
```

### `components/Footer.js`

```javascript
import React from 'react';

function Footer() {
  return (
    <footer>
      <p>Footer</p>
    </footer>
  );
}

export default Footer;
```

---

## **5. 메인 앱 구성**

### `App.js`

```javascript
import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import HomePage from './pages/HomePage';
import TodoDetailPage from './pages/TodoDetailPage';
import Header from './components/Header';
import Footer from './components/Footer';
import './App.css';

const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage />
  },
  {
    path: '/todos/:id',
    element: <TodoDetailPage />
  }
]);

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <RouterProvider router={router} />
      </main>
      <Footer />
    </div>
  );
}

export default App;
```

### `App.css`

```css
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  color: #333;
}

.App-header {
  background-color: #282c34;
  padding: 20px;
  color: white;
  text-align: center;
}

.App-header nav a {
  margin: 0 15px;
  color: #61dafb;
  text-decoration: none;
}

.App-header nav a:hover {
  color: #21a1f1;
}

main {
  padding: 20px;
}

footer {
  text-align: center;
  margin-top: 40px;
}
```

---

## **변경 요약**

1. `HomePage`는 Todo 목록과 생성 및 삭제 기능을 담당합니다.
2. `TodoDetailPage`는 Todo의 세부 정보와 상태 업데이트 및 수정 기능을 제공합니다.
3. 모든 필요 기능이 두 페이지로 통합되었습니다.