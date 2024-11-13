---

# .NET MAUI로 Mac 데스크톱 앱 개발하기 (Google을 초기 화면으로 로딩)

이 가이드는 MAUI와 Blazor Hybrid를 사용하여 Mac에서 Google을 초기 화면으로 설정한 데스크톱 애플리케이션을 만드는 방법을 안내합니다.

## 목차

- [사전 요구 사항](#사전-요구-사항)
- [1. .NET MAUI 워크로드 설치](#1-net-maui-워크로드-설치)
- [2. 새로운 MAUI Blazor 앱 생성](#2-새로운-maui-blazor-앱-생성)
- [3. 프로젝트 설정 수정 (Mac 데스크톱 전용)](#3-프로젝트-설정-수정-mac-데스크톱-전용)
  - [`MyBlazorHybridApp.csproj` 수정](#myblazorhybridappcsproj-수정)
- [4. Google을 초기 화면으로 설정](#4-google을-초기-화면으로-설정)
  - [`MainPage.xaml` 수정](#mainpagexaml-수정)
  - [`MainPage.xaml.cs` 수정](#mainpagexamlcs-수정)
- [5. 빌드 및 실행](#5-빌드-및-실행)
  - [5.1 클린 빌드](#51-클린-빌드)
  - [5.2 프로젝트 빌드](#52-프로젝트-빌드)
  - [5.3 애플리케이션 실행](#53-애플리케이션-실행)
- [6. 애플리케이션 배포](#6-애플리케이션-배포)
  - [6.1 애플리케이션 퍼블리시](#61-애플리케이션-퍼블리시)
  - [6.2 코드 서명 확인](#62-코드-서명-확인)
  - [6.3 애플리케이션 패키징](#63-애플리케이션-패키징)
    - [.dmg 파일 생성](#dmg-파일-생성)
    - [.zip 파일 생성](#zip-파일-생성)
- [7. 문제 해결과 추가 팁](#7-문제-해결과-추가-팁)
  - [문제 해결](#문제-해결)
  - [추가 팁](#추가-팁)

---

## 사전 요구 사항

1. **macOS 최신 버전**을 사용 중인지 확인합니다.
2. **.NET 8.0 SDK 설치**: [Microsoft 공식 사이트](https://dotnet.microsoft.com/download/dotnet/8.0)에서 SDK를 설치합니다.
3. **Visual Studio 2022 for Mac**: GUI 기반의 개발이 필요한 경우 설치합니다.
4. **Xcode 설치**: Mac 애플리케이션 개발을 위해 [Xcode](https://apps.apple.com/kr/app/xcode/id497799835?mt=12)를 설치합니다.

---

## 1. .NET MAUI 워크로드 설치

```bash
dotnet workload install maui
```

위 명령어로 MAUI와 관련된 모든 패키지와 템플릿을 설치합니다.

---

## 2. 새로운 MAUI Blazor 앱 생성

```bash
dotnet new maui-blazor -n MyBlazorHybridApp
cd MyBlazorHybridApp
```

- `-n MyBlazorHybridApp`: 프로젝트 이름
- `cd MyBlazorHybridApp`: 생성된 프로젝트 디렉터리로 이동

---

## 3. 프로젝트 설정 수정 (Mac 데스크톱 전용)

Mac 데스크톱용으로만 애플리케이션을 타겟팅하려면 `MyBlazorHybridApp.csproj` 파일을 수정합니다.

### `MyBlazorHybridApp.csproj` 수정

```xml
<Project Sdk="Microsoft.NET.Sdk.Razor">
  <PropertyGroup>
    <TargetFramework>net8.0-maccatalyst</TargetFramework>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyBlazorHybridApp</RootNamespace>
    <UseMaui>true</UseMaui>
    <SingleProject>true</SingleProject>
    <ApplicationTitle>MyBlazorHybridApp</ApplicationTitle>
    <ApplicationId>com.yourcompany.myblazorhybridapp</ApplicationId>
    <ApplicationDisplayVersion>1.0.0</ApplicationDisplayVersion>
    <ApplicationVersion>1</ApplicationVersion>
    <SupportedOSPlatformVersion>14.0</SupportedOSPlatformVersion>
    <CodesignKey>Apple Development: Your Name (Team ID)</CodesignKey>
    <CodesignEntitlements>Entitlements.plist</CodesignEntitlements>
    <CodesignProvision>Automatic</CodesignProvision>
  </PropertyGroup>
</Project>
```

이 설정을 통해 Mac Catalyst에서만 실행되도록 구성합니다.

---

## 4. Google을 초기 화면으로 설정

### `MainPage.xaml` 수정

`MainPage.xaml`에서 `WebView`를 추가하여 Google 페이지가 로딩되도록 합니다.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="MyBlazorHybridApp.MainPage">

    <WebView x:Name="MyWebView" />

</ContentPage>
```

### `MainPage.xaml.cs` 수정

`MainPage.xaml.cs`에서 `WebView`의 `Source` 속성을 설정하여 Google을 초기 화면으로 로드합니다.

```csharp
using Microsoft.Maui.Controls;

namespace MyBlazorHybridApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
            MyWebView.Source = "https://www.google.com";
        }
    }
}
```

---

## 5. 빌드 및 실행

### 5.1 클린 빌드

```bash
dotnet clean
```

### 5.2 프로젝트 빌드

```bash
dotnet build -f net8.0-maccatalyst
```

### 5.3 애플리케이션 실행

```bash
dotnet run -f net8.0-maccatalyst
```

Mac Catalyst 애플리케이션이 실행되면 초기 화면에 `google.com`이 표시됩니다.

---

## 6. 애플리케이션 배포

### 6.1 애플리케이션 퍼블리시

```bash
dotnet publish -f net8.0-maccatalyst -c Release
```

퍼블리시된 애플리케이션은 `bin/Release/net8.0-maccatalyst/publish/`에 생성됩니다.

### 6.2 코드 서명 확인

```bash
codesign --verify --deep --strict /path/to/publish/MyBlazorHybridApp.app
```

필요시 수동으로 코드 서명합니다.

```bash
codesign --deep --force --verify --verbose --sign "Apple Development: Your Name (Team ID)" /path/to/publish/MyBlazorHybridApp.app
```

### 6.3 애플리케이션 패키징

애플리케이션을 `.dmg` 또는 `.zip` 파일로 압축하여 배포합니다.

#### .dmg 파일 생성

```bash
hdiutil create /path/to/MyBlazorHybridApp.dmg -srcfolder /path/to/publish/MyBlazorHybridApp.app
```

#### .zip 파일 생성

```bash
cd /path/to/publish/
zip -r MyBlazorHybridApp.zip MyBlazorHybridApp.app
```

---

## 7. 문제 해결과 추가 팁

### 문제 해결

- **코드 서명 오류**: 키체인 접근에서 올바른 인증서를 확인합니다.
- **애플리케이션 경로 확인**: `Applications` 폴더에 애플리케이션이 설치되었는지 확인합니다.

### 추가 팁

- 프로젝트의 `MainPage.xaml.cs`에서 URL을 다른 페이지로 변경하여 다양한 웹 사이트를 초기 화면으로 설정할 수 있습니다.
- 배포 전, 다양한 macOS 환경에서 테스트하여 호환성을 확인하세요.

---

이제 Mac Catalyst에서 Google을 초기 화면으로 로딩하는 MAUI 애플리케이션이 준비되었습니다.