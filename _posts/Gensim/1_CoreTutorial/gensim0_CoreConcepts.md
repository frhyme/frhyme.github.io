---
title: gensim - Core Tutorial - Core Concept
category: python-libs
tags: python python-libs gensim nlp similarity tf-idf
---

## 2-line summary 

- gensim의 기본 개념인 Document, corpus, vector, model에 대해서 정리하였습니다. 
- gensim은 "같은 document일지라도 corpus가 다르면 다른 형태로 vector화된다는 것"을 가정합니다. 따라서, 많은 경우 기본 argument가 bow_corpus를 필요로 하죠.

## intro 

- [gensim - Core Tutorial - Core Concept](https://radimrehurek.com/gensim/auto_examples/)의 내용을 공부하면서 정리하였습니다. 
- 이 챕터에서는 gensim을 구성하는 다음 4가지 핵심 요소에 대해서 공부합니다. 
    1) `Document`: 그냥 'text'
    2) `Corpus`: document의 집합 
    3) `Vector`: 수학적으로 편리하게 사용하기 위해서 document를 수치적으로 표현한 것.
    4) `Model`: vector를 다른 '것'으로 변환해주는 알고리즘(가령, Document의 Vector를 입력받아서, label로 변환해주는 것.)

## Document

- Gensim에서 `document`는 text sequence를 말합니다(기본적으로는 그냥 string이라고 생각해도 상관없다는 말이죠). Document는 상당히 많은 범위를 말하는데, 140자의 tweet, 한 문단, journal article abstract, book까지 모든 "text sequence"를 말합니다. 
- 즉, 짧든 길든, 단일하게 구성된 그냥 string이다, 라고 생각해도 상관없다는 이야기죠. 
- 물론 이렇게만 쓰면 약간 "재귀적으로 생각하게 되긴 합니다. "야 그러면 document를 잘라도 또 document가 된다는 이야기냐?"라고 말할 수 있죠. 네, 일단은 그렇다고 봐야 할 것 같네요. 

```python
document = "Any text sequence"
```

## Corpus 

- `Corpus`는 Document의 집합을 말합니다. Gensim에서 Corpora는 두 가지 역할을 담당하는데요, 
    1) Model을 학습(training)하기 위한 input. 모델은 corpus를 사용해서 내부 parameter를 업데이트함. 또한, 이 과정에서 gensim은 unsupervised learning에 집중하고 있음. 
    2) 이미 학습된 model을 사용해서, 새로운 document에 대해서 

```python
document1 = "I am a boy"
document2 = "You are a girl"
text_corpus = [document1, document2]
```

- corpus는 사실 무엇이든 될 수 있는데요, 이 때, 의미없는 keyword은 제외하게 됩니다. 가령 "the", "a", "for"와 같은 단어들은 언어생활에서는 매우 중요하지만, 오히려 너무 빈번하게 나오므로 별 의미가 없는 것이죠. 
- 따라서, corpus를 구성하는 document들에 대해서 이와 같은 무의미한 키워드들을 제외해주고, 전체 corpus에서 단 1번 등장한 키워드(min_count가 1)들도 모두 제외해줍니다.
- 다만, 여기서는 token을 단일한 워드에 대해서만 구성해줬습니다. 다시 말하자면, "Human machine"이라는 단어에 대해서는 무시하고, "Human"과 "Machine"과 같이 분리시켜서 이해하고 있다는 것이죠. 뭐, word2vec으로 표현할 경우에는 별 문제가 없을 것 같기는 합니다만(충분히 학습되었다고 가정한다면)

```python
from collections import Counter
import itertools
import pprint 

text_corpus = [
    "Human machine interface for lab abc computer applications",
]

text_corpus = [text.lower().split() for text in text_corpus]

# document 별로 존재하는 word에 대해서 
# stoplist(너무 빈번하거나, 너무 희귀하건)를 만들어서 제외함.
word_counter = Counter(itertools.chain.from_iterable(text_corpus))
stoplist = set('for a of the and to in'.split(' ')) 
min_count = 1
stoplist.update(set([w for w, f in word_counter.items() if f<=min_count]))
# Lowercase each document, split it by white space and filter out stopwords
texts = []
for document in text_corpus: 
    word_in_document = filter(lambda word: True if word not in stoplist else False, document)
    texts.append(list(word_in_document))

pprint.pprint(texts)
```

## Vector representation of Document.

