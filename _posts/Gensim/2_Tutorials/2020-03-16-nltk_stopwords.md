---
title: nltk - corpus - stopwords
category: python-libs
tags: python python-libs nltk stopwords
---

## 2-line summary 

- stopwords는 보통 "너무 빈번하게 나와서 아무 정도가 없는 'a'와 같은 단어들"을 말합니다. 
- 그리고,`nltk.corpus.stopwords.words('english')`에 이미 정의되어 있죠.

## stopwords and nltk.stopwords

- 자연어처리를 할때, 너무 빈번하게 나와서, 아무의미 없다고 판단되는 단어들을 보통 ["stopword"](https://en.wikipedia.org/wiki/Stop_words)라고 부릅니다. 가령, 'a', 'the'와 같은 단어들은 모든 구문(phrase)들에 매우 많이 등장하며 그렇기 때문에 아무 의미를 가지지 못합니다. 
- 사실 연구자 혹은 분석가가 자연어처리중에 보면, "아 이 단어는 제외해야겠구나"라는 생각이 옵니다. 앞에서 본 것처럼 너무 명확하고, 아무 의미가 없는 것이니까요. 
- 혹은 [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) 값을 사용할 수도 있습니다. 즉, TF-IDF는 "Term Frequency - Inverse Document Frequency"를 말하며, 키워드의 빈도(TF)가 클수록 크고, 등장한 문서의 비율(DF)가 클수록 작아지죠. 즉, DF가 클수록 작아지며 보통 stopword는 DF가 큽니다. 대부분의 문서에서 많이 등장한다면 제외하는 것이 좋겠죠.
- 또한, `nltk.corpus.stopwords.words('english')`를 사용해서 보편적으로 사용되는 stopwords를 다음처럼 가져올 수도 있죠. 

```python 
import nltk

print("== nltk.corpus.stopwords.words('english')")
en_stop_words = set(nltk.corpus.stopwords.words('english'))
for i, w in enumerate(en_stop_words):
    print(w, end=" ")
    if (i+1)%10==0:
        print("")
print("=="*20)
```

- `nltk.corpus.stopword` 에는 다음 단어들이 포함되어 있죠. 보면 대략 합당하고 느껴집니다.

```
========================================
== nltk.corpus.stopwords.words('english')
----------------------------------------
mustn more when now m their d too we her
couldn't ours with most were and off hasn haven him
shan't aren you've during being ve mightn should've because doesn't
its yours haven't should couldn didn't do hadn't s just
about she you'd for myself so other am had which
ourselves doesn who my did to won't have again at
all these few before wasn wasn't that very by needn
there or this doing further of re shan each an
itself shouldn't ain be weren same why ll only once
then above you'll mightn't isn't was where been our under
not if i no own your over are in you
can out having it's than hadn how you're me here
a y between isn does that'll both yourselves mustn't such
yourself until ma hasn't into whom don is some o
through herself needn't t shouldn what down himself against any
but won as she's themselves from on below aren't the
they wouldn theirs will weren't hers don't them his didn
up while has wouldn't he after it nor those 
```

## remove stopword from corpus

- 따라서, 자연어처리를 할때, 다음처럼 stopword를 지워주고 진행하는 것이 좋습니다. 
- 그 과정은 그냥 다음과 같죠.

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sentences_with_stopwords = [
    "I am a boy", 
    "you are a girl", 
    "he is a man",
]
# 우선 word tokenize
sentences_with_stopwords = [word_tokenize(s.lower().strip())
                            for s in sentences_with_stopwords]

# stopword에 포함되는 word들은 모두 제외함.
sentences_without_stopwords = [
    [w for w in w_l if w not in stopwords.words('english')]
    for w_l in sentences_with_stopwords
]
print("=="*20)
for s1, s2 in zip(sentences_with_stopwords, sentences_without_stopwords):
    print(f"{s1} => {s2}")
print("=="*20)
```

```
========================================
['i', 'am', 'a', 'boy'] => ['boy']
['you', 'are', 'a', 'girl'] => ['girl']
['he', 'is', 'a', 'man'] => ['man']
========================================
```

## wrap-up 

- 다만, stop-word를 없애는 것이 좋은지 아닌지는 직접 판단해야 합니다. 만약 기존 sentence에서 stopwords를 없애면, 기존에 비해서 word간의 간격이 짧아지죠. 저라면, 충분한 데이터가 있다고 생각되면 stopword를 없애지 않고, 없다고 판단되면 없애도록 하겠습니다.
- 또한, 그전에, 전체 문서의 등장 비율인 Document-Frequency를 파악한 다음 분포에 따라서 일정한 기준에 맞춰서 제외하는 것이 좋겠죠.

## reference

- [geeks for geeks: removing stop words in nltk python](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/)