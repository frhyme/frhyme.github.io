---
title: 파이썬에서 이미지를 저장할 때 공백을 없앱시다. 
category: python-lib
tags: python python-lib image matplotlib padding margins 
---

## 그림을 저장할 때, 공백등을 모두 없애서 저장합시다. 

- 차트 같은 것을 그릴 때는 별 문제가 없는데, 차트가 아니라, 말 그대로 이미지, `plt.imshow()`를 통해서 보여진 이미지를 변형해서 다시 이미지 파일로 넣어줄 때는 좀 문제가 있습니다. 
- margin, padding 등이 너무 들어가 있습니다. 이걸 전부 싹 지워버리고 싶었어요. 

## do it

- 우선, figure의 크기를 잘 정해야 합니다. 우리가 그리는 이미지의 크기와 비슷한 비율로 그려야 합니다. 그렇지 않으면, 어떤 경우라도 나머지 공백이 크게 나오게 됩니다. 
    - 그래서, 가능하면, width, height의 비율에 맞춰서 `figsize`를 세팅해주는 것이 좋아요. 
- 공백을 없애는 방법은 여러가지인데, 대략 다음과 같습니다. 

- `plt.axis('off')`: 축 없애기 
- `plt.xticks([]), plt.yticks([])`: 틱 없애기(틱이 기본적으로 약간의 텍스트 공백을 차지하기 때문에 없애야 합니다. 
- `plt.tight_layout()`: 이건 원래, 현재 figure상에서 배치되어 있는 놈들의 공백을 적당하게 잘 배치해주는 거죠, 물론 여기서는 필수적으로 필요한 놈은 아닙니다. 
- `plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)`: 얘가 중요한데, 현재 베치되어 있는 subplot들의 위치를 다 조절해주는 겁니다. 
    - left, bottom을 0으로 두면, 경계에 둔다는 것이고, right, top를 1로 둔다는 것은 또 다른 경계에 둔다는 것이죠. 
    - hspace, wspace의 경우는 subplot이 여러 개일때 subplot간의 간격을 의미합니다. 

## 진짜 do it

- 그래서 아래 코드를 사용해서 진짜 표현해보면, 두 그림이 서로 다른 것을 알 수 있습니다. 

```python
"""
이미지 공백 제거 
"""

import numpy as np 
import matplotlib.pyplot as plt

img = np.random.normal(0, 10, (300, 800))
height, width = img.shape
## 일단은, 무조건 만든 figure에 맞춰서 그림이 저장됨. 
## 따라서, figsize를 넣으려는 img의 height, width를 고려하여 진행하는 것이 좋을 수 있음. 
## figure size를 웬만하면, 한쪽을 1로 고정하고 보여주는 것이 좋을 수 있음. 

figsize = (1, height/width) if height>=width else (width/height, 1)
## image with padding and margin
plt.figure(figsize=figsize) 
plt.imshow(img, cmap=plt.cm.Blues)
plt.savefig("../../assets/images/markdown_img/180703_img_with_padding.png", dpi=100)

## image without padding and margin
plt.figure(figsize=figsize) 
plt.imshow(img, cmap=plt.cm.Blues)
plt.axis('off'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
plt.savefig("../../assets/images/markdown_img/180703_img_without_padding.png", 
            bbox_inces='tight', 
            pad_inches=0, 
            dpi=100
           )
```

![](/assets/images/markdown_img/180703_img_with_padding.png)

![](/assets/images/markdown_img/180703_img_without_padding.png)