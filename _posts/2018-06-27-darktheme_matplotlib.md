---
title: matplotlib 테마 바꾸기 
category: python-lib
tags: matplotlib python-lib python theme 
---

## matplotlib 테마 바꾸기 

- 최근에 jupyter notebook에서 jupyter lab으로 변경했습니다. 그리고 jupyter lab의 까만 화면으로 변경했는데, 바꾸고 보니까, `matplotlib`에서 그림을 그릴 때, tick이 잘 안보이는 문제가 있어요. 
- 기본적으로 `matplotlib`는 그림이 하얀색 배경에 그려진다고 가정합니다. 따라서, tick이 모두 검은색으로 되어 있죠. 
- dark theme을 적용했을 때는 이게 겹쳐서 잘 안 보이는데, 이를 어떻게 해결할 수 있을까? 하는 생각이 들어서 정리해봤습니다. 

## plt.style.use()

- `plt.style.use()`에 넣으면 됩니다. argument로는 다음을 넣을 수 있어요. 
    - 'default'
    - 'dark_background'
    - 'classic'
    - 'ggplot'
    - 'seaborn'
- 다만, 이게 전부 독립적으로 적용되지 않고, 다음 스타일을 적용하면, 이전에 적용되었던 것들이 남아있는 경우가 있어요. 
- 의도적으로 여러 style을 합쳐서 적용하는 것은 상관없는데, 이전에 적용한 것이 남아있을때는 약간 마음에 들지않습니다. 

## dark_background

- 한 쥬피터 노트북 안에서 여러 스타일을 함께 쓰면, 이전의 스타일이 남아있어서 예쁘게 안 그려지는 것 같아요. 
- 그래서 저는 예쁜거 하나만 그리기로 했씁니다. 
- 화면이 어두울 때는 다음 세팅을 하고 그리면 좋아요. 

```python
import numpy as np 
import matplotlib.pyplot as plt 
## 이걸 세팅해주세요. 
plt.style.use(['dark_background'])
##############
xs = np.random.normal(0, 3, (100, 3))

plt.figure(figsize=(12, 4))
for i in range(0, 3):
    x = xs[:, i]
    plt.plot(range(0, len(x)), x, linewidth=1, linestyle='--', label='x_{}'.format(i))
plt.legend()
plt.grid(False) # grid를 없앴습니다. 
plt.savefig('../../assets/images/markdown_img/180627_plt_style_use_dark_background.svg')
plt.show()
```

![](/assets/images/markdown_img/180627_plt_style_use_dark_background.svg)


## wrap-up

- 뭐, `ggplot`, `seaborn`도 좋다는 사람이 많은데, 저는 보통때는 그냥 default를 쓰고, 어두울때는 이걸 쓰고 딱 그렇게 하면 될것 같아요. 

## reference

- <https://matplotlib.org/_images/sphx_glr_style_sheets_reference_007.png>