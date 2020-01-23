---
title: plt.annotate의 화살표 특성 제어하기 
category: python-lib
tags: python python-lib matplotlib arrow annotation font 
---

## arrow의 특성 제어하기 

- `matplotlib`로 그림을 그린 다음에, 설명을 추가할 때 종종 `plt.annotate`를 사용해서 화살표를 그려줍니다. 
- 그런데, 이때 화살표 특성을 추가하는 것이 낯설어서 기록해두려고 작성했습니다. 

```python
import matplotlib.pyplot as plt

## font 가져오기 
import matplotlib.font_manager as fm
BMDOHYEON = fm.FontProperties(fname='/Users/frhyme/Library/Fonts/BMDOHYEON_otf.otf')
#########

## 그림 그리기 
plt.figure(figsize=(12, 6))
plt.annotate('dd', ## 텍스트
             
             xy=(0.1, 0.4), ## 화살이 가르킬 위치 
             xytext=(0.8, 0.6), ## 텍스트 위치 
             fontsize=40, ## font 크기 
             fontproperties=BMDOHYEON, 
             arrowprops=dict(facecolor='red', ## 내부 색깔 
                             edgecolor='black', ## 선 색깔 
                             fill=True, ## 내부가 비어짐(fill white와 같은 )
                             shrink=0.15, ## 텍스트로부터 얼마나 떨어진 위치에서 화살표가 시작하는가? 0이 최소 1이 최대  
                             headwidth=80, ## 화살 너비
                             headlength=100, ## 화살 길이 
                             width=30, ## 화살표에서 화살이 아닌 부분의 너비  
                             linewidth=10, ## polygon의 선 
                             linestyle=':', ## 선의 특성 
                             alpha=0.8, ## 투명도, line, fill을 따로 지정할 수 있는지는 모르겠음. 
                             )
            )
plt.savefig('../../assets/images/markdown_img/180731_arrow_props.svg')
plt.show()
```

![](/assets/images/markdown_img/180731_arrow_props.svg)

- 이렇게 변경할 수 있습니다. 하하핫 

## wrap-up

- 찾아보니, 특성을 변경할 수 있는 것들이 좀 더 있습니다만, 일단 그 부분까지는 제가 굳이 커버할 필요가 없을 것 같아서 넘어갑니다. 


