## **1. ShopRest 백엔드 클론 및 설정**

### 1.1 저장소 클론

백엔드 프로젝트를 로컬 환경에 다운로드합니다.

```bash
git clone https://github.com/DDottan/ShopRest.git
cd ShopRest
```

### 1.2 패키지 설치

Node.js 패키지를 설치하여 서버를 실행할 준비를 합니다.

```bash
npm install
```

## **2. 백엔드 서버 실행**

### 2.1 서버 시작

```bash
node index.js
```

### 2.2 실행 확인

- 서버가 정상적으로 실행되면 콘솔에 다음 메시지가 출력됩니다:
    
    ```
    Server running on port 3000
    ```
    
- 브라우저 또는 Postman에서 아래 URL을 열어 서버가 정상적으로 동작하는지 확인합니다:
    
    ```
    http://localhost:3000/products
    ```
    
- 초기 상태에서는 빈 배열이 반환될 수 있습니다:
    
    ```json
    []
    ```
    

## **3. API 테스트**

API가 제대로 작동하는지 확인하기 위해 `curl` 명령어나 Postman을 사용하여 각 엔드포인트를 테스트합니다.

### 3.1 사용자 가입 (POST)

```bash
curl -X POST http://localhost:3000/users/signup \
-H "Content-Type: application/json" \
-d '{"username": "user1", "password": "pass123"}'
```

**결과 예시:**

```json
{
  "message": "회원가입 성공",
  "user": {
    "id": "1691234567890",
    "username": "user1"
  }
}
```

### 3.2 사용자 로그인 (POST)

```bash
curl -X POST http://localhost:3000/users/login \
-H "Content-Type: application/json" \
-d '{"username": "user1", "password": "pass123"}'
```

**결과 예시:**

```json
{
  "message": "로그인 성공",
  "user": {
    "id": "1691234567890",
    "username": "user1"
  }
}
```

### 3.3 모든 상품 조회 (GET)

```bash
curl -X GET http://localhost:3000/products
```

**결과 예시:**

```json
[]
```

### 3.4 상품 추가 (POST)

```bash
curl -X POST http://localhost:3000/products \
-H "Content-Type: application/json" \
-d '{"name": "Laptop", "price": 1500}'
```

**결과 예시:**

```json
{
  "id": "1691234567891",
  "name": "Laptop",
  "price": 1500,
  "createdAt": "2024-12-30T00:00:00.000Z"
}
```

### 3.5 장바구니 상품 추가 (POST)

```bash
curl -X POST http://localhost:3000/cart \
-H "Content-Type: application/json" \
-d '{"userId": "user1", "productId": "1691234567891", "quantity": 2}'
```

**결과 예시:**

```json
{
  "id": "1691234567892",
  "userId": "user1",
  "productId": "1691234567891",
  "quantity": 2
}
```

### 3.6 사용자 장바구니 조회 (GET)

```bash
curl -X GET http://localhost:3000/cart?userId=user1
```

**결과 예시:**

```json
[
  {
    "id": "1691234567892",
    "userId": "user1",
    "productId": "1691234567891",
    "quantity": 2
  }
]
```
