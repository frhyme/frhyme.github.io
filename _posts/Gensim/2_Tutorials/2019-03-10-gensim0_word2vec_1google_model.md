---
title: gensim - tutorial - word2vec - basic
category: python-libs
tags: python python-libs gensim similairty word2vec nlp 
---

## 2-line summary 

- google이 이미 word2vec의 결과로 각 word에 대한 vector를 만들어서 배포하였습니다. 하지만 용량이 커서 작은 용량에서는 어렵죠. 그래서 작은 용량의 word2vec vector로 존재합니다. 
- vector를 특정 분야에 맞게 특화시키킬 원할 경우, `Word2vec.intersect_word2vec_format(googleNews_filepath, binary=True, lockf=1.0)`을 통해 쉽게 초기값을 설정할 수 있습니다.


## gensim - tutorial - word2vec - GoogleNews

- 이전의 글에서는 gensim을 사용해서 word2vec으로 단어들을 표현하고, 그 다음, 

## read pre-trained word2vec 

- [word2vec-GoogleNews-vectors](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)에서 이미 학습된 word2vector를 다운받을 수 있습니다. 다만, "학습된 모델"을 가져오는 것이 아니라, "학습된 vector"만을 수치로 가져오는 것이죠.
- vector만 가져올 경우 "학습을 추가로 진행할 수 없습니다". 즉, 그냥 값만 사용해서 유사도를 측정하는 것이 다이긴 하죠. 물론, 이것만으로도 대단하기는 하죠. 
- 또한, [word2vec-GoogleNews-vectors](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)는 압축을 풀면 약 3기가로 매우 데이터의 용량이 큽니다(일단 저의 맥북은 램이 4기가죠 호호호. 사실 4기가 램가지고 무슨 머신러닝을 공부하냐는 말이 많지만, 그덕에 효율적으로 메모리를 관리하는 스킬이 늘지 않았을까, 라고 저를 위로해봅니다). 
- 이를 해결하기 위해서는 우선 아래의 방법으로 상위 n개의 단어만 가져올 수 있죠. `limit`에 값을 넘겨주면 됩니다.

```python
GoogleSlimModel = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(
    googleNews_filepath, binary=True, limit=50000
)
```

### GoogleNews-vectors-negative300-SLIM

- 하지만, 저는 [GoogleNews-vectors-negative300-SLIM](https://github.com/eyaler/word2vec-slim/blob/master/GoogleNews-vectors-negative300-SLIM.bin.gz)를 사용하기로 합니다. 이 아이는 약 300메가바이트로 훨씬 가볍습니다. 링크를 타고 가시면 어떤 방법으로 word를 추려내었는지 정리되어있고, 그냥 "상위 n개"와 같은 방식보다는 좀더 합리적인 것 같네요.

```python 
import gensim
import time

# 내 컴퓨터에서는 읽을 때, 약 10초가 걸림.
googleNews_filepath = "GoogleNews-vectors-negative300-SLIM.bin"
start_time = time.time()
print(f"== {googleNews_filepath} load as word2vec model start")
GoogleSlimModel = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(
    googleNews_filepath, binary=True
)
print(f"== {googleNews_filepath} load as word2vec model complete, {time.time() - start_time}")

print()
"""
실행시 아래 결과가 나와야 정상적임.
[('SUV', 0.8532191514968872), ('vehicle', 0.8175784349441528), ('Jeep', 0.7567334175109863), ('sedan', 0.7446292042732239), ('truck', 0.7273114919662476)]
"""
assert GoogleSlimModel.wv.most_similar(positive=['car', 'minivan'], topn=5) == [('SUV', 0.8532191514968872), (
    'vehicle', 0.8175784349441528), ('Jeep', 0.7567334175109863), ('sedan', 0.7446292042732239), ('truck', 0.7273114919662476)]
print('== complete')
```


## Transfer learning. 

- 엄밀히 따지면, transfer learning은 아니지만, 비슷하므로 일단 그렇게 이름을 지어봤습니다.
- vector가 아니라 "모델" 자체를 가져올 수 있었다면, 그 모델로부터 제가 원하는 특정한 텍스트들에 대해서 학습을 더 진행하여 의미있는 결과를 얻을 수 있을 것 같은데, 불행히도 그냥 벡터만 받을 수 있죠. 
- 그러나, 조금 더 생각해보면, 그냥 초기 값을 더 벡터로 초기화하면 되는 것 아닐까? 싶어요. 그 다음에 새운 데이터를 학습시킨다면, 조금씩 그 데이터가 업데이트되겠죠(물론 아마도 어떤 움직임을 가져오려면 훨씬 많은 학습이 필요하긴 합니다).

### word2vec.intersec_word2vec_format()

- [word2vec documentation](https://tedboy.github.io/nlps/_modules/gensim/models/word2vec.html#Word2Vec.load_word2vec_format)을 보면, `intersect_word2vec_format()`라는 메소드가 있습니다. 이 아이는, 외부의 file로부터 이미 생성된 vocabulary에 대해서 초기화를 진행해주죠. 단, 이를 위해서는 `wv.vocab`에 이미 external_file와 같은 word가 존재해야 합니다.
- 추가로, 기본적으로는 외부에서 가져온 vector에 어떤 수정도 진행되지 못하도록 lock이 걸려 있습니다(이는 나름 합리적인 결정이죠). 따라서, 만약 추가로 vector를 업데이트하고 싶다면, `lockf=1.0`으로 argument를 넘겨주는 것이 필요합니다.
- 즉, 다음처럼 이미 만들어진 `TranferedModel`이라는 word2vec model에 외부 파일로에 저장된 keyed_vector의 weight를 덮어 쓰워주는 것이죠.

```python
TranferedModel.intersect_word2vec_format(
    googleNews_filepath, binary=True, lockf=1.0
)
```

### python implementation.

- 이 전체 과정을 python으로 표현하면 다음과 같습니다.
    1) LOAD pre-trained key vector: 외부에서 이미 학습된 key-vector, `PreTrainedKeyvector`를 가져옴 
    2) MAKE new word2vec model: 우리가 사용할 새로운 word2vec model, `TranferedModel`를 만들어줌.
    3) BUILD vocab by PreTrainedKeyvector word Vocabulary: `TranferedModel`의 vocab을 우선 우리의 데이터 `sentences`로 업데이트해줌. 
    4) UPDATE vocab by sentences: `PreTrainedKeyvector`로부터 vocab을 업데이트해줌. 
    5) INITIALIZED word vector: `PreTrainedKeyvector`의 wordvector들을 `TranferedModel`에 업데이트해줌.
    6) TRAIN new data set: 새로운 데이터 `sentencs`를 업데이트하면서 조정.

