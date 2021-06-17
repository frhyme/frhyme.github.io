---
title: docker - ubuntu container 구동하기 
category: docker
tags: docker ubuntu container
---

## docker - ubuntu container 구동하기 

- 이제 docker를 이용해서, ubuntu container를 하나 구동해보려고 합니다.
- docker를 이용해서 ubunut image를 docker hub에서 찾고, local로 가져옵니다.
  - `docker images`: local에 존재하는 docker image를 보여줍니다.
  - `docker search image_name`: docker hub에서 image_name을 검색해서 관련된 image들을 가져옵니다.
  - `docker pull image_name`: docker hub로부터 local로 image를 가져옵니다.

```bash
$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
$ docker search ubuntu
NAME                                                      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                                                    Ubuntu is a Debian-based Linux operating sys…   12375     [OK]       
dorowu/ubuntu-desktop-lxde-vnc                            Docker image to provide HTML5 VNC interface …   539                  [OK]
websphere-liberty                                         WebSphere Liberty multi-architecture images …   273       [OK]       
...
$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
345e3491a907: Pull complete 
57671312ef6f: Pull complete 
5e9250ddb7d0: Pull complete 
Digest: sha256:adf73ca014822ad8237623d388cedf4d5346aa72c270c5acc01431cc93e18e2d
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       latest    7e0aa2d69a15   7 weeks ago   72.7MB
```

- 이제 가져온 image를 기반으로 하는 container를 돌려 봅니다.
  - `docker ps -a`: 현재 돌아가고 있는 container를 모두 보여준다.
  - `docker run -dit --name container_name image_name`: image_name을 기반으로 하는 docker container의 이름을 container_name으로 하는 컨테이너를 시작한다.
    - `d`: Run container in background and print container ID. 즉 해당 컨테이너를 백그라운드에서 돌려준다는 것이죠.
    - `i`: Keep STDIN open even if not attached
    - `t`: Allocate a pseudo-TTY
    - 보통, `i`, `t`는 함께 쓰이는데요, 일단은 이렇게 붙여서 쓰면, 제 터미널에서 컨테이너 터미널로 바로 붙어서 커맨드를 사용할 수 있다, 라고 생각하시면 됩니다.
  - `docker attach container_name`: container_name을 가진 docker에 붙습니다. 
    - 다만, 컨테이너에 터미널로 붙은 다음, `exit`로 나오게 되면 자동으로 해당 컨테이너가 꺼지게 되죠. 만약 컨테이너를 끄지 않고 나오고 싶다면, ctrl + p, ctrl + q 를 연속으로 누르면 끄지 않고 외부로 나올 수 있죠.

```bash
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
$ docker run -dit --name first_ubuntu ubuntu
85220b53a10c85cab9cb6240d6958f19dd0860c033720eca2b1ab34085a0584a
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
85220b53a10c   ubuntu    "/bin/bash"   4 seconds ago   Up 3 seconds             first_ubuntu
$ docker attach first_ubuntu
root@85220b53a10c:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@85220b53a10c:/# exit
exit
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                     PORTS     NAMES
85220b53a10c   ubuntu    "/bin/bash"   46 seconds ago   Exited (0) 2 seconds ago             first_ubuntu
$ docker start first_ubuntu
first_ubuntu
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
85220b53a10c   ubuntu    "/bin/bash"   54 seconds ago   Up 2 seconds             first_ubuntu
$ docker stop first_ubuntu
first_ubuntu
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS                     PORTS     NAMES
85220b53a10c   ubuntu    "/bin/bash"   About a minute ago   Exited (0) 3 seconds ago             first_ubuntu
```

## wrap-up

- 일단은 간단하게, docker를 사용해서 컨테이너를 구동해 봤습니다.
- 이게 실제로 가상머신이 맞다면, 로컬에서 이 가상머신에 통신해서 정보를 전달하고, 전달받고, 뭐 이런 작업들이 가능해야겠죠. 따라서, 특정 port를 통해 통신하도록 설정할 수도 있고 할텐데, 이건 나중에 해보겠습니다. 오늘은 그냥 컨테이너를 구동하고, 내부에서 이것저것 설정을 해봤다, 정도로 만족합니다.