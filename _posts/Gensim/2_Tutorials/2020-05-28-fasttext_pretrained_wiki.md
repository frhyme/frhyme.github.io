---
title: FastText, 학습된 모델과 벡터 가져와서 사용하기
category: NLP
tags: nlp fasttext gensim python python-libs machine-learning
---

## Intro

- fasttext는 2017년 당시에 유행했던 방법론이며, word2vec이 Out-Of-Vocabulary 문제를 해결해주지 못하는 반면, fasttext의 경우는 word과 word간의 형태적 유사성을 n-gram의 단위에서 고려함으로써 vocab에 존재하지 않는 word에 대해서도 벡터로 표현해준다는 강점을 가집니다. 
- 따라서, 상대적으로 적은 수의 data에서도 꽤 효과적으로 사용될 수 있죠.

## What is FastText? 

- FastText에 구현된 방법론은 논문 [Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606)에 근거합니다. 그리고 논문 제목에서 보이는 것처럼, fasttext는 각 word의 subword information 정보를 활용하여, word를 벡터화하죠. 
- fastText의 기본 원리는 단어에 존재하는 "morphological structure"를 활용하여, 단어의 의미 정보를 추출해내는 것입니다. 이는, 전통적인 traditional word embedding 방식인 word vocabulary에 근거한 word embedding 방식에서는 존재하지 않았던 것이죠. 
- 따라서, 기존의 word2vec의 경우에는 word vocabulary에 존재하지 않는 "새로운 단어"에 대해서는 vector로 표현할 수 없었습니다. 

