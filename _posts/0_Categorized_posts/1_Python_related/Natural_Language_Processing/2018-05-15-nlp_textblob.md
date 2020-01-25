---
title: textblob, nltk를 활용하여 간단하게 텍스트 처리합시다. 
category: python-lib
tags: python python-lib textblob nlp inflection

---

## text에 간단한 전처리를 하기 위해 textblob, nltk를 사용합시다.

- 사실 nlp에서 가장 중요한 것은 데이터 전처리입니다. 텍스트는 너무 중구난방이라서, 깔끔하게 정리해주는 게 굉장히 중요하고 또 필요합니다. 따라서 여기서는 비교적 단순하고 빠르게 사용할 수 있는 텍스트 처리 기법들을 정리합니다. 
- 사람들이 `nltk`를 많이 쓰기는 하는데, 요즘에는 `textblob`도 많이 쓰는 것 같아요. 얘가 비교적 빠르게 사용할 수 있는 것 같기도 합니다. 
- 그래서 여기서는 `textblob`에 있는 함수들을 활용하여 비교적 간단하게(다시 말하면 정교하지 않게) 텍스트를 처리하는 방법을 알아봅니다.

### singularize

- singularize만 잘해줘도 사실 많은 단어들이 정제됩니다. 여기서 보면, `textblob`의 경우 무리하게 복수를 변경해주는 것을 알 수 있습니다. 예를 들어 process ==> proces. 
- 따라서 가능하면 단어를 단수로 바꾸어줄 때는 `inflection`를 쓰는 것이 좋습니다. 
- 물론 `inflection`의 경우도 data 를 datum으로 바꾸거나 하는 경우가 있어서 확인이 필요함. 

```python
simple_sentence = "Business Process Management systems (BPMS) are a rich source of events that document the execution of processes and activities within these systems. "

print("""**inflection을 사용하여 singularize를 한 경우""")
from inflection import singularize
for w in simple_sentence.lower().split(" "):
    if w != singularize(w):
        print("{} ==> {}".format(w, singularize(w)))
print()
print("""**textblob를 활용하여 singularize를 한 경우 """)
from textblob import TextBlob
blob = TextBlob(simple_sentence.lower())
for w in blob.words:
    if w != w.singularize():
        print("{} ==> {}".format(w, w.singularize()))
```

```
**inflection을 사용하여 singularize를 한 경우
systems ==> system
events ==> event
processes ==> process
activities ==> activity

**textblob를 활용하여 singularize를 한 경우 
business ==> busines
process ==> proces
systems ==> system
bpms ==> bpm
events ==> event
processes ==> process
activities ==> activity
systems ==> system
```


## lemmatize vs. stemming 

- 둘 다 nltk.stem 아래에 있는 것을 보면 알 수 있듯이 이는 일종의 단어 가지치기 기법이다. 
    - lemmatize: 결과가 실제로 있는 단어.
    - stemming: 결과가 실제로 없는 단어일 수 있음.
- `singularize`를 쓰지 않고, `lemmatize`를 사용하는 것이 더 좋을 수도 있으나, 단 '복합어'에 대해서는 처리를 못해줌. 
    - 복합어일 경우에는 이를 split 한 다음 lemmatize를 먹이고 다시 합쳐주는 작업을 해야 하는 것으로 보임. 

```python
from nltk.stem import WordNetLemmatizer, PorterStemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
for w in ['increases', 'plays', 'business processes', 'business']:
    print("word: '{}', stemming ==> '{}', lemmatize ==> '{}'".format(w, stemmer.stem(w), 
                                                               lemmatizer.lemmatize(w)
                                                              ))
```

- 결과를 보면 lemmatize는 사전에 있는 단어를 출력하는 반면 stemming은 사전에 없는 단어를 출력함.

```
word: 'increases', stemming ==> 'increas', lemmatize ==> 'increase'
word: 'plays', stemming ==> 'play', lemmatize ==> 'play'
word: 'business processes', stemming ==> 'business process', lemmatize ==> 'business processes'
word: 'business', stemming ==> 'busi', lemmatize ==> 'business'
```


