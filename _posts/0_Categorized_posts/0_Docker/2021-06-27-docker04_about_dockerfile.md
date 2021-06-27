---
title: docker - dockerfile
category: docker
tags: docker dockerfile container image
---

## docker - dockerfile

- dockerfile을 사용하면, container의 환경을 좀더 정확하게 구축할 수 있습니다.
- 아래 내용에서 보는 것처럼, 그냥 리눅스 커맨드들이 쭉 쓰여져 있는 형태다, 라고만 생각하셔도 일단은 상관이 없죠.

```dockerfile
FROM ubuntu

RUN mkdir new_folder
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y zsh
RUN apt-get install -y git
RUN apt-get install -y wget

RUN wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh
RUN bash install.sh
```

- 그 다음 `docker build` 명령어를 사용하여 image를 생성해줍니다. 
  - `-f`: file path 
  - `-t`: image name

```zsh
$ docker build -t my_dev_env -f Dockerfile .                                                                       
[+] Building 10.0s (13/13) FINISHED                                                                                                                                                                         
 => [internal] load build definition from Dockerfile                                                                                                                                                   0.0s
 => => transferring dockerfile: 299B                                                                                                                                                                   0.0s
 => [internal] load .dockerignore                                                                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                                                                       0.0s
 => [1/9] FROM docker.io/library/ubuntu                                                                                                                                                                0.0s
 => CACHED [2/9] RUN mkdir new_folder                                                                                                                                                                  0.0s
 => CACHED [3/9] RUN apt-get update                                                                                                                                                                    0.0s
 => CACHED [4/9] RUN apt-get install -y vim                                                                                                                                                            0.0s
 => CACHED [5/9] RUN apt-get install -y zsh                                                                                                                                                            0.0s
 => CACHED [6/9] RUN apt-get install -y git                                                                                                                                                            0.0s
 => [7/9] RUN apt-get install -y wget                                                                                                                                                                  4.4s
 => [8/9] RUN wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh                                                                                                                      1.4s
 => [9/9] RUN bash install.sh                                                                                                                                                                          2.8s 
 => exporting to image                                                                                                                                                                                 1.3s 
 => => exporting layers                                                                                                                                                                                1.3s 
 => => writing image sha256:3ae41bcefe71e26729105a40fdee8133280b219e39524889f84406fa537464bb                                                                                                           0.0s 
 => => naming to docker.io/library/my_dev_env                                                                                                                                                          0.0s 
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
my_dev_env   latest    3ae41bcefe71   6 seconds ago    289MB
```

- 그 다음 아래 명령어를 사용해서 컨테이너를 만들어보면 잘 만들어지는 것을 알 수 있죠.

```zsh
$ docker run -dit --name my_dev_con1 my_dev_env
```
