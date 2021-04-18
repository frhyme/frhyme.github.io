---
title: konlpy - extract nouns
category: python-lib
tags: python python-lib konlpy nlp
---

## konlpy - extract nouns

- konlpy를 사용하여 한글 문장에서 noun, pos등을 뽑아내는 방법을 정리합니다.
- konlpy에는 `Kkma`, `Hannanum`, `Okt(Twitter)`, `Komoran`, `Mecab`와 같은 형태소 분석기(POS tagger)가 존재합니다.
- 해당 형태소 분석기들은 익숙한 단어들에 대해서는 명사를 잘 뽑아주지만, 낯선 단어들에 대해서는 잘 뽑아주지 못합니다.

```python
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Mecab
from konlpy.tag import Komoran
from konlpy.tag import Okt


# NLP
pos_tagger_dict = {
    "Kkma": Kkma(), 
    "Hannanum": Hannanum(), 
    "Okt": Okt(), 
    "Komoran": Komoran()
}
# "Mecab": Mecab(), 
# Exception: Install MeCab in order to use it: http://konlpy.org/en/latest/install/

sentences = [
    "안녕하세요. konlpy에 대해서 공부한 내용을 정리합니다",
    "konlpy는 일반적인 단어들에 대해서는 명사를 잘 뽑아줍니다",
    "하지만, 파이썬이나 아이유나 파이콘처럼 낯선 같은 단어들은 추출이 잘 되지 않습니다",
    "따라서, 낯선 단어들이 많이 있는 경우에은 konlpy에 효과적으로 작동하지 않습니다."
]

for each_sent in sentences:
    print(f"sentences: {each_sent}")
    for tagger_name, each_pos_tagger in pos_tagger_dict.items():
        nouns = each_pos_tagger.nouns(each_sent)
        print(f"= {tagger_name:8s}: {nouns}")
    print("--" * 50)
```

- 아래를 보시면, 잘 뽑아주는 경우도 있지만, konlpy처럼 낯선 단어들의 경우 명사로 뽑아주지 않거나, "파이콘"과 같은 단어도 분리한다거나 하는 문제가 생기죠.

```plaintext
sentences: 안녕하세요. konlpy에 대해서 공부한 내용을 정리합니다
= Kkma    : ['안녕', '공부', '내용', '정리']
= Hannanum: ['안녕', '공부', '내용', '정리']
= Okt     : ['대해', '공부', '내용', '정리']
= Komoran : ['안녕하세요', '공부', '내용', '정리']
----------------------------------------------------------------------------------------------------
sentences: konlpy는 일반적인 단어들에 대해서는 명사를 잘 뽑아줍니다
= Kkma    : ['일반적', '단어', '명사']
= Hannanum: ['일반적', '단어들', '명사']
= Okt     : ['일반', '단어', '대해', '명사']
= Komoran : ['일반', '단어', '명사']
----------------------------------------------------------------------------------------------------
sentences: 하지만, 파이썬이나 아이유나 파이콘처럼 낯선 같은 단어들은 추출이 잘 되지 않습니다
= Kkma    : ['파이', '이', '아이', '아이유나', '유나', '파이콘', '콘', '낯', '단어', '추출']
= Hannanum: ['파이썬', '아이유', '파이콘', '단어들', '추출']
= Okt     : ['파이썬', '아이유', '파', '이콘', '낯선', '단어', '추출']
= Komoran : ['파이썬', '아이유', '파', '이콘', '낯선', '단어', '추출']
----------------------------------------------------------------------------------------------------
sentences: 따라서, 낯선 단어들이 많이 있는 경우에은 konlpy과 효과적으로 작동하지 않습니다.
= Kkma    : ['단어', '경우', '은', '효과적', '작동']
= Hannanum: ['단어들', '경우', '효과적', '작동']
= Okt     : ['따라서', '낯선', '단어', '경우', '은', '과', '효과', '작동']
= Komoran : ['낯선', '단어', '경우', '효과', '작동']
----------------------------------------------------------------------------------------------------
```

## Wrap-up

- 이는 해당 형태소 분석기들이 모두 "이미 학습된 상태"로 제공되고 기존에 학습된 rule대로 명사를 뽑아내어주기 때문이죠.
- 따라서, 적용한 한글 문장들의 데이터에 특이한 단어들이 많다면 해당 형태소 분석기를 사용하는 것은 적합하지 않습니다.
- 이를 개선하여, 현재 데이터에 대해서 학습을 진행하여 명사를 추츨할 수 있는 패키지인 [soynlp](https://github.com/lovit/soynlp)가 존재합니다. 이는 제가 다음 글에서 작성해보겠습니다.
