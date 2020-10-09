---
title: joblib을 사용하여, 병렬 프로그래밍을 수행하자.
category: python-libs
tags: joblib
---

## Intro - 왜 갑자기 병렬 프로그래밍이 필요해졌는가?

- 최근에, 간단한 계산을 코딩하던 중에, for loop를 약 10억번 돌려야 하는 일이 있었습니다.
- for 문 내의 구문들은 덧셈 뺄셈 정도로 매우 간단한 수준이었고, 각 구문들은 서로 독립적이었죠. 각 구문의 결과가 다른 구문에게 영향을 미치지 않았습니다.
- 그러함에도 불구하고, 그냥 python에서 for loop을 약 10억번 돌려버리면, 하드웨어가 좋지 않은 일반적인 상황(저처럼 맥북에어로 코딩하는 사람)에서는 계산시간이 매우 오래 걸리게 됩니다.

### Numba 는 좀 아쉬움

- 간단한 코드를 좀 더 빠르게 수행하기 위해서, [Numba](https://numba.pydata.org/)라고 하는 "python 그리고 numpy code를 기계어로 변환해주는 JIT컴파일러"를 사용해보기도 했습니다. 어렵게 써있지만, 그냥 각 함수 앞에 decorator로 `@jit()`를 붙이면 끝나는 문제이기는 합니다.
- 다만, 몇몇 data structure들에 대해서(가령 set) deprecation되고 있고, numpy의 몇몇 함수들도 아직은 쉽게 컴파일해주지 못합니다. 약간, Numba스럽게 코딩을 수정해야 하는 문제들이 발생하는 것이죠. 물론 시간이 지나면 해결될 문제이기는 합니다만.
- 따라서 좀 다른 방법으로 간단하게 빠르게 만들 수 있는 방법이 없을까? 고민하게 되었습니다.

## Joblib - parallel processing

- 그래서 parallel processing을 지원하는 python library를 찾아보던 중에, [joblib](https://joblib.readthedocs.io/en/latest/)이라는 라이브러리가 있어서 이 아이를 좀 사용해보기로 했습니다.
- 실제로 joblib은 parallel processing 외에 다른 기능들도 지원하지만, 일단 이 포스트에서는 "joblib을 이용하여 parallel processing하는 방법"만을 다루겠습니다. 다른 내용들은 다음 글에서 다룰게요.
- 

## Reference

- [joblib - documentation](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html)
- ['속도를 높이는' 병렬 처리를 위한 6가지 파이썬 라이브러리](http://www.itworld.co.kr/news/153149)
