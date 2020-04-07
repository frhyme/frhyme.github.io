---
title: FastText에 document를 학습시킬 때, itertools.cycle 사용하기.
category: python-libs
tags: python python-libs fasttext itertools iterator generator
---

## Intro.

- 요즘 저는 FastText를 이용해서 단어의 의미를 학습시키고 있습니다. word2vec도 doc2vec도 있습니다만, fasttext의 경우는 vocabulary에 없는 단어들이라도 형태적인 유사성을 고려해서, 의미를 파악할 수 있다는 강점이 있죠. 따라서, 꽤 많은 경우 복합어에 대해서도 어느 정도 유추해준다는, 강점이 있습니다. 
- 다만, 슬프게도 제 맥북은 램이 4GB입니다. 좋은 컴퓨터를 가지신 분들은 좋겠지만, 저는 그래서, 일정 량을 넘치는 데이터의 경우 한번에 list로 변환하여 memory에 올릴 수 없어요. 즉, 저는, 한번에 올리지 못하고 generator로 변환해서 올려야 합니다. 

## Problem: couldn't train model by list, 

- 예를 들면 다음과 같습니다. generator를 만들어서 train시킵니다.

```python 
from gensim.models.fasttext import FastText

docs = ["i am a boy", "you are a girl"]
# 따라서, docs라는 corpus를 generator로 만들도록 하죠. 
# 즉, generator로 만들었으니까, 필요할 때 하나씩 읽는 형태로 변경된 것이죠.
docs = (s.lower().split(" ") for s in docs)
print(f"type of docs: {type(docs)}")

FTmodel = FastText(min_count=1, size=10)
# build_vocab: 우선 vocab을 만들고요. 
FTmodel.build_vocab(docs)
# train: 학습을 시켜줍니다.
FTmodel.train(sentences=docs, total_examples=FTmodel.corpus_count, epochs=10)
```

- 어떤가요? 잘 되는 것처럼 보이죠? 실제로 실행을 해보면, 아무 문제없이 잘 수행되는 것을 알 수 있습니다. 하지만, 실제로는 전혀 학습이 안되었죠.


### 왜 학습이 안되었는가? 

- 이는 결국 generator의 속성과 닿아 았습니다. generator는 한번 읽고 나면 비어 있습니다. 
- 다음 코드를 보시면, 처음에는 잘 출력해주지만, 그 다음에는 아무것도 없는 빈 리스트가 출력되죠.

```python
# generator를 만들었습니다. 
test_generator = (i for i in range(0, 3))
# 여기서는 잘 실행이 되지만, 
print(list(test_generator))
print("----------------")
# 여기서는 비어 있는 리스트가 그냥 출력됩니다.
print(list(test_generator))
```

- 두번째 출력할때는 아무것도 출력되지 않ㅎ습니다. 즉, 비어있는 generator에서 그냥 긁어온 것이니까요.

```
[0, 1, 2]
----------------
[]
```

## Solution: 매번 새로운 generator를 넘긴다.

- 따라서, 매번 새로운 generator를 생성해서 넘겨주는 식으로 진행해야 합니다. 
- 그리고 매번 새로 generator를 넘겨서 학습해준다고 생각해야 하죠.

```python
def RETURN_docs_generator():
    # 새로운 generator를 생성해서 RETURN해준다.
    docs = ["i am a boy", "you are a girl"]
    docs = ( s.lower().split(" ") for s in docs )
    return docs

FTmodel = FastText(min_count=1, size=10)
FTmodel.build_vocab(RETURN_docs_generator())
print("buile vocab done")
for epoch in range(0, 10):
    # epochs를 1로 설정해서 새롭게 매번 넘겨준다고 생각하고 접근해야함.
    FTmodel.train(sentences=RETURN_docs_generator(), total_examples=FTmodel.corpus_count, epochs=1)
    print(f"-- EPOCH: {epoch}")
print("== complete")
```

- 혹은 generator를 반복하는 `itertools.repeat`과 `itertools.chain.from_iterable`를 사용해서 한번에 더 많은 자료를 넘겨서 학습시킬 수도 있습니다.
- 즉, corpus 자체를 

```python
def RETURN_docs_generator():
    # 새로운 generator를 생성해서 RETURN해준다.
    docs = ["i am a boy", "you are a girl"]
    docs = ( s.lower().split(" ") for s in docs )
    return docs

FTmodel = FastText(min_count=1, size=10)
FTmodel.build_vocab(RETURN_docs_generator())
print("buile vocab done")
FTmodel.train(
    sentences=itertools.chain.from_iterable(itertools.repeat(RETURN_docs_generator(), 3)), 
    total_examples=FTmodel.corpus_count, 
    epochs=1)
print(f"-- EPOCH: {epoch}")
print("== complete")
```