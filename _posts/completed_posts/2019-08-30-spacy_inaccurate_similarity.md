---
title: spacy 정확하지 않은 similarity 
category: python-libs
tags: python python-libs spacy nlp similarity 
---

## 단어간 유사성이 이상하게 되어요!

- 저는 파이썬 자연어처리 라이브러리인 spacy를 사용해서, 단어간 유사성을 비교할때가 있습니다. 
- 그런데 말이죵, 이상하게 유사성이 제대로 안 나올 때가 많습니다. 
- 예를 들어서 아래 코드를 실행하면, 

```python
import spacy
spacy_nlp = spacy.load('en_core_web_lg')

words_lst =['dog', 'cat', 'banana']
for a in words_lst:
    for b in words_lst:
        spacy_a = spacy_nlp(a)
        spacy_b = spacy_nlp(b)
        spacy_sim = spacy_a.similarity(spacy_b)
        print(f"{a}, {b} ==> spacy nlp: {spacy_sim}")
```

- 다음처럼, 정확하게 값이 나오지 않습니다. 

```
dog, dog ==> spacy nlp: 1.0
dog, cat ==> spacy nlp: 0.0
dog, banana ==> spacy nlp: -7.82873902177027e+17
cat, dog ==> spacy nlp: 0.0
cat, cat ==> spacy nlp: 1.0
cat, banana ==> spacy nlp: -8.24222188835327e+17
banana, dog ==> spacy nlp: -7.82873902177027e+17
banana, cat ==> spacy nlp: -8.24222188835327e+17
banana, banana ==> spacy nlp: 1.0
```

- 이게 이상해서, [제가 스택오버플로우에 답을 올린 적](https://stackoverflow.com/questions/52388291/spacy-similarity-method-doesnt-not-work-correctly)도 있는데, 아무도 정확한 이유를 알려주지 못했죠. 

## 답은 numpy야 바보야

- 답은 numpy에 있었습니다. 
- 되게 간단하게, 그냥 `import numpy as np`만 추가하면 정확히 됩니다.

```python
import numpy as np # added just one line 

import spacy
spacy_nlp = spacy.load('en_core_web_lg')

words_lst =['dog', 'cat', 'banana']
for a in words_lst:
    for b in words_lst:
        spacy_a = spacy_nlp(a)
        spacy_b = spacy_nlp(b)
        spacy_sim = spacy_a.similarity(spacy_b)
        print(f"{a}, {b} ==> spacy nlp: {spacy_sim}")
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
```

## wrap-up

- 아마도 의존성의 문제때문인 것으로 막연하게 생각됩니다만, 이상하죠. 
- 아무튼 해결이 되었으니 다행이죠 하하하하. 이전에는 그냥 안되길래 왜 안되나 싶었는데 매우 단순한 이유였습니다.

