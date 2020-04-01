---
title: gensim - tutorial - word2vec - basic
category: python-libs
tags: python python-libs gensim similairty word2vec nlp 
---

## 1-line summary 

- `gensim`을 이용하여 word2vec 모델을 구현하고, 학습시켜서 유용하게 쓰는 방법에 대하여 정리하였습니다.

## gensim - tutorial - word2vec

- word2vec은 이미 매우 유명한 머신러닝 알고리즘이죠. 사실 word2vec 자체는 shallow learning에 가깝지만, 이는 그냥 deep learning 기법으로 알려져 있기도 합니다. 
- 어떤 정보도 없는 plain text들, 단지 아주 많은, plain text들을 사용해서 단어들(word 혹은 token)를 vector space에 전사합니다. 이 때 사실 가장 중요한 것은 "아주 많은 plain text"가 필요하다는 것이죠. 네, 말 그대로 big data를 가지고 있고, 이를 효과적으로 처리할 수 있다면, 단지 "쉬운 방식"만으로도 의미있는 결과를 가져올 수 있다는 것이죠. 
- 이 방법이 의미가 있었던 것은 다음과 같은 결과 때문입니다. 

```
vec(“king”) - vec(“man”) + vec(“woman”) =~ vec(“queen”)
vec(“Montreal Canadiens”) – vec(“Montreal”) + vec(“Toronto”) =~ vec(“Toronto Maple Leafs”).
```

- 단, 하나 word2vec의 아쉬운 점이라면, "unfamiliar word"에 대해서는 vector를 추론해주지 못한다는 것이죠. 즉, "기존에 학습한 text data에 특정 단어가 포함되어 있지 않거나, 유효하지 않은 경우(min_count에 걸려서 고려하지 않는 경우)"일 때는 해당 word에 대해서 vector로 표현해주지 못합니다. 해당 word가 존재하는지는 `model.wv.vocab`에 해당 단어가 존재하는지를 체크해주는 것이 필요합니다.
- 이것이, 단 하나 존재하는 word2vec의 한계이며 만약 이 한계점이 매우 문제가 된다면, `FastText` 모델을 사용하는 것이 좋습니다.

### skipgram or CBOW

- word2vec은 input(단어)로 output(단어의 이웃들)을 유추하는 알고리즘입니다. 혹은 반대로, input(단어의 이웃들)로 output(단어)를 유추하죠. 이 두 방식이 각각 skipgram과 CBOW인데, 이 둘의 차이를 반드시 알 필요는 없다고, 생각해요. 비슷비슷하거든요물론 논문들에서는 어떤 차이가 있는지 설명하고 있다고 하지만, 저는 그정도로 민감하게 고려하지 않으므로 일단 넘어갑니다.


## Training own model. 

- 일단은 그냥 하면서 알아봅시다. 우리는 우리가 마음대로 생성해낸 sentence들에 대해서 word2vec model을 만들겁니다.

### Sentences

- 우선, 테스트니까 간단한 데이터를 넣어보려고 합니다. 아래와 같이, 간단한 문자열로 구성된 text들을 만듭니다. 
- 데이터를 가만히 보면, "남자"와 "여자"라는 두가지 관점이 보입니다. 매우 높은 확률로, 적합하게 학습을 시켰다면, 단어 "He"는 "king"과 가까워야 하고, "queen"은 "she"와 가까워야 겠죠. 

#### text.lower()

- 또한, 후처리에서 텍스트를 소문자로 변경합니다. 이는, 제가 학습하는 데이터에서, 대소문자의 차이를 신경쓰지 않겠다는 것이죠. 이후에 또 설명하겠지만, word2vec은 기존의 학습된 텍스트에 존재하는 단어들을 vector로 표현해주는 것을 말합니다. 다시 말해, 원래 데이터에 존재하지 않는 word는 vector로 표현할 수 없죠. 
- 이 때, "제가 모든 단어를 소문자로 변경"한다면, 만약 아래에서 "He"와 "he"는 하나의 단어로 변경됩니다. 즉, 만약 기존 데이터에서 capitalization이 영향을 끼칠 것이라고 고려된다면, lowering을 하지 않는 것이 좋겠죠.

