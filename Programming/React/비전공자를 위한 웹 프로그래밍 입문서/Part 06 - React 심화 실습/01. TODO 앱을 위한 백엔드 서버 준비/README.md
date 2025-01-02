## **1. TodoRest 백엔드 클론 및 설정**

### 1.1 저장소 클론

백엔드 프로젝트를 로컬 환경에 다운로드합니다.

```bash
git clone https://github.com/DDottan/TodoRest.git
cd TodoRest
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
    http://localhost:3000/todo
    ```
    
- 초기 상태에서는 빈 배열이 반환됩니다:
    
    ```json
    []
    ```
    

## **3. API 테스트**

API가 제대로 작동하는지 확인하기 위해 `curl` 명령어나 Postman을 사용하여 각 엔드포인트를 테스트합니다.

### 3.1 모든 Todo 조회 (GET)

```bash
curl -X GET http://localhost:3000/todo
```

**결과 예시:**

```json
[]
```

### 3.2 새 Todo 생성 (POST)

```bash
curl -X POST http://localhost:3000/todo \
-H "Content-Type: application/json" \
-d '{"title": "Test Task", "description": "Learn Backend Setup"}'
```

**결과 예시:**

```json
{
  "id": "1691234567890",
  "title": "Test Task",
  "description": "Learn Backend Setup",
  "completed": false
}
```

### 3.3 특정 Todo 조회 (GET)

```bash
curl -X GET http://localhost:3000/todo/1691234567890
```

**결과 예시:**

```json
{
  "id": "1691234567890",
  "title": "Test Task",
  "description": "Learn Backend Setup",
  "completed": false
}
```

### 3.4 Todo 수정 (PUT)

```bash
curl -X PUT http://localhost:3000/todo/1691234567890 \
-H "Content-Type: application/json" \
-d '{"title": "Updated Task", "description": "Backend Guide Updated"}'
```

**결과 예시:**

```json
{
  "id": "1691234567890",
  "title": "Updated Task",
  "description": "Backend Guide Updated",
  "completed": false
}
```

### 3.5 Todo 완료 처리 (PATCH)

```bash
curl -X PATCH http://localhost:3000/todo/1691234567890
```

**결과 예시:**

```json
{
  "id": "1691234567890",
  "title": "Updated Task",
  "description": "Backend Guide Updated",
  "completed": true
}
```

### 3.6 Todo 삭제 (DELETE)

```bash
curl -X DELETE http://localhost:3000/todo/1691234567890
```

**결과 예시:**

```json
{
  "success": true
}
```

