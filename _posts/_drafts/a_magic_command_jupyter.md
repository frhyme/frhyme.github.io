---
title: jupyter notebook에서 유용한 몇가지 magic command
category: python-lib
tags: magic-commmand jupyter-notebook python python-lib 
---
## jupyter notebook의 magic command를 정리합니다. 

- 사용할 수 있는 모든 매직 커맨드를 출력해줍니다. 일단 이것만 알아도 필요할때 보면서 해도 되죠. 

## 기본 개념 몇 가지 

- `%`의 경우는 line command 
- `%%`의 경우는 cell command

```jupyter 
%lsmagic 
```

- cell의 코드를 python file로 바로 작성해줍니다. 

```jupyter
%%writefile
```

- 시간 측정

```jupyter
%timeit
```

## reference

- <https://www.slideshare.net/dahlmoon/jupyter-notebok-20160815>