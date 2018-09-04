---
title: networkx github에 pull request 날리기
category: python-lib
tags: python python-lib networkx github pull 
---

## intro 

- [최근에 networkx github에 이슈를 하나 날렸습니다](https://github.com/networkx/networkx/issues/3129).
- networkx의 모든 layout(spring, shell 등)은 딕셔너리(key: node label, value: (x, y))로 리턴이 되는데, `rescale_layout`이라는 함수는 np.array로 인풋을 받습니다. 제 생각에 이건 좀 일반적인 느낌이 아니라고 생각이 되었고, 그래서 이걸 변형하는 것이 필요하다고 생각되었죠. 
- 아무튼 이슈에 올려 보니, 이런 답변이 왔습니다. 

> We wrote rescale_layout with those inputs to reduce the number of times we have to convert back and forth between arrays and dicts. How about implementing your suggestion as a new function rather than replacing the current one:

- 번역하면, "배열과 딕셔너리를 변환하는 횟수를 줄이기 위해서 rescale_layout 이라는 함수를 만들었다. 당신이 만든 이 함수를 새롭게 제안하는 것이 어떠냐"는 것이죠. 컨트리뷰션을 하라는 말인데, 뭐 해보기로 했습니다. 

## how to contribute it 

- [contributing guideline](https://github.com/networkx/networkx/blob/master/CONTRIBUTING.rst)을 읽어봅니다. 

- 간단히 말하면, 일단 fork 를 해서 새로운 리퍼지토리를 내 깃헙에 만들고, 
- git clone을 사용해서 로컬 컴퓨터에 설치하고, 
- 코드를 변경하거나 추가합니다. 
- 그다음 pull request를 날립니다(git command를 사용해서 해도 되는데, 저는 그냥 github에서 GUI로 진행했습니다). 
- 그럼 [이렇게 pull request가 생성](https://github.com/networkx/networkx/pull/3142)된 것을 볼 수 있습니다. 


## wrap-up 

- 영어를 잘해야 된다, 라는 생각이 오랜만에 들구요. 특히 해당 커밋이 적합하냐를 가지고 키보드배틀을 떠야 할 수도 있는데, 이렇게 못해서는 안된다 라는 생각이 듭니다. 
- 뭐, 일단은 날렸습니다. git을 잘 사용하지는 못해서, 이렇게 해도 되나 싶기는 한데, 뭐 일단 진행상황을 보면서 잘하고 있는지 보도록 하겠습니다. 