# 오디오 출력


## 핵심 강의

<b>동영상 준비 중</b>


## 강의 개요

ffmpeg을 이용하여 간단한 동영상 플레이어를 만들기 전에 음성 출력 방법에 대해서 알아보겠습니다.


## 강의 전 준비 사항

* Visual Studio 2015 Update 3 또는 이후 버전
* vcpkg 설치 및 라이브러리 설치
  * ["vcpkg 설치" 참고](/install/vcpkg/)
  * vcpkg install sdl2 ffmpeg
* [https://github.com/ryujt/ff-player](https://github.com/ryujt/ff-player) 예제 다운로드
  * src/decoding-audio 폴더의 예제를 참고하세요.


## 이 강의에서 다룰 내용

* AudioSDL 클래스: SDL2를 이용하여 오디오를 출력
* ffmpeg으로 영상(파일) 리소스 가져오기
  * http, ftp, rtmp, rtsp 등 다양한 프로토콜 지원
* 오디오 스트림을 찾아내기
* 오디오 코덱 오픈하기
* 오디오 리샘플링(resampling, 포멧 변환)
* 영상 리소스를 차례로 읽고 디코딩하여 오디오 출력하기


## WindowSDL

``` cpp
class AudioSDL {
public:
	/** 오디오를 출력하기 위한 장치를 오픈합니다.
	@param channels 오디오의 채널 수. 1: 모노, 2: 스테레오
	@param sampe_rate 오디오의 sampling rate.
	@param fpb 한 번에 처리할 프레임의 갯수
	*/
	bool open(int channels, int sample_rate, int fpb)

	/**	오디오를 출력합니다.
	@param data 출력할 오디오 데이터
	@param size 출력할 오디오 데이터의 크기
	*/
	void play(void* data, int size)

	/** 출력이 끝나지 않은 패킷의 갯수 */
	int getDelayCount()
```

## 전반적인 소스 구조

``` cpp
include ...

int main()
{
	// 오디오 소스(파일) 오픈

	// 오디오 스트림 찾기

	// 오디오 코덱 오픈

	// 오디오를 출력할 장치 오픈

	// 오디오 포멧 변환 (resampling) 준비

	// 파일(오디오 소스) 반복해서 끝까지 읽기
	while (...) {
		// 오디오 디코딩
		// 오디오 포멧 변환
		// 디코딩된 오디오를 출력
	}
}
```


## include 및 전처리

``` cpp
#include <stdio.h>
#include <Windows.h>
#include <ryulib/sdl_audio.hpp>

extern "C" {
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswresample/swresample.h>
}
```
* 1: Sleep() 함수를 사용하기 위해서 Windows.h 헤더를 가져옵니다.
* 3: 오디오 출력을 위한 헤더
* 5-9: ffmpeg에서 필요한 헤더 파일, C로 작성된 라이브러리이기 때문에 extern "C"으로 감싸야 합니다. 이에 대해서는 "네임 맹글링 (Name mangling)"을 검색해보시기 바랍니다.


## main() 함수

### 오디오 소스(파일) 오픈

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


### 오디오 스트림 찾기

``` cpp
	int audio_stream = -1;
	for (int i = 0; i < ctx_format->nb_streams; i++) {
		if (ctx_format->streams[i]->codecpar->codec_type == AVMEDIA_TYPE_AUDIO) {
			audio_stream = i;
			break;
		}
	}
	if (audio_stream == -1) return -2;
```
영상의 스트림 목록을 순회하면서 오디오 타입이 발견되면 해당 순번을 video_stream에 저장하고 반복을 멈춘다.


### 오디오 코덱 오픈

``` cpp
	AVCodecParameters* parameters = ctx_format->streams[audio_stream]->codecpar;
	AVCodec* codec = avcodec_find_decoder(parameters->codec_id);
	if (codec == NULL) return -2;
	AVCodecContext* ctx_codec = avcodec_alloc_context3(codec);
	if (avcodec_parameters_to_context(ctx_codec, parameters) != 0)  return -3;
	if (avcodec_open2(ctx_codec, codec, NULL) < 0) return -3;
```
* 1: 스트림 객체에서 오디오 컨텍스트 객체를 가져옵니다.
* 2: 컨텍스트의 codec_id에 맞는 코덱 객체를 가져옵니다.
* 3: 코덱 컨텍스트 객체를 생성합니다.
* 5: ctx_audio에서 ctx_codec으로 필요한 정보(파라메터)를 복사합니다.
* 6: 코덱을 사용할 수 있도록 오픈합니다.
위의 과정은 ffmpeg이 그렇게 설계되었을 뿐이기 때문에 굳이 과정 전체를 이해할 필요는 없습니다.


### 오디오를 출력할 장치 오픈

``` cpp
	AudioSDL audio;
	audio.open(parameters->channels, parameters->sample_rate, 1024);
```
* 2: 오디오를 출력할 장치를 오픈합니다.
  * parameters->channels: 출력할 오디오의 채널수 (1: 모노, 2: 스테레오 ...)
  * parameters->sample_rate: 출력할 오디오의 주파수 (샘플 수)
  * 1024: 한 번에 처리할 프레임 수 (오디오의 정보 개수)


### 오디오 포멧 변환 (resampling) 준비

``` cpp
	SwrContext* swr = swr_alloc_set_opts(
		NULL,
		parameters->channel_layout,
		AV_SAMPLE_FMT_FLT,
		parameters->sample_rate,
		parameters->channel_layout,
		(AVSampleFormat) parameters->format,
		parameters->sample_rate,
		0,
		NULL);
	swr_init(swr);
```
영상마다 오디오를 표현하는 방식이 다르기 때문에 AV_SAMPLE_FMT_FLT로 통일이 되도록 변환(resampling)하고 있습니다. 위의 코드는 변환을 위해 필요한 SwrContext 객체를 생성해서 swr 변수에 저장합니다.


### 오디오 출력

``` cpp
	AVFrame* frame = av_frame_alloc();
	if (!frame) return -4;

	AVFrame* reframe = av_frame_alloc();
	if (!reframe) return -4;

	AVPacket packet;

	// 파일(오디오 소스) 반복해서 끝까지 읽기
	while (av_read_frame(ctx_format, &packet) >= 0) {
		// 오디오 스트림만 처리
		if (packet.stream_index == audio_stream) {
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

				// 포멧 변환
				reframe->channel_layout = frame->channel_layout;
				reframe->sample_rate = frame->sample_rate;
				reframe->format = AV_SAMPLE_FMT_FLT;
				int ret = swr_convert_frame(swr, reframe, frame);

				int data_size = av_samples_get_buffer_size(NULL, ctx_codec->channels, frame->nb_samples, (AVSampleFormat) reframe->format, 0);
				audio.play(reframe->data[0], data_size);

				// 음성이 처리 될 때까지 기다리기
				while (audio.getDelayCount() > 2) Sleep(1);
			}
		}

		av_packet_unref(&packet);
	}
```
* 1: 디코딩 된 오디오 원본을 저장할 AVFrame 객체를 생성합니다.
* 4: 디코딩 된 원본 오디오의 포멧을 변환해서 저장할 AVFrame 객체를 생성합니다.
* 7: 영상 소스에서 읽어온 데이터를 저장할 AVPacket 객체를 생성합니다.
* 10-43: 파일의 끝까지 반복하면서 (더 이상 데이터가 읽혀지지 않을 때까지) 패킷을 읽고 디코딩한 후 오디오를 출력합니다.
  * 12: 이전에 찾아낸 오디오 스트림만 처리합니다.
  * 13: 디코더에게 읽어들인 데이터를 전송합니다.
  * 19-39: 디코딩이 끝난 데이터가 여러 프레임으로 구성되어 있을 수 있습니다. 그래서 프레임 수만큼 반복하면서 처리합니다.
    * 29-32: 디코딩이 끝난 오디오 데이터의 포멧을 변경합니다.
    * 34: 한 번에 처리되야할 샘플의 수를 구합니다. avcodec_receive_frame() 함수를 통해서 가져온 오디오 데이터의 샘플 수입니다.
    * 35: 오디오를 출력합니다.
    * 38: 출력 대기 중인 오디오가 2개 이하일 때까지 기다랍니다. 기다리지 않고 계속 실행하면 대기 중인 오디오 데이터가 메모리를 잠식하다가 메모리 부족으로 에러가 날 수도 있습니다.

::: tip
영상을 디코딩하면서 계속 표시만하기 때문에 영상이 빨리 감기처럼 빠르게 재생됩니다. 여기서는 전반적인 원리만을 설명하고 종료처리 등은 생략하였습니다.
:::


## 전체 코드

[https://github.com/ryujt/ff-player/blob/master/src/decoding-audio/decoding-audio/decoding-audio.cpp](https://github.com/ryujt/ff-player/blob/master/src/decoding-audio/decoding-audio/decoding-audio.cpp)