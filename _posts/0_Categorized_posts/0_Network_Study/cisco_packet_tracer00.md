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

### Case3: L2 스위치를 이용한 VLAN 설정

- VLAN은 서로 독립적으로 구성된 LAN을 말합니다. 물리적으로는 연결되어 있지만, 즉 유선상으로는 연결되어 있지만, 기기간에 연결되어 있지 않다는 이야기죠(ping이 응답하지 않는다는 이야기입니다). 
- 가령 회사에서 원래는 지역A에서 LAN을 구축하고, 지역B에서 LAN을 구축하였는데, 필요에 따라서 지역A와 지역B가 섞여 있는 방식으로 LAN을 구축해야 할 수 있죠. 그럼 어떻게 해야 하나요. 선을 끌어다가 저 멀리까지 구축을 해야 하나요? 그렇게도 할 수 있는 매우 번거롭죠.
- 따라서, 우리는 L2스위치를 사용해서 소프트웨어적으로 가상의 LAN을 구축할 수 있습니다. 
- L2스위치에 컴퓨터 1, 2, 3, 4를 다음 IP 주소로 설정해줍니다. IP 주소를 보면 앞의 모두 `192.1.1`로 앞 부분이 동일한 것을 알 수 있습니다. 얘네의 서브넷 마스크는 `255.255.255.0`이죠.
  - Computer1 IP Address: 192.1.1.1
  - Computer2 IP Address: 192.1.1.2
  - Computer3 IP Address: 192.1.1.3
  - Computer4 IP Address: 192.1.1.4
- 모든 컴퓨터를 L2스위치와 Straight_Line으로 연결합니다. 그리고 ping을 때려보면 아무 문제없이 서로 연결됩니다 호호.
- 이제 VLAN을 설정합니다. Computer 1, 2를 하나로 묶고, Computer 3, 4를 하나로 묶겠습니다. vlan 1번의 경우 기본 값이기 때문에 설정할 수 없습니다.

```plaintext
Switch>enable
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.

// vlan 10, vlan 20 을 만들어줍니다.
Switch(config)#vlan 10
Switch(config-vlan)#name vlan10
Switch(config-vlan)#exit
Switch(config)#vlan 20
Switch(config-vlan)#name vlan20
Switch(config-vlan)#exit

// interface별로 vlan을 설정해줍니다.
Switch(config)#interface fastEthernet0/1
Switch(config-if)#switchport access vlan 10
Switch(config-if)#exit

Switch(config)#interface fastEthernet0/2
Switch(config-if)#switchport access vlan 10
Switch(config-if)#exit

Switch(config)#interface fastEthernet0/3
Switch(config-if)#switchport access vlan 20
Switch(config-if)#exit

Switch(config)#interface fastEthernet0/4
Switch(config-if)#switchport access vlan 20
Switch(config-if)#exit
Switch(config)#end
```

- 이렇게 설정해주고 나면, 컴퓨터1-2는 서로 접근되고, 컴퓨터3-4는 서로 접근되지만, 두 VLAN간에는 접근되지 않습니다.

### Cas4: 스위치 2개로 VLAN 구성하기

- 이전에는 스위치 1개로 VLAN을 구성했습니다. 그런데, 이번에는 스위치 2개로 VLAN을 구성해보려고 해요. 
  - VLAN10: 스위치1에 연결된 컴퓨터1, 스위치2에 연결된 컴퓨터3
  - VLAN20: 스위치1에 연결된 컴퓨터2, 스위치2에 연결된 컴퓨터4
- 서로 다른 스위치 간에는 CrossCable을 연결해주어야 합니다.
- 스위치1에서는 다음처럼 설정해줍니다.

```plaintext
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.

Switch(config)#interface fastEthernet0/1
Switch(config-if)#switchport access vlan 10
Switch(config-if)#exit

Switch(config)#interface fastEthernet0/2
Switch(config-if)#switchport access vlan 20
Switch(config-if)#end
```

- 스위치2에서는 다음처럼 설정해줍니다.
  
```plaintext
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#interface fastEthernet0/1
Switch(config-if)#switch access vlan 10
Switch(config-if)#exit
Switch(config)#interface fastEthernet0/2
Switch(config-if)#switch access vlan 20
Switch(config-if)#end
```

