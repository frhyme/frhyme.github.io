---
title: Docker - Mac에 Docker 설치하고 간단히 사용해보기 
category: docker
tags: docker mac container dockerfile
---

## Docker - Mac에 Docker 설치하고 간단히 사용해보기

- 맥북에 Docker를 설치해보기로 했습니다. Docker야 이제 개발자들의 기본 기술 Stack이라고 봐도 무방하기 대문에, Docker가 무엇인지는 굳이 하나하나 설명할 필요가 없다고 생각합니다. 그리고 이쪽 기술이 워낙 빠르게(제가 따라잡을 수는 없을 정도로) 성장하고 있기 때문에, 모든 것을 다 알기도 어렵구요. 그리고, 저는 기술이 무엇인지 그 개념을 하나하나 파악하면서 따라가는 것보다는 "아니 일단 몰라도 한번 써볼까?"의 마음으로 접근하는 것이 더 많을 것을 배울 수 있다, 라고 생각해요. 그러니, Docker가 뭐지? 라는 생각이 드신다면 일단 어떻게든 깔아서 슥슥 따라해보시는 것이 좋을 것 같습니다.
- Docker는 일단 "가상머신"이다, 라고만 생각하셔도 됩니다. 저의 경우 맥북에 설치를 하게 될텐데, MacOS와 독립된 새로운 컴퓨터를 하나 더 설치하는 것이죠. 그냥 기존 OS에 설치하면 안돼? 라는 생각이 들 수도 있지만, 라이브러리간 의존성을 해결하는 하나의 깔끔한 이미지를 만들어두면 관리상에 유용한 점들이 많이 생기죠.
- 이 글에서는 Docker를 Mac에 설치하는 것부터 아주 간단하게 사용하는 방법까지를 정리해보려 합니다.

## Install Docker

