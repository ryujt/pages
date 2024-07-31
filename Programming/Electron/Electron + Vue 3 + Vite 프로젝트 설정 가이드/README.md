# Electron + Vue 3 + Vite 프로젝트 설정 가이드

이 가이드는 Electron, Vue 3, 그리고 Vite를 사용하여 기본적인 "Hello World" 애플리케이션을 만드는 과정을 설명합니다.

## 필수 조건

- Node.js (v14 이상)
- npm (v6 이상)

## 1. 프로젝트 생성

먼저, Vite를 사용하여 새 Vue 프로젝트를 생성합니다:

```bash
npm create vite@latest electron-vue-vite -- --template vue
cd electron-vue-vite
npm install
```

## 2. Electron 관련 패키지 설치

프로젝트에 Electron과 관련 개발 도구를 추가합니다:

```bash
npm install electron electron-builder vite-plugin-electron -D
```

## 3. 프로젝트 구조 설정

다음과 같은 프로젝트 구조를 만듭니다:

```
electron-vue-vite/
├── electron/
│   └── main.js
├── src/
│   ├── App.vue
│   └── main.js
├── index.html
├── package.json
└── vite.config.js
```

## 4. Electron 메인 프로세스 파일 생성

`electron/main.js` 파일을 생성하고 다음 내용을 추가합니다:

```javascript
const { app, BrowserWindow } = require('electron')
const path = require('path')

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION === 'true',
      contextIsolation: process.env.ELECTRON_NODE_INTEGRATION !== 'true',
    },
  })

  if (process.env.VITE_DEV_SERVER_URL) {
    win.loadURL(process.env.VITE_DEV_SERVER_URL)
  } else {
    win.loadFile(path.join(__dirname, '../dist/index.html'))
  }
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})
```

## 5. Vite 설정 파일 수정

`vite.config.js` 파일을 다음과 같이 수정합니다:

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'

export default defineConfig({
  plugins: [
    vue(),
    electron({
      entry: 'electron/main.js',
    }),
  ],
})
```

## 6. package.json 수정

`package.json` 파일을 다음과 같이 수정합니다:

```json
{
  ...
  "type": "commonjs",
  "main": "electron/main.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "electron:dev": "vite build && electron .",
    "electron:build": "vite build && electron-builder",
    "postinstall": "electron-builder install-app-deps"
  },
  ...
}
```

## 7. 애플리케이션 실행

개발 모드에서 애플리케이션을 실행하려면:

```bash
npm run electron:dev
```

## 8. 빌드 및 배포

프로덕션용 빌드를 생성하려면:

```bash
npm run electron:build
```

이 명령은 `dist_electron` 폴더에 배포 가능한 애플리케이션을 생성합니다.

## 주의사항

- Node.js와 npm 버전이 프로젝트 요구사항과 일치하는지 확인하세요.
- Electron 버전과 다른 의존성 버전이 호환되는지 확인하세요.
- 보안을 위해 프로덕션 환경에서는 `nodeIntegration: false`와 `contextIsolation: true`를 사용하는 것이 좋습니다.
- 문제가 발생하면 의존성을 재설치하거나 (`npm ci`), Node.js 캐시를 정리 (`npm cache clean --force`)해 보세요.

이 가이드를 따라 설정하면 기본적인 Electron + Vue 3 + Vite 프로젝트가 구성됩니다. 추가 기능이나 최적화가 필요한 경우 각 도구의 공식 문서를 참조하세요.