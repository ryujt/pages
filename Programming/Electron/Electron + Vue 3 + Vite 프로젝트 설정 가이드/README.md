# Electron + Vue 3 + Vite 프로젝트 설정 가이드

이 가이드는 Electron, Vue 3, 그리고 Vite를 JavaScript로 사용하여 기본적인 "Hello World" 애플리케이션을 만드는 과정을 설명합니다.

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
npm install electron electron-builder vite-plugin-electron vite-plugin-electron-renderer -D
```

## 3. 프로젝트 구조 설정

다음과 같은 프로젝트 구조를 만듭니다:

```
electron-vue-vite/
├── electron/
│   ├── main.js
│   └── preload.js
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
      preload: path.join(__dirname, 'preload.js')  // 이 경로가 올바른지 확인하세요
    },
  })

  if (process.env.VITE_DEV_SERVER_URL) {
    win.loadURL(process.env.VITE_DEV_SERVER_URL)
  } else {
    win.loadFile(path.join(__dirname, '../dist/index.html'))
  }

  win.webContents.openDevTools()
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

// 디버깅을 위한 코드
console.log('Preload path:', path.join(__dirname, 'preload.js'))
console.log('__dirname:', __dirname)
console.log('App path:', app.getAppPath())
```

## 5. preload.js 파일 생성

`electron/preload.js` 파일을 생성하고 다음 내용을 추가합니다:

```javascript
const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  sendMessage: (message) => ipcRenderer.send('message', message),
  onReceiveMessage: (callback) => ipcRenderer.on('message', (event, message) => callback(message)),
  versions: process.versions
})

window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) element.innerText = text
  }

  for (const dependency of ['chrome', 'node', 'electron']) {
    replaceText(`${dependency}-version`, process.versions[dependency])
  }
})
```

## 6. Vite 설정 파일 수정

`vite.config.js` 파일을 다음과 같이 수정합니다:

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'
import { resolve } from 'path'

export default defineConfig({
  plugins: [
    vue(),
    electron({
      entry: 'electron/main.js',
      vite: {
        build: {
          outDir: 'dist-electron',
        },
      },
    }),
    electron({
      entry: 'electron/preload.js',
      onstart(options) {
        options.startup()
      },
    }),
  ],
  build: {
    outDir: 'dist',
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
})
```

## 7. package.json 수정

`package.json` 파일을 다음과 같이 수정합니다:

```json
{
  "name": "electron-vue-vite",
  "version": "1.0.0",
  "main": "dist-electron/main.js",
  "scripts": {
    "dev": "vite",
    "build": "vite build && electron-builder",
    "preview": "vite preview",
    "electron:dev": "vite build && vite build --config vite.config.js && electron ."
  },
  "build": {
    "appId": "com.example.electron-vue-vite",
    "productName": "Electron Vue Vite App",
    "files": [
      "dist/**/*",
      "dist-electron/**/*"
    ],
    "directories": {
      "output": "release/${version}"
    },
    "win": {
      "target": ["nsis", "portable"]
    }
  },
  ...
}
```

## 8. 애플리케이션 실행

개발 모드에서 애플리케이션을 실행하려면:

```bash
npm run electron:dev
```

## 9. 빌드 및 배포

프로덕션용 빌드를 생성하려면:

```bash
npm run build
```

이 명령은 `dist` 폴더에 Vue 앱을, `dist-electron` 폴더에 Electron 관련 파일들을 생성합니다.

## 주의사항

- Node.js와 npm 버전이 프로젝트 요구사항과 일치하는지 확인하세요.
- Electron 버전과 다른 의존성 버전이 호환되는지 확인하세요.
- 문제가 발생하면 의존성을 재설치하거나 (`npm ci`), Node.js 캐시를 정리 (`npm cache clean --force`)해 보세요.
- `vite-plugin-electron`과 `vite-plugin-electron-renderer`를 사용하여 Electron의 메인 프로세스와 프리로드 스크립트를 올바르게 빌드하고 관리합니다.

이 가이드를 따라 설정하면 JavaScript 기반의 Electron + Vue 3 + Vite 프로젝트가 정상적으로 작동할 것입니다. 추가 기능이나 최적화가 필요한 경우 각 도구의 공식 문서를 참조하세요.
