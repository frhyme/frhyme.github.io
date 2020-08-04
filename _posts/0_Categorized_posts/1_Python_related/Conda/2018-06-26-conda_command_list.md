---
title: conda command를 정리해봅니다.
category: others
tags: python conda anaconda
---

## 오늘 또 파이썬을 갈아엎었습니다

- 사실 python은 매우 많은 종류의 라이브러리들을 쓸 수 있다는 측면에서 매우 강력하지만, 그만큼 라이브러리들의 버전관리, 충돌 문제들이 효과적으로 핸들링되지 못하여, 번거로운 일들이 많습니다.
- 오늘은 "jupyter notebook에서 GIF 만들기"를 해보려고 했는데, 하다보니 오류가 발생했고, 이를 해결하기 위해 새로운 라이브러리를 설치했더니 
    1) matrolib를 제대로 읽어오지 못하고, 
    2) jupyter notebook의 폰트들이 다 망가지는 문제점이 발생했습니다.
- 고민을 하다가, 기존에 있던 python과 conda를 다 날려버리고, 다시 설치해버리기로 했습니다. 냉정히 말해서 이게 제일 깔끔합니다.
- 그리고, 하는 김에 "저는 늘 같은 실수를 반복하는 종류의 인간"이기 때문에, 콘다에서 사용할 수 있는 다른 종류의 커맨드들을 좀 정리해보기로 했습니다. 물론. 정리해놓고 쓰지 않을 것이라는 것을 저는 잘 알고 있긴 합니다만.
- 특히 `pip`와 다른 점들이 있어서, 한번 기억해둘 필요성은 있는 것 같아요.

## Conda cheat sheet

```bash
conda info # 현재 콘다 버전 확인 
```

```bash
conda update conda #conda 업데이트
```

```bash
conda install PACKAGE PACKAGE #패키지 인스톨. 연달아서 여러 개 할 수도 있습니다. 
```

```bash
conda update PACKAGE #패키지 업데이트
```

```bash
conda update -all #가급적이면 쓰지마세요. 오류가 막 발생할 수 있습니다. 
```

```bash
conda uninstall PACKAGE #conda remove 와 같습니다. 
```

## managing environment 

- 저는 혼자 컴퓨터를 쓰니까 잘 안쓰지만, 파이썬 여러 버전을 쓰면서 테스트를 해야할 경우들이 생기잖아요. 아나콘다는 그걸 지원해줍니다. 대략 다음과 같은 기능들이 가능하긴 한데, 사실 쓰지는 않습니다 호호.
  1) 필요한 파이썬 환경을 생성하고
  2) 필요한 파이썬 환경을 비활성화하고
  3) 다시 활성화하고
  4) 삭제한다
- Docker를 사용해본 적이 있으신 분들은 익숙하실텐데, Conda는 필요에 따라 일종의 가상 파이썬 환경을 만들어서 띄워버리는 것이죠. 앞서 말한 것처럼, python은 라이브러리의 버전간 상호 충돌 문제가 의외로 빈번하게 일어납니다. 따라서, 어떤 stable한 상태에 들어갔다면, 현재의 상태를 그대로 기억해두고, 다음에 필요할때 가져와서 쓰는게 필요하거든요.
- 물론, 귀찮으므로 보통은 쓰지 않게 되기는 합니다 호호호.

## wrap-up

- conda를 설치하기는 했지만, `pip`도 여전히 쓸 수는 있습니다. 필요하면 다 쓰시고요. 
- 설치하는 것 자체는문제가 없는데, 몇 가지 라이브러리들(만약 그 라이브러리가 아나콘다에 있는 경우도 있으니까)을 지울 때는 조심하셔야 합니다. 
- 앞서 말한 바와 같이, 아나콘다는 파이썬 라이브러리간의 디펜던시를 해결하기 위한 일종의 잘 정리된 종합선물세트 같은 아이에요. 내부의 모든 라이브러리는 최대한 버그가 없는 상태로 잘 뭉쳐져 있는 것이죠. 
- 만약 사용자가, 특정한 라이브러리(어쩌면 scipy 같은 매우 중요한 라이브러리)를 마음대로 지운다면 충돌로 인해서 문제가 발생할 수도 있는 거니까요. 

## reference

- [Stackoverflow - How to uninstall Anaconda completely from macOS](https://stackoverflow.com/questions/42182706/how-to-uninstall-anaconda-completely-from-macos)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
