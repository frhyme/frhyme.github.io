---
title: gensim - model - Phrases
category: python-libs
tags: python python-libs gensim phrases gensim-model bigram ngram
---

## 2-line summary 

- `gensim.Phrases`는 텍스트에서 빈번하게 등장하는 bi-gram을 발견해주는 모델입니다. 
- 만약, 2개의 word-token만 붙이는 것이 아니라, 여러 word들을 이어 붙이고 싶다면, `gensim.Phrases`을 반복하여 새로운 모델을 만들어줘야 합니다. Bigram => BiBigram => BiBigram

## gensim.Phrases

- 주어진 text들로부터 간단하게라도 단어의 빈도들을 파악하려고 할 때, 중요한 것은 문장에서 "하나의 단위"를 어떻게 정의할 것인가 죠. 
- 가령, "research and development"라는 단어 집합이 있다고 합시다. 그리고 text들에서 해당 단어집합이 그대로 반복된다면, "research", "and", "development"라는 3개의 단어로 쪼개지 않고, "research and development"라는 단어를 하나의 집단으로 이해하여 문장으로부터 뽑아내는 것이 훨씬 아름답겠죠. 
- 물론, 이는 어려운 작업이지만, `gensim.Phrases`를 사용해서 비교적 간단하게 뽑아낼 수 있습니다. 

## extract bigram using `gensim.Phrases`

- bigram은 문장에서 앞뒤로 연속된 단어 조합을 말합니다. 가령 `[i, am, a, boy]`가 있다면, "i_am", "am_a", "a_boy"가 bigram이 되죠. 
- `gensim.Phrases`을 사용하면, 상대적으로 빈번히 등장하는 bigram을 찾아낼 수 있습니다.

### extract word-list from sentences

- 일단 다음과 같이 간단한 문장들이 있다고 하겠습니다. 그냥 임의로 집어넣은 것이며, 어떻게 동작하는지를 보여주기 위해서 일단 만든 것이죠. 
- `sentences`를 우선 " "(스페이스)를 기준으로 모두 쪼갭니다.

```python
sentences = [
    'it is a science',
    'research and development', 
    'research and development',
    'computer science'
]
word_lsts = [s.lower().strip().split(" ") for s in sentences]
for w in word_lsts:
    print(w)
```

```
['it', 'is', 'a', 'science']
['research', 'and', 'development']
['research', 'and', 'development']
['computer', 'science']
```

### Build and Train Phrases model. 

- 그다음에는 `gensim.Phrases`에 만들어진 word_lst를 넘기면 끝납니다. parameter를 설명하자면,  
    - `min_count`: 최소한 min_count보다 많이 등장한 token들에 대해서 만들어줌
    - `threshold`: default는 10.0이며, 이 값이 작을수록 두 token을 붙여서 새로운 token으로 만드는 경향이 높아집니다. 즉, 값을 조절하면서, 잘 만들어지는지를 체크해야겠죠. 무조건 양수여야 하며, 웬만하면 복합어로 만들고 싶은 경우, `0.01`과 같은 값을 넘겨줍니다. 
    - `delimiter`: token들이 합쳐져서 새로운 word가 만들어질 때, 연결점을 어떻게 표시할지를 의미합니다. 가령 `"a"`와 `"b"`를 합치고, 우리가 delimiter로 `b"_"`를 넘겨줬다면, `"a_b"`가 만들어지겠죠. 다만, string으로 넘기는 것이 아니라, byte string으로 넘겨줘야 합니다. 이로 인해 생기는 이슈는 뒤쪽에서 다루도록 할게요.
- 그리고, 만들어진 모델 `Bigram_Model`에 대해서 `Bigram_Model[w_l]`를 통해 해당 word_lsts에서 타당한 bigram list를 생성할 수 있습니다.


```python
import gensim
"""
------------------------------
# min_count : token의 최소 등장 수 
------------------------------
# threshold: 10.0 (default) 높을수록 연결을 안해줌
------------------------------
# delimiter: 새롭게 만들어지는 token의 연결 표시 부호(byte string)
"""
Bigram_Model = gensim.models.Phrases(word_lsts, min_count=1, threshold=1, delimiter=b"_")

for w_l in word_lsts:
    print(f"raw    sentences: {w_l}")
    bigram_s = Bigram_Model[w_l]
    print(f"Bigram sentences: {bigram_s}")
    print("--"*20)
```

