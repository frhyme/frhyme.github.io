---
title: Graph-Embedding lib를 설치해봅시다. 
category: python-libs
tags: github python-libs graph_embedding
---

## install from github

- 이전에 제가 SDNE를 사용하기 위해서 썼던 라이브러리는 [이 아이](https://github.com/xiaohan2012/sdne-keras) 입니다. 
- 좋은 라이브러리이기는 한데, SDNE밖에 없다는 단점이 있습니다(뭐, 사실 이걸 굳이 단점으로 할수 있나 싶기는 한데 아무튼)
- 그래서 찾아보니까, [깃헙에서 star의 수가 더 많고, 그래프 임베딩에 관한 다른 라이브러리들도 함께 통합되어 있는 리퍼지토리를 찾았습니다](https://github.com/shenweichen/GraphEmbedding)
- 또, 이 아이는 깃헙에서 클론한 다음 바로 설치할 수 있는 것 같아서, 직접 설치해서 사용해보려고 합니다. 

## clone and install

- 우선 clone 해옵니다.

```
git clone <repositor_url>
```

- 다른 거 뭐 설정하지 않고 그대로 clone했기 때문에 `GraphEmbedding`이라는 이름의 폴더가 생성되었습니다.
- 이제 설치를 해줍니다.

```
python setup.py install 
```

- warning이 하나 뜨기는 했는데, 뭐 설치되는것 같으니 문제가 없는가보죠 하하하. 
- 이제 잘 되는지 보려고 예제폴더에 들어가서 간단한 파일을 실행시켜줍니다.


```
cd examples
python 
```

- 다음과 같은 오류가 발생합니다. 뭐 뻔하죠. 텐서플로우랑 다른 라이브러리랑 의존성이 제대로 해결되지 않은 것이겠쬬. 


```
AttributeError: module 'tensorflow.python.pywrap_tensorflow' has no attribute 'TFE_DEVICE_PLACEMENT_EXPLICIT'
```

- 그래서, 다시 지우기로 결심합니다. 
    - 설치한 파일들을 기록하고, 
    - 텍스트파일에서 다 읽어서 하나씩 지워줍니다.

```
python setup.py install --record uninstall.txt
cat uninstall.txt | xargs rm -rf
```

## wrap-up

- 귀찮네요 하하핫. 좀 더 편하게 쓸 수 있을줄 알았는데 하하하. 
- 그냥 지우기로 했습니다 하하하 


## reference

- <https://stackoverflow.com/questions/1550226/python-setup-py-uninstall>