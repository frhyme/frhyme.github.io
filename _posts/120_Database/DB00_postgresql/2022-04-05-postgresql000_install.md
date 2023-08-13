---
title: postgresql 000 - Install postgresql
category: postgresql
tags: db database posgresql sql
---

## postgresql 000 - Install postgresql

- 지금까지는 주로 OracleDB를 주로 사용해 왔는데요. postgresql을 한번 공부해보면서 그 내용들을 정리해보려고 합니다.
- 로컬에 설치하지 않고, docker를 설치한 다음 docker에 가상으로 띄워서 접속해보려고 합니다. 이게, 매번 귀찮아서 그냥 local에 그대로 설치하다 보면 이후에 충돌이 발생한다거나 하는 문제가 있더라고요.
- 문제는 docker를 사용하지 않은지 오래되었다는 건데....뭐 이번에 복습하면 되죠 호호호.
- docker에서 ubuntu를 image로 새로운 container를 생성하고, 해당 container에 접속해 봅니다.

```sh
$ docker create --name ubuntu_postgresql ubuntu
...
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS    PORTS     NAMES
...            ubuntu    "/bin/bash"   2 seconds ago   Created             ubuntu_postgresql
$ docker start ubuntu_postgresql
$ docker exec -it ubuntu_postgresql bin/bash
```

- 여기에 postgresql을 설치하고, 테스트를 해보기로 합니다.
- 현재 설치된 ubuntu 버전을 확인해 봅니다.

```sh1
$ cat etc/issue
Ubuntu 20.04.2 LTS \n \l
```

### Install postgresql by apt