- [Docker - official site](https://www.docker.com/products/docker-desktop)에서 Docker Desktop(Mac with intel chip)을 설치해줍니다. 저는 구형 맥북이라서 intel chip을 사용하고 있거든요. 저도 M1 사고 싶읍니다 흑흑.
- 다운받아서 설치하고 나면, 터미널에서도 `docker`를 치면 커맨드가 인식이 됩니다.
- 사실 너무 쉽게 설치되어서 조금 당혹스럽네요. 이전에 윈도우에서 docker를 설치할 때는 기본적인 환경 변수들(가령, hyper-v)을 조절해주고, 다른 다양한 번거로움들이 있었던 것 같은데, 맥에서는 바로 설치가 됩니다. 이게 경우에 따라서는 장점일 수도 있는데, 세부적으로 어떻게 운영되는지 모른다는 점에서 좀 아쉽기도 해요. 뭐, 이건 나중에, docker에서 새로운 우분투 컨테이너를 설치한다음 그 환경에서 새롭게 또 설치하면서 익숙해지도록 하죠.

## Docker - Client and Server

- Docker가 정상적으로 설치되었는지 확인하기 위해서, `docker version` 명령어를 사용해서 버전을 확인해 봅시다. 
- 보통 프로그램을 설치하면, 1개의 버전만 나오지만, docker의 경우 Client, Server의 버전이 각각 나오게 됩니다. 하나를 설치한 것 같지만, 사실은 2개가 설치되어 있다는 것이죠.
- 개념적으로 보면, 우리가 docker 명령어를 사용하면, docker client에 전달되고, 이 값이 docker server로 전달되어 수행되죠. 즉, 실제로는 docker server가 작업을 모두 수행한다고 보시면 됩니다. 잘 모르지만, 이렇게 설치되어 있는 이유가 있겠죠. 나중에 알아보기로 하고 일단은 진도를 빼겠습니다.

```bash
$ docker version
Client:
 Cloud integration: 1.0.17
 Version:           20.10.7
 API version:       1.41
 Go version:        go1.16.4
 Git commit:        ...
 Built:             Wed Jun  2 11:56:22 2021
 OS/Arch:           darwin/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.7
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       ...
  Built:            Wed Jun  2 11:54:58 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
 ...
 runc:
 ...    
 docker-init:
 ...
```

## docker run 

- 이제 배경 설명은 그만하고, 실제로 container를 돌려 보겠습니다.
- `docker run`을 사용해서 컨테이너를 운영합니다. 옵션들로는 각각 다음들이 있죠.
  - `-d`: detach mode, 백그라운드 모드
  - `-p`: host와 container의 port를 연결합니다. 아래 명령어에서 보면, 80:80이 함께 작성되어 있는데, 이는 host에서의 80 port와 container의 80 port를 연결한다는 것을 말하죠. 무슨말이지? 싶다면, 컨테이너를 실행한 다음, host에서 크롬 브라우저를 킨 다음 `localhost:80`에 접속해 보면, docker getting started 가 뜹니다. 
  - `image_name`: 그다음 사용한 image_name을 지정해줍니다. 저는 일단 `docker/getting-started:latest`를 사용해서 설치해봅니다. 뭔지 모르겠는데, 튜토리얼에 있으니까 그냥 해봅니다.
- 실행하려고 하는 container의 image(블루프린트)가 local에 설치되어 있지 않은 경우, docker-hub에서 자동으로 가져오게 됩니다. 제가 설치하는 `docker/getting-started`의 경우는 [docker hub - getting started](https://hub.docker.com/r/docker/getting-started)에서 가져오죠. 그 외에도 docker hub에는 여러 image들이 이미 준비되어 있습니다. 필요하다면 마음대로 가져와서 써도 될 것 같은데, 정확하게 쓰려면 license 부분도 보면 좋을 것 같네요.

```bash
$ docker run -d -p 80:80 docker/getting-started
Unable to find image 'docker/getting-started:latest' locally
latest: Pulling from docker/getting-started
... : Pull complete 
Digest: 
Status: Downloaded newer image for docker/getting-started:latest
```

- 잘 설치되어 있는지 보려면 `docker ps`를 사용해 봅니다. 네, docker getting-started를 image로 하는 docker container가 돌고 있네요. 

```bash
$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                               NAMES
...            docker/getting-started   "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp   recursing_sutherland
```

- 사실 뭐, tutorial에서 저 image를 사용해서 해보라고 해서 해보기는 했는데, 얘는 도통 뭐하는 놈인줄 모르겠네요. 
- 저는 지금까지, docker로 띄우는 image는 무조건 OS여야 한다고 생각했던 것 같습니다. 그런데, 얘는 OS가 아니라, 그냥 웹 어플리케이션 같이 느껴져요. 그렇다면, 반드시 OS 가 아니어도 실행이 된다는 건데, 아직은 이게 좀 낯설게 느껴져요. 
- 일단 제가 알고 있는 지식들에서 정리를 해보겠습니다. 제가 docker 명령어를 내리면, docker client에서 인식을 하고, 얘는 이걸 docker server로 돌려버리죠. 즉, 제가 요청한 docker 명령어는 사실 docker server에서 돌아간다는 이야기죠. 그런데, docker server에서 돌리는 container는 OS 가 아니라, web application입니다. 그렇다면, docker server 내에 혹은 그 위에 web application이 돌아가도록 해주는 OS와 비슷한 무엇이 있는게 아닐까? 하는 생각이 드네요. 일단은 제가 가지고 있는 얄팍한 지식으로 추론한 것은 이정도네요. 뭐 다음에 더 자세하게 알게 되겠죠.

## Dockerfile

- 우리가 선택한 image를 더 자세하게 알고 싶다면, 해당 image의 dockerfile을 확인하면 됩니다. [docker - getting started - Dockerfile](https://github.com/docker/getting-started/blob/master/Dockerfile)를 확인해 보면 대략 다음과 같은 내용이 들어 있죠.
- Dockerfile은 image에 대한 명세서(Specification)을 말합니다. "이 이미지는 어떤 프로그램으로 구성되어 있어요"라는 것을 말하는 거죠. Image와 Dockerfile은 같은 놈이다, 라고 생각해도 일단은 문제가 없을 거라고 생각합니다. 즉, 해당 image를 정확하게 알고 싶다면 우선 Dockerfile을 명확하게 이해하는 것이 필요하겠죠.
  - `FROM python:alpine`: 이미지 이름을 "python"으로 가지고, tag가 "alpine"으로 붙어 있는 image를 기본으로 가져갑니다. tag는 일종의 버전이라고 보시면 되요. alpine용 python을 기본 image로 가져와서, 얘를 고쳐서 사용한다, 정도로 이해하면 되겠네요.
  - `RUN command`: RUN command는 명령어를 직접 수행한다는 말이죠. 쉘 스크립트라고 이해해도 상관없을 것 같습니다. 
- 즉, 현재 Dockerfile에는 대략 다음의 내용들이 작성되어 있다고 할 수 있네요.
  - alpine용 python을 image로 가져와서 requirements.txt에 적혀 있는 python package들을 다 설치해주고,
  - 마찬가지로 alpine용 nodejs를 설치해주고, 쓸모없는 모듈들을 정리해주는 것처럼 보입니다.
  - 그다음 alpine용 python 환경에서, 뭔가를 실행해주고, 또 실행해주고 뭐 그러는 것처럼 보이네요 흠.
- alpine은 아주 경량화된 linux, 즉 OS인 셈이죠. 컨테이너에는 기본적으로 이런 아주 작은 크기의 OS 함께 설치되어 있는 것으로 보입니다. 즉, `python:alpine` 컨테이너를 구동시키게 되면, alpine OS와 그 위에서 운영되는 python이 함께 딸려오는 것처럼 보이네요. 그래요 그래야 말이 되죠.

```dockerfile
# Install the base requirements for the app.
# This stage is to support development.
FROM python:alpine AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run tests to validate app
FROM node:12-alpine AS app-base
RUN apk add --no-cache python g++ make
WORKDIR /app
COPY app/package.json app/yarn.lock ./
RUN yarn install
COPY app/spec ./spec
COPY app/src ./src
RUN yarn test

# Clear out the node_modules and create the zip
FROM app-base AS app-zip-creator
RUN rm -rf node_modules && \
    apk add zip && \
    zip -r /app.zip /app

# Dev-ready container - actual files will be mounted in
FROM base AS dev
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]

# Do the actual build of the mkdocs site
FROM base AS build
COPY . .
RUN mkdocs build

# Extract the static content from the build
# and use a nginx image to serve the content
FROM nginx:alpine
COPY --from=app-zip-creator /app.zip /usr/share/nginx/html/assets/app.zip
COPY --from=build /app/site /usr/share/nginx/html
```

## wrap-up

- 네, 갑작스럽지만 일단 마무리합니다. 오늘 해본 것과 요약은 대략 다음과 같습니다.
  - docker를 맥북에 매우 쉽게 설치 해봄.
  - 아주 기본적인 컨테이너를 실행해 보고, dockerfile이 어떻게 구성되어 있는지 역으로 추측해봄.
- 부족한 부분이 많지만, 적당히 괜찮은 시작인 것 같습니다. 다음에는, python container말고, ubuntu 컨테이너를 돌려 보도록 하겠습니다.

## Reference

- [Docker - official site](https://www.docker.com/products/docker-desktop)
