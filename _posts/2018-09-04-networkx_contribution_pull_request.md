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

## commnet about pull request 

- pull request를 생성하고 기다리면, [해당 프로젝트에서 권한을 가진 멤버](https://github.com/dschult)가 코멘트를 남겨 줍니다. 코멘트는 대략 다음과 같아요. 

```
Thanks for this!

Just a couple comments -- mostly about getting the function integrated with the whole networkx API.

- You should include the new function in the __all__ variable defined at the top (to have it imported to the networkx namespace.
- You should add "See Also" sections to both rescale function's doc_string to refer to each other
- You should update the documentation page doc/reference/drawing.rst by adding the name of the new function to the list of layout functions
- You should add a few simple tests to networkx/drawing/tests/test_layout.py to make sure this function runs and gives reasonable answers.
- The first line defining pos_v unpacks the position tuple only to repack it as a tuple again. Could do: pos_v = np.array(pos.values()) or just remove the line and in the next line replace pos_v with np.array(pos.values()).
```

- 번역을 해보면 대략 다음과 같습니다. 

```
1) 해당 파일의 맨 윗줄에 있는 `__all__`이라는 변수에 니가 새로 만든 함수 이름을 집어넣고, ==> 고침
2) 두 가지 rescaled function(니가 만든 것, 원래 있는 것) 모두에 "See Also"섹션을 넣어서 서로 참고할 수 있도록 해라 ==> 고침 
3) doc/reference/drawing.rst 의 도큐멘테이션 페이지에 너의 새로운 펑션이름을 집어넣어라. ==> 고침. 
4) networkx/drawing/tests/test_layout.py 에 몇 가지 심플 테스트를 넣어라. ==> empty graph에 대해서 문제 없도록 고침 
5) 너의 첫번째 함수는 tuple을 패킹, 언패킹하는데, 이건 이상하니까 알아서 고쳐라. ==> 고침 
```

- 1), 3), 5)는 매우 간단하구요. 
    - 다만 5)의 경우는 말하는대로 고쳤더니, 오히려 문제가 생깁니다. `nx.rescale_layout` 경우는 2차원의 np.array를 input으로 받는데, `np.array(pos_v.values())`의 경우는 `np.array()`로 변환되지 않습니다. 따라서, 조금 변형해서 고쳤습니다. 
- 2)의 경우는 docstring에 다음 내용을 넣어줍니다. 

```
See Also
--------
rescale_layout
```

- 4)는 제가 직접 예외가 될 수 있는 테스트 펑션을 집어넣으라는 이야긴데요 흠. 대충 체크해보니까, empty dictionary에 대해서 제가 만든 코드가 작동하지 않습니다. 이 부분을 만들어서 테스트 펑션으로 넣어주고, 제 함수도 고쳤습니다. 

- 그리고 다음처럼 글을 써서 다시 pull request를 날립니다. 

```
There are some comment to integer it. and I fixed it all.

You should include the new function in the all variable defined at the top (to have it imported to the networkx namespace. ==> complete
You should add "See Also" sections to both rescale function's doc_string to refer to each other ==> complete
You should update the documentation page doc/reference/drawing.rst by adding the name of the new function to the list of layout functions ==> complete
You should add a few simple tests to networkx/drawing/tests/test_layout.py to make sure this function runs and gives reasonable answers. ==> complete, make simple test for checking empty graph
The first line defining pos_v unpacks the position tuple only to repack it as a tuple again. Could do: pos_v = np.array(pos.values()) or just remove the line and in the next line replace pos_v with np.array(pos.values()). ==> little changed it. However, pos_v = np.array(pos.values()) will raise error "AttributeError: 'dict_values' object has no attribute 'shape'" in rescale_layout, so I should changed it to pos_v = np.array(list(pos.values())) with converting list
Thanks for your help.
If there were more issues or feedback to reflect it, Please let me know.
```

- 흐음...그런데, 이번에는 github 상에서 빨간 x 표시가 뜨면서 뭐가 잘 안되었다는 내용이 있습니다. build에서 뭔가 문제가 있는 것 같은데....몰라서 그냥 두었습니다....
    - 체크해보니, 괄호를 하나 안 넣었습니다...
    
- 고치고 다시 날립니다. [여기서](https://github.com/networkx/networkx/pull/3146) 볼 수 있어요. 

### trivia 

- 아무튼, 사소한 걸 좀 정리해봅니다. 
- 저한테 코멘트를 달아주신 분은 [Dan schult](http://www.colgate.edu/facultysearch/facultydirectory/dschult)라는 분입니다. 1984년에 대학교를 졸업하신 분인데(제가 태어나기도 전에 대학교를 졸업하시고, 아직까지도 직접 오픈소스 프로젝트에 참여하고 있다니 매우 신기한 부분이군요), 특히 우리나라는 나이가 많아질수록 오픈소스 프로젝트에 직접 참여하는 경향성이 줄어든다는 것을 고려해보면 매우 신기한 것이 아닌가 싶어요. 그리고 프린스턴 경제학 석사, 노스웨스턴 응용수학 박사입니다 쩐다앙. 
- 최근에 제출한 논문들은 대부분 복잡계+물리학 쪽인 것 같아요
- 그분이 계신 학교는 [colgate university ](https://en.wikipedia.org/wiki/Colgate_University)입니다. 잘 모르던 학교인데, 미국 동북부에서는 매우 유명한 사립 학교로군요. 


## wrap-up 

- 영어를 잘해야 된다, 라는 생각이 오랜만에 들구요. 특히 해당 커밋이 적합하냐를 가지고 키보드배틀을 떠야 할 수도 있는데, 이렇게 못해서는 안된다 라는 생각이 듭니다. 
- 뭐, 일단은 날렸습니다. git을 잘 사용하지는 못해서, 이렇게 해도 되나 싶기는 한데, 뭐 일단 진행상황을 보면서 잘하고 있는지 보도록 하겠습니다. 