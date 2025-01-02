## 1. **Node.js 설치**

1. [Node.js 공식 웹사이트](https://nodejs.org)로 이동합니다.  
2. LTS(Long-Term Support) 버전을 다운로드하여 설치합니다.  
3. 설치가 완료되면 아래 명령어로 Node.js와 npm이 설치되었는지 확인합니다:  
   ```bash
   node -v
   npm -v
   ```
   - `node -v`: Node.js 버전 출력  
   - `npm -v`: npm(Node Package Manager) 버전 출력  

---

## 2. **React 프로젝트 생성**

React 프로젝트를 생성하려면 Facebook에서 제공하는 **Create React App** 도구를 사용할 수 있습니다.

### 1. **터미널에서 프로젝트 디렉토리로 이동**
   ```bash
   cd 원하는_디렉토리_경로
   ```

### 2. **React 프로젝트 생성**
   아래 명령어를 실행하여 새 React 애플리케이션을 생성합니다:
   ```bash
   npx create-react-app 프로젝트명
   ```
   예: `npx create-react-app my-app`

   - `npx`: npm 5.2+ 및 Node.js 8.2+에 포함된 도구로, 라이브러리를 전역 설치 없이 실행 가능.
   - `프로젝트명`: 생성될 React 애플리케이션의 디렉토리 이름.

### 3. **프로젝트 생성 완료**
   프로젝트가 생성되면 다음과 같은 디렉토리 구조가 생성됩니다:
   ```
   프로젝트명/
   ├── node_modules/
   ├── public/
   ├── src/
   ├── .gitignore
   ├── package.json
   ├── README.md
   └── yarn.lock (또는 package-lock.json)
   ```

---

## 3. **React 애플리케이션 실행**

### 1. **생성된 프로젝트 디렉토리로 이동**
   ```bash
   cd 프로젝트명
   ```

### 2. **애플리케이션 실행**
   ```bash
   npm start
   ```
   - 이 명령어를 실행하면 기본 웹 브라우저가 열리며 `http://localhost:3000`에서 애플리케이션이 실행됩니다.

---

## 4. **필수 패키지 설치 (선택 사항)**

프로젝트에 필요한 추가 라이브러리를 설치하려면 `npm install` 명령어를 사용합니다.  
예를 들어, 다음과 같은 라이브러리를 설치할 수 있습니다:

- **React Router** 설치:
  ```bash
  npm install react-router-dom
  ```

- **Redux 상태 관리 라이브러리** 설치:
  ```bash
  npm install redux react-redux
  ```

---

## 5. **코드 편집**

1. 프로젝트의 `src/` 디렉토리에서 React 컴포넌트 파일을 수정하거나 새로운 파일을 추가합니다.  
2. 코드 편집기를 사용해 개발합니다. **VS Code**를 추천합니다.

---

## 6. **React 빌드**

1. 애플리케이션을 프로덕션 환경에 배포하려면 빌드를 수행합니다:  
   ```bash
   npm run build
   ```
2. `build/` 디렉토리가 생성되며, 배포 가능한 최적화된 파일이 포함됩니다.

---

## 7. **프로젝트 종료 및 다시 시작**

- **애플리케이션 종료**:
  터미널에서 `Ctrl + C`를 눌러 서버를 중지합니다.  
- **다시 시작**:
  프로젝트 디렉토리로 이동 후 `npm start` 명령어를 실행합니다.
