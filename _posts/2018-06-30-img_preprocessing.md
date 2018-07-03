---
title: 파이썬에서 image를 처리합시다. 
category: python-lib
tags: python python-lib image pillow matplotlib numpy png jpg 
---

## 왜 갑자기 image인가요

- 음...저는 약간 뭘 하다가 늘 삼천포로 빠지는 스타일입니다. 지금도 원래는 `gym`을 이용해서 강화학습을 하다가 넘어왔어요. 
- 이게 왜 그런거냐면, `gym`을 이용해서 학습을 할때, 현재 어떻게 되고 있는 상황을 렌더링하는 것이 필요합니다. 게임이니까요.
    - 그런데 쥬피터 노트북에 embeded로 상황을 렌더링하는 것이 안되요. 쥬피터 노트북 밖에서 화면이 뜨는데, 여기서 오류가 많이 발생해요. 
    - 그래서 이걸 gif로 고치거나, video로 고치거나 해야 할것 같은데, 이것도 잘안되요(비디오 코덱문제) 
    - 처음에는 이게 간단할줄 알았는데, 생각보다 매우 간단하지 않더라구요. 
- 그 과정에서, 제가 이미지나 비디오 등 처리에 대해서 너무 모르는 것이 아닌가? 싶어서 일단 이미지 처리부터 다시 정리해보기로 했습니다. 
- 그래서, 이 포스트는 파이썬에서 이미지를 어떻게 읽고! 쓰고! 변화합니까! 가 되겠네요. 

## png or jpg or svg

- 보통 `matplotlib`로 플로팅을 한 다음에, 그림을 그려줄 때, png나 jpg보다는 svg의 형태로 많이 뿌려줍니다. svg는 제가 다른 포스트에서도 썼지만, scalable vector graphic인데, 그림에 대한 정보를 xml의 형태로 표현해요. png, jpg는 픽셀의 형태로 저장합니다. 그래서. png, jpg는 `np.array`로 변환이 쉬운 반면, svg는 변환이 어려워요. 
- 우선 png의 경우는 무손실 그림 저장 포맷이고, RGBA(Red, Green, Blue, Alpha)라는 네가지 레이어로 이미지를 저장합니다. 
- jpg의 경우는 손실 그림 저장 포맷이고, RGB(Red, Green, Blue)로 이미지를 저장합니다. 
- 뭐 이런 차이가 있기는 한데, 일단은 크게 신경쓰지 않으셔도 됩니다. 우리는 그냥 이미지를 읽고, 이미지를 씁니다. 그게 다에요. 

## read image

- 일단 간단하게 image를 읽어봅시다.
- 앞서서 RGBA, RGB로 각각 다르다고 했지만, 이미지를 읽을때는 이 파일명은 내부에서 알아서 이해해 주는 것 같아요(단, svg는 읽을 수 없구요)

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# 샘플 그림을 그립시다. 
plt.style.use("default")
jpg_img_arr = mpimg.imread('/Users/frhyme/Downloads/google2.0.0.jpg')
jpg_IMG = Image.open('/Users/frhyme/Downloads/google2.0.0.jpg')
print(type(jpg_img_arr))# 얘는 np.array
print(type(jpg_IMG))# 얘는 PIL.JpegImagePlugin.JpegImageFile' 오브젝트
print((jpg_img_arr == np.array(jpg_IMG)).mean())# 다행히 np.array로 변환이 쉬움. 

height, width, layer = jpg_img_arr.shape

