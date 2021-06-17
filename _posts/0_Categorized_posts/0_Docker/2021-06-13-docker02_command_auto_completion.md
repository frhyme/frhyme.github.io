---
title: docker - command auto completion
category: docker
tags: docker command bash zsh zshrc
---

## docker - command auto completion

- docker에서 command를 사용할 때, tab completion이 먹히지 않습니다. 가령, `docker ru`을 누르고 tab을 누르면, `docker run`으로 될 수 있어야 하는데, 뜨지 않죠.
- 뭐, `run`정도야 문제가 아닌데, `docker rmi`를 사용할 때는 난수화되어 있는 image_id 값을 하나하나 입력해야 한다는 번거로움이 있습니다. 그래서, docker command에 대해서 tab completion이 가능하도록 설정해보려고 합니다.

## with zsh

- [docker - command completion](https://docs.docker.com/compose/completion/)에 자세한 내용이 나와 있습니다.
- 저는 zsh를 사용하기 때문에, 그냥 `.zshrc` 파일에 아래 내용을 작성하고 나면 끝나네요. "..."에는 사용하는 다른 plugin들의 이름이 작성되어 있으면 됩니다.

```plaintext
plugins=(... docker docker-compose)
```

## Reference

- [docker - command completion](https://docs.docker.com/compose/completion/)
