---
title: spacy - Named Entity Recognition 사용하기 
category: python-libs
tags: spacy python python-libs ner nlp 
---

## intro 

- [spacy]() 에서는 간단한 Named Entity Recognition을 제공해줍니다. 
- [Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)

- 예를 들어서 다음과 같은 문장이 있다고 할때 

> Jim bought 300 shares of Acme Corp. in 2006.

- 문장의 각 요소를 다음처럼 인식해서 알려주는 것을 말합니다. 

> [Jim]Person bought 300 shares of [Acme Corp.]Organization in [2006]Time.

- 어떻게 할 수 있느냐? 라고 물어본다면, 모릅니다. 나중에 알아볼게요. 저는 우선은, 각 entity가 무엇인지를 인식하는 것만을 사용해보려고 합니다. 

## using spacy 

- spacy를 사용해서 NER을 해보려고 합니다(저는 colaboratory에서 사용했습니다)

```python
!pip install spacy
import spacy 
!python -m spacy download en_core_web_lg

nlp = spacy.load('en_core_web_lg')
"""
- 여기서 먼저 중요한 것은, 아래를 사용하면 안됩니다. 
- 아래 라이브러리의 경우는 word2vector만 가져오는 라이브러리라서, 
- 아래의 라이브러리를 사용할 경우에는 similarity만 사용할 수 있고, 다른 것들은 사용할 수 없습니다. 
- 따라서 NER을 사용하기 위해서는 위의 라이브러리를 가져오시면 됩니다. 
nlp = spacy.load('en_vectors_web_lg')
"""

doc = nlp("Google Apple $ 5.1 billion Wednesday Korea America USA baseball")
for e in doc:
    if e.ent_type_ != "":
        print(f"{e} ==> {e.ent_type_}")
```

- 아래에서 보시는 것처럼, 각각의 명사들이 어떤 타입인지를 알려줍니다. 

```
Google ==> ORG
$ ==> MONEY
5.1 ==> MONEY
billion ==> MONEY
Wednesday ==> DATE
Korea ==> GPE
America ==> ORG
USA ==> ORG
```

## wrap-up

- 뭐, 너무 간단해서 더 추가할게 없네요 하하핫. 