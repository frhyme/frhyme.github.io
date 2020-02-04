---
title: python - jupyter notebook theme 변경하기. 
category: python-libs
tags: python python-libs jupyter-notebook
---

## jupyter notebook theme 변경하기. 

- 우선 세부적으로 설정을 바꾸고 싶으신 분들은 [jupyter notebook 커스토마이징하기.](https://frhyme.github.io/python-lib/jupyter_notebook_font_change/)라는, 제가 전에 쓴 글을 봐주시면 됩니다. 하지만, 가능하면 하나하나씩 설정을 바꾸지 마시고, 테마로 한번에 뜯어고치시는 것이 유지보수 측면에서 훨씬 좋습니다.

- 일단 `jupyterthemes`를 설치해줍니다. 

```
pip install jupyterthemes
```

- 다음을 치면 적용할 수 있는 테마들이 쭉 뜨죠. 

```
jt -l 
```

- 적용할 수 있는 테마는 다음과 같습니다.

```
Available Themes:
   chesterish
   grade3
   gruvboxd
   gruvboxl
   monokai
   oceans16
   onedork
   solarizedd
   solarizedl
```

- 그 다음 특정 테마를 적용하려면 다음과 같이 하면 됩니다. 저는 `chesterish`를 적용했어요.

```
jt -t themename
```


