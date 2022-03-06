---
title: Install and Use htop
category: bash
tags: bash shell htop unix linux  brew
---

## Install and Use htop

- 개발 중에 현재 CPU 등에 과부하가 얼마나 걸리는지 확인하기 위하여, htop이라는 어플리케이션을 설치해보려고 합니다.
- Ubuntu 드에서는 apt-get 을 이용하여 설치하지만, macOS에서는 apt-get을 설치하는 것이 불가능하므로, brew를 이용하여 설치합니다.
- 그리고 `htop`을 실행하면 htop이 실행되고, 현재 대략적인 리소스 사용 상황을 파악할 수 있습니다.

```sh
brew install htop
htop
```

### htop in macOS, HHKB

- htop 실행 후 setup하려면 F2 키를 눌러야 합니다. 하지만 맥에서는 기본적으로 F 키 들에 화면 밝기와 같은 function들이 매핑되어 있어서, F2키를 누르려면, Fn 키를 누른 상태에서 F2 키를 눌러야 합니다. Fn 키를 누르지 않고 바로 F2키가 눌리게 하려면, 시스템 환경 설정 > 키보드 > 'F1, F2 등의 키를 표준 기능 키로 사용'을 활성화 해주면 됩니다.
- 다만, 저의 경우는 맥북에 HHKB(해피해킹 키보드)를 연결해서 사용합니다. 일반적인 키보드들처럼 F1키와 숫자 키가 독립적으로 존재하지 않고, 숫자 키만 존재합니다. Fn키를 누른 상태에서 숫자 키를 누르면 그게 F 키가 되는 셈이죠. 그리고 맥북을 쓰기 때문에 기본적으로는 Function 키에 화면 밝기 변경, 소리 변경과 같은 키가 매핑되어 있습니다. 즉, 현재로서는 F2와 같은 키를 클릭할 수 있는 방법이 없습니다. 그리고 F2 키를 활성화시키게 되면 화면 밝기와 같은 키가 비활성화됩니다.
- 그동안 맥북+해피해킹의 한계를 몰랐는데, 직접 F2와 같은 키를 눌러야 할때는 번거로움이 발생하네요.
- 다만, 이는 키보드의 특성으로 인해 발생하는 문제가 해결할 수는 없어 보입니다. [키보드매니아 - 해피해킹에서 맥전용 fn키는 어떻게 사용하나요?](http://www.kbdmania.net/xe/qanda/8980481)를 확인해 보면 미션 컨트롤을 사용해서 우회하는 방법을 사용하는 것으로 보입니다.

## Wrap-up

- 일단은 간단하게 htop을 설치하고 사용해봤습니다. 세부적인 설정은 mac + HHKB의 문제로 인해서 번거로울 것 같지만, 한번씩 그냥 모니터링하기는 좋겠네요.

## Reference

- [[macOS] htop을 이용하여 mac을 관리하기](https://sukvvon.tistory.com/37)
- [서버 모니터링 프로그램 Htop 사용 방법 – Ubuntu 기준](https://happist.com/557995/%EC%84%9C%EB%B2%84-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-htop-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-ubuntu)
