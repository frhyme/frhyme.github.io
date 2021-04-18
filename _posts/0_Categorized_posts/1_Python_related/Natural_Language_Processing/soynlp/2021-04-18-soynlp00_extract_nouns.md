---
title: soynlp - extract nouns
category: python-lib
tags: python python-lib konlpy nlp soynlp
---

## soynlp - extract nouns

- konlpy의 경우 이미 학습된 데이터를 바탕으로 일반적인 단어들에서 명사를 뽑아내 줍니다. 그러나, 비교적 새로운 단어들인 "파이썬", "파이콘"과 사람이름과 같은 고유명사들에 대해서는 명사를 잘 추출해주지 못하죠. 따라서, 만약 내가 가지고 있는 corpus가 특이한 vocabulary를 가지고 있다면, konlpy를 사용해도 효과적인 결과를 얻지 못합니다.
- 이를 해결한 라이브러리가 바로 [soynlp](https://github.com/lovit/soynlp)입니다. 현재 제가 가지고 있는 corpus를 새로 학습해서 전체 corpus에서 명사를 가져오는 형태죠. 알고리즘은 대략, 낯선 단어라고 해도 "는"과 같은 조사 앞에 있는 단어라면 명사일 확률이 높다, 라는 측면으로 접근해서 bipartite한 Left - Right Graph를 만들어서 처리해주는 것 같습니다. 다만, 문장에서 명사를 각각 가져올 수 있는 것이 아니라, 전체 corpus에서 명사를 모두 뽑아서 가져와야 한다는 것이 konlpy와 비교했을 때 조금은 다른 점이죠.
- 우선은 다음 커맨드를 사용해서 설치합니다.

```bash
$ pip install soynlp
Collecting soynlp
  Downloading soynlp-0.0.493-py3-none-any.whl (416 kB)
     |████████████████████████████████| 416 kB 1.8 MB/s 
Collecting psutil>=5.0.1
  Downloading psutil-5.8.0-cp38-cp38-macosx_10_9_x86_64.whl (236 kB)
     |████████████████████████████████| 236 kB 27.2 MB/s 
Collecting scipy>=1.1.0
  Downloading scipy-1.6.2-cp38-cp38-macosx_10_9_x86_64.whl (30.8 MB)
     |████████████████████████████████| 30.8 MB 16.9 MB/s 
Collecting scikit-learn>=0.20.0
  Downloading scikit_learn-0.24.1-cp38-cp38-macosx_10_13_x86_64.whl (7.2 MB)
     |████████████████████████████████| 7.2 MB 23.1 MB/s 
Collecting threadpoolctl>=2.0.0
  Downloading threadpoolctl-2.1.0-py3-none-any.whl (12 kB)
Collecting joblib>=0.11
  Downloading joblib-1.0.1-py3-none-any.whl (303 kB)
     |████████████████████████████████| 303 kB 34.3 MB/s 
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, psutil, soynlp
Successfully installed joblib-1.0.1 psutil-5.8.0 scikit-learn-0.24.1 scipy-1.6.2 soynlp-0.0.493 threadpoolctl-2.1.0
```

## Do it 

- 간단한 코드는 다음과 같습니다.
  - soynlp에는 3가지 종류의 noun extractor가 있습니다. `LRNounExtractor_v2`가 `LRNounExtractor`에 비해 성능이 더 좋다고는 하는데, 저는 `LRNounExtractor`가 더 좋은 것 같아요. 다 사용해보고, 적합하다고 판단되는 것을 사용하시면 될것 같습니다.
  - 학습을 위한 `train_sentences`는 list of String으로 들어가면 됩니다.

```python
from soynlp.noun import LRNounExtractor
from soynlp.noun import LRNounExtractor_v2
from soynlp.noun import NewsNounExtractor


def get_noun_sorted_by_frequency(noun_extractor):
    """
    Description
    이미 학습되어 있는 noun_extractor의 noun을 
    frequency 내림차순으로 정렬하여 리턴함.
    """
    return_lst = list()
    nouns = noun_extractor.extract()
    for (each_noun, each_noun_info) in nouns.items():
        each_noun_dict = {
            "noun": each_noun,
            "frequency": each_noun_info.frequency, 
            "score": each_noun_info.score
        }
        return_lst.append(each_noun_dict)
    return_lst = sorted(return_lst, key=lambda x: x['frequency'], reverse=True)
    return return_lst

"""
train_sentences: list of String
"""
train_sentences = [
    "sentence1",
    "sentence2",
]

noun_extractor_dict = {
    "LRNounExtractor": LRNounExtractor(verbose=False), 
    "LRNounExtractor_v2": LRNounExtractor_v2(verbose=False), 
    "NewsNounExtractor": NewsNounExtractor(verbose=False)
}

for noun_ext_name, noun_ext in noun_extractor_dict.items():
    # train
    noun_ext.train(train_sentences)
    print(f"== extractor: {noun_ext_name}")
    # noun을 빈도 니림차순으로 정렬하여 리턴
    noun_lst = get_noun_sorted_by_frequency(noun_ext)
    for noun in noun_lst[:20]:
        print(noun)
    print("--" * 50)
```

## Wrap-up

- [soynlp](https://github.com/lovit/soynlp)를 개발하신 분의 블로그는 [lovit.github.io](https://lovit.github.io/)입니다. 저도 블로그를 운영하지만, 저는 그냥 공부한 것들을 마구마구 그냥 올리는 느낌이 좀 더 큰 데 반해서 이 분은 다른 사람들이 이해하기 쉽도록 글을 꼼꼼하게 작성해서 올리시죠. 다른 사람 블로그를 여러 번 들어가게 되는 일이 많지 않은데, 이 분 글은 좀 자주 보게 됩니다. 혹시 시간이 나시면 이 분 블로그에서 글을 한번 보셔도 많은 도움이 될 거에요.

## Reference

- [soynlp](https://github.com/lovit/soynlp)
- [lovit.github.io](https://lovit.github.io/)