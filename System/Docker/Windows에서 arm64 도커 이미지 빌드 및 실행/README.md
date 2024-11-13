# Windows에서 arm64 도커 이미지 빌드 및 실행

Windows x86 기반 시스템에서 ARM64 아키텍처용 우분투 이미지를 빌드하고 해당 컨테이너를 실행하려면 Docker의 `buildx` 기능을 활용하여 멀티 플랫폼 이미지를 생성해야 합니다. 아래는 단계별 가이드입니다.

1. **Docker Desktop 설치 및 설정**

   - **Docker Desktop 설치**: [Docker 공식 웹사이트](https://www.docker.com/products/docker-desktop/)에서 Windows용 Docker Desktop을 다운로드하여 설치합니다.

   - **WSL 2 활성화**: Docker Desktop은 WSL 2(Windows Subsystem for Linux 2)를 필요로 합니다. [Microsoft의 WSL 2 설치 가이드](https://docs.microsoft.com/ko-kr/windows/wsl/install)를 참고하여 WSL 2를 활성화합니다.

2. **Docker Buildx 활성화**

   - **빌더 인스턴스 생성 및 사용 설정**:

     ```bash
     docker buildx create --name mybuilder --use
     ```

   - **빌더 확인**:

     ```bash
     docker buildx ls
     ```

     위 명령어를 통해 생성된 빌더가 활성화되었는지 확인합니다.

3. **QEMU 에뮬레이션 설정**

   - **QEMU 설치**: 멀티 아키텍처 빌드를 위해 QEMU를 설치합니다.

     ```bash
     docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
     ```

4. **멀티 플랫폼 이미지 빌드**

     ```bash
     docker buildx build --platform linux/arm64 -f ubuntu-22.04-dotnet-8.0-arm64 -t dotnet-ubuntu-arm64 .
     ```

     위 명령어에서 `<DockerHub_사용자명>`을 본인의 Docker Hub 사용자명으로 대체합니다.

5. **ARM64 컨테이너 실행**

   - **컨테이너 실행**: 빌드한 이미지를 기반으로 ARM64 컨테이너를 실행합니다.

     ```bash
     docker run --rm --platform linux/arm64 dotnet-ubuntu-arm64
     ```

     이렇게 하면 Windows x86 시스템에서 ARM64 아키텍처용 우분투 컨테이너를 실행할 수 있습니다.

**참고 자료**

- [Docker 공식 문서: 멀티 플랫폼 빌드](https://docs.docker.com/build/building/multi-platform/)
- [Docker Buildx로 멀티 플랫폼 이미지 빌드하기](https://blog.taehun.dev/docker-buildx-)
- [멀티 플랫폼 빌드를 위한 Docker Buildx](https://gurumee92.tistory.com/311) 
