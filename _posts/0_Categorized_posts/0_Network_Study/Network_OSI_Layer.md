---
title: 네트워크는 무엇인가.
category: 
tags: 
---

## 기본적인 네트워크의 개념들을 정리해보기로 합니다

## OSI 7계층이란?

- OSI 7계층은 네트워크 상에서 통신이 일어나는 과정을 7단계로 나눈 것을 말합니다.
- 통신이 일어나는 과정은 단계적이고, 만약 7단계에서 문제가 생긴다면, 순차적으로 아래 레벨의 단계에서 문제가 발생했기 때문인 것이죠.
- OSI에서는 7계층으로 네트워크의 레벨을 분리하였지만, TCP/IP Protocol 에서는 4단계(Application, Transport, Internet, Network Interface)로 구분합니다.

### OSI L1 - Physical Layer(물리 계층)

- 이 계층에서는 데이터를 전기적인 신호로 받아서 그대로 주고 받는 기능만을 수행합니다. 이 계층에 속하는 장치는 케이블, 허브를 말할 수 있습니다.
- 다른 레벨에서는 받으려는 데이터가 무엇이고, 어디로 가는지, 그리고 오류가 있을 경우 수정하는 기능을 해주기도 하지만, 이 레벨에서는 아무것도 수정하지 않고, 그대로 전달만 할 뿐입니다.
- 이 때 통신하는 데이터의 단위는 Bit입니다. 전기적 성질을 그대로 사용하니까 당연한 것이겠죠.

### OSI L2 - DataLink Layer

- L1인 물리계층을 통해 전달받는 정보의 흐름을 관리하여, 정보가 문제없이 전달될 수 있도록 합니다. 이 과정에서는 오류를 찾아주기도 하고, 필요할 경우 재전송을 하는 기능을 가지고 있기도 하죠.
- 이 계층에서 전달하는 단위를 '프레임'이라고 합니다. 
- 또한, 여기서는 Mac Address를 가지고 통신하게 됩니다. 
- 스위치가 여기에 속하는 장비죠.

### OSI L3 - Network Layer

- L1에서는 전기적으로 연결하고, L2에서는 간단한 오류를 검출하고, 각 기기에 배정된 MAC Address를 사용해서 기기에 통신을 합니다.
- L3에 속하는 기기는 '라우터'인데, 라우터는 "데이터를 목적기기까지 전달하는 기능"을 수행합니다. 
- 가령 게임방A 네트워크에서 게임방B 네트워크로 데이터를 전달해야 한다면, 두 네트워크 간에 데이터를 전달하기 위해서 어떤 경로를 통해서 가야하는지를 탐색하는 것이 필요하죠. 이렇게, 출발지로부터 목적지까지 어떻게 가는지, 이를 찾아주고 보내는 것을 라우터가 진행하죠.
  - 물론, L3에 속하는 스위치도 존재합니다.
- 이 단계에서는 IP주소를 사용합니다(L2에서는 Mac Address를 사용함)




### OSI L7 - Application Layer

- 일반적으로 인터넷을 한다고 하면, "웹브라우저를 켜서 http"를 사용합니다. 사람이 직접 사용하는 프로토콜은 보통 최상위 레이어죠. 웹브라우저에서 쓰는 것처럼 http 프로토콜을 이용해서 통신하는 것이 계층, L7에 속합니다. 
- HTTP, FTP, SMTP, POP3, IMAP 등이 이 단계에 속하죠.
- 이 단계가 구성되어 있다면, 일반적인 네트워크 소프트웨어의 UI부분, 웹브라우저 위에서 문제없이 네트워크를 사용하는 것이 가능하죠.

--- 

### 허브 - L1 Physical Layer

- 기본적으로 허브, 스위치는 모두 네트워크 멀티탭이라고 생각하면 됩니다.
- '허브'의 경우는 왕복 일차선으로 여러 통신들에 대해서 병렬적으로 처리하는 것이 아닌, 순차적으로 하나씩 처리한다고 보면 됩니다. 이 때 흥미롭게도 대역폭 또한 나누어서 쓰게 되죠. 따라서 만약 '허브'가 가지고 있는 대역폭이 10이고 5개의 기기에 연결되어 있다면 각 기기가 배정받을 수 있는 최대의 대역폭은 2가 되는 것이죠. 또한, '허브'는 OSI layer로 봤을 때, L1에 속하는 낮은 레벨의 네트워크 장비죠.
- 또한 '허브'는 만약 5개의 기기에 연결되어 있다고 하면 하나의 기기로부터 전달받은 데이터 프레임(패킷)을 연결된 모든 기기로 한번에 보내게 됩니다. 이를 '플러딩(Flooding)'이라고 하는데, 수신된 링크를 제외한 나머지 링크로 패킷을 일괄적으로 단순히 복사 전송하는 것을 말하죠.
- 따라서, 동시에 복수의 허브에서 데이터 프레임을 전송하게 되면 데이터 충돌(collision)이 발생하게 되고, 당연히 네트워크에는 부하가 걸리게 되죠.

### 스위치 - L2 Data Link Layer

- 연결된 모든 링크에 데이터를 송수신하는 '허브'와 달리 '스위치'는 해당 데이터를 필요로 하는 하나의 기기에게 타겟팅을 해서 보내게 됩니다. 또한, 양방향으로 통신을 하는 것이 가능하죠.
- 각 기기에 대해서 독립적인 MAC Address와 포트를 기록해두고, 전체 장비에 데이터를 보내는 것이 아니라, 해당 기기에만 데이터를 보내는 것을 말하죠.
- 다만, 프레임이 전송되어야 하는 MAC address가 현재 스위치에 기록되어 있지 않다면(또한 다른 몇 가지 경우들에 대해서는), '허브'와 마찬가지로 모든 기기로 프레임을 전송하는 '플러딩'을 수행하게 됩니다. 간단히 말하자면, "누구한테 보내져야 하는지 모르겠으니, 모두에게 보내도록 한다"라는 전략인 셈이죠. 그리고 당연히 이런 경우에는 네트워크에 과부하가 걸리게 됩니다. 그리고, 이를 해결하기 위해서 VLAN이 도입되게 되었죠.

