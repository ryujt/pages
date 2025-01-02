## **프로젝트 구조**

```
D:\Projects\ShopApp\
├── src\
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   ├── api\
│   │   ├── api.js
│   │   ├── users.js
│   │   ├── products.js
│   │   ├── cart.js
│   ├── stores\
│   │   ├── userStore.js
│   │   ├── productStore.js
│   │   ├── cartStore.js
│   ├── pages\
│   │   ├── HomePage.js
│   │   ├── SignUpPage.js
│   │   ├── LoginPage.js
│   │   ├── ProductListPage.js
│   │   ├── ProductDetailPage.js
│   │   ├── CartPage.js
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
  baseURL: 'http://localhost:3000',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default apiClient;
```

### `api/users.js`

```javascript
import apiClient from './api';

export const signUp = async (username, password) => {
  const response = await apiClient.post('/users/signup', { username, password });
  return response.data;
};

export const login = async (username, password) => {
  const response = await apiClient.post('/users/login', { username, password });
  return response.data;
};
```

### `api/products.js`

```javascript
import apiClient from './api';

export const fetchProducts = async () => {
  const response = await apiClient.get('/products');
  return response.data;
};

export const fetchProductById = async (id) => {
  const response = await apiClient.get(`/products/${id}`);
  return response.data;
};

export const createProduct = async (name, price) => {
  const response = await apiClient.post('/products', { name, price });
  return response.data;
};

export const updateProduct = async (id, name, price) => {
  const response = await apiClient.put(`/products/${id}`, { name, price });
  return response.data;
};

export const deleteProduct = async (id) => {
  const response = await apiClient.delete(`/products/${id}`);
  return response.data;
};
```

### `api/cart.js`

```javascript
import apiClient from './api';

export const fetchCart = async (userId) => {
  const response = await apiClient.get('/cart', { params: { userId } });
  return response.data;
};

export const addToCart = async (userId, productId, quantity) => {
  const response = await apiClient.post('/cart', { userId, productId, quantity });
  return response.data;
};

export const updateCartItem = async (cartId, quantity) => {
  const response = await apiClient.put(`/cart/${cartId}`, { quantity });
  return response.data;
};

export const deleteCartItem = async (cartId) => {
  const response = await apiClient.delete(`/cart/${cartId}`);
  return response.data;
};
```

---

## **2. Zustand 스토어(`stores`)**

### `stores/userStore.js`

```javascript
import { create } from 'zustand';
import { signUp, login } from '../api/users';

const useUserStore = create((set) => ({
  user: null,
  error: null,
  loading: false,
  signUpUser: async (username, password) => {
    set({ loading: true, error: null });
    try {
      const data = await signUp(username, password);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  loginUser: async (username, password) => {
    set({ loading: true, error: null });
    try {
      const data = await login(username, password);
      set({ user: data.user, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default useUserStore;
```

### `stores/productStore.js`

```javascript
import { create } from 'zustand';
import { fetchProducts, fetchProductById, createProduct, updateProduct, deleteProduct } from '../api/products';

const useProductStore = create((set) => ({
  products: [],
  selectedProduct: null,
  loading: false,
  error: null,
  fetchAllProducts: async () => {
    set({ loading: true, error: null });
    try {
      const data = await fetchProducts();
      set({ products: data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  fetchProductDetail: async (id) => {
    set({ loading: true, error: null });
    try {
      const data = await fetchProductById(id);
      set({ selectedProduct: data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  createNewProduct: async (name, price) => {
    set({ loading: true, error: null });
    try {
      await createProduct(name, price);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  updateExistingProduct: async (id, name, price) => {
    set({ loading: true, error: null });
    try {
      await updateProduct(id, name, price);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  deleteExistingProduct: async (id) => {
    set({ loading: true, error: null });
    try {
      await deleteProduct(id);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default useProductStore;
```

### `stores/cartStore.js`

```javascript
import { create } from 'zustand';
import { fetchCart, addToCart, updateCartItem, deleteCartItem } from '../api/cart';

const useCartStore = create((set) => ({
  cartItems: [],
  loading: false,
  error: null,
  fetchCartItems: async (userId) => {
    set({ loading: true, error: null });
    try {
      const data = await fetchCart(userId);
      set({ cartItems: data, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  addCartItem: async (userId, productId, quantity) => {
    set({ loading: true, error: null });
    try {
      await addToCart(userId, productId, quantity);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  updateCartQuantity: async (cartId, quantity) => {
    set({ loading: true, error: null });
    try {
      await updateCartItem(cartId, quantity);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  removeCartItem: async (cartId) => {
    set({ loading: true, error: null });
    try {
      await deleteCartItem(cartId);
      set({ loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  }
}));

export default useCartStore;
```

---

## **3. 컴포넌트 페이지(`pages`)**

### `pages/HomePage.js`

```javascript
import React from 'react';

function HomePage() {
  return (
    <div>
      <h1>홈 페이지</h1>
      <p>쇼핑몰에 오신 것을 환영합니다.</p>
    </div>
  );
}

export default HomePage;
```

### `pages/SignUpPage.js`

```javascript
import React, { useState } from 'react';
import useUserStore from '../stores/userStore';

function SignUpPage() {
  const { signUpUser, loading, error } = useUserStore();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSignUp = async (e) => {
    e.preventDefault();
    await signUpUser(username, password);
  };

  if (loading) {
    return <p>회원가입 중...</p>;
  }

  return (
    <div>
      <h1>회원가입</h1>
      {error && <p>{error}</p>}
      <form onSubmit={handleSignUp}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="아이디" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="비밀번호" />
        <button type="submit">회원가입</button>
      </form>
    </div>
  );
}

export default SignUpPage;
```

