---
title: plt.legend의 font 변경하기 
category: python-lib
tags: python python-lib matplotlib legend font 
---

## plt.legend의 font 변경하기.

- 대부분의 plt 구성요소에서는 그냥 다음과 같이 진행합니다.

```python

import matplotlib.font_manager as fm

## otf 파일을 읽고, 폰트프로터리로 만들고 
BMDOHYEON = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMDOHYEON_otf.otf')
BMJUA = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMJUA_otf.otf')
BMHANNA = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMHANNA_11yrs_otf.otf')
SDMiSaeng = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/SDMiSaeng.ttf')

## 필요할 때 넘겨줍니다. 
plt.annotate('스트링', fontsize=20, fontproperties=BMDOHYEON)
plt.xticks(fontproperties=BMJUA, fontsize=15)

```

- 당연히 `plt.legend()`에서도 `fontproperties`로 넘겨주면 된다고 생각했는데, 생각처럼 되지 않습니다. 

```python
plt.legend(fontproperties=BMJUA)
```

```
TypeError: __init__() got an unexpected keyword argument 'fontproperties'
```

- [stackoverflow에도 약간 대답이 부실하더라구요](https://stackoverflow.com/questions/21933187/how-to-change-legend-fontname-in-matplotlib/51721142#51721142). 처음 만들 때 값을 설정해서 한번에 넘겨주는 방식이 아니라, 일단 구성요소(legend)를 만들고 그 다음에, set method를 통해서 바꾸어주는 형식인 것 같아요. 마음에 들지 않아서 변경했습니다. 

## 이렇게 합니다. 

- 그래서 찾아보다 보니 다음처럼 하면 됩니다. 
- fontproperties에서 이름을 받아서, 이름을 `prop`으로 넘겨주면 됩니다. 


```python
import matplotlib.font_manager as fm
## your font directory 
font_path = '/Users/frhyme/Library/Fonts/BMDOHYEON_otf.otf'
## font_name 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.legend(prop={'family':font_name, 'size':20})
```

## wrap-up

- 어떤 경우에는 `fontproperties`를 넘기고, 어떤 경우에는 `fontproperties`의 이름을 넘겨야 합니다. 왜 이렇게 헷갈리게 되어 있는지 잘 모르겠군요. 