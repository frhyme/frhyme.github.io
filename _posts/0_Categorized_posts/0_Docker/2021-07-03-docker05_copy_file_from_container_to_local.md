---
title: docker - copy file from container to local
category: docker
tags: docker dockerfile container image 
---

## docker - copy file from container to local

- docker container를 사용하다 보면, docker container에 있는 특정 파일을 local로 가져와야 할 때가 있습니다. 그럴 때는 다음 명령어를 사용하면 됩니다.
- 아래 명령어는 `ubuntu_container2`의 `/root/test.sh/` 경로에 있는 파일을 local의 `a.sh`로 가져오는 명령을 수행하죠.

```bash
$ docker cp ubuntu_container2:/root/test.sh ~/a.sh
```