### `pages/LoginPage.js`

```javascript
import React, { useState } from 'react';
import useUserStore from '../stores/userStore';

function LoginPage() {
  const { loginUser, loading, error } = useUserStore();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    await loginUser(username, password);
  };

  if (loading) {
    return <p>로그인 중...</p>;
  }

  return (
    <div>
      <h1>로그인</h1>
      {error && <p>{error}</p>}
      <form onSubmit={handleLogin}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="아이디" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="비밀번호" />
        <button type="submit">로그인</button>
      </form>
    </div>
  );
}

export default LoginPage;
```

### `pages/ProductListPage.js`

```javascript
import React, { useEffect } from 'react';
import useProductStore from '../stores/productStore';

function ProductListPage() {
  const { products, fetchAllProducts, loading, error } = useProductStore();

  useEffect(() => {
    fetchAllProducts();
  }, [fetchAllProducts]);

  if (loading) {
    return <p>상품 불러오는 중...</p>;
  }

  if (error) {
    return <p>에러 발생: {error}</p>;
  }

  return (
    <div>
      <h1>상품 목록</h1>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - {product.price}원
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductListPage;
```

### `pages/ProductDetailPage.js`

```javascript
import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import useProductStore from '../stores/productStore';

function ProductDetailPage() {
  const { id } = useParams();
  const { selectedProduct, fetchProductDetail, loading, error } = useProductStore();

  useEffect(() => {
    fetchProductDetail(id);
  }, [fetchProductDetail, id]);

  if (loading) {
    return <p>상품 정보를 불러오는 중...</p>;
  }

  if (error) {
    return <p>에러 발생: {error}</p>;
  }

  if (!selectedProduct) {
    return <p>해당 상품을 찾을 수 없습니다.</p>;
  }

  return (
    <div>
      <h1>{selectedProduct.name}</h1>
      <p>가격: {selectedProduct.price}원</p>
    </div>
  );
}

export default ProductDetailPage;
```

### `pages/CartPage.js`

```javascript
import React, { useEffect } from 'react';
import useCartStore from '../stores/cartStore';
import useUserStore from '../stores/userStore';

function CartPage() {
  const { user } = useUserStore();
  const { cartItems, fetchCartItems, loading, error, updateCartQuantity, removeCartItem } = useCartStore();

  useEffect(() => {
    if (user) {
      fetchCartItems(user.id);
    }
  }, [fetchCartItems, user]);

  if (!user) {
    return <p>로그인 후 이용해 주세요.</p>;
  }

  if (loading) {
    return <p>장바구니 불러오는 중...</p>;
  }

  if (error) {
    return <p>에러 발생: {error}</p>;
  }

  return (
    <div>
      <h1>장바구니</h1>
      <ul>
        {cartItems.map((item) => (
          <li key={item.id}>
            상품ID: {item.productId}, 수량: {item.quantity}
            <button onClick={() => updateCartQuantity(item.id, item.quantity + 1)}>+</button>
            <button onClick={() => updateCartQuantity(item.id, item.quantity - 1)}>-</button>
            <button onClick={() => removeCartItem(item.id)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CartPage;
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
        <Link to="/">홈</Link>
        <Link to="/products">상품목록</Link>
        <Link to="/cart">장바구니</Link>
        <Link to="/signup">회원가입</Link>
        <Link to="/login">로그인</Link>
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
      <p>© 쇼핑몰</p>
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
import { createBrowserRouter, RouterProvider, Outlet } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SignUpPage from './pages/SignUpPage';
import LoginPage from './pages/LoginPage';
import ProductListPage from './pages/ProductListPage';
import ProductDetailPage from './pages/ProductDetailPage';
import CartPage from './pages/CartPage';
import Header from './components/Header';
import Footer from './components/Footer';
import './App.css';

// 공통 레이아웃 컴포넌트
function Layout() {
  return (
    <div className="App">
      <Header />
      <main>
        <Outlet /> {/* 현재 경로의 페이지가 렌더링되는 위치 */}
      </main>
      <Footer />
    </div>
  );
}

// 라우터 정의
const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />, // 공통 레이아웃을 사용
    children: [
      { path: '/', element: <HomePage /> },
      { path: '/signup', element: <SignUpPage /> },
      { path: '/login', element: <LoginPage /> },
      { path: '/products', element: <ProductListPage /> },
      { path: '/products/:id', element: <ProductDetailPage /> },
      { path: '/cart', element: <CartPage /> }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />;
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

## **6. 실행 및 테스트**

1. **패키지 설치**
    
    ```bash
    npm install react-dom@^18.2.0 axios react-router-dom web-vitals zustand
    ```
    
2. **개발 서버 실행**
    
    ```bash
    npm start
    ```
    
3. **테스트**
    
    - `/signup` 페이지에서 회원가입 후, 회원가입 성공 메시지가 뜨는지 확인합니다.
    - `/login` 페이지에서 로그인 후, user 정보가 정상적으로 스토어에 저장되는지 확인합니다.
    - `/products` 경로에서 상품 목록이 표시되는지 확인합니다.
    - `/products/:id` 경로에서 해당 상품 상세 페이지가 정상적으로 표시되는지 확인합니다.
    - `/cart` 페이지에서 장바구니 아이템 목록이 표시되는지 확인합니다.
    - 홈(`/`) 페이지에서 정상적으로 렌더링되는지 확인합니다.