#### Word tokenize

- `gensim.models.Word2Vec`에서 필요로 하는 데이터는 "list of word list"입니다. 즉, "문자열"이 아니라, word들도 분할해줘야 한다는 이야기죠. 
- 저는 일단 편의를 위해서 `string.split(" ")`을 통해서 간단하게 처리해주었지만, 사실은 이렇게 하는 것이 항상 옳지는 않습니다. 우선, 이렇게 처리할 경우 복합어에 대해서는 전혀 고려하지 못한다거나, 하는 다른 문제점들이 있으며, 좀더 잘 사용하기 위해서는 다른 word-tokenizer를 사용하는 것이 좋습니다.
- 코드는 다음과 같습니다.

```python
sentences = [
    "He is a king", "She is a queen",
    "he is a boy", "She is a girl",
    "He is a man", "She is a woman"
] * 1000
# 모든 단어를 lower()로 소문자화 처리한다. 이는 단어들의 대소문자의 차이를 무시한다는 것을 말한다.
sentences = [sent.lower().strip().split(" ")for sent in sentences]
# ex) [['I', 'am', 'a', 'boy'], ['you' 'are' 'a' 'girl']]
```

### Sentence training

- 이제 만든 것을 word2vec model에 넣어서 학습시킵시다. `gensim.models.Word2Vec`에 parameter로 넘겨주면 됩니다. 
- 학습이 완료된  `model.wv`에 대해서 각 word와 vector를 다음과 같이 꺼내어올 수 있습니다.

```python 
import gensim

"""
Word2Vec PARAMETER:
- sentences: word_list of list 
ex) [['I', 'am', 'a', 'boy'], ['you' 'are' 'a' 'girl']]
min_count: sentence에 들어있는 단어들 중 vocabulary에 등록할 최소한의 단어 빈도 
- size: vector size. 
당연하지만, size가 크면 더 rich한 정보를 담을 수 있음.
"""
model = gensim.models.Word2Vec(
    sentences=sentences, 
    min_count=1, size=50
)
# `model.wv[word]`를 통해 word의 wordvector를 확인할 수 있다. 
for word in model.wv.vocab:
    word_vec = model.wv[word]
    print(f"word: {word} - vector, type: {type(word_vec)}, shape: {word_vec.shape} ")
print("--"*20)
print("word not in wv.vocab doesn't have a vector.")

```

- word vector는 `model.wv[word]`를 통해서 사용할 수 있으며, 너무 길어서 일단 다음으로 유형과, 크기만 출력하였습니다

```
word: he - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: is - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: a - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: king - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: she - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: queen - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: boy - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: girl - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: man - vector, type: <class 'numpy.ndarray'>, shape: (50,)
word: woman - vector, type: <class 'numpy.ndarray'>, shape: (50,)

```

- 또한, 이전에 학습할 때, 소문자에 대해서만 학습시켰으므로, 아래처럼 대소문자가 섞여 있는 word는 `model.wv.vocab`에 없다고 생각하여, 에러가 발생됩니다. 즉, 넣을 때도 capital을 고려해야 한다는 것이죠.

```python
for w in ['YOU', 'you', 'You']:
    try: 
        print(f""""word '{w}'     in vocabulary" => {model.wv[w]}'""")
    except Exception as e: 
        print(e)
```
```
----------------------------------------
word not in wv.vocab doesn't have a vector.
"word 'YOU' not in vocabulary"
"word 'you' not in vocabulary"
"word 'You' not in vocabulary"
```


### Similarity in gensim.

