---
title: img file들로부터 gif로 변형하기
category: python-lib
tags: python image gif python-lib imageio matplotlib np.array numpy 
---

## 이미지 파일을 gif로 변형합니다.

- 그동안, 나름대로 `np.array`를 그대로 비디오로 만들어주는 형식으로 활용을 했는데, 이게 잘 안되는 것 같아요. 
- 그래서, 그냥 이미지 파일들을 죽 만든 다음에, 그 이미지들을 읽어서 비디오로 만들어주는 형식이 훨씬 효율적인 것 같습니다. 
- 다 만든다음 `os` 모듈로 다 지워주면 되니까요. 

## do it

- `imageio`라는 모듈을 사용해서, 이미지를 읽고 씁니다. `gif` 파일도 잘 만들어줍니다. 아주 좋아요. 
- 여기서도 figure를 `np.array`로 변환해서 넣어봤는데, 이유는 정확히 모르겠지만 잘 안되요. 
- 그냥 파일을 생성한 다음에 그 이미지를 읽고, 쓰는게 더 좋은것 같아요. 

```python
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

def img_file_to_gif(img_files, output_file_name):
    ## imge 파일 리스트로부터 gif 생성 
    imgs_array = [np.array(imageio.imread(img_file)) for img_file in img_file_lst]
    imageio.mimsave(output_file_name, imgs_array, duration=0.5)

plt.style.use('dark_background')

node_size = 1000
x = np.random.normal(0, 1, node_size)
y = np.random.normal(0, 1, node_size)

#### sample image generation 
img_file_lst = []
for i in range(0, 20):
    f = plt.figure(figsize=(12, 6), dpi=100)
    to = (i+1)*50
    plt.scatter(x[:to], y[:to], alpha=0.5, color='blue')
    plt.xlim([-3, 3]), plt.ylim([-3, 3])
    output_img_file_name = '../../assets/images/markdown_img/180703_1520_test_img_{}.png'.format(i)
    img_file_lst.append(output_img_file_name)
    plt.savefig(output_img_file_name)
    plt.close()

img_file_to_gif(img_file_lst, "../../assets/images/markdown_img/180703_1520_test_gif.gif")

print('complete')
#### sample image delete 
for img_file in img_file_lst:
    if os.path.exists(img_file):
        os.remove(img_file)
print('image file delete complete')
```

![](/assets/images/markdown_img/180703_1520_test_gif.gif)

## wrap-up

- 이유를 모르겠네....위에서도 결국 이미지를 읽은 다음에 `np.array`로 변환해서 넣어주는데, 왜 안되냐.....시바 