- 다음에서 보시는 것처럼, 조금 빈번한 경우에는 두 단어가 합쳐져서 새로운 단어로 만들어지죠.

```
raw    sentences: ['it', 'is', 'a', 'science']
Bigram sentences: ['it', 'is', 'a', 'science']
----------------------------------------
raw    sentences: ['research', 'and', 'development']
Bigram sentences: ['research_and', 'development']
----------------------------------------
raw    sentences: ['research', 'and', 'development']
Bigram sentences: ['research_and', 'development']
----------------------------------------
raw    sentences: ['computer', 'science']
Bigram sentences: ['computer', 'science']
----------------------------------------
```

### Phrases.vocab: key and value

- 다만, 여기서 해당 모델의 vocab이 어떻게 구성되어 있는지 조금 더 자세하게 보겠습니다. 
- `Bigram_Model.vocab.keys()`를 통해서 현재 만든 모델의 vocabulary를 확인할 수 있습니다만, 결과를 보면 모든 string 앞에 `b`가 붙어 있는 것을 알 수 있습니다. 이는 해당 string이 byte string이라는 말이죠. 

```python
print("== Bigram_Model.vocab.keys()")
print(Bigram_Model.vocab.keys())
print("--"*20)
```
```
== Bigram_Model.vocab.keys()
dict_keys([b'it', b'is', b'it_is', b'a', b'is_a', b'science', b'a_science', b'research', b'and', b'research_and', b'development', b'and_development', b'computer', b'computer_science'])
```

- 뭐 그래도 string 아니야? 라고 생각하실 수 있지만, 아닙니다. byte string과 string은 다를 자료형이고, 아래를 실행했을 때, 다른 결과가 나오게 됩니다. 즉, 어떤 word가 vocab게 있는지 확인하기 위해서는, `string.decode('utf-8')`로 변환을 한 다음 진행해야 한다는 것이죠. 

```python
print("it" in Bigram_Model.vocab.keys())
print(b"it" in Bigram_Model.vocab.keys())
```
```
False
True
```

- 그리고, `gensim.Phrases` vocab의 key는 min_count를 1로 설정했을 경우, 존재하는 모든 unigram과 bigram으로 구성됩니다. 그리고, value는 key의 등장 횟수를 말합니다. `collections.Counter`와 유사하며, 이미 빈도가 확인된 것이므로 각 key의 등장 횟수를 알고 싶다면, `gensim.Phrases.vocab[key]`로 접근해서 가져오면 됩니다.

```python
for word, word_count in Bigram_Model.vocab.items():
    word = word.decode('utf-8')
    print(f"{word:10} : {word_count:2d}")
```


### Scoring

- 두 token이 있을 때, 이 token을 연결할지 말지는 다음 scoring에 따라서 결정됩니다. 
- 두 token, `w1`, `w2`의 빈도를 곱한 값을 분모에 두고, `w1_w2`가 등장한 빈도를 분모에 두고 `min_count`를 빼줍니다. 그리고, vocab의 모든 단어로 multiply를 해주죠. 즉, "각각의 단어들이 등장했을 때 보다 "w1_w2"로 등장하는 비율이 얼마나 되는지를, 대략 계산한다고 보시면 됩니다.

```python
def scoring(bigram_str, vocab_counter):
    min_count = 1
    w1w2_count = vocab_counter[bigram_str]
    w1, w2 = bigram_str.split("_")
    w1_count, w2_count = vocab_counter[w1], vocab_counter[w2]
    return (w1w2_count - min_count)/(w1_count*w2_count) * len(vocab_counter)
```

- 이 scoring 방식을 사용하여 vocabulary에 존재하는 bigram에 대해서 다음과 같이 계산을 해주면 "research_and"와, "and_development"는 3.5가 나옵니다. 따라서, `threshold`를 3.5보다 크게 하면, 연결되지 않게 되죠.