```python 
import gensim

# 우리가 업데이트하려고 하는 data가 다음 sentences에 있다고 합시다
# 그리고, 다음 데이터들은 모두 lower, strip, 공백으로 split되어 있다고 하죠. 
sentences = ["I am a boy", "You are a girl"]
sentences = [s.lower().strip().split(" ") for s in sentences]
#---------------------------------------------
# 1) LOAD pre-trained key vector
# model을 load한 것이 아니기 때문에, 바로 training하는 것이 불가능하죠.
googleNews_filepath = "GoogleNews-vectors-negative300-SLIM.bin"
PreTrainedKeyvector = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(
    googleNews_filepath, binary=True, limit=20
)
#---------------------------------------------
# 2) MAKE new word2vec model
# PreTrainedKeyvector와 `vector_size`가 같은 word2vec model을 생성해줌.
TranferedModel = gensim.models.Word2Vec(
    size=PreTrainedKeyvector.vector_size, min_count=1)
#---------------------------------------------
# 3) BUILD vocab by PreTrainedKeyvector word Vocabulary
# TranferedModel.build_vocab([[]]) # list of list 
# ** list of list 로 넘겨줘야 함.
TranferedModel.build_vocab([PreTrainedKeyvector.wv.vocab.keys()])
#---------------------------------------------
# 4) UPDATE vocab by sentences
# update parameter를 True로 설정.
TranferedModel.build_vocab(sentences, update=True)
#---------------------------------------------
# 5) INITIALIZED word vector 
# vocab에 있는 단어들의 vector를 `googleNews_filepath`에 있는 값으로 모두 업데이트해줌.
# lockf=1.0 : 보통은 vector를 update하지 못하도록 lock이 걸려 있는데, 여기서는 이걸 품. 
TranferedModel.intersect_word2vec_format(
    googleNews_filepath, binary=True, lockf=1.0
)
#---------------------------------------------
# 6) TRAIN new data set. 
print("== Before New data training")
print(TranferedModel.wv['boy'][:10])
TranferedModel.train(sentences, total_examples=len(sentences), epochs=100)
print("== After New data training")
print(TranferedModel.wv['boy'][:10])
```

- 아래 새롭게 training한 결과를 보시면 조금씩 값이 변경되는 것을 알 수 있습니다. 따라서, 새로운 데이터로 조금씩 업데이트를 하면서 진행할 수 있죠.

