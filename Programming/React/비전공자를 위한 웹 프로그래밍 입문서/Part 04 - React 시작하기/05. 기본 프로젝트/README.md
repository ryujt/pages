## **프로젝트 구조**

```
D:\Projects\Do\test-react\
├── src\
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   ├── setupTests.js
│   ├── api\
│   │   ├── api.js
│   │   ├── users.js
│   │   ├── posts.js
│   ├── stores\
│   │   ├── userStore.js
│   │   ├── postStore.js
│   ├── pages\
│   │   ├── HomePage.js
│   │   ├── UsersPage.js
│   │   ├── PostsPage.js
│   ├── components\
│   │   ├── Header.js
│   │   ├── Footer.js
```

---

## **1. API 통신(`api`)**

### `api/api.js`

```javascript
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default apiClient;
```

### `api/users.js`

```javascript
import apiClient from './api';

export const fetchUsers = async () => {
  const response = await apiClient.get('/users');
  return response.data;
};
```

### `api/posts.js`

```javascript
import apiClient from './api';

export const fetchPosts = async () => {
  const response = await apiClient.get('/posts');
  return response.data;
};
```

---

## **2. Zustand 스토어(`stores`)**

### `stores/userStore.js`

```javascript
import { create } from 'zustand';
import { fetchUsers } from '../api/users';

const useUserStore = create((set) => ({
  users: [],
  loading: false,
  error: null,
  fetchAllUsers: async () => {
    set({ loading: true, error: null });
    try {
      const users = await fetchUsers();
      set({ users, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default useUserStore;
```

### `stores/postStore.js`

```javascript
import { create } from 'zustand';
import { fetchPosts } from '../api/posts';

const usePostStore = create((set) => ({
  posts: [],
  loading: false,
  error: null,
  fetchAllPosts: async () => {
    set({ loading: true, error: null });
    try {
      const posts = await fetchPosts();
      set({ posts, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default usePostStore;
```

---

## **3. 컴포넌트 페이지(`pages`)**

### `pages/HomePage.js`

```javascript
import React from 'react';

function HomePage() {
  return (
    <div>
      <h1>Home Page</h1>
    </div>
  );
}

export default HomePage;
```

### `pages/UsersPage.js`

```javascript
import React, { useEffect } from 'react';
import useUserStore from '../stores/userStore';

function UsersPage() {
  const { users, fetchAllUsers, loading, error } = useUserStore();

  useEffect(() => {
    fetchAllUsers();
  }, [fetchAllUsers]);

  if (loading) {
    return <p>Loading users...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <strong>{user.name}</strong> ({user.username}) - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UsersPage;
```

### `pages/PostsPage.js`

```javascript
import React, { useEffect } from 'react';
import usePostStore from '../stores/postStore';

function PostsPage() {
  const { posts, fetchAllPosts, loading, error } = usePostStore();

  useEffect(() => {
    fetchAllPosts();
  }, [fetchAllPosts]);

  if (loading) {
    return <p>Loading posts...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>Post List</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostsPage;
```

---

## **4. 컴포넌트(`components`)**

### `components/Header.js`

```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="App-header">
      <nav>
        <Link to="/">Home</Link>
        <Link to="/users">Users</Link>
        <Link to="/posts">Posts</Link>
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
import UsersPage from './pages/UsersPage';
import PostsPage from './pages/PostsPage';
import Header from './components/Header';
import Footer from './components/Footer';
import './App.css';

const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage />
  },
  {
    path: '/users',
    element: <UsersPage />
  },
  {
    path: '/posts',
    element: <PostsPage />
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

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #fff;
  margin: 10px 0;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

## **6. 실행 및 테스트**

1. **패키지 설치**
    
    ```bash
    npm install
    ```
    
2. **개발 서버 실행**
    
    ```bash
    npm start
    ```
    
3. **테스트**
    
    - `/users` 경로에서 사용자 목록이 잘 표시되는지 확인합니다.
    - `/posts` 경로에서 게시물 목록이 잘 표시되는지 확인합니다.
    - `/` 경로(홈)에서 `HomePage`가 렌더링되는지 확인합니다.