```python
vocab_counter = {}
for w, w_count in Bigram_Model.vocab.items():
    vocab_counter[w.decode('utf-8')] = w_count
for k, v in vocab_counter.items():
    if "_" in k:
        print(k, scoring(k, vocab_counter))
```
```
it_is 0.0
is_a 0.0
a_science 0.0
research_and 3.5
and_development 3.5
computer_science 0.0
```

## Extract Tri-gram from text

- 기본적으로는 `gensim.Phrases()`를 사용해서 bigram을 생성하지만, 이를 반복적으로 수행하면, trigram을 만들 수도 있습니다. 
- 다만, 정확하게 보면, 늘 trigram이 되는 것이 아니라, 생성된 bigram word list를 input으로 bi-bigram work list를 만들어주는 것에 가깝죠. 
- 다음 코드에서 `Bigram_Model`과 `BiBigram_Model`을 만들고 vocab을 비교해봅니다.

```python
# BUILD and Train Bigram Model 
Bigram_Model = gensim.models.Phrases(word_lsts, min_count=1, threshold=1.0, delimiter=b"_")
# BUILD and Train BIBigram Model by output of Bigram Model
# 기존의 word-list를 그대로 사용한 것이 아니라, Bigram_Model에 집어넣고 
# 그 결과를 다시 집어넣어서 vocab을 만들고 train. 
BiBigram_Model = gensim.models.Phrases(Bigram_Model[word_lsts], min_count=1.0, threshold=1.0, delimiter=b"_")

Bigram_vocab_set = set(Bigram_Model.vocab.keys())
BiBigram_vocab_set = set(BiBigram_Model.vocab.keys())
print("== Bigram Model vocab")
print(Bigram_vocab_set)
print("--"*20)
print("== BiBigram Model vocab")
print(BiBigram_vocab_set)
print("--"*20)
print("== Bigram에는 있으나, BiBigram에는 없는 vocab")
print(Bigram_vocab_set - BiBigram_vocab_set)
print("== BiBigram에는 있으나, Bigram에는 없는 vocab")
print(BiBigram_vocab_set - Bigram_vocab_set)
print("--"*20)
print("=="*20)
```

- 결과를 보면, `Bigram_Model`의 vocab에는 "research"가 있지만, BiBigram에는 "research"가 없고, 대신 "research_and"가 들어가 있는 것을 알 수 있습니다. 반대로, `BiBigram_Model`에는 "research and development"가 들어가 있는 것을 알 수 있죠.
- 즉, bigram을 선형적으로 이어 붙여서, 가까운 놈들을 반복적으로 만들어주다보면 좀 더 넓은 범위의 phrase들을 파악해낼 수 있습니다. 

```
== Bigram Model vocab
{b'computer', b'a_science', b'science', b'research', b'and_development', b'computer_science', b'development', b'is_a', b'it_is', b'and', b'is',b'it', b'research_and', b'a'}
----------------------------------------
== BiBigram Model vocab
{b'it', b'computer_science', b'computer', b'is', b'science', b'development', b'research_and_development', b'a_science', b'research_and', b'it_is', b'is_a', b'a'}
----------------------------------------
== Bigram에는 있으나, BiBigram에는 없는 vocab
{b'research', b'and_development', b'and'}
----------------------------------------
== BiBigram에는 있으나, Bigram에는 없는 vocab
{b'research_and_development'}
----------------------------------------
```

## wrap-up

- 오늘 정리한 것은, 주어진 sentence에서 간단한 지표를 사용하여 빈번하게 등장하는 bigram을 만드는 방법입니다. `gensim.Phrase` 사용하며, threshold에 따라서 그 결과는 달라지게 되죠. 
- 한번에 tri-gram을 만들 수는 없고, 우선 bigram을 만든 다음 생성된 bigram에 대해서, 다시 이 아이들을 연결할 필요가 있는지 다시 체크합니다. 만약 이번에도 threshold를 넘긴다면, 이 아이들도 다시 연결해줘야 겠죠. 


## reference

- [gensim - models - Phrases](https://radimrehurek.com/gensim/models/phrases.html#gensim.models.phrases.Phrases)
- [stackoverflow: gensim phrases model scoring](https://datascience.stackexchange.com/questions/25524/how-does-phrases-in-gensim-work)