- 주어진 corpus에 잠재되어 있는 구조(혹은 의미)를 추론하려면 우선 document를 수학적으로 표현하는 것이 필요합니다. 굳이 word2vec과 같은 것을 사용하지 않아도, 그냥 비교적 단순한 feature들, 가령 "몇 개의 문단으로 구성되어 있는가?", "단어는 몇 개 존재하는가?"와 같은 다양한 방법으로 각 corpus 혹은 document를 수치화할 수 있죠. 

### Bag-of-Words. 

- 가장 흔히 쓰는 방법으로는, "Bag-of-word"라고 부르는 "word가 몇 개나 들어있나"를 feature로 모델링해서 사용하기도 합니다.또한, 이를 그냥 Binary로(들어있으면 1 아니면 0)으로 할 것인가, frequency를 그대로 쓸 것인지, word token을 길이가 1인 걸로 할 것인지, 1을 넘는 것들로 할 것인지 등 여러 방법이 혼합되어 있게 되죠.
- 일단, 충분히 큰 텍스트들에 대해서, 비슷한 단어 조합들로 구성되어 있자면, 그 두 문단은 비슷할 가능성이 높습니다. 물론 어느 정도 한계는 있겠지만, 일단 이 가정에 근거해서 문제를 풀어 나가는 것이죠.
- 추가로, Bag-of-word를 사용해서 Vector로 표현한다면, 해당 matrix에는 0인 값이 매우 많이 존재하게 됩니다. 이런 경우 sparse-matrix를 사용해서 메모리의 효율성을 높이죠.
- 이 글에서는 모든 document에 2번 이상 등장한 워드를 기존 word vocabulary로 설정하여, 각 document를 12-dimensional vector로 표현하였습니다.
- 다만, 다시 말하지만, 이 모든 것은 결국 "Bag-of-word가 해당 Document의 특성을 그대로 반영한다"라는 가정에 근거하죠. 


- 이를 위해 gensim에서는 우선, `gensim.corpora.Dictionary`를 사용하여, 기존의 corpus에서 등장한 token들에 대해서 id를 부여해줍니다. 사실, 그냥 string을 token으로 관리해도 되지만, 이렇게 할 경우에는 메모리에 과부하가 걸릴 수 있죠. 
- 따라서, 각각 integer로 구성된 id를 부여합니다. 

```python
# 만들어진 processed_corpus에 대해서 Dictionary로 관리해줌
dictionary = gensim.corpora.Dictionary(processed_corpus)
print(f"== dictionary:")
print(dictionary)
print("--"*10)

# dictionary의 구성된 token들의 id가 무엇인지 알 수 있음
# 우선 token을 매번 string으로 관리해도 되지만, 이렇게 할경우 메모리에서 발생하는 용량에 부하가 걸릴 수 있음
# 따라서, 보통은 token에 대해서 integer로 id를 매겨서 관리함. 
# 이후 다른 new_doc에 대해서 bag-of-word의 형태로 표현하려고 할때 
# (token, frequency)가 아니라, (token_id, frequency)의 형태로 표현됨.
print("== dictionary.token2id")
print(dictionary.token2id)
print("--"*10)

new_doc = "Human Human computer interaction"
new_doc_words = [w.strip() for w in new_doc.lower().split(" ")]
# new_doc_words에 대한 bag-of-word 표현. 
new_vec = dictionary.doc2bow(new_doc_words)
print(f"new_doc: {new_doc}")
print(new_doc_words)
print(new_vec)
# method가 있지만 lazy함. dictionary.token2id를 사용해서 reverse mapping
id2token_dict = {id: token for token, id in dictionary.token2id.items()}
print([ (id2token_dict[token_id], f) for token_id, f in new_vec])
```

```
== dictionary:
Dictionary(12 unique tokens: ['computer', 'human', 'interface', 'response', 'survey']...)
--------------------
== dictionary.token2id
{'computer': 0, 'human': 1, 'interface': 2, 'response': 3, 'survey': 4, 'system': 5, 'time': 6, 'user': 7, 'eps': 8, 'trees': 9, 'graph': 10, 'minors': 11}
--------------------
new_doc: Human Human computer interaction
['human', 'human', 'computer', 'interaction']
[(0, 1), (1, 2)]
[('computer', 1), ('human', 2)]
```



## Model 

