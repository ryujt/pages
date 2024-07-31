# Electron과 C++ 연동 프로젝트 생성 튜토리얼

이 튜토리얼에서는 Electron 프로젝트에서 C++를 연동하는 방법을 단계별로 설명합니다.

## 전제 조건

이 튜토리얼을 따라하기 전에 다음 도구들이 시스템에 설치되어 있어야 합니다:

1. **Node.js와 npm**: 최신 LTS 버전을 권장합니다.
   - 설치: https://nodejs.org/

2. **Python**: node-gyp는 Python을 필요로 합니다 (2.7, 3.5, 3.6, 3.7, 또는 3.8 버전).
   - 설치: https://www.python.org/downloads/

3. **C++ 컴파일러**:
   - Windows: Visual Studio Build Tools
     - 설치: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - macOS: Xcode Command Line Tools
     - 설치: Terminal에서 `xcode-select --install` 실행
   - Linux: GCC
     - 설치: `sudo apt-get install build-essential` (Ubuntu/Debian)

4. **node-gyp**: npm을 통해 전역으로 설치할 수 있습니다.
   ```
   npm install -g node-gyp
   ```

이러한 도구들이 올바르게 설치되어 있는지 확인 후 튜토리얼을 진행해 주세요.

## 1. Electron 프로젝트 생성

먼저 새로운 Electron 프로젝트를 생성합니다:

```bash
mkdir electron-cpp-example
cd electron-cpp-example
npm init -y
npm install electron --save-dev
```

## 2. 기본 Electron 앱 설정

### package.json 수정

`package.json` 파일을 다음과 같이 수정합니다:

```json
{
  "name": "electron-cpp-example",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "devDependencies": {
    "electron": "^x.x.x"
  }
}
```

### main.js 생성

`main.js` 파일을 생성하고 기본 Electron 앱 코드를 작성합니다:

```javascript
const { app, BrowserWindow } = require('electron');

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile('index.html');
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
```

### index.html 생성

`index.html` 파일을 생성합니다:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Electron C++ Example</title>
</head>
<body>
    <h1>Electron C++ Example</h1>
    <div id="result"></div>
    <script src="renderer.js"></script>
</body>
</html>
```

## 3. Node.js 네이티브 애드온 설정

C++ 애드온을 위한 패키지를 설치합니다:

```bash
npm install node-gyp --save-dev
npm install node-addon-api --save
```

`binding.gyp` 파일을 생성하고 다음 내용을 추가합니다:

```json
{
  "targets": [
    {
      "target_name": "cpp_addon",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "cpp_addon.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ]
    }
  ]
}
```

## 4. C++ 애드온 코드 작성

`cpp_addon.cc` 파일을 생성하고 다음 코드를 작성합니다:

```cpp
#include <napi.h>

Napi::String HelloMethod(const Napi::CallbackInfo& info) {
  Napi::Env env = info.Env();
  return Napi::String::New(env, "Hello from C++!");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "hello"),
              Napi::Function::New(env, HelloMethod));
  return exports;
}

NODE_API_MODULE(cpp_addon, Init)
```

## 5. 애드온 빌드

다음 명령어로 C++ 애드온을 빌드합니다:

```bash
node-gyp configure build
```

## 6. Electron 앱에서 C++ 애드온 사용

`renderer.js` 파일을 생성하고 다음 코드를 작성합니다:

```javascript
const addon = require('./build/Release/cpp_addon.node');

document.addEventListener('DOMContentLoaded', () => {
  const result = document.getElementById('result');
  result.textContent = addon.hello();
});
```

## 7. 앱 실행

이제 Electron 앱을 실행할 수 있습니다:

```bash
npm start
```

이 예제에서는 C++로 작성된 간단한 "Hello" 함수를 Electron 앱에서 호출합니다. 실제 프로젝트에서는 이를 확장하여 더 복잡한 C++ 기능을 구현하고 Electron 앱에서 사용할 수 있습니다.

## 주의사항

- C++ 컴파일러가 시스템에 설치되어 있어야 합니다.
- Windows 사용자의 경우 Visual Studio Build Tools가 필요할 수 있습니다.
- 보안을 위해 프로덕션 환경에서는 `nodeIntegration: true`와 `contextIsolation: false` 설정을 피하고, 대신 preload 스크립트를 사용하는 것이 좋습니다.