- 그리고 스위치간 연결된 포트는 trunk로 설정해줍니다. "트렁크(Trunk)"란 복수의 스위치를 한 개의 스위치처럼 묶는 것을 말합니다. 즉 물리적으로는 여러 대의 스위치이지만, 논리적으로 하나의 스위치로 통합해버리는 것을 말하죠. 

```plaintext
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#interface fastEthernet0/10
Switch(config-if)#switchport mode trunk 
```

- 이렇게 하고 나서 서로 ping을 때려보면 의도한 대로 되는 것을 알 수 있습니다.


### Case5: 스위치 2개로 VLAN + 이더채널 

- "이더채널"은 물리적인 복수의 선을 논리적인 1 개의 선으로 구성하는 것을 말합니다. 가령, 대역폭이 커져야 하는 구간에 선을 여러 개 연결하고, 이더채널로 설정해버리면 대역폭이 증가되죠. 보통 스위치 간에 대역폭을 늘리고 로드 밸런싱을 하기 위해서 사용됩니다.
- 그냥 선만 추가하면 알아서 해주지 않을까? 싶지만 그렇지 않습니다. 실제로 두 스위치 사이에 CrossCable을 몇 개 더 연결하고 ping을 날려보면 문제없이 되는 것처럼 보이지만, 사실 모든 포트에 녹색 불이 들어온 것이 아니죠. 양쪽에 모두 녹색이 들어온 것은 한 개 밖에 없습니다. 그리고, 이 녹색 선을 삭제하면, 다른 선에 녹색불이 들어오죠. 즉 그냥 Redundancy 역할, 장애 시 커버해주는 역할만을 수행하고 이다고 보면 됩니다.
- 따라서 우리는 이 선들을 합쳐서 하나의 선으로 만들어보려고 합니다. 양쪽 스위치에 모두 아래 명령어를 실행해줘야 합니다.

```plaintext
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.

Switch(config)#interface range fastEthernet0/10-12
Switch(config-if-range)#channel-group 1 mode on
Switch(config-if-range)#
Creating a port-channel interface Port-channel 1

%LINK-5-CHANGED: Interface Port-channel1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
%SPANTREE-2-RECV_PVID_ERR: Received 802.1Q BPDU on non trunk Port-channel1 VLAN1.

%SPANTREE-2-BLOCK_PVID_LOCAL: Blocking Port-channel1 on VLAN0001. Inconsistent port type.
Switch(config-if-range)#end

// 잘 설치되었는지 확인
Switch#show etherchannel summary 
Flags:  D - down        P - in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------------------------

1      Po1(SU)           -      Fa0/10(P) Fa0/11(P) Fa0/12(P) 
```

- 이렇게 양쪽에 다 해주고 나면, 두 스위치에 있는 포트 6개에 모두 녹색 불이 들어온 것을 알 수 있습니다.
- 그런데, ping을 때려봐도 연결이 되지 않는 것을 알 수 있습니다. 이는 이전에 물리적인 포트 설정들이 다 날아가고, 논리적인 포트로 통합되었기 때문이죠. 따라서, 이제 그 둘을 서로 다시 연결해주는 작업이 필요합니다.
- 양 스위치에서 아래 명령어를 실행해줍니다. 

```plaintext
Switch>enable 
Switch#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.

Switch(config)#interface range fastEthernet0/10-12

Switch(config-if-range)#channel-group 1 mode active
Switch(config-if-range)#
Creating a port-channel interface Port-channel 1

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/10, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/10, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/11, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/11, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/12, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/12, changed state to up

Switch(config-if-range)#interface port-channel 1

Switch#show etherchannel summary
Flags:  D - down        P - in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------------------------

1      Po1(SD)           LACP   Fa0/10(I) Fa0/11(I) Fa0/12(I) 
```

- 그리고 나머지 컴퓨터들을 모두 연결해주면, 이더채널이 완성됩니다.

### Case







## Further Issues

L3 스위치 
Multi layer Switch 
라우터
스위치 + 이더채널
spanning tree

라우터, 라우터와 정적연결
