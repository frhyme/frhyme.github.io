---
title: image를 섞어서 새로운 이미지를 만듭니다. 
category: python-lib
tags: python python-lib image PIL pillow matplotlib numpy 
---

## 두 이미지를 섞어보려고 합니다. 

- cv2, pillow에서 이미지를 섞을 때, 특별한 함수를 쓰던데, 사실 둘다 np.array라는걸 가정하고 보면 이게 뭐가 어렵나 싶어요. 
- 그냥 적당한 weight로 곱하면 되지 안 그렇습니까? 

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 

img = Image.open('/Users/frhyme/Downloads/IMG_9715.JPG')
img_a, img_b = np.array(img), img_a*20
# 아래에서 image를 256으로 나누워주는 이유는, plt.imshow()의 한계때문인데
# 0-256 사이의 정수거나, 0-1사이의 float만 지원함. 
# 즉, 1이 넘는 float은 문제가 발생함. 
blend_rates = np.linspace(0, 1, 5)
#plt.imshow(img_blended)
f, axes = plt.subplots(1, len(blend_rates), figsize=(12, 12))
for i, r in enumerate(blend_rates):
    blended_img = (img_a*(1-r) + img_b*r)/256
    axes[i].imshow(blended_img), axes[i].axis('off')
    axes[i].set_xticks([]), axes[i].set_yticks([]), 
    axes[i].set_title("img_a: {}, img_b: {}".format(1-r, r), fontsize=8)
plt.savefig('../../assets/images/markdown_img/180630_1850_cat_blended.svg')
plt.show()
```

- 아래처럼 적절하게 이미지를 섞었습니다. 

![](/assets/images/markdown_img/180630_1850_cat_blended.svg)