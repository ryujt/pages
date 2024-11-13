# EC2에 Node.js 서버 설치 가이드

이 가이드는 Amazon EC2 인스턴스에 Node.js 서버를 설치하고 실행하는 방법을 설명합니다. Amazon Linux 운영 체제를 사용한다고 가정합니다.

## 1. Node.js 설치

먼저, NVM(Node Version Manager)을 사용하여 Node.js를 설치합니다.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
source ~/.nvm/nvm.sh
```

NVM이 설치되면 원하는 Node.js 버전을 설치할 수 있습니다. 예를 들어:

```bash
nvm install lts
```

## 2. 서버 디렉토리 생성 및 초기화

서버를 위한 새 디렉토리를 만들고 초기화합니다.

```bash
mkdir server
cd server
npm init -y
```

## 3. 서버 코드 작성

`index.js` 파일을 생성하고 서버 코드를 작성합니다. 예를 들어:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!');
});

server.listen(3000, '0.0.0.0', () => {
  console.log('Server running on port 3000');
});
```

## 4. 시스템 서비스 설정

Node.js 서버를 시스템 서비스로 실행하기 위해 서비스 파일을 생성합니다.

```bash
sudo vi /etc/systemd/system/node-server.service
```

다음 내용을 파일에 입력합니다:

```ini
[Unit]
Description=Node Server
After=network.target

[Service]
ExecStart=/home/ec2-user/.nvm/versions/node/v20.17.0/bin/node /home/ec2-user/server/index.js
WorkingDirectory=/home/ec2-user/server
Restart=always
User=ec2-user
Group=ec2-user

[Install]
WantedBy=multi-user.target
```

* v20.17.0은 자신이 설치한 node의 버전에 따라서 다릅니다.

## 5. 서비스 시작 및 활성화

서비스 파일의 권한을 설정하고, 서비스를 시작합니다:

```bash
sudo chmod 644 /etc/systemd/system/node-server.service
sudo systemctl daemon-reload
sudo systemctl start node-server
sudo systemctl enable node-server
```

서비스 상태를 확인하려면:

```bash
sudo systemctl status node-server
```

이제 Node.js 서버가 EC2 인스턴스에서 실행되고 있으며, 시스템 재부팅 후에도 자동으로 시작됩니다.