f, axes = plt.subplots(2, 2, figsize=(8, 8*height/width))
## original img plotting 
axes[0][0].imshow(jpg_img_arr[:, :, :]), axes[0][0].axis('off')
axes[0][0].set_xticks([]), axes[0][0].set_yticks([])# 이걸 하지 않으면 tick이 남아있어서 간격이 생김. 
# Red, Green, Blue로 구분하여 표현. colormap 또한, 그 형식에 맞춰서 표현 
# 실제 그림을 보면 색깔별로 어느 정도 구분되어 있는 것을 알 수 있음. 
cmaps = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]
for i in range(1, 4):
    axes[i//2][i%2].imshow(jpg_img_arr[:, :, i-1], cmap=cmaps[i-1])
    axes[i//2][i%2].set_xticks([]), axes[i//2][i%2].set_yticks([])# 이걸 하지 않으면 tick이 남아있어서 간격이 생김. 
    axes[i//2][i%2].axis('off')
plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
## sutplots_adjust는 subplot 간에 간격을 붙이려고 쓴건데, 쓰고보니 어떻게 쓰는건지 모르겠음. 그냥 모르겠음...
plt.margins(0, 0, tight=False)
# pad_inches를 0으로 두고 저장하면, 공백없이 저장됨. 
plt.savefig("../../assets/images/markdown_img/180628_1935_google_rgb.svg", pad_inches=0)
plt.show()
```

- 아래 그림에서 보는 것처럼 subplot이 그려졌고, 색깔별로 구분되어 그려졌음을 알 수 있음. 

![](../../assets/images/markdown_img/180628_1935_google_rgb.svg)


## figure to np.array

- 아래 함수를 쓰시면, 간단하게 현재 `plt.figure()`를 `np.array`로 변환할 수 있습니다. 

```python
import numpy as np 
import matplotlib.pyplot as plt 

def figure_to_array(fig):
    """
    plt.figure를 RGBA로 변환(layer가 4개)
    shape: height, width, layer
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)
```

## svg to png

- 앞서 말씀드린 것처럼, svg는 픽셀 단위로 표현되지 않아서, 일반적인 이미지 라이브러리에서 잘 읽지 못합니다.
- 따라서, 경우에 따라서, svg를 png로 변환해주어야 하는 것이 필요하구요. 그럴때, `cairosvg`라는 라이브러리를 씁니다. 
- 아래 코드에서 보는 것처럼 간단히 `url`, `write_to`, `dpi`를 설정해주면 알아서 잘 그려줍니다. 

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

cairosvg.svg2png(url="../../assets/images/markdown_img/180629_1521_simple_svg.svg", 
                 write_to="../../assets/images/markdown_img/180629_1521_simple_png.png", 
                 dpi = 100
                )
```

![](/assets/images/markdown_img/180629_1521_simple_svg.svg)

![](/assets/images/markdown_img/180629_1521_simple_png.png)


## blur or convolution 

- 이미지를 약간 뿌옇게 해주고 싶을때 사용합니다. 

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("default")
img = mpimg.imread('/Users/frhyme/Downloads/IMG_9715.JPG')
#img = cv2.imread('/Users/frhyme/Downloads/') # cv2로 읽으면 칼라맵이 바뀌는 경우가 있는듯. 
height, width, layer = img.shape
# 어느 정도의 사이즈를 컨볼루션할 것인가를 결정하는 부분이다.
# 1일때는 큰 차이가 없고, 이 값이 커질수록, 뿌옇게 보이는 것을 알 수 있다. 
imgs = [cv2.blur(img, (i, i)) for i in [1, 10, 20, 50, 200]]
f, axes = plt.subplots(1, len(imgs), figsize=(12, 8))
for i in range(0, len(axes)):
    axes[i].imshow(imgs[i]), axes[i].axis('off')
    axes[i].set_xticks([]), axes[i].set_yticks([])
plt.savefig('../../assets/images/markdown_img/180630_1817_cat_blur.svg')
plt.show()
```

![](/assets/images/markdown_img/180630_1817_cat_blur.svg)

## transpose and rotation 

- image는 `np.array`입니다. 물론 height, width, layer로 되어 있는 조금 복잡한 구조이기는 한데, 
- 따라서 이 np.array를 변환하면, 이미지 또한 변합니다. 그렇게 생각하면, 공대생들에게는 조금 더 편하게 이해되는 부분이 있는 것 같아요. 
- 저는 transpose를 사용했습니다. 여기서 `img.transpose(1, 0, 2)`는 원래 height, width, layer였던 구조를 width, height, layer로 바꾸겠다는 말입니다. layer는 그대로죠. 

```python
f, axes = plt.subplots(1, 3, figsize=(12, 3))
imgs = [img, img.transpose(1, 0, 2), np.rot90(img)]
titles = ['original img', 'tranpose', 'rotate 90']
for i, j in enumerate(imgs):
    axes[i].imshow(j)
    axes[i].set_xticks([]), axes[i].set_yticks([])
    axes[i].axis('off'), axes[i].set_title(titles[i]), 
plt.savefig('../../assets/images/markdown_img/180630_1820_cat_transpose_rot.svg')
plt.show()
```

![](/assets/images/markdown_img/180630_1820_cat_transpose_rot.svg)

## to gray scale 

- gray scale로 변환할때 `0.299 R + 0.587 G + 0.114 B` 이러한 공식을 쓴다고 합니다. 저는 처음 알았군요. 그냥 더해서 나누면 되는줄. 
- grapy scale로 적용하고 나면, 원래 (height, width, layer)였던 np.array가 layer가 3인 형태가 됩니다. 
- 즉 이 때는 특정한 칼라맵을 그대로 적용해도 된다는 거죠. 그래서 칼라맵을 뿌려주면 그 값에 따라서, 칼라링이 됩니다. 

```python
# 0.299 R + 0.587 G + 0.114 B, https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
from PIL import Image
import numpy as np 

img = Image.open('/Users/frhyme/Downloads/IMG_9715.JPG')
img_np = np.array(img)

img_np.transpose(2, 0, 1)
r = img_np.transpose(2, 0, 1)[0]
g = img_np.transpose(2, 0, 1)[1]
b = img_np.transpose(2, 0, 1)[2]
img_gray= r*0.299 + g*0.587 + b*0.114

cmaps = [plt.cm.gray, plt.cm.rainbow, plt.cm.Reds_r, plt.cm.Blues_r, plt.cm.cividis, plt.cm.cubehelix, plt.cm.magma]
f, axes = plt.subplots(1, len(cmaps), figsize=(15, 6))
for i in range(0, len(cmaps)):
    axes[i].imshow(img_gray, cmap=cmaps[i])
    axes[i].set_xticks([]), axes[i].set_yticks([]), axes[i].set_title(cmaps[i].name)
plt.savefig('../../assets/images/markdown_img/180630_1824_cat_gray_to_colormap.svg')
plt.show()
``` 

![](/assets/images/markdown_img/180630_1824_cat_gray_to_colormap.svg)


## resizing and rotating 45

- 사이즈를 변환하거나, 회전할때 `pillow` 라이브러리를 쓰면 유용합니다. 

```python
# simple transformation 
from PIL import Image

img = Image.open('/Users/frhyme/Downloads/IMG_9715.JPG')
print("original img shape: {}".format(np.array(img).shape))
# resize 
resized_img = np.array(img.resize((500, 100)))# width, height
plt.imshow(resized_img)
plt.savefig("../../assets/images/markdown_img/180630_1832_resized_cat.svg")
plt.figure()
# rotate
rotated_img = np.array(img.rotate(45))# width, height
plt.imshow(rotated_img)
plt.savefig("../../assets/images/markdown_img/180630_1832_rotated_cat.svg")
```

![](/assets/images/markdown_img/180630_1832_resized_cat.svg)

![](/assets/images/markdown_img/180630_1832_rotated_cat.svg)

## image blending

- 이미지를 섞습니다. 그냥 곱해서 더해주면 되는거에요 사실 하하핫

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

![](/assets/images/markdown_img/180630_1850_cat_blended.svg)

## wrap-up

- 간단하게 파이썬으로 이미지를 처리하는 방법들을 정리했습니다. 
- 몇 가지 수확이라면, '이미지는 어레이다' 라는 아주 심플한 개념을 머릿속에 탑재했다는 것이죠. 그냥 매트리스를 다룬다고 생각하고 이미지를 생각하면 될것 같습니다. 
- 그리고 RGB, RGBA, PNG, SVG, JPG 등 아주 기본적인 이미지 처리 용어들에 대해서 익숙해졌다는 것이 얻은 것이랄까요? 

## reference

- <https://matplotlib.org/gallery/misc/agg_buffer_to_array.html>

