---
title: svg는 무엇이고, 또 파이썬에서 어떻게 읽을 수 있나요? 
category: python-lib
tags: python python-lib image svg png matplotlib
---

## 우선, SVG가 뭔가요. 

- 저는 파이썬으로 코딩하고, 그 결과를 마크다운으로 작성해서 블로그에 올립니다. 보통 파이썬으로 코딩한 결과는 `matplotlib`로 저장하는데, 그때 확장자를 매번, `svg`로 합니다. 왜냐면, 이렇게 해야 화질이 항상 높거든요
- `dpi`로 저장하는 것이 아니라, 그림을 일종의 벡터로 저장하기 때문에, 큰 화면이든 작은 화면이든 깨지지 않습니다. 이게 무척 좋은것 같아요. 그런데 SVG가 무슨 뜻이죠???

## Scalable Vector Graphics

- [위키피디아](https://ko.wikipedia.org/wiki/스케일러블_벡터_그래픽스)에 의하면.

> 스케일러블 벡터 그래픽스(Scalable Vector Graphics, SVG)는 2차원 벡터 그래픽을 표현하기 위한 XML 기반의 파일 형식으로, 1999년 W3C(World Wide Web Consortium)의 주도하에 개발된 오픈 표준의 벡터 그래픽 파일 형식이다. SVG 형식의 이미지와 그 작동은 XML 텍스트 파일들로 정의 되어 검색화·목록화·스크립트화가 가능하며 필요하다면 압축도 가능하다.

- 일단, 그림이 아니라, **이미지의 벡터들을 표현한 문서** 라고 생각해야겠군요. 그래서 파이썬에서 다른 이미지들처럼 그대로 읽는 것이 불가능했습니다. 다른 이미지들을 RGB/RGBA 의 형태로, `np.array`의 형태로 담겨 있다고 생각해도 상관없는데, SVG는 **문서**거든요. 

## how to read it in python

- 일단, `numpy`, `matplotlib`에서는 읽을 수 없습니다. 얘네는 이미지가 픽셀로 되어 있는 경우(png, jpg 등)만 읽을 수 있습니다. 앞서 말씀드린 것처럼 svg는 이미지를 표현함 **문서** 니까요. 

- [cairo svg](https://cairosvg.org/documentation/)를 설치합니다. 

```bash
pip install cairosvg
```

- 그 다음에, `cairosvg.svg2png`를 사용하면 됩니다. 저는 임의로 이미지를 만들었습니다. 

![](/assets/images/markdown_img/180629_1521_simple_svg.svg)

```python
#cairosvg.svg2png(#url="/path/to/input.svg", write_to="/tmp/output.png")
import matplotlib.pyplot as plt
import cairosvg
import numpy as np 

w = 2048
a = np.random.normal(0, 1, w**2).reshape(w, w)
plt.imshow(a, cmap=plt.cm.Reds, alpha=0.8)
#plt.axis('off')
plt.xticks([])
plt.yticks([])
plt.savefig("../../assets/images/markdown_img/180629_1521_simple_svg.svg")
plt.show()

### 이미 svg 파일이 있다면, 아래코드만 사용하면 됩니다. 
cairosvg.svg2png(url="../../assets/images/markdown_img/180629_1521_simple_svg.svg", 
                 write_to="../../assets/images/markdown_img/180629_1521_simple_png.png", 
                 dpi = 100
                )
```

- png 파일이 만들어졌습니다 뿅. 

![](/assets/images/markdown_img/180629_1521_simple_png.png)


## reference

- <http://ithub.tistory.com/75>
- <https://cairosvg.org/documentation/>