- 자, 이제 우리는 Bag-of-Word라고 하는 아주 간단한 방식으로 document들을 vector로 표현했습니다. 그리고, 이 vector를 input으로 사용해서, 다른 무엇을 output으로 만들어낼 수 있겠죠. 흔히 말하는 "label을 예측한다"와 같은 것, 그를 위한 모델을 세우는 부분이 여기서 설명되죠. "model"이라는 것은 사실, "어떤 vector space에 속한 vector를 다른 vector space에 속한 vector로 변환해주는 것"이라고 생각하는 것이 가장 명쾌합니다(물론, 이렇게 말하면, data-preprocessing도 일종의 model로 해석될 수 있지만, 여기서는 넓은 의미에서 그렇게 생각하는 것 같네요)

### TF-IDF representation 

- 여기서는 가장 간단한 예로, tf-idf model의 예를 듭니다. bag-of-word와 유사하나, tf-idf는 "다른 문서에서도 공통적으로 많이 등장하는 단어들의 경우 그 weight를 줄이고, 다른 문서에서 잘 안 등장하지만, 이 문서에서만 등장하는 독특한 특성을 잡아내는 모델"을 말합니다. 즉, 단어의 희소성을 반영하는 것이죠.
- 사실, 엄밀히 따지면, `Tfidf`가 모델에 속해야 하는지는 잘 모르겠습니다. 이는 오히려, vector representation에 속하는 것이 아닐까, 싶습니다만. 여기서는 training, predcition을 구분한 것이죠. `bow_corpus`를 train_set으로 사용해서 모델을 학습하고, 그 (이미 학습된) 결과를 활용해서 새로운 document를 vector로 표현해주기 때문에, 여기서는 tf-idf 또한 하나의 모델이다, 라고 말한 것 같네요.
- 다만, 매우 당연하게도, `dictionary`에 존재하지 않는 단어들을 넣으면 vector로 변환해주지 못합니다.

```python
# train the model
tfidf_model = gensim.models.TfidfModel(bow_corpus)
# transform the "system minors" string
words = "system minors".lower().split()
print(tfidf_model[dictionary.doc2bow(words)])
# dictionary의 token에 해당 단어들이 없을 경우에는 계산이 되지 않음.
words = "A B".lower().split()
print(tfidf_model[dictionary.doc2bow(words)])
```

```
[(5, 0.5898341626740045), (11, 0.8075244024440723)]
[]
```


### Similarity 

- TF-IDF로 표현된 document에 대해서, 아래 방법을 사용해서 similarity를 계산할 수도 있습니다.
- 조금 흥미로운 것은, 보통 similarity를 계산할 때는 그냥 `similarity(vector_A, vector_B)`의 형식으로 계산합니다. 다른 python library들에서도 대부분 그러했던 것 같아요. 
- 그러나, 여기서는, `corpus`를 bow_corpus로 받아서, 관리하고, 그 다음에 "bow_corpus의 모든 document들 전체에 대해서 유사도(similarity)를 측정"하여 그 결과를 보여줍니다. 다만, 이 때 similarity가 `A`, `B`간의 vector만을 고려하는 것이 아니라, 전체 분포에 기반, 혹은 bow_corpus의 모든 document의 관계를 고려하여, 유별나게 더 유사하다, 는 것을 담고 있는지에 대해서는 체크하는 것이 필요할 것 같습니다. 사실 그렇지 않다면 굳이 bow_corpus를 한번에 넘겨주는 식으로 개발하지 않지 않았을까? 하는 것이 제 개인적인 생각입니다. 

```python
similarity_model = gensim.similarities.SparseMatrixSimilarity(
    corpus=tfidf_model[bow_corpus], num_features=12
)

query_document = 'system engineering'.split()
query_bow = dictionary.doc2bow(query_document)
query_tfidf = tfidf_model[query_bow]
sims = similarity_model[query_tfidf]
for doc_id, doc_sim in enumerate(sims):
    print(f"Document_{doc_id} similarity: {doc_sim}")
```

```
Document_0 similarity: 0.0
Document_1 similarity: 0.32448703050613403
Document_2 similarity: 0.4170757234096527
Document_3 similarity: 0.718481183052063
Document_4 similarity: 0.0
Document_5 similarity: 0.0
Document_6 similarity: 0.0
Document_7 similarity: 0.0
Document_8 similarity: 0.0
```

## wrap-up 

