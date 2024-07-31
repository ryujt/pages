# 논리계층 설계 및 코딩

## 핵심 강의

<iframe width="800" height="450" src="https://www.youtube.com/embed/G2JhYdY_muE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## 강의 개요

이제부터는 본격적으로 ffmpeg을 이용하여 간단한 동영상 플레이어를 만들어 볼 예정입니다.
다만, 원리를 이해하는데 방해되지 않도록 최소 기능부터 시작하겠습니다.
그리고, 논리계층과 구현계층을 나눠서 설명드릴 예정이며, 이 강의는 논리계층에 대한 이야기입니다.


## 강의 전 준비 사항

* Visual Studio 2015 Update 3 또는 이후 버전
* vcpkg 설치 및 라이브러리 설치
  * ["vcpkg 설치" 참고](/install/vcpkg/)
  * vcpkg install sdl2 ffmpeg
* [https://github.com/ryujt/ff-player](https://github.com/ryujt/ff-player) 예제 다운로드


## 이 강의에서 다룰 내용

* 동상 플레이어의 논리계층 설계 및 구현


## 논리계층 설계

![](./pic-1.png)

* Scheduler 클래스의 자세한 사용법은 다음 링크에서 참고하시기 바랍니다. [http://10bun.tv/beginner/episode-2/#scheduler](http://10bun.tv/beginner/episode-2/#scheduler)
* FFPlayer는 Scheduler, FFStream, FFAudio, FFVideo 네 개의 클래스로 나눠서 구현할 예정입니다.
* FFPlayer에서 open(), close() 등은 스레드를 사용하지 않고 동기 호출을 사용해도 상관없지만, play()의 경우에는 비동기 호출이 되어야 FFPlayer를 사용하는 프로세스가 멈추지 않게 됩니다. 예를 들어 메인 스레드에서 play()가 동기 방식으로 호출된다면, play()를 호출하는 순간부터 멈추기 버튼 등을 사용하지 못하고 재생이 끝날 때까지 기다려야 할 것입니다.
* play() 내부 동작에서만 별도의 스레드를 사용하여 처리해도 되지만, 그렇게 되면 두 개의 다른 스레드 이용해서 하나의 논리를 구성해야 하고 이렇게 되면 임계 영역을 사용하는 등 복잡해질 수 있습니다. Scheduler를 사용하면 쉽게 FFPlayer의 모든 동작이 비동기적으로 같은 스레드에서 동작하도록 할 수 있습니다.
* FFPlayer의 open(), close(), play(), pause() 메소드를 호출하면 Scheduler에 큐에 요청된 작업을 큐에 넣습니다.
* Scheduler는 반복하면서 큐에 있는 작업을 하나씩 OnTask 이벤트로 발생시킵니다. 발생된 이벤트의 task 인자의 종류에 따라서 아래와 같은 진행이 이루어집니다.
  * TASK_OPEN
    * FFStream.open()을 실행하여 동영상 파일을 열고 읽을 준비를 합니다.
    * 동영상 파일이 열리면 동영상 파일 정보를 FFAudio.open(), FFVideo.open() 메소드에 전달하여 디코딩을 준비합니다.
  * TASK_CLOSE
    * FFStream.close(), FFAudio.close(), FFVideo.close() 메소드를 실행하여 파일을 닫고 리소스를 반환합니다.
  * TASK_PLAY
    * FFStream.play()를 호출하여 재생 상태 플래그를 true로 변경한다.
  * TASK_PAUSE
    * FFStream.pause()를 호출하여 재생 상태 플래그를 false로 변경한다.
* Scheduler는 큐에 쌓인 작업을 처리하는 동시에 반복적으로 OnRepeat 이벤트를 발생시킵니다. "FFStream.isPlaying() == true" 이면서 "FFAudio.isEmpty() == true"인 경우에는 즉, 재생 중이면서 오디오 버퍼가 비어있다면 FFStream.read() 메소드로 파일에서 패킷을 가져와서 오디오 패킷이면 FFAudio에 또는 비디오 패킷이면 FFVideo에 저장합니다.
* FFAudio, FFVideo 클래스는 내부의 별도의 스레드를 이용하여 패킷을 디코딩하고 출력할 예정입니다. 만약 이 부분이 동기화 되어서 실행된다면, 비디오가 디코딩되는 동안 오디오는 재생될 수 없는 상태가되어 소리가 지속적으로 끊기는 등의 현상이 발생하게 됩니다.

::: tip 오디오와 비디오를 싱크하는 방식에 대해서

위에서는 오디오를 기준으로 비디오를 싱크하는 방법으로 설계되어 있습니다. 하지만, 일반적인 동영상 플레이어는 타이머가 별도로 준비되어 오디오와 비디오가 타이머의 현재 시간에 맞춰서 진행되도록 합니다.

이 강의에서는 단순한 방식으로 최대한 빠르고 쉽게 전체적인 흐름을 이해할 수 있도록 내용을 최소화하였습니다. 그래서 좀 더 쉬운 오디오 기준의 싱크 방법을 선택했는데요, 간혹 동영상 파일 내에 오디오만 없는 구간이 있는 경우에 문제가 될 수 있습니다. 오디오가 없는 곳의 영상이 고속으로 빨리감기 한 것처럼 보이게 될 것입니다.

동영상 패킷에는 pts라고 자신이 출력되어야 할 시간이 정해져 있습니다. 이것이 패킷의 파일 안에서의 위치와 비례하지 않을 수 있기 때문에 오디오만으로 싱크한 경우에는 화면 출력이 중간 중간 건너 뛰는 현상이 나타날 수 있습니다.
:::


## 논리계층의 코드

``` cpp
#pragma once

#include <ryulib/Scheduler.hpp>
#include "FFStream.hpp"
#include "FFAudio.hpp"
#include "FFVideo.hpp"

const int TASK_OPEN = 1;
const int TASK_CLOSE = 2;
const int TASK_PLAY = 3;
const int TASK_PAUSE = 4;

using namespace std;

class FFPlayer {
public:
	FFPlayer()
	{
		scheduler_.setOnTask([&](int task, const string text, const void* data, int size, int tag){
			switch(task) {
				case TASK_OPEN: {
					if (stream_.open(text)) {
						// TODO: open error
						audio_.open( stream_.getContext() );
						video_.open( stream_.getContext() );
					} else {
						// TODO: open error
						printf("open error \n");
					}
				} break;

				case TASK_CLOSE: {
					stream_.close();
					audio_.close();
					video_.close();
				} break;

				case TASK_PLAY: {
					stream_.play();
				} break;

				case TASK_PAUSE: {
					stream_.pause();
				} break;
			}
		});

		scheduler_.setOnRepeat([&](){
			if (stream_.isPlaying() == true) {
				if (audio_.isEmpty()) {
					AVPacket* packet = stream_.read();
					if (packet != nullptr) {
						if (packet->stream_index == audio_.getStreamIndex()) {
							audio_.write(packet);
						} else if (packet->stream_index == video_.getStreamIndex()) {
							video_.write(packet);
						} else {
							av_packet_free(&packet);
						}
					} else {
						// TODO: EOF
					}
				}
			}
		});

		scheduler_.start();
	}

	~FFPlayer()
	{
		scheduler_.terminateNow();
	}

	void open(string filename)
	{
		scheduler_.add(TASK_OPEN, filename);
	}

	void close()
	{
		scheduler_.add(TASK_CLOSE);
	}

	void play()
	{
		scheduler_.add(TASK_PLAY);
	}

	void pause()
	{
		scheduler_.add(TASK_PAUSE);
	}

private:
	Scheduler scheduler_;
	FFStream stream_;
	FFAudio audio_;
	FFVideo video_;
};
```
* 에러 및 EOF 처리 등은 당분간 무시하고 최대한 빨리 기본적인 동작을 확인하고 테스트 할 수 있도록 하겠습니다.
* 다이어그램(Job Flow)을 통해서 설계한 내용을 코드로 옮기는 방법에 대해서는 [http://10bun.tv/beginner/episode-1/](http://10bun.tv/beginner/episode-1/)을 참고하시기 바랍니다.


## FFStream의 인터페이스

``` cpp
#pragma once

using namespace std;

class FFStream {
public:
	bool open(string filename)
	{
		return true;
	}

	void close()
	{
	}

	void play()
	{
	}

	void pause()
	{
	}

	bool isPlaying() { return true; }

	AVPacket* read()
	{
	}
private:
};
```

## FFAudio의 인터페이스

``` cpp
#pragma once

class FFAudio {
public:
	bool open(AVFormatContext* context)
	{
		return true;
	}

	void close()
	{
	}

	void write(AVPacket* packet)
	{
	}

	bool isEmpty() { return true; }

private:
};
```

## FFVideo의 인터페이스

``` cpp
#pragma once

class FFVideo {
public:
	bool open(AVFormatContext* context)
	{
		return true;
	}

	void close()
	{
	}

	void write(AVPacket* packet)
	{
	}

	bool isEmpty()
	{
	}

private:
};
```