- apt를 사용해서 postgresql을 설치할 계획입니다.
- [APT(Advanced Package Tool))](https://en.wikipedia.org/wiki/APT_(software))은 debian기반의 리눅스 배포판에서 중요한 패키지들을 설치하기 위해 사용하는 툴입니다.
- `sudo: command not found`가 뜨는 것은 현재 유저가 `root`이기 때문에 그런 것이 아닐까 싶어요. 일단은 신경 쓰지 않고 진행해보겠습니다.

```sh
root@1084f3813dad:/etc/apt# sudo apt update
bash: sudo: command not found
root@1084f3813dad:/etc/apt# apt update
Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Get:3 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [1096 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
Get:6 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [25.8 kB]
Get:7 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [863 kB]
Get:8 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [1721 kB]
Get:9 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [11.3 MB]
Get:10 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [177 kB]
Get:11 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages [1275 kB]
Get:12 http://archive.ubuntu.com/ubuntu focal/restricted amd64 Packages [33.4 kB]
Get:13 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [30.3 kB]
Get:14 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [2136 kB]
Get:15 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1149 kB]
Get:16 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [1173 kB]
Get:17 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [26.0 kB]
Get:18 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [51.2 kB]
Fetched 21.7 MB in 9s (2340 kB/s)
Reading package lists... Done
Building dependency tree
Reading state information... Done
35 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

- 그리고, postgresql을 설치합니다.

```sh
$ apt install postgresql
...
Current default time zone: 'Asia/Seoul'
Local time is now:      Sat Apr  2 13:45:25 KST 2022.
Universal Time is now:  Sat Apr  2 04:45:25 UTC 2022.
Run 'dpkg-reconfigure tzdata' if you wish to change it.
...
Success. You can now start the database server using:

    pg_ctlcluster 12 main start

Ver Cluster Port Status Owner    Data directory              Log file
12  main    5432 down   postgres /var/lib/postgresql/12/main /var/log/postgresql/postgresql-12-main.log
```

### service postgresql start

- `service postgresql start`로 실행해도 되는데? systemctl만으로 되는게 아니었음.

- `su - postgres`: `su`는 "switch user"를 의미합니다. linux command로 현재 접속 중인 linux 계정을 변경하겠다는 것을 의미하죠. 해당 커맨드 실행 후 "root"가 "postgre"로 변경됩니다.
- `service postgresql start`: postgresql을 시작한다는 의미의 커맨드입니다.
  - `service`: service command는 보통 System V Init script를 실행하기 위해서 사용됩니다. System V init Script는 보통 `etc/init.d`내에 존재하죠. 그렇다면 "System V init script"가 무엇인지 설명을 해야 될것 같은데, 죄송스럽게도 잘 모릅니다. 하하하. 그래도 아는 대로 설명하자면, "Init"은 리눅스에서 프로세스들의 프로세스(parent process)를 가리키는 개념인 것으로 보입니다. 그리고 Init을 구현한 것(Implementation) 중 하나가 SystemV 라고 하네요. 이외에도 Systemd, upstart 등도 있다고는 합니다. 뭐, 일단은 그냥 "리눅스에서 관련 있는 프로세스를 하나로 묶어서 관리하는 단위" 정도로 이해하고 넘어가기로 합니다.
  - `service <system_v_init_script_name> start`: `<system_v_init_script_name>`을 시작한다는 말로 이해하면 될 것 같습니다.
- 아무튼, 이를 통해 posgresql을 실행하고 `psql`을 통해 잘 되는 것을 확인하였습니다.

```sh
$ service postgresql start
 * Starting PostgreSQL 12 database server
$ ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Apr04 pts/0    00:00:00 /bin/bash
postgres  4003     1  0 00:28 ?        00:00:00 /usr/lib/postgresql/12/bin/postgres -D /var/lib/postgresql/12/main -c config_file=/etc/postgresql/12/main/postgresql.conf
postgres  4005  4003  0 00:28 ?        00:00:00 postgres: 12/main: checkpointer
postgres  4006  4003  0 00:28 ?        00:00:00 postgres: 12/main: background writer
postgres  4007  4003  0 00:28 ?        00:00:00 postgres: 12/main: walwriter
postgres  4008  4003  0 00:28 ?        00:00:00 postgres: 12/main: autovacuum launcher
postgres  4009  4003  0 00:28 ?        00:00:00 postgres: 12/main: stats collector
postgres  4010  4003  0 00:28 ?        00:00:00 postgres: 12/main: logical replication launcher
root      4022     1  0 00:28 pts/0    00:00:00 ps -ef
$ psql
psql: error: FATAL:  role "root" does not exist
$ whoami
root
$ su - postgres
$ whoami
postgres
$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=#
```

## Wrap-up

- 처음에는 `service` command를 사용하지 않고, `systemctl`을 사용하였습니다. `systemctl` 또한 Linux Init Implementaion 중 하나로 보입니다만, `systemctl`을 사용했을 때는 postgresql이 동작되지 않았습니다. 뭔가 세팅이 빠져 있었던 것이겠죠.
- ubuntu에 postgresql을 설치하는 것보다, 처음부터 postgresql이 설치되어 있는 image를 받아서 container를 구동하는 것이 더 효율적이지 않았을까? 하는 생각이 중간에 잠시 들었습니다만, 이렇게 돌아 돌아 가는 것이 학습의 길이라고 생각해 봅니다 호호.
- `systemctl`을 사용했을 때의 log는 다음과 같습니다. [stackoverflow - docker system has not been booted with systemd as init system](https://stackoverflow.com/questions/59466250/docker-system-has-not-been-booted-with-systemd-as-init-system)을 확인해 보면, docker 레벨에서 뭔가 잠겨 있는 것으로 보이기도 하는데요. 잘못 조절했다가는 문제가 발생할 것 같아서 더 진행하지 않았습니다.

```sh
$ systemctl start postgresql
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

- 이제 docker container에 postgresql을 띄웠으니, 로컬 맥북에서 docker container과 통신하여 쿼리를 날리고 결과를 전달받고 할 수 있지 않을까? 하는 생각이 드네요. 나중에 한번 해보도록 하겠습니다 호호.

## Reference

- [systemd란?](https://etloveguitar.tistory.com/57)
- [Ubuntu 환경에서 PostgreSQL 설치 후 리모트 접속하기](https://yeojin-dev.github.io/blog/postgresql-ubuntu/)
- [linuxjourney - lesson -sysv - overview](https://linuxjourney.com/lesson/sysv-overview)
