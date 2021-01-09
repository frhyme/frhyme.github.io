---
title: 맥북에 VirtualBox를 사용해서 윈도우10을 설치했습니다.
category: others
tags: macOS VirtualBox Window BootCamp
---

## 맥북에 VirtualBox를 사용해서 윈도우10을 설치했습니다

- 맥북에서 윈도우10을 설치했습니다. 보통 맥북에서 윈도우(혹은 다른 OS)를 사용하려면 다음과 같은 방법들이 있다고 하죠.
  1. **부트캠프**: MacOS와 Windows의 CPU가 동일하기 때문에, 하드웨어 구조가 같죠. 따라서 개념적으로 같은 구조에 윈도를 까는 게 가능하죠. BootCamp는 이렇게 컴퓨터를 껐다가 킬 때 MacOS를 키는 것이 아니라, 윈도우를 키도록 해주는 것을 말합니다. 즉, 사실 맥북을 산 게 아니라 그냥 괜찮은 컴퓨터를 산 것과 같다는 이야기죠. 따라서, 멀쩡한 맥북에서 MacOS를 지워버리고 윈도우를 설치하는 것이 가능하고 반대로 멀쩡한 노트북에 윈도우를 지우고 해킹한 맥OS를 설치하는 것 또한 가능하죠.
     - 하드웨어에 바로 붙는 것이기 때문에 성능이 나쁘지 않지만, 그래도 맥을 주로 쓰는 사람에게는 불편함이 꽤 있습니다. 윈도우를 사용하다가 맥북을 사용해야 하는 경우에는 윈도우를 끄고 다시 맥북을 켜야 하고 그 반대의 일에도 또 껐다가 켜야 하죠. 어쩔 수 없는 것이기는 합니다만.
     - [설치에 대한 자세한 내용은 여기를 보시면 됩니다.](https://support.apple.com/ko-kr/HT201468)
  2. **Parallels**: MacOS에서 새로운 OS를 사용한다는 것을 전제로 거의 완벽한 호환성과 성능을 지원합니다. 부트캠프처럼 하드웨어에 붙는 것이 아니라, OS 위에서 프로그램처럼 돌아가는 것이기 때문에 그냥 윈도우를 하나의 프로그램처럼 쓰게 되죠. 그러함에도 성능 자체의 결함이 거의 없죠. 다만, 버전에 따른 미묘한 문제들이 발생하고 가격이 매우 비쌉니다 하하핳.
  3. **VirtualBox**: 저는 가난하기 때문에 VirtualBox를 사용했습니다. 설치하고 나니 아무래도 마우스 감이 좀 느리고, 화면 자체도 심리스하지는 않지만, 무료이며 패러렐즈 비슷한 효과를 내줄 수 있다는 점에서, 그냥 얘를 사용하기로 했습니다.

## 실제로 설치하기

- 윈도우10으로 설치하는 경우 일단은, 무료, 라고 생각하셔도 됩니다. [왜 윈도우10이 무료처럼 배포되는지 궁금하신 분들은 이 링크를 확인하시면 됩니다](https://www.itworld.co.kr/insight/94913.) 아래 영상에 자세하게 나와 있으니 참고하시면 됩니다.
- 우선, 30GB에서 40GB 정도의 여유 하드디스크 공간은 가진 상태로 시작하셔야 합니다.
- 저는 [MAC 에서 VirtualBox 를 이용하여 가상 머신에 Windows 10 설치하기](https://www.youtube.com/watch?v=iAEuVtX61zk) 를 참고하여 설치했습니다.