- 자, 이제 우리는 우리가 데이터를 word2vec 모델에 집어넣어서 학습을 시켰습니다. 이 말은, 곧 우리가 정의한 vector space에 word들을 적절하게 흩뿌려 놓았다는 말이 되는 것이죠. 따라서 모든 word는 vector space에 표현되므로, 모두 vector를 가집니다. 여기서, 우리는 더이상 그게 word인지는 고려하지 않아도 됩니다. 그냥 vector일 뿐이죠. 
- 이제 우리는 어떤 word(다시 말해서 어떤 vector)에 대해서 가장 가까운 vector가 무엇인지 찾으려고 합니다. 여기서 '가깝다'라는 것을 측정하기 위한 많은 방법들이 있겠지만, 보통 cosine similarity를 많이 사용합니다. 
- cosine similarity는 보통 "벡터의 크기"가 중요하지 않고, 방향이 중요한 경우에 많이 사용하게 되죠. 보면, word의 경우 text에 많이 등장하면 magnitue가 커지는 경향성이 있습니다. 하지만, 그 크기가 중요한 것이 아니라, unit vector, 즉 방향성이 word에서는 중요하죠. 따라서, 이런 경우에는 cosine similarity를 사용하게 됩니다.


#### wv.similarity

- 우선, 두 word vector의 유사도(similarity)를 비교하기 위해서는 보통 `model.wv.similarity`를 사용합니다. 다만, 이 방법은 두 word vector에 대해서 cosine similarity를 적용한 것과 동일하죠.


```python
from sklearn.metrics.pairwise import cosine_similarity 

w1, w2 = 'he', 'king'
w1_w2_sim = model.wv.similarity(w1=w1, w2=w2)
w1_vec, w2_vec = model.wv[w1].reshape(1, -1), model.wv[w2].reshape(1, -1)
w1_w2_cos_sim = cosine_similarity(w1_vec, w2_vec)[0][0]
print("model.wv.similarity:", w1_w2_sim)
print("cosine_similarity of w1_vec, w2_vec:", w1_w2_cos_sim)
```

```
model.wv.similarity: 0.99511516
cosine_similarity of w1_vec, w2_vec: 0.9951151
```

#### most_similar by word

- 그 다음으로, 단어의 조합으로 가장 가까운 단어를 찾을 수도 있죠. 각각 `positive`, `negative`에 집어넣어서 단어들간의 관계와 그 유사도 정도를 가져올 수도 있죠.

```python
print(model.wv.most_similar(positive=['king'], negative=[], topn=3))
print(model.wv.most_similar(positive=['queen'], negative=[], topn=3))
```

```
[('a', 0.9980628490447998), ('boy', 0.9980459213256836), ('man', 0.9975786209106445)]
[('girl', 0.9973964691162109), ('woman', 0.9970500469207764), ('he', 0.9963347315788269)]
```

#### most_similar by vector 