- 본 글에서는 gensim의 core concept를 다루었습니다. 다시, gensim에서 중요하게 생각하는 다음 4가지 개념을 정리하자면, 다음과 같습니다. 
    1) `Document`: 그냥 'text'이며 보통 `lower().split()`을 적용하여, 단어별로 구성된 list로 생각하는 것이 좋음. 또한, 이 아이도 bag-of-word로 표현하여 보통 관리.
    2) `Corpus`: document의 집합을 말하며, "하나의 단일한 데이터 집합"이라는 개념으로 보는 것이 좋음. 가령, tf-idf model을 만들거나, similarity model을 만들 때도 기본적으로 받아들이는 argument가 corpus이며, 이는 "이 모델의 기본 가정인 이 corpus로부터 출발한다"라는 개념이 담긴 것으로 "내 마음대로 생각함" 
    3) `Vector`: 수학적으로 편리하게 사용하기 위해서 document를 수치적으로 표현한 것. 여기서는 bag-of-word만을 사용하여 vector로 표현하였고, tf-idf는 model에 포함되는 것으로 생각하였음.
    4) `Model`: vector를 다른 '것'으로 변환해주는 알고리즘(가령, Document의 Vector를 입력받아서, label로 변환해주는 것.) tf-idf를 여기서는 모델로 생각함. 어떻게 생각하면 이는 타당한 것이, corpus별로 tf-idf의 변환 형태가 달라질 수 있음. 즉, 다시 말하지만, corpus는 "기본 데이터 집합 혹은 분포"를 말하며, 이 분포가 다르면 다른 모델이라는 것, 이 개념을 적극적으로 반영하고 있는 것으로 보임.


## reference

- [gensim - Core Tutorial - Core Concept](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html#sphx-glr-auto-examples-core-run-core-concepts-py)


## raw-code

```python
import gensim
from gensim import corpora
from collections import Counter
import itertools
import pprint 

text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

text_corpus = [text.lower().split() for text in text_corpus]


# document 별로 존재하는 word에 대해서 
# stoplist(너무 빈번하거나, 너무 희귀하건)를 만들어서 제외함.
word_counter = Counter(itertools.chain.from_iterable(text_corpus))
stoplist = set('for a of the and to in'.split(' ')) 
min_count = 1
stoplist.update(set([w for w, f in word_counter.items() if f<=min_count]))
processed_corpus = []
for document in text_corpus: 
    word_in_document = filter(lambda word: True if word not in stoplist else False, document)
    processed_corpus.append(list(word_in_document))
#pprint.pprint(processed_corpus)
print(f"== processed corpus:")
print(processed_corpus)
print("--"*10)
# 만들어진 processed_corpus에 대해서 Dictionary로 관리해줌
dictionary = gensim.corpora.Dictionary(processed_corpus)
print(f"== dictionary:")
print(dictionary)
print("--"*10)

# dictionary의 구성된 token들의 id가 무엇인지 알 수 있음
# 우선 token을 매번 string으로 관리해도 되지만, 이렇게 할경우 메모리에서 발생하는 용량에 부하가 걸릴 수 있음
# 따라서, 보통은 token에 대해서 integer로 id를 매겨서 관리함. 
# 이후 다른 new_doc에 대해서 bag-of-word의 형태로 표현하려고 할때 
# (token, frequency)가 아니라, (token_id, frequency)의 형태로 표현됨.
print("== dictionary.token2id")
print(dictionary.token2id)
print("--"*10)

new_doc = "Human Human computer interaction"
new_doc_words = [w.strip() for w in new_doc.lower().split(" ")]
# new_doc_words에 대한 bag-of-word 표현. 
new_vec = dictionary.doc2bow(new_doc_words)
print(f"new_doc: {new_doc}")
print(new_doc_words)
print(new_vec)
# method가 있지만 lazy함. dictionary.token2id를 사용해서 reverse mapping
id2token_dict = {id: token for token, id in dictionary.token2id.items()}
print([ (id2token_dict[token_id], f) for token_id, f in new_vec])
print("--"*10)
print("== all document to bow")
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
pprint.pprint(bow_corpus)
print("--"*10)
# train the model
tfidf_model = gensim.models.TfidfModel(bow_corpus)
# transform the "system minors" string
words = "system minors".lower().split()
print(tfidf_model[dictionary.doc2bow(words)])
# dictionary의 token에 해당 단어들이 없을 경우에는 계산이 되지 않음.
words = "A B".lower().split()
print(tfidf_model[dictionary.doc2bow(words)])

print("--"*10)

similarity_model = gensim.similarities.SparseMatrixSimilarity(
    corpus=tfidf_model[bow_corpus], num_features=12
)

query_document = 'system engineering'.split()
query_bow = dictionary.doc2bow(query_document)
query_tfidf = tfidf_model[query_bow]
sims = similarity_model[query_tfidf]
for doc_id, doc_sim in enumerate(sims):
    print(f"Document_{doc_id} similarity: {doc_sim}")

```