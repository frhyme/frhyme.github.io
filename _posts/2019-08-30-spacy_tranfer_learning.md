---
title: spacy 에 새로운 단어와 벡터를 넣어줍시다. 
category: python-libs
tags: python python-libs spacy nlp similarity transfer-learning
---

## 기존 학습된 벡터들에 새로운 벡터들을 넣어주고 싶어요. 

- 이미 spacy에는 꽤 잘 작동하는 워드투벡이 있습니다. 간단한 처리를 할때는 그냥 이걸 사용해주는 것이 훨씬 좋죠. 
- 그런데, 없는 경우들이 있씁니다. 저는 특수한 분야의 텍스트를 다루는데, spacy에서 다루는 워드투벡에는 일반적인 워드들만 있어서, 제가 원하는 유사도 측정이 정확하게 되지 않을때가 많습니다. 
- 따라서, 이를 위해서 일종의 전이학습(transfer-learning)이 필요할 때가 있죠. 
- 물론 여기서는 정확히 transfer-learning을 한다기보다는, 약간 vocabulariry와 vector를 업데이트해준다, 라고 보시는 것이 좀더 좋습니다. 여기서 vocab은 당연히 복합어가 아닌 하나의 단어여야 하고요. 

## do it. 

- 아래에서는 dog라는 단어에 아무 벡터가 지정해줍니다. 단 여기서도 해당 벡터의 길이는 300차원이어야 합니다. 
- 결과를 보면, 당연히 유사도가 이전과 다르게 나오는 것을 알 수 있죠.

```python
# numpy의 경우 spacy간에 word간의 semantic similarity를 계산할때 필요함. 
# 없어도 계산은 되는데, 값이 매우 이상하게 나옴
import numpy

# 라이브러리를 가져오고.
import spacy
spacy_nlp = spacy.load('en_core_web_lg')

# 간단히 값들의 유사도를 비교해봄.
words_lst =['dog', 'cat', 'banana']
for a in words_lst:
    for b in words_lst:
        spacy_a = spacy_nlp(a)
        spacy_b = spacy_nlp(b)
        spacy_sim = spacy_a.similarity(spacy_b)
        print(f"{a}, {b} ==> spacy nlp: {spacy_sim}")
print("=="*20)

# 지금까지는 en_core_web_lg에 이미 학습된 벡터를 가지고 진행한 것임. 
# 그러나, 만약 우리가 원하는 워드와 거기에 해당하는 벡터 값이 없는 경우가 있을 수 있음. 
# 따라서, 특수한 vocab에 대해서 추가로 넣어주는 것이 필요함. 

# 값을 워드와 벡터(300차원)으로 딕셔너리로 구성하고, 
new_vector_data_dict = {
    'dog': numpy.random.uniform(-1, 1, (300,))
}

# 아래와 같은 방식으로, vocab에 하나씩 값을 업데이트해줌.
for word, vector in new_vector_data_dict.items():
    spacy_nlp.vocab.set_vector(word, vector)

for a in words_lst:
    for b in words_lst:
        spacy_a = spacy_nlp(a)
        spacy_b = spacy_nlp(b)
        spacy_sim = spacy_a.similarity(spacy_b)
        print(f"{a}, {b} ==> spacy nlp: {spacy_sim}")
    
print("=="*20)
```

```
dog, dog ==> spacy nlp: 1.0
dog, cat ==> spacy nlp: 0.8016855517329495
dog, banana ==> spacy nlp: 0.24327647954195658
cat, dog ==> spacy nlp: 0.8016855517329495
cat, cat ==> spacy nlp: 1.0
cat, banana ==> spacy nlp: 0.28154364860188125
banana, dog ==> spacy nlp: 0.24327647954195658
banana, cat ==> spacy nlp: 0.28154364860188125
banana, banana ==> spacy nlp: 1.0
========================================
dog, dog ==> spacy nlp: 1.0
dog, cat ==> spacy nlp: 0.06367532184777439
dog, banana ==> spacy nlp: -0.010021774106347485
cat, dog ==> spacy nlp: 0.06367532184777439
cat, cat ==> spacy nlp: 1.0
cat, banana ==> spacy nlp: 0.28154364860188125
banana, dog ==> spacy nlp: -0.010021774106347485
banana, cat ==> spacy nlp: 0.28154364860188125
banana, banana ==> spacy nlp: 1.0
========================================
```

## wrap-up

- 즉 이 방법을 사용해서 모든 단어는 아니고, 몇몇 특수한 단어들, 특히 기존 보캡에 없는 단어들을 중심으로 학습을 시켜서 넣어주면, 일반성+특수성을 모두 고려하게 되지 않을까? 하고 생각해봅니다. 하하하하