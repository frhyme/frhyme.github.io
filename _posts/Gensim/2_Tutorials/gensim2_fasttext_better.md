---
title: gensim - tutorial - fastText 2편 
category: python-libs
tags: python python-libs gensim similairty word2vec nlp doc2vec fastText
---

## 

나의 목적은 결국 "composite word"를 이해할 수 있도록 학습을 시키는 것을 말함. 
여기서는, 그렇다면 fastText를 학습시킬때, 



## 2-line summary 

- word2vec의 경우, 존재하지 않는 word(vocab에 등록되지 않은 word)에 대해서는 vector로 표현해주지 못합니다.
- 반면 fastText의 경우는, word와 word간의 형태적 유사성을 고려함으로써, vocab에 존재하지 않는 word에 대해서도 벡터로 표현할 수 있을 뿐만 아니라, vocab 내에 존재하는 형태적으로 유사한 키워드의 유사도를 높게 표현해낼 수 있죠. 

## word2vec의 한계 

- word2vec의 경우, 존재하지 않는 word(vocab에 등록되지 않은 word)에 대해서는 vector로 표현해주지 못합니다. 가령 word2vec의 vocabulary에 "research"는 있지만, "researches"는 없는 경우가 있다고 할게요. 사람이 보기에는 'researches'가 사람이 보기에는 매우 비슷한 단어이며, 따라서 비슷한 벡터가 나오는 것이 맞지만, 에러가 발생하죠. 
- 다시 말하면, word2vec은 명확하게 정의된 vocabulary에 대해서, vocabulary에 존재하는 단어들은 모두 서로 다르다, 라는 가정하고, 학습을 하게 됩니다. 즉, 문장 상에서 research와 researches의 앞 뒤 노드들이 의미적으로 비슷하지 않을 경우에는 유사도 낮게 나올 수도 있다는 것을 의미합니다. 
- 따라서, word2vec의 경우 "형태적 유사성"을 고려하지 못함은 물론 frequency가 낮은 키워드들에 대해서는 효과적으로 필터링을 해주지 못합니다. 이런 종류의 문제를 "out of vocabulary"라고 하죠. 

## What is FastText? 

- FastText에 구현된 방법론은 논문 [Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606)에 근거합니다. 그리고 논문 제목에서 보이는 것처럼, fasttext는 각 word의 subword information 정보를 활용하여, word를 벡터화하죠. 
- fastText의 기본 원리는 단어에 존재하는 "morphological structure"를 활용하여, 단어의 의미 정보를 추출해내는 것입니다. 이는, 전통적인 traditional word embedding 방식인 word vocabulary에 근거한 word embedding 방식에서는 존재하지 않았던 것이죠. 따라서, 기존의 word2vec의 경우에는 word vocabulary에 존재하지 않는 "새로운 단어"에 대해서는 vector로 표현할 수 없었습니다. 