- 그 외에도, word를 넣는 것이 아니라, vector에 대해서도 가장 유사한 단어를 찾을 수 있죠. 
- 만약 positive, negative를 넣고 싶다면, positive인 경우에는 그냥 더해주고, negative인 경우에는 그냥 빼주면 됩니다. cosine similarity이기 때문에, 문제없습니다. 
- 다만, 이 결과는 `model.wv.most_similar`와는 조금 다를 수 있어요. `model.wv.most_similar`의 경우, word vector의 합으로 새로운 벡터를 만들어서 처리하는 것이 아니라, [Linguistic Regularities in Sparse and Explicit Word Representations](https://www.aclweb.org/anthology/W14-1618.pdf)에서 정의한 방식을 사용합니다. 이 방식은 `model.wv.most_similar_cosmul`와 거의 같죠. 조금 더 설명하자면, "positive인 벡터들과 가장 가까우면서, negative와 먼 vector를 찾는 것"이라고 생각하시면 됩니다. 

```python
print("--"*20)
positive = ['king', 'queen']
negative = ['she']
print("== model.wv.most_similar")
print(model.wv.most_similar(positive=positive, negative=negative, topn=3))
print("== model.wv.similar_by_vector")
print(model.wv.similar_by_vector(vector=model.wv['king'] + model.wv['queen'] - model.wv['she'], topn=3))
print("== model.wv.most_similar_cosmul")
print(model.wv.most_similar_cosmul(positive=positive, negative=negative, topn=3))
print("--"*20)
```

```
----------------------------------------
== model.wv.most_similar
[('boy', 0.9923207759857178), ('man', 0.9913779497146606), ('a', 0.989335298538208)]
== model.wv.similar_by_vector
[('king', 0.9602953195571899), ('boy', 0.9553458094596863), ('man', 0.953208863735199)]
== model.wv.most_similar_cosmul
[('boy', 0.9992761015892029), ('man', 0.9987999200820923), ('a', 0.997772753238678)]
----------------------------------------
```

## Save and Load other model 

- 사실 학습이라는 것 자체가 매우 오래 걸리기도 하고, 이미 학습한 모델을 가져와서 새롭게 학습을 한다거나, 하는 것이 필요할 때도 있죠. 가령, 남이 잘 만들어놓은 generalized model을 가져와서, 특정한 어떤 분야에 맞도록 fitting을 하는 경우가 있을 테니까요.

## Resuming Training. 

- 이미 특정 corpus를 사용해서 학습을 완료한 경우, 여기에 추가로 학습을 진행하고 싶을 때가 있습니다. 
- 저의 경우는 이미 gensim을 통해서 완료된 결과에 대해서 새로운 abstract를 사용해서 추가로 학습을 시키는 것을 목적으로 하죠. 이렇게 할 경우, 이미 확보된 generality를 그대로 이용하고, 특정 분야에 적합한 specificity를 확보할 수 있게 되죠.
- 우선, 학습한 모델을 저장하는 방식은 두 가지가 있습니다. model을 그대로 저장하는 방법 그리고 학습이 완료된 wordvector만 저장하는 방법, 이렇게 두 가지가 있죠. 

### Save and Load word2vec model. 

- 아래의 방식으로, 이미 만들어진 model을 저장하고 불러와서, 학습을 이어나갈 수 있습니다.

```python
# Save model 
model_output_file_name = "test_word2vec"
model.save(model_output_file_name)
print(f"== word2vec model save as: {model_output_file_name}")
# Load model
model = gensim.models.Word2Vec.load(model_output_file_name)
print(f"== {model_output_file_name} load as word2vec model")

# Resume Training on pre-trained model
more_sentences = [
    ['Advanced', 'users', 'can', 'load', 'a', 'model',
     'and', 'continue', 'training', 'it', 'with', 'more', 'sentences']
]
# 일단 vocabn을 업데이트해줘야 함.
model.build_vocab(more_sentences, update=True)
model.train(more_sentences, total_examples = len(more_sentences), epochs=10)
```

### Save and Load word2vec keyed vector. 

- 아래처럼 word2vec 만 저장하고 불러올 수도 있지만, 이 경우에는 `train`이 불가하죠.

```python
output_file_name = "just_keyed_vector"
model.wv.save(output_file_name)
just_vector_model = gensim.models.KeyedVectors.load(output_file_name)
print(just_vector_model.wv['king'])
```


## wrap-up

- 예전에도 gensim을 사용해서 word2vec을 학습하고 사용하는 방법을 정리한 적이 있습니다. 다만, 그때는 몇 가지 부분에서 이해하지 못하고 넘어간 것이 있는데, 이번에는 어떻게 굴러가는지 거의 완벽하게 이해한 것 같아요. 
- 공부를 계속 하면서 느끼는 즐거움은 결국, "이전에 이해하지 못했거나, 넘어간 것을 완벽하게 이해했을 때" 가장 크게 오는 것 같습니다. 그게 공부를 멈추지 않고 계속 더 하게 만드는 가장 큰 원동력이죠.


## reference

- [gensim - tutorials - word2vec](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py)
- [GoogleNews-vectors-negative300-SLIM](https://github.com/eyaler/word2vec-slim/blob/master/GoogleNews-vectors-negative300-SLIM.bin.gz)
- [Linguistic Regularities in Sparse and Explicit Word Representations](https://www.aclweb.org/anthology/W14-1618.pdf)
