---
title: gensim - tutorial
category: python-libs
tags: python python-libs
---

## Intro. 

- 요즘은 자연어처리를 사용하여 논문을 써야 합니다. 주로, 전처리 쪽을 담당하고 있기는 하지만요. 
- 주로 `gensim`을 사용하고 있으며, [Gensim - Documentation](https://radimrehurek.com/gensim/auto_examples/index.html)에 있는 내용들을 공부하여 다음과 같이 정리하였습니다.

## 작성 시간 순.

- 2020년 03월 10일: [gensim - Core Tutorial - Core Concept]()
    - `gensim`의 기본 개념인 Document, corpus, vector, model에 대해서 정리하였습니다. 
- 2020년 03월 10일: [gensim - tutorial - word2vec - basic]()
    - `gensim`을 이용하여, word2vec 모델을 구현하고, 학습한 다음 사용할 수 있는 메소드 들에 대해서 정리하였습니다. 




- 2020년 04월 01일: [gensim - Tutorial - Word Mover Distance(WMD)]() 
    - Word Mover Distance(WMD)는 "사용자가 제출한 query(혹은 sentence)에 대해서 가장 관련 있는 문서를 찾도록 해주는 머신러닝 분야의 중요한 기술"입니다. 기본적으로 EarthMover's Distance와 유사하며, 두 sentence가 가지고 있는 word의 분포를 변활할때 필요한 "최소한의 비용"을 거리로 계산합니다. 
- 2020년 04월 01일: [Earth Mover's Distance and pyemd]() 
    - 추가로, gensim에서 WordMover Distance를 계산할 때 사용하는 라이브러리인 `pyemd`와 Earth Mover Distance에 대해서도 좀 더 자세하게 정리하였습니다.



## reference

- [Gensim - Documentation](https://radimrehurek.com/gensim/auto_examples/index.html)