```
== Before New data training
[ 0.08396781  0.05888199  0.03327355 -0.04599067  0.00570528  0.01289132
 -0.04163549 -0.02613106  0.04947481  0.00411564]
== After New data training
[ 0.08395655  0.05888071  0.03327597 -0.04598987  0.00569793  0.0128962
 -0.04163208 -0.02612745  0.04948092  0.00411575]
```


## wrap-up

- 사실, 이것이 얼마나 잘 작동할지에 대해서는 약간 의문이 있긴 합니다. 새로운 데이터에 대해서 epoch을 어떻게 하느냐에 따라서 결과가 달라질 수도 있고 한데, 그래도, 훨씬 빠르게 결과를 만들 수 있지 않을까, 라고 저 혼자 생각해봅니다 하하하.

## reference

- [GoogleNews-vectors-negative300-SLIM](https://github.com/eyaler/word2vec-slim/blob/master/GoogleNews-vectors-negative300-SLIM.bin.gz)
- [word2vec-GoogleNews-vectors](https://github.com/mmihaltz/word2vec-GoogleNews-vectors)
- [stackoverflow : how-to-initialize-a-new-word2vec-model-with-pre-trained-model-weights](https://datascience.stackexchange.com/questions/10695/how-to-initialize-a-new-word2vec-model-with-pre-trained-model-weights)
- [stackoverflow : gensim-doc2vec-intersect-word2vec-format-command](https://stackoverflow.com/questions/46013294/gensim-doc2vec-intersect-word2vec-format-command)


## raw-code

```python
import gensim
import time

if False: 
    # 내 컴퓨터에서는 읽을 때, 약 10초가 걸림.
    googleNews_filepath = "GoogleNews-vectors-negative300-SLIM.bin"
    start_time = time.time()
    print(f"== {googleNews_filepath} load as word2vec model start")
    GoogleSlimModel = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(
        googleNews_filepath, binary=True
    )
    print(f"== {googleNews_filepath} load as word2vec model complete, {time.time() - start_time}")

    print()
    """
    실행시 아래 결과가 나와야 정상적임.
    [('SUV', 0.8532191514968872), ('vehicle', 0.8175784349441528), ('Jeep', 0.7567334175109863), ('sedan', 0.7446292042732239), ('truck', 0.7273114919662476)]
    """
    assert GoogleSlimModel.wv.most_similar(positive=['car', 'minivan'], topn=5) == [('SUV', 0.8532191514968872), (
        'vehicle', 0.8175784349441528), ('Jeep', 0.7567334175109863), ('sedan', 0.7446292042732239), ('truck', 0.7273114919662476)]
    print('== complete')


if False:
    # 우리가 업데이트하려고 하는 data가 다음 sentences에 있다고 합시다
    # 그리고, 다음 데이터들은 모두 lower, strip, 공백으로 split되어 있다고 하죠. 
    sentences = ["I am a boy", "You are a girl"]
    sentences = [s.lower().strip().split(" ") for s in sentences]

    #---------------------------------------------
    # LOAD pre-trained key vector
    # model을 load한 것이 아니기 때문에, 바로 training하는 것이 불가능하죠.
    googleNews_filepath = "GoogleNews-vectors-negative300-SLIM.bin"
    PreTrainedKeyvector = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(
        googleNews_filepath, binary=True, limit=20
    )
    #---------------------------------------------
    # MAKE new word2vec model
    # PreTrainedKeyvector와 `vector_size`가 같은 word2vec model을 생성해줌.
    TranferedModel = gensim.models.Word2Vec(
        size=PreTrainedKeyvector.vector_size, min_count=1)
    #---------------------------------------------
    # BUILD vocab by PreTrainedKeyvector word Vocabulary
    # TranferedModel.build_vocab([[]]) # list of list 
    # ** list of list 로 넘겨줘야 함.
    TranferedModel.build_vocab([PreTrainedKeyvector.wv.vocab.keys()])
    #---------------------------------------------
    # UPDATE vocab by sentences
    # update parameter를 True로 설정.
    TranferedModel.build_vocab(sentences, update=True)
    #---------------------------------------------
    # INITIALIZED word vector 
    # vocab에 있는 단어들의 vector를 `googleNews_filepath`에 있는 값으로 모두 업데이트해줌.
    # lockf=1.0 : 보통은 vector를 update하지 못하도록 lock이 걸려 있는데, 여기서는 이걸 품. 
    TranferedModel.intersect_word2vec_format(
        googleNews_filepath, binary=True, lockf=1.0
    )
    #---------------------------------------------
    # TRAIN new data set. 
    print("== Before New data training")
    print(TranferedModel.wv['boy'][:10])
    TranferedModel.train(sentences, total_examples=len(sentences), epochs=100)
    print("== After New data training")
    print(TranferedModel.wv['boy'][:10])
```