## extract sentence, word, n-gram, noun phrases, tags 

- `nltk`에서도 `textblob`과 비슷한 라이브러리들이 많이 있지만, noun phrase를 뽑는 것 같은 경우는 `nltk`에서 지원하지 않는 것 같다. 정확하게는 직접 뽑는 것이 없는 것이고 간단하게 코딩해서 만들 수 있는 부분이 있을 것 같기는 함. 

### using textblob

```python
simple_sentence = """
Business Process Management systems (BPMS) are a rich source of events that document the execution of processes and activities within these systems. 
"""
simple_text
from textblob import TextBlob
blob = TextBlob(simple_sentence).lower()
print("words: {}".format(blob.words))
print()
print("noun_phrases: {}".format(blob.noun_phrases))
print()
print("word and tags: {}".format(blob.tags))
print()
print("n grams: {}".format(blob.ngrams(2)))
print()
```

```
words: ['business', 'process', 'management', 'systems', 'bpms', 'are', 'a', 'rich', 'source', 'of', 'events', 'that', 'document', 'the', 'execution', 'of', 'processes', 'and', 'activities', 'within', 'these', 'systems']

noun_phrases: ['business process management systems', 'rich source']

word and tags: [('business', 'NN'), ('process', 'NN'), ('management', 'NN'), ('systems', 'NNS'), ('bpms', 'NN'), ('are', 'VBP'), ('a', 'DT'), ('rich', 'JJ'), ('source', 'NN'), ('of', 'IN'), ('events', 'NNS'), ('that', 'WDT'), ('document', 'VBP'), ('the', 'DT'), ('execution', 'NN'), ('of', 'IN'), ('processes', 'NNS'), ('and', 'CC'), ('activities', 'NNS'), ('within', 'IN'), ('these', 'DT'), ('systems', 'NNS')]

n grams: [WordList(['business', 'process']), WordList(['process', 'management']), WordList(['management', 'systems']), WordList(['systems', 'bpms']), WordList(['bpms', 'are']), WordList(['are', 'a']), WordList(['a', 'rich']), WordList(['rich', 'source']), WordList(['source', 'of']), WordList(['of', 'events']), WordList(['events', 'that']), WordList(['that', 'document']), WordList(['document', 'the']), WordList(['the', 'execution']), WordList(['execution', 'of']), WordList(['of', 'processes']), WordList(['processes', 'and']), WordList(['and', 'activities']), WordList(['activities', 'within']), WordList(['within', 'these']), WordList(['these', 'systems'])]
```

### using nltk 

```python
import nltk.tokenize

simple_text = """
Business Process Management systems (BPMS) are a rich source of events that document the execution of processes and activities within these systems. 
Business Process Management analytics is the family of methods and tools that can be applied to these event streams in order to support decision making in organizations. 
""".lower().strip()

print(nltk.tokenize.sent_tokenize(simple_text))
print(nltk.tokenize.word_tokenize(simple_text))

"""make n grams 
"""
from nltk import ngrams
print(list(ngrams(nltk.tokenize.word_tokenize("I am a boy"), 2)))
```

```
['business process management systems (bpms) are a rich source of events that document the execution of processes and activities within these systems.', 'business process management analytics is the family of methods and tools that can be applied to these event streams in order to support decision making in organizations.']
['business', 'process', 'management', 'systems', '(', 'bpms', ')', 'are', 'a', 'rich', 'source', 'of', 'events', 'that', 'document', 'the', 'execution', 'of', 'processes', 'and', 'activities', 'within', 'these', 'systems', '.', 'business', 'process', 'management', 'analytics', 'is', 'the', 'family', 'of', 'methods', 'and', 'tools', 'that', 'can', 'be', 'applied', 'to', 'these', 'event', 'streams', 'in', 'order', 'to', 'support', 'decision', 'making', 'in', 'organizations', '.']
[('I', 'am'), ('am', 'a'), ('a', 'boy')]
```

## Reference 

- <http://textblob.readthedocs.io/en/dev/>
- <https://dzone.com/articles/nlp-tutorial-using-python-nltk-simple-examples>