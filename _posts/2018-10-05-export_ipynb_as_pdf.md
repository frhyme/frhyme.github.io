---
title: jupyter notebook을 ipynb로 익스포트하기 
category: python-libs
tags: python python-libs jupyter-notebook pdf ide macos
---

## intro 

- 다들 IDE를 뭘 쓰시는지 모르겠습니다만, 저는 jupyter notebook을 사용하고 있습니다. 
- 다양한 장점이 있지만 테스트를 하면서, 코딩을 하는데 최적화되어 있다고 생각해요. 
- 또한 마크다운과 코드를 함께 쓸 수 있기 때문에 협업측면에서도 매우 좋다고 생각하구요. 

## so what 

- 아무튼 jupyter notebook으로 작업한 내용을 pdf로 꽤 예쁘게 뽑아낼 수 있다고 알려져 있습니다만, export notebook as pdf를 하면 아래와 같은 에러가 뜨는 경우들이 있습니다. 

```
500 : Internal Server Error
The error was:
nbconvert failed: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.
```

- 정리하면, xelatex가 PATH에 없고, 없으면 설치해라 라는 말이죠. 
- 일단 [해당 링크](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex)에 들어가봅니다. 

- 이래저래 말은 길지만, 간단하게 말하면, 

> For converting to PDF, nbconvert uses the TeX document preparation ecosystem. 

- TeX를 설치하면 다 해결된다는 이야기죠. 

## mactek

- [여기에서 설치](http://tug.org/mactex/mactex-download.html)합니다. 용량이 3.2기가로 매우 크네요. 
- 설치합니다.
- 설치했는데도 안되네요. 

## xelatex

- 설치 오류는 이전과 같았습니다. 여전히 `xelatex not found`였죠. 

- 그럼 말 그대로 [xelatex를 한번 설치해보도록 합니다](http://www.texts.io/support/0001/). 

- 그래도 안됩니다. .......

- 일단 다 지우기로 합니다. 

## where is texlive??

- 여기서 또 빡치는 포인트는, 이전에 설치한 Mactex의 설치 포인트가 일반적이지 않다는 것입니다. 
- `/usr/local/texlive`에 있는데, 여기는 GUI로 들어갈 수는 없습니다. 
- 여기에 들어가려면, finder에서 폴더로 이동을 누른 다음, 저 텍스트를 그대로 쳐 줘야 합니다. 



## Reveal.js

- 바로 pdf로 변환하는 것은 포기하고, 다만 
- Reveal.js를 이용해서 html 로 변환하고, 그 다음에 pdf로 변환하니까 잘 되기는 하네요. 
- 다만, 이 경우에도, pdf로 변환하면, 코드가 다 망가집니다. 


## wrap-up

- 그저, jupyter notebook을 pdf로 바꾸는 것만을 원한 것 뿐인데, 너무 일이 커져버린 느낌이 있습니다. 
- 함부로 뭔가를 설치하지 맙시다. 
- 그리고 그냥 html 문서로 공유합시다. 뭐가 문제입니까 좋기만 한데. 


## reference

- <http://hellogohn.com/post_one193>