---
title: np.random.seed in jupyter notebook
category: python-lib
tags: python python-lib numpy jupyter-notebook random
---

## 인트로

- 저는 jupyter notebook에서 코딩을 합니다. 경우에 따라서, jupyter notebook이 불편하다고 느끼는 사람들도 있어요. 전통적인 IDE들과는 다르게, 브라우저에서 돌아가는 것도 그렇고, cell별로 코딩을 하는데, cell들간의 namespace는 공유되고(따라서 막 코딩하면서 코드 라인이 길어지면 매우 힘들어지기도 합니다) 뭐 그런것들이 낯설수도 있습니다. 
- 뭐 그래도 IDE에서는 실행결과(특히 그림)를 파악하는 것이 조금 어려운 반면, 얘는 그게 매우 쉬워요. 그래서 저는 씁니다. 

## random.seed

- 사족이 길었습니다만. 실제로 좋아지는 지 정확히 보려면 경우에 따라서, 아래 코드로 random을 고정해두는 것이 필요하잖아요. 

```python
np.random.seed(42)
```

- 문제 아닌 문제는 이 코드는 cell별로 따로 작동한다는 것이죠. 그래서 가능하면 해당 값을 상수로 처리하고, 셀에서 random을 사용할 경우에는 무조건 붙여두는 것이 좋습니다. 

```python
RANDOM_SEED = 20
np.random.seed(RANDOM_SEED)
```

## with simpy

- simpy를 쓸 때는 함수 내에 선언해야 할 때도 있습니다. 참고하세요. 