---
title: 확률적 언어 모형을 만들어서, 그럴듯한 문장을 생성합니다. 
category: python-lib
tags: python python-lib nltk numpy counter movie_reviews
---

## 확률모형을 이용하여 그럴법한 문장을 만들어봅시다 

- [이 포스트](https://datascienceschool.net/view-notebook/a0c848e1e2d343d685e6077c35c4203b/)를 참고하여 코드와 내용을 아주 조금 수정하였습니다. 
- 저는 보통 말을 할때, 전체 문장을 다 만든 다음에 말을 하지 않아요. 약간 말을 하면서 뱉어진 단어가, 새로운 단어를 끌고 온다는 느낌으로 말을 하게 될때가 많습니다. 사실 대부분의 사람이 그렇지 않을까? 싶기도 하구요. 
- 확률적 언어 모형이란, 사실 이것을 참고하여 만들어진 것 같아요. '말'이라는 것은 이미 말해진 것(context)에 의해서 나올 수 있는 종류의 단어들이 결정되고, 거기서 어떤 확률에 의해서 어떤 단어가 나올지 결정된다고 봅니다. 
    - 그 context의 깊이? 혹은 거리 를 결정할 수 있는데, 1칸일 경우에는 unigram, 2칸 일 경우에는 bigram, 3칸 일 경우에는 tri-gram이 됩니다. 
    - 당연히, 이 깊이가 깊어질수록 더 잘 예측하고, 문장도 더 잘 생성할 수 있겠죠? 당연한겁니다. context가 'I'일 때와, context가 'I', 'am'일 때는 에측할 수 있는 정도가 다르겠죠. 
- 이를 직접 코딩해보면 다음처럼 할 수있습니다. 물론 제가 앞서 말씀드린 포스트를 참고해서 약간 수정한 코드입니다. 

## code 

### required library and reading data 

- `nltk`에 있는 movie_review를 활용하여, 확률적 모형을 구성합니다.
- 읽어들이고, `map`, `filter`를 활용하여 읽었습니다. 
- 또한, 문장 앞 뒤에, 'SS', 'SE'를 각각 넣어줍니다. 이렇게 해줘야, petri-net에서 stard, end를 만들어주는 것과 유사한 형태. 

```python
import nltk
import numpy as np 
from nltk.corpus import movie_reviews
from collections import Counter

nltk.download('movie_reviews')
nltk.download('punkt')
"""
- sentence의 앞에는 SS(setence start), 뒤에는 SE(sentence end)를 넣어준다. 
- 단어의 수가 4개 이상인 경우에 대해서만 고려
"""
sentences = map(lambda w_lst: ['SS']+w_lst+['SE'], movie_reviews.sents())
sentences = filter(lambda w_lst: True if len(w_lst) >= 5 else False, sentences)
sentences = list(sentences)
```

### make bigram

- 코드는 복잡해 보이지만, 다음으로 정리할 수 있습니다. 
    - 문장에서 연속된 bigram을 다 뽑고
    - bigram은 각각 context, word로 구분되며
    - context별로 word의 확률적 분포를 계산한다. 

```python
def calculate_bigram(sentence_lst):
    """
    - bigram을 만들고, 단어가 나왔을 때, 그 다음에 어떤 단어가 나올 condition prob을 만든다
    - Counter말고 dictionary로 만들어도 되는데, most_common이 있기 때문에 Counter을 사용함
    - 만약 tri-gram을 만들 경우에는 nested Counter가 3개가 나오게 된다. k1, k2, k3
    """
    bigram_dict = Counter()
    for w_lst in sentence_lst:
        bigram_in_s = [(w_lst[i], w_lst[i+1]) for i in range(0, len(w_lst)-1)]
        for bigram in bigram_in_s:
            w1, w2 = bigram
            if w1 not in bigram_dict.keys():
                bigram_dict[w1] = Counter({w2:1})
            else:
                if w2 not in bigram_dict[w1].keys():
                    bigram_dict[w1][w2] = 1
                else:
                    bigram_dict[w1][w2] += 1
    ## normalization 
    for context in bigram_dict.keys():
        sum_v_in_context = sum(bigram_dict[context].values())
        for k in bigram_dict[context].keys():
            bigram_dict[context][k] /= sum_v_in_context
    return bigram_dict
```

### sentence_score

- 문장을 넣었을 때, 이 아이가, 얼마나 그럴싸하게 만들어진 문장인지를 평가합니다. 
- 간단하게, 앞서 계산한 확률적 모형으로, 나올 수 있는 가능성이 얼마나 되는가? 를 평가하죠. 
    - 사실 그냥 곱하기곱하기곱하기입니다.

```python
def sentence_score(w_lst):
    """
    - 그냥 p를 모두 곱해진 것과 값은 같음
    - np.log로 변환하고, 더해준다음, np.exp로 하는게 더 좋음 
    """
    bigram_prob = np.array([bigram[w_lst[i]][w_lst[i+1]] for i in range(len(w_lst) - 1)])
    bigram_prob = np.log(bigram_prob).sum()
    return np.exp(bigram_prob)
```

### generate_sentences

- 확률적 모형을 활용하여 문장을 생성합니다. 

```python
def generate_sentence(seed=None):
    if seed is not None:
        np.random.seed(seed)
    context, sentence = "SS", []
    while context in bigram.keys():
        """
        - random하게 적합한 w를 확률에 따라서 생성한다. 
        - np.random.choice(words, probs)와 방식이 같은데, np.random.choice의 경우 크기가 32가 넘어가면 안됨
        """
        words, probs = list(bigram[context].keys()), list(bigram[context].values())
        idx = np.argmax( np.random.multinomial(n=1, pvals=probs) )
        w = words[idx]
        if w == "SE": # 선정한 word가 문장의 끝이라는 말이므로, 종결함 
            break
        else:
            # 결과로 나온 문장을 보면 특수문자도 많고, 문제가 많은데, 이러한 부분은 여기서 if를 사용해서 조절해주는 것이 필요함. 
            # 나는 귀찮아서 하지 않았습니다. 하하하하핫
            sentence.append(' '+w)
        context = w # context update 
    return "".join(sentence+['.']).strip().capitalize()

### main function 
bigram = calculate_bigram(sentences) # bigram의 확률을 학습하여 정리
print("--------------------")
for i in range(0, 5):
    print("sentence {}:".format(i).upper())
    print(generate_sentence())
    print("--------------------")
```

- 다음과 같은 결과가 나오는데, 뭔가 맞는거 같기도 하고, 아닌것 같기도 합니다. 

```
--------------------
SENTENCE 0:
Once seemingly clean and an entertaining ..
--------------------
SENTENCE 1:
The clever artwork , as a possible job ..
--------------------
SENTENCE 2:
We ' s not nearly flawless , and not a story " ( catherine zeta - cliff , leaving prison - driller ?.
--------------------
SENTENCE 3:
Kenneth williams delivers one misstep of all are good plot line deliveries , and three films of his skin - in the director burton authored a black comedy when the pledge ( 7 / 10 ( but it is very different ..
--------------------
SENTENCE 4:
Scattershot and all these are strong performance as it ' s not a busy with by this if you could somehow produced ( damon , but loveable eddie murphy s wife is revealed , the first played in which serve as artificial this " m gonna tell if this movie involves a very impressive proficiency does give too much for the rock and stand - hour and consists of norm schrager nailed this film , its messages , the soviet leader of the constant self - staged action scenes and , and every situation to perform well ..
--------------------
```

- 한글로 바꾸어주면....이상한 문장들이 되는군요. 특히 길수록 전체 내용이 이상해지는데, 꼼꼼히 읽지 않고 대충 읽으면 그럴싸해보입니다. 

```
--------------------
SENTENCE 0:
일단 겉으로는 깨끗하고 재미있는 ..
--------------------
SENTENCE 1:
가능한 일로 영리한 삽화 ..
--------------------
SENTENCE 2:
우리는 거의 완벽한 것이 아니라 이야기가 아닙니다. "(캐서린 제타 클리프, 교도소를 떠나는 - 드릴러?
--------------------
SENTENCE 3:
케네스 윌리엄스는 모든 음모 중 하나를 잘못 전달합니다. 줄거리 감독 인 burton은 서약서 (7 / 10 (그러나 매우 다른 ..)를 할 때 흑인 코미디를 썼습니다.
--------------------
SENTENCE 4:
Scattershot과 이것들은 모두 당신이 어떻게 든 생산할 수 있다면 바쁜 것이 아니기 때문에 강력한 성능을 발휘합니다. (damon,하지만 사랑스러운 eddie murphy의 아내가 공개됩니다.이 영화는 인공적인 역할을합니다. 매우 인상적인 숙달은 바위와 시간에 너무 많은 것을주고, 규범 schrager가이 영화, 메시지, 꾸준한 자기 단계 액션 장면의 평의회 지도자, 그리고 잘 수행 할 모든 상황을 찍은 것으로 구성됩니다.
--------------------
```

## wrap-up

- 여기서는 간단하게 bigram에서의 확률적 모형을 만들었지만, 더 복잡한 형태로 확률적 모형을 만들 수 있을 것 같기도 합니다. probabilistical graphical model을 만들어서 재밌는 것들을 좀 해볼 수 있을 것도 같은데, 일단 조금 더 공부해보고, 나중에 진행해보겠습니다. 

## whole code 

```python
import nltk
import numpy as np 
from nltk.corpus import movie_reviews
from collections import Counter

nltk.download('movie_reviews')
nltk.download('punkt')
"""
- sentence의 앞에는 SS(setence start), 뒤에는 SE(sentence end)를 넣어준다. 
- 단어의 수가 4개 이상인 경우에 대해서만 고려
"""
sentences = map(lambda w_lst: ['SS']+w_lst+['SE'], movie_reviews.sents())
sentences = filter(lambda w_lst: True if len(w_lst) >= 5 else False, sentences)
sentences = list(sentences)

def calculate_bigram(sentence_lst):
    """
    - bigram을 만들고, 단어가 나왔을 때, 그 다음에 어떤 단어가 나올 condition prob을 만든다
    - Counter말고 dictionary로 만들어도 되는데, most_common이 있기 때문에 Counter을 사용함
    - 만약 tri-gram을 만들 경우에는 nested Counter가 3개가 나오게 된다. k1, k2, k3
    """
    bigram_dict = Counter()
    for w_lst in sentence_lst:
        bigram_in_s = [(w_lst[i], w_lst[i+1]) for i in range(0, len(w_lst)-1)]
        for bigram in bigram_in_s:
            w1, w2 = bigram
            if w1 not in bigram_dict.keys():
                bigram_dict[w1] = Counter({w2:1})
            else:
                if w2 not in bigram_dict[w1].keys():
                    bigram_dict[w1][w2] = 1
                else:
                    bigram_dict[w1][w2] += 1
    ## normalization 
    for context in bigram_dict.keys():
        sum_v_in_context = sum(bigram_dict[context].values())
        for k in bigram_dict[context].keys():
            bigram_dict[context][k] /= sum_v_in_context
    return bigram_dict
def sentence_score(w_lst):
    """
    - 그냥 p를 모두 곱해진 것과 값은 같음
    - np.log로 변환하고, 더해준다음, np.exp로 하는게 더 좋음 
    """
    bigram_prob = np.array([bigram[w_lst[i]][w_lst[i+1]] for i in range(len(w_lst) - 1)])
    bigram_prob = np.log(bigram_prob).sum()
    return np.exp(bigram_prob)
def generate_sentence(seed=None):
    if seed is not None:
        np.random.seed(seed)
    context, sentence = "SS", []
    while context in bigram.keys():
        """
        - random하게 적합한 w를 확률에 따라서 생성한다. 
        - np.random.choice(words, probs)와 방식이 같은데, np.random.choice의 경우 크기가 32가 넘어가면 안됨
        """
        words, probs = list(bigram[context].keys()), list(bigram[context].values())
        idx = np.argmax( np.random.multinomial(n=1, pvals=probs) )
        w = words[idx]
        if w == "SE": # 선정한 word가 문장의 끝이라는 말이므로, 종결함 
            break
        else:
            # 결과로 나온 문장을 보면 특수문자도 많고, 문제가 많은데, 이러한 부분은 여기서 if를 사용해서 조절해주는 것이 필요함. 
            # 나는 귀찮아서 하지 않았습니다. 하하하하핫
            sentence.append(' '+w)
        context = w # context update 
    return "".join(sentence+['.']).strip().capitalize()

### main function 
bigram = calculate_bigram(sentences) # bigram의 확률을 학습하여 정리
print("--------------------")
for i in range(0, 5):
    print("sentence {}:".format(i).upper())
    print(generate_sentence())
    print("--------------------")
```

## reference 

- <https://datascienceschool.net/view-notebook/a0c848e1e2d343d685e6077c35c4203b/>