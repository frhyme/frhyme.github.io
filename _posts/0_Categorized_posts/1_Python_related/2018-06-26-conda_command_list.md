---
title: conda command 정리 
category: others
tags: python conda
---

## 오늘 또 파이썬을 갈아엎었습니다. 

- 오늘은 "쥬피터 노트북에서 gif를 만들기"를 해보려고 했는데, 하다보니까 오류가 발생했고, 새로운 라이브러리를 설치했더니,    
    - matplotlib를 제대로 읽어오지 못하고, 
    - jupyter notebook의 폰트들이 이상하게 변경되는 등의 문제가 있었습니다. 
- 화가 나서 기존에 있던 파이썬과 콘다를 다 날려버리고, 콘다를 다시 설치하기로 했씁니다. 이게 제일 깔끔해요. 
- 하는 김에, 저는 같은 실수를 반복하는 종류의 인간이기 때문에, 콘다에서 사용할 수 있는 커맨드들을 좀 정리해보기로 했습니다.
- 특히, pip 와 미묘하게 다른 부분이 있어서 이참에 정리를 해두는 것이 좋을 것 같아요. 

## conda cheat sheet

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

- 저는 혼자 컴퓨터를 쓰니까 잘 안쓰지만, 파이썬 여러 버전을 쓰면서 테스트를 해야할 경우들이 생기잖아요. 
- 아나콘다는 그걸 지원해줍니다. 대략 다음 기능들이 있는데. 
    - 필요한 환경을 생성하고
    - 필요한 환경을 활성화하고
    - 쓰지 않을때는 비활성화하고
    - 필요없으면 지웁니다. 
- 사실 저는 굳이 쓰지 않습니다. 나중에 필요해지면 쓰도록 하겠습니다 하하하핫


## wrap-up

- conda를 설치하기는 했지만, `pip`도 여전히 쓸 수는 있습니다. 필요하면 다 쓰시고요. 
- 설치한는 것은 문제가 없는데, 몇 가지 라이브러리들(만약 그 라이브러리가 아나콘다에 있는 경우도 있으니까)을 지울 때는 조심하셔야 합니다. 
- 앞서 말한 바와 같이, 아나콘다는 파이썬 라이브러리간의 디펜던시를 해결하기 위한 일종의 잘 정리된 종합선물세트 같은 아이에요. 내부의 모든 라이브러리는 최대한 버그가 없는 상태로 잘 뭉쳐져 있는 것이죠. 
- 만약 사용자가, 특정한 라이브러리(어쩌면 scipy 같은 매우 중요한 라이브러리)를 마음대로 지운다면 충돌로 인해서 문제가 발생할 수도 있는 거니까요. 

## reference

- <https://stackoverflow.com/questions/42182706/how-to-uninstall-anaconda-completely-from-macos>
- <https://conda.io/docs/_downloads/conda-cheatsheet.pdf>