![morphological structure](https://www.cs.bham.ac.uk/~pjh/sem1a5/pt2/pt2_intro_morph_1.gif)

- 즉, n-gram을 vector로 학습을 시키고, 그걸 이용해서 단어를 다시 어떤 차원에 전사하는 것이죠.
- 이 방법을 통하면 "computer"와 "computers"간의 유사성을 알아서 어느 정도 인지하게 됩니다. 서로 동일한 n-gram을 상당히 많이 가지고 있으니까요.

## FastText - Model and Vectors 

- 그리고, [fasttest - Wiki word vectors](https://fasttext.cc/docs/en/pretrained-vectors.html)에서 각각의 언어에 대해서 fasttext 모델과 학습된 벡터를 가져올 수 있습니다.
- 여기서 "모델(model)을 가져온다는 것"과 **"학습된 벡터를 가져오는 것"**은 다릅니다. 
  - **모델을 가져오는 것**: 모델 자체를 가져오는 것이므로, 가져온 모델을 사용해서 추가적인 학습이 가능합니다. 만약, 충분히 일반화된 모델을 가져올 수 있다면, 그 모델로부터 출발하여, 제가 가진 특별한 데이터를 들이붓고 제가 원하는 분야에 적합한 모델로 fitting할 수 있겠죠. 당연히, 그냥 벡터를 가져오는 것보다는 용량이 훨씬 큽니다.
  - **벡터를 가져오는 것**: 벡터만 가져오는 것을 말합니다. 즉, 이미 vocabulary가 완성되어 있고, 이 vocabulary에 속하는 키워드들에 대해서 벡터값이 무엇인지 보여주는 것을 의미하죠. 보통 공개된 벡터들은 충분히 잘 학습된 모델의 결과물이기 때문에, 그것만으로도 충분히 쓸만 하기는 합니다. 
- 따라서, 필요에 따라서 둘 중에 선택해서 가져오면 되겠죠. 
- [fasttest - Wiki word vectors](https://fasttext.cc/docs/en/pretrained-vectors.html)에서 영어 자료를 다운 받으면 다음과 같은 2가지의 파일이 존재합니다.
  - `wiki.en.bin`: binary file이며, 모델 그 자체를 말한다. sub-word에 대한 정보들을 모두 가지고 있기 때문에, 용량이 크다.
  - `wiki.en.vec`: text file이며, subword에 대한 벡터 값은 가지고 있지 않고, keyword에 대한 값만 가지고 있습니다. 따라서, `wiki.en.bin`보다는 용량의 크기가 작으며, word2vec_format으로 읽어야 합니다.
- 두 파일 모두 용량이 8GB 정도 매우 큽니다. 만약 램의 용량이 충분하지 않다면, 사용하지 않는 것을 추천드립니다.

### LOAD Pre-trained fasttext VECTOR

- 우선, 학습된 벡터, `wiki.en.vec`를 읽어보겠습니다. 
- 이 아이는 그냥 텍스트이므로 다음의 코드로 파일처럼 읽을 수 있죠.

```python
with open("./wiki.en/wiki.en.vec", "r") as f:
    word_size, vector_size = f.readline().split(" ")
    print(f"word_size  : {word_size:7s}")
    print(f"vector_size: {vector_size.strip():7s}")
    print("==" * 20)
    for i in range(0, 10):
        line = str(f.readline())
        ws = line.split(" ")
        kwd, kwd_vec = ws[0], ws[1:]
        print(f"{kwd:7s} :: {kwd_vec[:5]}")
```

- 실행 결과는 다음과 같습니다.
- 즉, 그냥, 한줄마다 각 `단어`에 매칭되는 벡터값들이 존재하는 것 뿐이죠.
- 이 것만으로도 어느 정도는 단어간의 유사도 등을 계산하고 처리할 수 있지만, 충분하지 못하게 느껴집니다.

```plaintext
word_size  : 2519370
vector_size: 300    
========================================
,       :: ['-0.023167', '-0.0042483', '-0.10572', '0.042783', '-0.14316']
.       :: ['-0.11112', '-0.0013859', '-0.1778', '0.064508', '-0.24037']
the     :: ['-0.065334', '-0.093031', '-0.017571', '0.20007', '0.029521']
</s>    :: ['0.050258', '-0.073228', '0.43581', '0.17483', '-0.18546']
of      :: ['0.048804', '-0.28528', '0.018557', '0.20577', '0.060704']
-       :: ['-0.12278', '-0.036748', '0.20728', '-0.018277', '-0.0016348']
in      :: ['0.12367', '-0.13965', '0.044877', '0.18919', '-0.10997']
and     :: ['-0.031533', '0.046278', '-0.12534', '0.19165', '-0.1266']
'       :: ['-0.17489', '-0.13695', '0.13345', '-0.07282', '0.038794']
)       :: ['-0.2126', '-0.1625', '0.19291', '-0.025168', '-0.053647']
```

- 아무튼, 이 아이를 gensim에서 읽으려면 다음의 방식으로 사용하면 됩니다.

```python
from gensim.models.keyedvectors import KeyedVectors
# 다 읽으려면 너무 시간이 오래 걸려서, 상위 10000개만 읽음.
model = KeyedVectors.load_word2vec_format('./wiki.en/wiki.en.vec', limit=10000)
# load 된 model 자체가 <class 'gensim.models.keyedvectors.Word2VecKeyedVectors'
print(f"Type of model: {type(model)}")
print(model.most_similar('teacher'))
print(model.similarity('teacher', 'teaches'))
```

- 다만, fastext로 학습한 것이지만, `load_word2vec_format`으로 읽는 것이, 조금 의아할 수 있죠. 
- 결론적으로 보면 fastext로 학습을 한 것이든, word2vec으로 학습을 한 것이든 결과물은 각 단어에 대한 vector가 되고, 그 결과만 모아놓았다면 그것이 무엇이든 아무 상관이 없습니다.
- 우리는 어차피, 존재하는 벡터를 가지고 그대로 사용하기만 할 것이니까, `Word2VecKeyedVectors`로, vocabulary에 존재하는 단어들만을 사용하는 것이죠. 
- 즉, 결과적으로는 subword에 대한 정보가 없기 때문에, 혹시라도 out-of-vocabulary에 대해서는 예측할 수 없습니다.

### LOAD Pre-trained fasttext MODEL

- 이제, 모델 자체를 가져와봅니다. 
- 이전에 다운받아서 압축한 파일에서 `wiki.en.bin`파일이 바로 모델이죠.
- 모델을 다운받으면, subword에 대한 정보가 모두 유효하게 남아있으므로 추가로 학습하는 것 또한 가능하죠.
- 아래 코드에서 보시는 것처럼, `gensim.models.FastText.load_fasttext_format`를 통해서 해당 파일을 읽으면 됩니다.

```python 
from gensim.models import FastText as FT

print(f"== LOAD fasttext START at {datetime.datetime.now()}")
model = FT.load_fasttext_format('wiki.en/wiki.en.bin')
print(f"== LOAD fasttext   END at {datetime.datetime.now()}")

print(model.most_similar('teacher'))
# Output = [('headteacher', 0.8075869083404541), ('schoolteacher', 0.7955552339553833), ('teachers', 0.733420729637146), ('teaches', 0.6839243173599243), ('meacher', 0.6825737357139587), ('teach', 0.6285147070884705), ('taught', 0.6244685649871826), ('teaching', 0.6199781894683838), ('schoolmaster', 0.6037642955780029), ('lessons', 0.5812176465988159)]
print(model.similarity('teacher', 'teaches'))
```

- 실행 결과는 다음과 같습니다. 
- 중간에 끼어져 있는 DeprecationWarning은 아래에 따로 설명하였습니다.
- 다만 제 맥북이 RAM이 16GB임에도 불구하고, 올리는데만 약 6분의 시간이 걸리더군요.
- 물론, 대략 16GB의 RAM이 있어야 해당 모델을 램에 문제없이 올릴 수 있구요.

```plaintext
== LOAD fasttext START at 2020-05-28 20:01:07.534669
gensim_fasttext_pretrained_vector.py:21: DeprecationWarning: Call to deprecated `load_fasttext_format` (use load_facebook_vectors (to use pretrained embeddings) or load_facebook_model (to continue training with the loaded full model, more RAM) instead).
  model = FT.load_fasttext_format('wiki.en/wiki.en.bin')
== LOAD fasttext   END at 2020-05-28 20:07:22.647851
gensim_fasttext_pretrained_vector.py:24: DeprecationWarning: Call to deprecated `most_similar` (Method will be removed in 4.0.0, use self.wv.most_similar() instead).
  print(model.most_similar('teacher'))
[('teache', 0.7893729209899902), ('teacher,', 0.7844669818878174), ('teachers', 0.7713972926139832), ('teacherman', 0.7344011068344116), ('teached', 0.7318556904792786), ('teacher/pupil', 0.7292030453681946), ('teachers`', 0.728623628616333), ('schoolteacher', 0.7279098629951477), ('teachera', 0.7274622917175293), ('‘teacher', 0.7261096239089966)]
gensim_fasttext_pretrained_vector.py:26: DeprecationWarning: Call to deprecated `similarity` (Method will be removed in 4.0.0, use self.wv.similarity() instead).
  print(model.similarity('teacher', 'teaches'))
0.58209455
```

### Call to deprecated `load_fasttext_format`

- 다만, 위의 방식으로 할 경우, 아래와 같은 `DeprecationWarning` 메세지가 하나 뜨는 것을 알 수 있는데요.
  - 해석하면 `FT.load_fasttext_format`는 옛날 방식이다. 
  - `load_facebook_vectors`를 사용해서 벡터를 가져오거나, 
  - `load_facebook_model`를 사용해서, 모델을 가져와라. 

```plaintext
gensim_fasttext_pretrained_vector.py:21: DeprecationWarning: Call to deprecated `load_fasttext_format` (use load_facebook_vectors (to use pretrained embeddings) or load_facebook_model (to continue training with the loaded full model, more RAM) instead).
  model = FT.load_fasttext_format('wiki.en/wiki.en.bin')
```

- 따라서, 코드를 다음과 같이 변경합니다.
  - 이전에는 `FastText`에서 가져왔다면, 
  - 이제는 모두 소문자인 `fasttext`에서 가져온다는 것이 작은 차이죠.
- 이렇게 변경하고 나면, warning message 없이 잘 뜨는 것을 알 수 있습니다.

```python 
from gensim.models import fasttext

print(f"== LOAD fasttext START at {datetime.datetime.now()}")
model = fasttext.load_facebook_model("./wiki.en/wiki.en.bin")
print(f"== LOAD fasttext   END at {datetime.datetime.now()}")

print(model.most_similar('teacher'))
print(model.similarity('teacher', 'teaches'))
```

```plaintext
== LOAD fasttext START at 2020-05-28 19:51:57.887353
== LOAD fasttext   END at 2020-05-28 19:58:10.851310
[('teache', 0.7893729209899902), ('teacher,', 0.7844669818878174), ('teachers', 0.7713972926139832), ('teacherman', 0.7344011068344116), ('teached', 0.7318556904792786), ('teacher/pupil', 0.7292030453681946), ('teachers`', 0.728623628616333), ('schoolteacher', 0.7279098629951477), ('teachera', 0.7274622917175293), ('‘teacher', 0.7261096239089966)]
0.58209455
```

## wrap-up

- 9GB를 한번에 RAM에 올리는 것이기는 하지만, 생각보다 로드만 하는데도 시간이 많이 걸려서 놀랐습니다.
- 그리고, 당연하지만 배터리도 아주 빠르게 날아가더군요 호호호호
- 완벽하게 계산을 하지는 못해도, 어느 정도 하기 위해서 RAM을 16GB로 해서 맥북을 샀는데, 여전히 제대로 된 계산을 돌리기는 어려울 것으로 보입니다 호호호.