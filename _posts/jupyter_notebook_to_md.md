---
title: jupyter notebook 파일을 마크다운으로 편하게 변환합시다. 
category: python
tags: python jupyter-notebook markdown
---

## intro

- 파이썬으로 공부한 것들을 정리할 때, 보통 `jupyter notebook`을 활용합니다. 블로그에 포스트를 하려면 `markdown`으로 변환해야 하는데, `jupyter notebook`에서 마크다운으로 다운 받으면 해당 디렉토리에 바로 다운 되는 것이 아니라, 다운로드 폴더에 다운이 되고 이를 다시 옮겨야 하는 사소한 부수적인 작업이 생깁니다. **저는 정말 이런게 싫어요**

- 그래서 찾아보니까 [이런 내용](https://github.com/jupyter/nbconvert)을 찾을 수 있었습니다. 로컬에서 바로 옮길 수 잇는 것 같군요. 흠...