### VLAN(Virtual Local Area Network)

- "2계층(Logical Layer)에서 논리적이고 유연한 망을 설계할 수 있는 가상 LAN)"
- 앞서 말한 바와 같이, VLAN을 사용하는 이유는 "한 네트워크 내에서 '플러딩'으로 인해 발생하는 네트워크 과부하"를 줄이기 위함이죠.
- 하나의 예를 들어, 만약 집에 스위치가 두 개가 있다고 합시다. 그리고 컴퓨터 A, B를 스위치A에 C, D를 스위치B에 연결했다고 하죠. 그렇다면 물리적으로 봤을 때도, 현재는 두 개의 서로 다른 네트워크가 생성된 것입니다. 물리적으로 구분되어 있죠.
- 하지만, 늘 이렇게 물리적으로 구분할 수는 없죠. 우리에게는 단 1개의 스위치만 있고, 이를 통해 2개의 논리적 네트워크를 만들어보겠다고 하겠습니다.
- 해당 스위치는 포트가 10개 있다고 하죠. 이 때 1번부터 5번까지의 포트에 대해서 VLAN1을 구성하고, 6번부터 10번까지를 VLAN2로 구성한다고 하겠습니다. 이렇게 할 경우, 물리적으로 하나의 스위치에 연결되어 있지만, 두 기기를 서로 간에 통신하는 것이 불가능합니다.
- 이런 방식으로, 네트워크를 논리적으로 구분하는 것을 VLAN이라고 하죠.

#### VLAN의 장점

- 앞서 말한 것과 같이, 데이터가 해당 기기에 정확하게 전달되지 않았을 때 모든 기기에 데이터를 전송해버리는 '플러딩'이 네트워크에서 발생합니다. 그런데, 만약 하나의 단일네트워크에 1000개의 기기가 연결되어 있고 여기서 플러딩이 발생한다면 네트워크에 과부하가 걸리는 것은 너무도 당연한 일이죠. 따라서, 우선은 네트워크에서 발생할 수 있는 트래픽을 막는다는 것이 가장 큰 장점입니다.
- 그 외로는 물리적인 연결없이 하나의 스위치에서 설정할 수 있기 때문에, 네트워크를 필요에 따라 편하게 구분해서 관리할 수 있다는 것, 그리고 네트워크 보안을 말할 수 있겠죠.

#### VLAN 구성방법 

- 포트로 연결하기: 연결된 포트들에 대해서, 포트에게 각각 서로 다른 VLAN을 설정해주는 것을 말합니다. 포트 1, 2, 3, 4에게는 VLAN1을 포트 5, 6, 7, 8에게는 VLAN2을 주면 논리적으로 서로 다른 (가상의)네트워크에 기기들이 연결되고 다른 네트워크 2개가 생성된 셈이죠.
- MAC Address로 연결하기: 기기의 랜카드(네트워크 어댑터)에는 모두 고유의 맥 어드레스를 가지고 있습니다. 즉, 맥 어드레스만으로도 해당 기기의 고유성이 보장되고, 이를 통해 VLAN을 구성할 수도 있죠. 

### 라우터 - L3 Network Layer

- 라우터는 IP주소와 같이, Layer 3에 있는 주소를 참고하여, 목적지의 포트로 데이터를 전송하게 됩니다.
- 허브와 스위치는 각각 모두 하나의 네트워크를 설정하기 위해 사용됩니다. 가령, 한 '게임방'이 하나의 네트워크다, 라고 생각하셔도 되는 것이죠.
- 다만, 그렇다면 한 '게임방'에서는 온라인게임을 원활하게 하기 위해서 다른 '게임방'과 연결되는 작업이 필요하겠죠. 즉, 이렇게 서로 다른 네트워크를 연결하기 위해서 사용되는 장비가 바로 '라우터'인 것이죠.
- '라우터'는 특정 네트워크에서 전달받은 데이터가 도달되어야 하는 가장 효과적인 길을 찾고 그 길을 통해 목적지에 데이터가 무사히 도착할 수 있도록 해줍니다.
- 조금 더 설명하자면, 하나의 단일된 네트워크 내에서는 연결된 기기들에 대한 정보를 비교적 정확하게 알 수 있습니다. 어떤 기기/OS/프로토콜 등에 대해서 한 네트워크 내에서는 그 정보가 문제없이 공유되죠.
- 다만 하나의 네트워크를 넘어서 다른 네트워크들과 연결이 될 때는 대상이 되는 기기의 환경에 대한 정보를 정확하게 알기 어렵습니다. 따라서, 이런 경우에는 라우터를 통해 서로 다른 네트워크간의 연결을 지원하는 것이 필요해지죠.

### 공유기 

### V-LAN
- 
- 라우터
- 허브
- 공유기
- 스위치
- OSI 7계층
- TCP/IP 
- vlan

- 브로드캐스팅과 플러딩의 차이점? 
  - 개념적으로는 비슷하게 느껴지는데, 흠.

## Further Issues

## Reference

- [스위치, 라우터, 허브 차이점](https://brownbears.tistory.com/190)
- [vlan이란 무엇인가](https://m.blog.naver.com/PostView.nhn?blogId=skytk123&logNo=120194129402&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [OSI 7계층](https://adrian0220.tistory.com/84)
- [OSI 7계층이란?](https://shlee0882.tistory.com/110)