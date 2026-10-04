---
title: "맥에서 ftp 서버 띄우기"
date: 2022-03-19
category: "others"
tags: ["ftp", "macOS"]
permalink: "/others/run_ftp_server_on_mac/"
---

## 맥에서 ftp 서버 띄우기 - Intro

- 최근에 갤럭시 탭을 샀습니다. 저는 애플을 좋아해서, 아이폰, 맥북, 아이패드, 애플왓치 모두 갖추고 있는데요. 애플 제품끼리는 모두 에어드롭을 사용하면 되는데 애플과 갤럭시는 서로 데이터(가령 사진)을 옮기는게 어렵더군요. 물론 메일이나, 카카오톡을 이용하면 문제가 없습니다만.
- 그러던 와중에 갤럭시 탭에서 맥북에 ftp로 접속하는 방법은 불가능한가? 라는 생각이 들었습니다. 맥북에서 nodeJS를 이용해서 띄운 서버에 갤럭시탭에서 http로 접속하는 것은 가능했거든요.
- 따라서, 비슷한 방식으로 맥에서 ftp 서버를 열면 갤럭시에서 ftp서버에 접속할 수 있지 않을까? 하는 생각이 들어서 시도해보기로 합니다.

## 간단한 방법 - 맥 - 원격 로그인

