---
title: plt에서 custom marker를 사용할 수 있을까요? 
category: python-lib
tags: python python-lib matplotlib marker numpy

---

## custom marker를 사용할 수 있을까요?  

- plt로 그림을 그리는 중에 marker를 사용하다보니 조금 더 예쁘게, 정확하게는 상황에 맞게 그려보고 싶다는 생각을 했습니다. 
- 현재는 아주 간단하게, 커피를 얼마나 먹었는지 패턴을 정리했는데, marker를 커피 icon으로 할 수는 없을까? 하는 생각이 드는거죠. 그러다보니, custom marker를 사용할 수는 없나? 라는 생각이 들었습니다. 
- 다행히도, 믿음의 스택오버플로우에 이미 [포스트](https://stackoverflow.com/questions/2318288/how-to-use-custom-marker-with-plot) 가 올라와있씁니다만...뭔가 이건 약간 변칙의 방법인것 같은데 흠. 
- 한참 찾아보니, [여기서](https://www.programcreek.com/python/example/102442/matplotlib.offsetbox.OffsetImage) 좀 그나만 비슷하게 할 수 있는 것 같습니다. 

## 어떻게 image를 scatter합니까? 

- 우선, `plt.imread`로 이미지를 읽은 다음
- `OffsetImage`에 이미지를 넣어줍니다(이 때 zoom을 통해 적절하게 줄여줍니다)
- 그다음 `AnnotationBbox`에 `OffsetImage`과 figure위에 그려져야 하는 x, y좌표를 넣고 
- `plt.gca().add_artist`를 이용해 현재 axis에 `AnnotationBbox`를 넣어주면 됩니다. 

```python
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def image_scatter(image_path, x_lst, y_lst):
    f = plt.figure(figsize=(12, 5))
    img = OffsetImage(plt.imread(image_path), zoom=0.05)
    
    for x, y in zip(x_lst, y_lst):
        plt.gca().add_artist(
            AnnotationBbox(img, (x, y), frameon=False)
        )
    plt.plot(x_lst, y_lst)
    plt.savefig('../../assets/images/markdown_img/180618_1844_img_scatter.svg')
    plt.show()
    return f

x = np.linspace(1, 10, 5)
y = np.exp(x)

image_scatter('/Users/frhyme/Downloads/hot-coffee.png', x, x)
print("")
```

![](/assets/images/markdown_img/180618_1844_img_scatter.svg)

## wrap-up

- 왠지, 나중에 어려울 것 같아서 간단하게 함수로 만들어두었습니다. 자세하게 알아보면 좀 더 쓸부분이 있을 것 같은데, 저는 일단은 이정도로만 하려고 합니다.
- annotationbbox, offsetimage 등은 이후에 좀 유용하게 쓸수 있을 것도 같은데, 일단은 이정도로만 하겠습니다. 


## reference

- <https://stackoverflow.com/questions/2318288/how-to-use-custom-marker-with-plot>
- <https://stackoverflow.com/questions/22566284/matplotlib-how-to-plot-images-instead-of-points>
- <https://www.programcreek.com/python/example/102442/matplotlib.offsetbox.OffsetImage>