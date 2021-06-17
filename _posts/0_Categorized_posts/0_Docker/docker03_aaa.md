---
title: docker - what? 
category: docker 
tags: docker container image
---

## docker - dddd

- 아래 패키지들을 다 작성해서, 이미지를 만들려면 dockerfile을 작성해야 하는것 같은데.

- 일단 ubuntu기반 docker container를 새로 만들어준다.
  - `apt-get`: 우분투를 포함한, 데비안 계열의 운영체제에서 사용하는, 패키지 관리도구. ubuntu를 기본 컨테이너로 구동했을 때, `vi`는 따로 설치되어 있지 않기 때문에, 얘를 설치하기 위해서 사용합니다.

```bash
$ apt-get update
$ apt-get install vim
$ apt-get install curl
$ apt-get install wget
$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ bash Anaconda3-2021.05-Linux-x86_64.sh 
$ source .bashrc
$ apt-get install zsh
$ apt-get install git
$ wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
$ sh install.sh
$ source .zshrc
```


```
sh | (anon):12: character not in range
``` 

- 위 문제는 아래 명령어를 통해 해결하면 됨.

```bash
sudo apt-get install -y language-pack-en
sudo update-locale
zsh
```


- 기본 shell 을 변경해줍니다.

```zsh
$ chsh -s /usr/bin/zsh
```