- 이미 비슷한 질문이 있었는데요. [Clien - 모하비에서 ftp 서버 활성화 하는 방법은 없나요?](https://www.clien.net/service/board/cm_mac/12692903)에 답변이 있습니다. 맥에서 SSH, SFTP르 열어주기 때문에, 아래 방식으로 사용하면 됩니다.

1. 맥 > 시스템 환경 설정 > 공유 > 원격 로그인 활성화 
1. 갤럭시 탭 > 내 파일 > 네트워크 저장공간 > 네트워크 저장공간 추가 > SFTP 서버 > 맥북의 IP , 22 포트, 맥 ID, PW 입력 

- 이제 갤럭시 탭에서 맥의 파일들을 폴더처럼 사용할 수 있습니다.

## 실패한 방법 - vsftpd

- unix에서 vsftpd를 통해 직접 ftp 서버를 구동해보려고 하였으나, 오류와 함께 진행되지 않았습니다.
- 이유를 곱씹어 보자면, 아마도 다음이 아닐까 합니다(아닐 수도 있습니다).

1. vsftp는 yum을 통해 설치하고, 보통 centos 계열에서 사용되는 것으로 보입니다. 하지만, mac은 yum을 사용할 수 없기 때문에, `brew install`을 통해 우회해서 설치하죠. 이 과정에서 무엇인가 쪼금 삐끗한게 아닐까 싶어요. 실제로 설치가 이상하게 된 것 같아서 reinstall을 반복하기도 했습니다.
2. vsftp는 xinetd라는 외부 데몬에서 돌아가는 프로세스라는 말이 있었습니다. 대충, vsftp를 구동해주는 데몬인 것 같은데요. 제가 맞이한 오류는 "이미 xinetd에서 vsftp 가 사용하려는 port인 22를 사용하고 있어서, vsftp를 구동할 수 없다"라는 것이었죠. 문제는 맥 내에서 xinetd가 설치된 경로를 찾을 수 없었다는 것이죠. `etc/xinetd` 경로에 있다고 하는데, 설치된 적이 없고, 현재 실행중인 프로세스들을 뒤져봐도, xinetd는 사용된 적이 없어서, 명확하게 확인하는 것이 어려웠습니다.
3. vsftp는 실행시 root나 sudo 권한을 요구했습니다. 이 권한이 달라서, 문제가 발생했을 가능성도 있을 것 같구요.

- 뭐 어쨌거나, 실패했습니다. 그리고, 아래 내용을 진행하고 나니 맥이 눈에 띄게 느려진 모습을 발견했고 여러 번 컴퓨터를 재시작한 다음에야 조금 나아지더군요. 앞으로는 더 관심을 가지지 않으려 합니다. 호호.

### macOS에서 vsftpd 구동 - 실패기

- 이번에는 조금 복잡하게 진행해 보겠습니다. 직접 ftp 서버를 띄워볼게요.
- [FTP(VSFTPD) 서버 설치 및 설정 방법](https://dololak.tistory.com/670)를 확인해 보니, [wikipedia - vsftpd](https://en.wikipedia.org/wiki/Vsftpd)를 사용하여 linux에서 ftp를 띄울 수 있는 것으로 보입니다.
-  vsftpd를 설치하려면 yum을 사용해야 하는데요, 저는 맥을 쓰고 있어서 yum을 사용할 수 없습니다(yum은 Redhat based Linux에서 사용하는 패키지 매니저). 따라서, brew를 이용해서 설치해 보기로 합니다.

```sh
$ brew install vsftpd
...
To use chroot, vsftpd requires root privileges, so you will need to run
`sudo vsftpd`.
You should be certain that you trust any software you grant root privileges.

The vsftpd.conf file must be owned by root or vsftpd will refuse to start:
  sudo chown root /usr/local/etc/vsftpd.conf

To restart vsftpd after an upgrade:
  sudo brew services restart vsftpd
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/vsftpd/sbin/vsftpd /usr/local/etc/vsftpd.conf
==> Summary
🍺  /usr/local/Cellar/vsftpd/3.0.5: 14 files, 288.8KB
==> Running `brew cleanup vsftpd`...
```

- 설치가 완료되었으니 이제 실행을 해봅니다.
- 그러나, 여러 오류와 함께 진행되지 않는군요.

```sh
$ usr/local/opt/vsftpd/sbin/vsftpd /usr/local/etc/vsftpd.conf
500 OOPS: vsftpd: must be started as root (see run_as_launching_user option)
$ /usr/local/Cellar/vsftpd/3.0.5 ❯ sudo /usr/local/opt/vsftpd/sbin/vsftpd /usr/local/etc/vsftpd.conf
500 OOPS: config file not owned by correct user, or not a file
$ sudo chown root /usr/local/etc/vsftpd.conf
$ sudo /usr/local/opt/vsftpd/sbin/vsftpd /usr/local/etc/vsftpd.conf
500 OOPS: could not bind listening IPv4 socket
$ vi /usr/local/etc/vsftpd.conf
# standalone으로 시작하기 위해 svftpd.conf 내
# listen=NO 로 변경하였으나, 아래와 같은 오류가 발생함.
sudo /usr/local/opt/vsftpd/sbin/vsftpd /usr/local/etc/vsftpd.conf
500 OOPS: vsftpd: not configured for standalone, must be started from inetd
```

- 혹시 이미 port 점유 중인가 싶어서, 확인해봤지만, 그래 보이지는 않습니다.
- inetd에서 발생하는 문제라고 하여, process를 확인해봤으나 없고, 설치되어 있는 것처럼 보이지도 않거든요.

```sh
# 현재 사용중인 port를 확인하고,
# TCP 22번 포트를 사용하는지 확인합니다.
$ sudo lsof -i TCP:22
```

## Wrap-up

- 일단은 여기까집니다. 이후에 언젠가 유닉스에서 ftp 작업을 해야 할때 참고해보겠습니다.
- 아, 하나 더 시도해볼 수 있는 정도는 docker로 유닉스 환경을 하나 띄운 다음 해당 환경에서 위 내용을 그대로 다시 해보는 것도 있겠네요. local에서는 지금 여러 프로세스가 충돌이 발생할 수 있어서, 환경을 다시 세팅해서 시도해보는 것이 필요해 보입니다.

## Reference

- [FTP(VSFTPD) 서버 설치 및 설정 방법](https://dololak.tistory.com/670)
- [Clien - 모하비에서 ftp 서버 활성화 하는 방법은 없나요?](https://www.clien.net/service/board/cm_mac/12692903)
- [homebrew - vsftpd](https://formulae.brew.sh/formula/vsftpd)
- [KLDP - [vsftp]500 OOPS:could not bind listening IPv4 socket ??](https://kldp.org/node/41994)
- [stackexchange - installing vsftpd 500 oops colud not bind listening ipv4 socket](https://unix.stackexchange.com/questions/185190/installing-vsftpd-500-oops-could-not-bind-listening-ipv4-socket)