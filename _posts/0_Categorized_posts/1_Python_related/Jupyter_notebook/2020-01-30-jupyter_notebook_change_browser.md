---
title: python - jupyter notebook web browser 변경하기.
category: python-libs
tags: python python-libs jupyter-notebook
---

## intro. 

- 저는 맥북을 쓰고 있습니다. 그래서 기본 브라우저는 보통 safari로 설정되어 있죠. 
- 저한테는 크롬이 주 웹 브라우저이고, 따라서 그냥 jupyter notebook은 safari에서 굴러가도록 하는 것이 필요에 따라서는 더 편할 때도 있습니다. 개발+웹브라우징이 모두 크롬에서 돌아가면 헷갈릴 때가 있거든요. 
- 하지만 그래도, 굳이 바꾸고 싶을 때가 있을 수 있으니, 바꾸는 방법을 설명합니다.

## change default web browser. 

- [stackoverflow에 질문](https://stackoverflow.com/questions/47772157/how-to-change-the-default-browser-used-by-jupyter-notebook-in-windows)이 올라와 있지만, 이 질문은 잘못되었습니다. 위처럼 실행해도 다음과 같은 오류만 발생하게 됩니다. 


```
[W 14:44:28.287 NotebookApp] No web browser found: could not locate runnable browser.
```

- 그래서, 더 찾아보니 [이 블로그의 내용](https://medium.com/@tyagi.sudarshini/change-default-browser-in-jupyter-notebook-mac-667b56a3274e)이 정확하더군요. 

### ~/.jupyter/jupyter_notebook_config.py

- 기본 폴더 내에 `.jupyter`라는 폴더가 있고, 그 안에 `jupyter_notebook_config.py`라는 python 파일이 있습니다. 없다면, 아래 커맨드를 쳐서 생성하시면 됩니다. 확장자가 json 등이 아니라, python이라는 것이 조금 신기하죠.

```
$ jupyter notebook --generate-config
```

- 해당 파일 내에 99번 째 라인에 가면 아래와 같은 코드가 있습니다. 

```python
#c.NotebookApp.browser = ''
```

- 이걸 아래처럼 바꿔줍니다. 

```python
c.NotebookApp.browser = 'open -a /Applications/Google\ Chrome.app %s'
```

- 그리고 실행하면, 잘 됩니다.

## reference

- <https://medium.com/@tyagi.sudarshini/change-default-browser-in-jupyter-notebook-mac-667b56a3274e>