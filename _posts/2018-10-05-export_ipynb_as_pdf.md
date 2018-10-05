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

- [여기에서 설치](http://tug.org/mactex/mactex-download.html)합니다. 용량이 32기가로 매우 크네요. 
