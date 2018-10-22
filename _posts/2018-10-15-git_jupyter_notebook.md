---
title: git으로 Jupyter notebook 파일 관리하기 
category: python-libs
tags: python python-libs git jupyter-notebook jupyter vcs
---

## intro

- 저는 코딩을 jupyter notebook으로만 합니다(이 얘기는 매번 하는 것 같기는 합니다만). 코드 작성 중에 코드를 테스트 해보기도 편하고, 지금 잘 되고 있는지를 파악하면서 코딩하기가 편합니다. 
    - 단, 그래서 여러 cell로 구분되어 있을 경우 namespace에서 발생하는 문제점들이 있기는 하지만, 뭐 그래도 괜찮은 것 같아요. 

- 다만, 여기에 약간은 심각한 문제가 있는데, jupyter notebook이 웹브라우저 위에서 돌아가는 방식이다 보니까, 실수로 뒤로 가기를 누를 경우에 IDE에서 다른 웹페이지로 튕겨나갈 때가 있습니다. 기존 코드가 잘 살아 있다면 문제가 없지만 가끔 코드가 잘못되는 경우가 있어요. 

- 음, 간단하게 워드의 예를 들어봅시다. 워드를 사용하다가 실수로 잘못 저장하거나 하는 경우가 있잖아요? 그럴때 요즘 워드는 예전 히스토리를 통해서 비교적 간단하게 복구를 할 수 있습니다.
- 그런데 jupyter notebook은 그게 좀 어려워요. 가끔 뻗는 경우도 있고 그렇고. 

## wrap-up

- 처음에는 jupyter notebook과 git 을 섞어서 사용하는 방법을 정리해서 쓰려고 했는데, 자료를 좀 찾다보니 필요없을 것 같아요
- google에서 만든 [colab](https://colab.research.google.com/)을 이용하는 편이 더 좋습니다. 구글 드라이브 내에서 실행되는 것이라서, 구글 드라이브의 버전관리를 그대로 사용할 수 있습니다.
    - 버전관리라고 하니까 무척 거창해보이지만, 파일 내에 여러 저장 포인트가 있고, 해당 저장포인트로 돌아가는 것이 쉬운 편입니다. 
- 그래서, 다음에 그냥 [colab](https://colab.research.google.com/)을 사용해보고, 그 결과를 공유하는 포스트를 다시 쓰는 편이 나을 것 같네요. 


## wrap-up

- <https://cfss.uchicago.edu/fall2016/git06.html>
- <http://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/>