![morphological structure](https://www.cs.bham.ac.uk/~pjh/sem1a5/pt2/pt2_intro_morph_1.gif)

### Enriching Word Vectors with Subword Information 초록 초월번역 

- 논문의 초록을 번역하면 대략 다음과 같습니다. 
- 연속된 단어를 표현하는 방식(Continuous word representation)에 있어서, unlabeled corpora에 대해서 학습하는 것이 충분히 의미있다는 것을 word2vec과 같은 많은 NLP의 연구들이 증명했다. 
- 다만, 대부분의 연구들은 단어의 morphology를 무시하였으며, vocabulary에 존재하는 word들에 대해서 각각 구별되는(distinct) vector를 적용하였다는 한계를 가진다. 특히, 이는 아주 큰 vocabulary와 희소한 단어들에게 한계가 될 수 있다. 
- 따라서, 이 연구에서는 각 단어들을 "bag of character n-gram"으로 표현하였으며, 이를 통해 word를 character n-gram의 합으로 표현하게 됩니다. 
- 이를 통해 어떤 word가 vocabulary에 존재하지 않더라도, character n-gram으로 표현하여, 새로운 단어에 대한 vector를 빠르게 예측할 수 있습니다.

### When to use FastText

- fastText의 기본 원리는 단어에 존재하는 "morphological structure"를 활용하여, 단어의 의미 정보를 추출해내는 것입니다. 이는, 전통적인 traditional word embedding 방식인 word vocabulary에 근거한 word embedding 방식에서는 존재하지 않았던 것이죠. 따라서, 기존의 word2vec의 경우에는 word vocabulary에 존재하지 않는 "새로운 단어"에 대해서는 vector로 표현할 수 없었습니다. 
- word2vec과 fastText를 비교해보면, fastText가 word2vec에 대해서, 특히, corpus의 수가 충분하지 않고 형태적 처리(syntactic task)에 대해서 유의미하게 뛰어난 것을 알 수 있습니다.
- semantic tast에 대해서는 word2vec이 조금 더 낫기는 하지만, 이는 corpus의 수가 늘어난다면 더 충분해지죠.
- 또한, 앞서 말한 바와 같이, FastText의 경우 ouf-of-vocabulary(OOV)에 대해서도 벡터로 표현할 수 있습니다(component char-ngram의 조합을 통해). 

## FastText Training.

- 그럼 이제 간단하게 gensim을 사용해서 fasttext 모델을 구현해보고 word2vec과 비교해보겠습니다.

### Corpus 

- 저는 간단한 작업을 할 거니까요, corpus를 다음과 같이 설정합니다.
- 우리의 corpus에는 i, am, a, boy, you, are, girl과 같은 vocabulary만이 존재하죠.

```python
# 다음과 같이 매우 간단한, 문장들을 corpus로 가정합니다.
sentences = [
    "I am a boy", "you are a girl"
]*10
sentences = [s.lower().strip().split(" ") for s in sentences]
```

### Build and Train word2vec and FastText

- word2vec, fasttext에 대해서 sentence를 학습시켜줍니다. 당연히 이 둘의 vocabulary는 동일하겠죠. 

```python
# ------------------------------------
# Word2vec Model.
WVmodel = gensim.models.Word2Vec(min_count=1, size=50)
WVmodel.build_vocab(sentences)
WVmodel.train(sentences, total_examples=len(sentences), epochs=300)
# ------------------------------------
# FastTest Model.
FTmodel = gensim.models.fasttext.FastText(min_count=1, size=50)
FTmodel.build_vocab(sentences)
FTmodel.train(sentences=sentences, total_examples=len(sentences), epochs=300)

# WVmodel, FTmodel 모두 같은 corpus로부터 생성되었기 때문에 vocabulary는 같습니다.
assert set(WVmodel.wv.vocab.keys()) == set(FTmodel.wv.vocab.keys())
```

### Infer Vector for Out-Of-Vocabulary

- `['boys', 'girls', 'your', 'bare']`라는 out-of-vocabulary에 대해서 vector를 뽑고, 현재 vocab에서 가장 유사하다고 생각되어지는 word와 그 유사도를 뽑아봅니다.

```python
# out of vocab에 대해서 word2vec, FastText의 결과가 다름을 보임.
print("=="*20)
out_of_vocabs = ['boys', 'girls', 'your', 'bare']
for oov in out_of_vocabs:
    print(f"Does WVmodel have <{oov}> in vocab?: {oov in WVmodel.wv.vocab}")
    try: # Word2vec의 경우 vocab에 없는 word의 경우 vector로 표현해주지 못함.
        print(f"vector of <{oov}> => {WVmodel.wv[oov]}")
    except Exception as e:
        print(f"- Exception: {e}")
    print("--"*20)        
    print(f"Does FTmodel have <{oov}> in vocab?: {oov in FTmodel.wv.vocab}")
    print(f"- vector of <{oov}> => {FTmodel.wv[oov][:2]}")
    most_similar_vocab = [f"{w}: {sim:.2f}" for w, sim in FTmodel.wv.most_similar(positive=[oov])]
    print(f"- {most_similar_vocab}")
    print("=="*20)
```

- 아래의 결과를 보시면, word2vec 모델의 경우는 각 단어들이 vocabulary에 없으므로 error를 발생시키는 반면, FastText의 경우는 없어도 error를 발생시키지 않습니다. 그리고, 형태적으로 유사한 단어들을 효과적으로 뽑아내어주죠. 
- 다만, "bare"의 경우는 "are"와 의미가 유사하다고 나오게 됩니다. 이는, 제가 학습한 corpus가 충분하지 않아서 발생한 것이기도 하고, 단지, 형태로만 보면 이 두 단어는 유사하니까요. 
- 다시 말해서, fastText는 vocab이 충분하지 않을 경우, 형태적인 유사성을 좀 더 많이 고려하게 된다는 이야기겠죠.

```
========================================
Does WVmodel have <boys> in vocab?: False
- Exception: "word 'boys' not in vocabulary"
----------------------------------------
Does FTmodel have <boys> in vocab?: False
- vector of <boys> => [-0.00340306 -0.00107505]
- ['boy: 0.72', 'a: 0.55', 'are: 0.51', 'am: 0.36', 'girl: 0.33', 'you: 0.30', 'i: 0.28']
========================================
Does WVmodel have <girls> in vocab?: False
- Exception: "word 'girls' not in vocabulary"
----------------------------------------
Does FTmodel have <girls> in vocab?: False
- vector of <girls> => [-0.01171619  0.01813882]
- ['girl: 0.90', 'are: 0.55', 'a: 0.49', 'you: 0.37', 'boy: 0.32', 'am: 0.21', 'i: 0.16']
========================================
Does WVmodel have <your> in vocab?: False
- Exception: "word 'your' not in vocabulary"
----------------------------------------
Does FTmodel have <your> in vocab?: False
- vector of <your> => [-0.01340261  0.02130295]
- ['you: 0.79', 'girl: 0.43', 'are: 0.42', 'a: 0.38', 'i: 0.31', 'boy: 0.29', 'am: 0.14']
========================================
Does WVmodel have <bare> in vocab?: False
- Exception: "word 'bare' not in vocabulary"
----------------------------------------
Does FTmodel have <bare> in vocab?: False
- vector of <bare> => [-0.01151661  0.00357832]
- ['are: 0.82', 'a: 0.47', 'you: 0.43', 'girl: 0.40', 'boy: 0.36', 'am: 0.27', 'i: 0.23']
========================================
```

### not in n-gram vocab

- 물론 그렇다고 해서 어떤 단어에 대해서도 다 vector를 추론해준다는 이야기는 아닙니다. 
- 아래와 같이 "hi"라는 단어를 넘기면 에러가 발생하죠. 저는 이미 vocab에 'i'가 존재하므로 'hi'에 대해서도 처리를 해줄 수 있을 거라고 생각했지만, 되지 않습니다. 다만, 'ham'은 됩니다('am'이 있으니까요). 관리하는 n-gram은 당연히 2-gram부터이며, 'hi'는 여기에 포함되지 않습니다.

```python
out_of_vocabs = ['hi']
for oov in out_of_vocabs:
    print(f"Does FTmodel have <{oov}> in vocab?: {oov in FTmodel.wv.vocab}")
    print(f"- vector of <{oov}> => {FTmodel.wv[oov][:2]}")
    most_similar_vocab = [f"{w}: {sim:.2f}" for w, sim in FTmodel.wv.most_similar(positive=[oov])]
    print(f"- {most_similar_vocab}")
    print("=="*20)
```

```
KeyError: 'all ngrams for word hi absent from model'
```

- 여기서 그렇다면 어떤 n-gram들이 있는지 뽑아내면 좋겠지만(마치. `WVmodel.wv.vocab`처럼요, 그 부분은 지원하지 않습니다. 
- 그 이유는 [github - facebook research - [unsupervised learning] Export ngram as text file? #21](https://github.com/facebookresearch/fastText/issues/21)을 읽어보시면 알 수 있는데요. 실제로 n-gram을 저장하는 것이 아니라, 따로 hash하여 처리하는 방식으로 개발하였기 때문에, 이를 반대로 가져올 수 없다고 합니다. 
- 다만, 저는 그렇다면 왜 그렇게 했는지 도 좀 궁금해지기는 하네요. 만약 제가 개발했다면, n-gram을 남긴 상태로 진행했을 것 같아요

### in vocabulary 

- 흔히들 out-of-vocabulary에 대해서만 쓰인다고 생각하지만, almost out-of vocabulary, 즉 빈도가 적은 단어들에 대해서는 형태적 유사성을 크게 고려하게 됩니다. 
- 아래 코드에서는 "boy"와 "boys"의 유사도를 비교하게 되며, corpus에서 "boys"의 경우는 단 1번만 등장하게 됩니다. 즉, rare word, almost out-of-vocabulary라고 할 수 있겠죠.

```python
import gensim

# 다음과 같이 매우 간단한, 문장들을 corpus로 가정합니다.
sentences = [
    "I am a boy", "you are a girl"
]*100 
sentences.append("we are boys")
sentences = [s.lower().strip().split(" ") for s in sentences]
# ------------------------------------
# Word2vec Model.
WVmodel = gensim.models.Word2Vec(min_count=1, size=50)
WVmodel.build_vocab(sentences)
WVmodel.train(sentences, total_examples=len(sentences), epochs=30)
# ------------------------------------
# FastTest Model.
FTmodel = gensim.models.fasttext.FastText(min_count=1, size=50)
FTmodel.build_vocab(sentences)
FTmodel.train(sentences=sentences, total_examples=len(sentences), epochs=30)

# WVmodel, FTmodel 모두 같은 corpus로부터 생성되었기 때문에 vocabulary는 같습니다.
assert set(WVmodel.wv.vocab.keys()) == set(FTmodel.wv.vocab.keys())

print(f"Word2vec similarity: {WVmodel.wv.similarity('boy', 'boys'):.4f}")
print(f"FastText similarity: {FTmodel.wv.similarity('boy', 'boys'):.4f}")
```

- word2vec의 경우 등장 빈도가 작으므로 처음부터 그 유사도가 매우 낮은 반면, FastText의 경우는 등장 빈도가 작으므로 형태적 유사도가 크게 영향을 주게 됩니다. 
- 따라서 결과를 보면 Fast Text의 경우, "boy"와 "boys"의 유사도가 word2vec과 달리 매우 크게 나오는 것을 알 수 있겠죠.

```
Word2vec similarity: 0.11250756680965424
FastText similarity: 0.8307760953903198
```

- `epoch`을 0으로 세팅한 다음에 유사도를 비교하면 다음과 같습니다. 즉, 아무것도 학습하지 않아도, 형태적인 유사도만으로 아래와 같은 결과가 나온다는 것이죠.

```
Word2vec similarity: -0.1181
FastText similarity: 0.3755
```

## wrap-up

- 정리하겠습니다. 
- word2vec의 경우는 단어의 앞 뒤 맥락을 고려하여 단어를 벡터로 표현하는 방식을 말합니다. 다만, 이 때 형태적으로 유사한 단어일지라도, 이를 전혀 고려하지 않고, "형태가 비슷해도 다를 수 있다"라는 것을 가정하고 시작합니다. 이로 인해, 빈도가 적은 단어들과, out-of-vocabulary에 대해서 잘 작동하지 못한다는 한계를 가지죠. 
- 반대로, fastext는 처음부터 "형태적인 유사성"을 고려합니다. 빈도가 적은 단어들과 out-of-vocabulary에 대해서는 "형태적인 유사성"이 있다고 가정하고 "형태적 유사성에 따른 'weight'"가 비교적 높게 반영되게 되죠. 따라서, fasttext에 대해서 전혀 학습을 하지 않고 vocabulary만 구성하였다면, "형태적 유사성"이 크게 고려됩니다. 
- "fastText가 형태적인 유사성을 고려해주고 하니까 더 좋은거 아니냐?"라고 말할 수도 있지만, 글쎄요. 많은 경우 그럴 수도 있겠지만, 단어의 학습량이 충분하지 않을 때, fasttext는 'bare'와 'are'를 비슷한 의미라고 판단하는 실수를 저질 수도 있습니다. 전혀 다른 의미인데도 불구하고 말이죠. 즉, 어떤 경우 fasttext는 형태적인 유사성을 고려하기 때문에, 더 왜곡된 결과를 만들어낼 수도 있다는 것이죠. 
- 다만, 그래도, 만약 현재 문서에 대해서 전처리하는 것이 어려울 때, 가령 모두 단수형으로 바꾸거나 하는 것이 어려운 많은 경우들에 대해서는, fasttext를 사용하는 것이 꽤나 효과적일 수 있을 것으로 보입니다.

## reference

- [gensim - tutorials - fasttext](https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py)
- [FastText, Word representation using subword](https://lovit.github.io/nlp/representation/2018/10/22/fasttext_subword/)
- [stackoverflow: fasttext is there a way export ngrams?](https://stackoverflow.com/questions/55121095/fasttext-is-there-a-way-export-ngrams)
- [github - facebook research - [unsupervised learning] Export ngram as text file? #21](https://github.com/facebookresearch/fastText/issues/21)