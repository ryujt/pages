# 영상 출력


## 핵심 강의

<b>동영상 준비 중</b>


## 강의 개요

ffmpeg을 이용하여 간단한 동영상 플레이어를 만들기 전에 영상 출력 방법에 대해서 알아보겠습니다.


## 강의 전 준비 사항

* Visual Studio 2015 Update 3 또는 이후 버전
* vcpkg 설치 및 라이브러리 설치
  * ["vcpkg 설치" 참고](/install/vcpkg/)
  * vcpkg install sdl2 ffmpeg
* [https://github.com/ryujt/ff-player](https://github.com/ryujt/ff-player) 예제 다운로드
  * src/decoding-video 폴더의 예제를 참고하세요.



## 이 강의에서 다룰 내용

* WindowSDL 클래스: SDL2를 이용하여 영상을 화면에 표시
* ffmpeg으로 영상(파일) 리소스 가져오기
  * http, ftp, rtmp, rtsp 등 다양한 프로토콜 지원
* 비디오 스트림을 찾아내기
* 비디오 코덱 오픈하기
* 영상 리소스를 차례로 읽고 디코딩하여 화면에 출력하기


## WindowSDL

``` cpp
class WindowSDL {
public:
	/** 영상을 출력하기 위한 윈도우를 생성(오픈)합니다.
	@param caption 윈도우의 제목
	@param width 윈도우의 넓이 (가로 크기)
	@param height 윈도우의 높이 (세로 크기)
	*/
	bool open(string caption, int width, int height)

	/** 윈도우를 닫습니다. */
	void close()

	/** 32비트 BITMAP을 윈도우에 표시합니다.
	@param bitmap 표시할 BITMAP 데이터
	*/
	void showBitmap32(void* bitmap)

	/** YUV 포멧 이미지를 윈도우에 표시합니다. */
	void showYUV(const Uint8* y_plane, int y_pitch, const Uint8* u_plane, int u_pitch, const Uint8* v_plane, int v_pitch)
```

## 전반적인 소스 구조

``` cpp
include ...

int main()
{
	// 비디오 소스(파일) 오픈

	// 비디오 스트림 찾기

	// 비디오 코덱 오픈

	// 비디오를 출력할 윈도우 오픈

	// 파일(비디오 소스) 반복해서 끝까지 읽기
	while (...) {
		// 비디오 디코딩
		// 디코딩된 영상을 화면에 표시
	}
}
```


## include 및 전처리

``` cpp
#include <stdio.h>
#include <ryulib/sdl_window.hpp>

extern "C" {
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libavutil/imgutils.h>
}
```
* 2: 비디오 출력을 위한 헤더
* 4-8: ffmpeg에서 필요한 헤더 파일, C로 작성된 라이브러리이기 때문에 extern "C"으로 감싸야 합니다. 이에 대해서는 "네임 맹글링 (Name mangling)"을 검색해보시기 바랍니다.


## main() 함수

### 비디오 소스(파일) 오픈

``` cpp
	//string filename = "D:/Work/test.mp4";
	string filename = "https://etc.s3.ap-northeast-2.amazonaws.com/AsomeIT.mp4";

	AVFormatContext* ctx_format = NULL;
	if (avformat_open_input(&ctx_format, filename.c_str(), NULL, NULL) != 0) return -1;
	if (avformat_find_stream_info(ctx_format, NULL) < 0) return -1;
```
* 1-2: 사용할 영상 소스(파일)을 지정합니다. ffmpeg은 http, ftp, rtmp, rtsp 등 다양한 프로토콜을 지원합니다.
* 5: 영상 소스를 오픈합니다. 에러가나면 프로그램을 종료합니다. 어느 부분에서 에러가 났는 지 알기 위해서 리턴 값을 달리하고 있습니다.
* 6: 영상 소스에 스트림 정보가 있는 지 확인합니다. 만약 아무것도 없는 영상이면 프로그램을 종료합니다.


### 비디오 스트림 찾기

``` cpp
	int video_stream = -1;
	for (int i = 0; i < ctx_format->nb_streams; i++)
		if (ctx_format->streams[i]->codecpar->codec_type == AVMEDIA_TYPE_VIDEO) {
			video_stream = i;
			break;
		}
	if (video_stream == -1) return -2;
```
영상의 스트림 목록을 순회하면서 비디오 타입이 발견되면 해당 순번을 video_stream에 저장하고 반복을 멈춘다.


### 비디오 코덱 오픈

``` cpp
	AVCodecParameters* parameters = ctx_format->streams[video_stream]->codecpar;
	AVCodec* codec = avcodec_find_decoder(parameters->codec_id);
	if (codec == NULL) return -3;
	AVCodecContext* ctx_codec = avcodec_alloc_context3(codec);
	if (avcodec_parameters_to_context(ctx_codec, parameters) != 0)  return -3;
	if (avcodec_open2(ctx_codec, codec, NULL) < 0) return -3;
```
* 1: 스트림 객체에서 비디오 컨텍스트 객체를 가져옵니다.
* 2: 컨텍스트의 codec_id에 맞는 코덱 객체를 가져옵니다.
* 3: 코덱 컨텍스트 객체를 생성합니다.
* 5: ctx_video에서 ctx_codec으로 필요한 정보(파라메터)를 복사합니다.
* 6: 코덱을 사용할 수 있도록 오픈합니다.
위의 과정은 ffmpeg이 그렇게 설계되었을 뿐이기 때문에 굳이 과정 전체를 이해할 필요는 없습니다.


### 비디오를 출력할 윈도우 오픈

``` cpp
	WindowSDL window;
	window.open("ffmpeg", ctx_codec->width, ctx_codec->height);
```
* 2: 영상을 출력할 윈도우를 오픈합니다.
  * 윈도우 타이틀(제목)에는 "ffmepg"이라고 표시합니다.
  * 윈도우 크기는 ctx_codec->width, ctx_codec->height로 지정합니다.


### 비디오 출력

``` cpp
	AVFrame* frame = av_frame_alloc();
	if (!frame) return -4;

	AVPacket packet;

	while (av_read_frame(ctx_format, &packet) >= 0) {
		// 비디오 스트림만 처리
		if (packet.stream_index == video_stream) {
			int ret = avcodec_send_packet(ctx_codec, &packet) < 0;
			if (ret < 0) {
				printf("Error sending a packet for decoding \n");
				return -5;
			}

			while (ret >= 0) {
				ret = avcodec_receive_frame(ctx_codec, frame);
				if (ret == AVERROR(EAGAIN) || ret == AVERROR_EOF) {
					break;
				} else if (ret < 0) {
					printf("Error sending a packet for decoding \n");
					return -5;
				}

				// 디코딩된 영상을 화면에 표시
				window.showYUV(frame->data[0], frame->linesize[0], frame->data[1], frame->linesize[1], frame->data[2], frame->linesize[2]);
			}
		}

		av_packet_unref(&packet);
	}
```
* 1: 디코딩 된 화면을 저장할 AVFrame 객체를 생성합니다.
* 4: 영상 소스에서 읽어온 데이터를 저장할 AVPacket 객체를 생성합니다.
* 6-30: 파일의 끝까지 반복하면서 (더 이상 데이터가 읽혀지지 않을 때까지) 패킷을 읽고 디코딩한 후 영상에 표시합니다.
  * 8: 이전에 찾아낸 비디오 스트림만 처리합니다.
  * 9: 디코더에게 읽어들인 데이터를 전송합니다.
  * 15-26: 디코딩이 끝난 데이터가 여러 프레임으로 구성되어 있을 수 있습니다. 그래서 프레임 수만큼 반복하면서 처리합니다.
    * 16: 디코딩이 끝난 데이터를 가져와서 화면에 표시할 준비를 합니다.
    * 25: 디코딩이 끝난 데이터를 화면에 표시합니다.

::: tip
영상을 디코딩하면서 계속 표시만하기 때문에 영상이 빨리 감기처럼 빠르게 재생됩니다. 여기서는 전반적인 원리만을 설명하고 재생 시간을 제어나 종료처리 등은 생략하였습니다.
:::


## 전체 코드

[https://github.com/ryujt/ff-player/blob/master/src/decoding-video/decoding-video/decoding-video.cpp](https://github.com/ryujt/ff-player/blob/master/src/decoding-video/decoding-video/decoding-video.cpp) 참고