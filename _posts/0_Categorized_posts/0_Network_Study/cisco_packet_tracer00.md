---
title: Cisco Packet Tracer로 네트워크를 공부해봅시다.
category: NetworkStudy
tags: NetworkStudy Network Hub Switch cisco
---

## Install Cisco Packet Tracer

- [Cisco Packet Tracer for MAC](https://mac.filehorse.com/download-cisco-packet-tracer/)을 다운받아 봅시다.
- 다운받아서 Next를 연타하여 설치합니다. 그리고 나면 "Cisco Packet Tracer", "Linguist", "maintenancetool" 등이 설치되어 있는 것을 알 수 있습니다.


### Case1: 두 컴퓨터를 바로 연결할 때 

- 두 컴퓨터에 각각 IP를 설정해줍니다. 저는 각각 `192.168.0.1`, `192.168.0.2`라는 아이피를 각각 설정해주었습니다.
- 그리고 다른 기기 없어 컴퓨터 간에만 바로 연결해주는 것이어서, 이 때는 Straight Line을 쓰는 것이 아니라, Twisted Line을 사용해서 연결해줘야 합니다. Strainght line은 보통 컴퓨터와 다른 기기간을 연결할 때 사용하죠.
- 그리고, `192.168.0.1` 의 터미널에서 아래를 실행해보면 아래와 같은 결과가 나오죠. 잘 나온다는 이야기입니다.

```plaintext
C:\>ping 192.168.0.2

Pinging 192.168.0.2 with 32 bytes of data:

Reply from 192.168.0.2: bytes=32 time<1ms TTL=128
Reply from 192.168.0.2: bytes=32 time<1ms TTL=128
Reply from 192.168.0.2: bytes=32 time<1ms TTL=128
Reply from 192.168.0.2: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.0.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

### Case2: 두 컴퓨터를 스위치로 연결할 때

- "컴퓨터1 - 스위치 - 컴퓨터2"로 연결하였습니다. Case1과 똑같은데, 그냥 Straight Line으로 스위치를 연결하였다는 차이만 있죠.
- 그냥 이렇게 하고 스위치에 아무 설정을 하지 않고도 위처럼 `ping`을 날리면 문제없이 잘 됩니다.

### Case3: 라우터를 사용해서 VLAN을 구성하기

- 