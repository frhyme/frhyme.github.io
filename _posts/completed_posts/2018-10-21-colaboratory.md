---
title: google colaboratory 사용하기 
category: python-libs
tags: python google colaboratory jupyter-notebook jupyter-lab python-libs
---

## intro 

- 저는 매우 오랫동안 jupyter notebook을 사용해 왔습니다(정확히는 지금은 jupyter-lab을 사용하고 있기는 한데). 
- 아무래도 코딩을 주기적으로 체크하면서 코딩을 하다보니까, 또 그래야 하는 일이기도 하고, 보통 jupyter notebook을 쓰는 것이 더 편합니다. 
- 특히 그냥 shift+enter 를 누르면 자동으로 해당 셀이 실행되니까, 편하기도 하구요. 
- 아무튼, 그러던 중에, 한 가지 크리티컬한 문제점을 발견했습니다. 

### how to make versions of code

- 일반적으로 프로젝트 단위에서 코드를 관리할 때는 git을 사용합니다. 
- git은 일종의 change management라고도 볼 수 있습니다. 
    - 제가 어떤 시점(A)에 코드를 작성하고 저장합니다. 
    - 이후 제가 어떤 시점(B)에 코드를 작성하고 저장합니다. 
    - 그런데 B를 수행하다가 문제가 생겨서, A로 돌아가고 싶으면 돌아가면 됩니다. git에서 이미 다 처리를 해놨으니까요. 
- 정확히는 조금 다르지만, 대략 이렇습니다. 

- 그런데 이게 jupyter notebook에서는 처리하는 것이 약간 어려운 것이, jupyter notebook은 코드와 아웃풋이 함께 관리되는 XML 문서이기 때문이죠. 예를 들어서, 해당 노트북에서 아웃풋을 없애면, 해당 XML 파일은 새롭게 작성된 파일처럼 여겨지지만, 사실은 같은 파일입니다. 말이 좀 이상한데 아무튼 잘 안되요 하하하핫. 

- 그래서 고민하다가, 구글 드라이브에서 처럼 저장에 대한 기록을 남겨주면 좀 편할 것 같다는 생각을 했죠.

## google - colaboratory 

- 그러다가, [colaboratory](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)를 발견했습니다.
- 몇 가지 주요한 피쳐를 말하자면 대략 다음과 같습니다. 
    - 구글 드라이브 내에서 운영되기 때문에, 파일 관리를 잘할 수 있다. 
        - jupyter notebook의 경우 웹브라우저 위에서 돌아가는데, 실수로 돌아가기를 누른다거나, 실수로 코드를 조금 지웠을 때, 이를 복구하는 작업이 좀 어렵습니다. 되는데, 뭐라고 할까, 엄밀하게 관리해주지 않는다, 라고 할까요. 
    - OS와 독립적으로 완전히 클라우드 내에서 돌아간다. 
        - 제가 로컬 컴퓨터에서 쥬피터 노트북을 구현하지 않아도 잘 돌아간다는 이야기죠. 즉, 구글 드라이브에서 실행하는 것이라면, 윈도우에서 돌리던, 맥에서 돌리던, 어디서 돌리던 문제가 없다는 이야기입니다. 
        - 즉, 로컬이 아니라(필요하면 로컬로 세팅할 수는 있지만), 도커를 이용해서 완전히 클라우드에서 돌아갑니다. 
        - 저의 경우 연구실 컴퓨터는 윈도우고, 저는 보통 맥북을 써서 이 충돌문제가 좀 있었는데, 이제 모두 웹브라우저 상에서만 돌아간다면, 이 걱정을 좀 덜 해도 되겠죠. 
    - 쥬피터 노트북과 완전히 동일하다(고 생각해도 된다)
    - stable한 많은 라이브러리들이 이미 설치되어 있다. 

- 말이 길었지만, 개 좋다는 이야기죠. 저는 이제 jupyter notebook도 지우고 아나콘다까지도 지우고, 다 구글에서 돌려버리고 싶은 마음까지도 있습니다. 

## wrap-up

- 상황에 따라서 GPU도 사용할 수 있다는 것 같은데, 그건 제가 나중에 한번 체크해보도록 하겠습니다. 
- 저는 일단은 그게 필요가 없어서요. 

## reference

- <https://brunch.co.kr/@jayden-factory/11>
- <https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d>