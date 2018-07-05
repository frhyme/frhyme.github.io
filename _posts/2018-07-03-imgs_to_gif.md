---
title: img file들로부터 gif로 변형하기
category: python-lib
tags: python image gif python-lib imageio matplotlib np.array numpy 
---

## 이미지 파일을 gif로 변형합니다.

- 그동안, 나름대로 `np.array`를 그대로 비디오로 만들어주는 형식으로 활용을 했는데, 이게 잘 안되는 것 같아요. 
- 그래서, 그냥 이미지 파일들을 죽 만든 다음에, 그 이미지들을 읽어서 비디오로 만들어주는 형식이 훨씬 효율적인 것 같습니다. 
- 다 만든다음 `os` 모듈로 다 지워주면 되니까요. 

## 우선, 몇 가지를 설치해야 합니다. 

- 우선 Moviewriter를 설치해야 합니다. 
- 처음에 저는 matplotlib의 animation을 실행했을 때 `RuntimeError: No MovieWriters available!`라는 에러를 봤는데, 현재 컴퓨터에서 사용할 수 있는 moviewriter가 없다는 말이죠. 
- 여기저기 찾아보니 `ffmpeg`라는 걸 설치하라고 하더라고요. 설치합니다.

```bash
brew install ffmpeg
```

- 설치 이후에 바로 안될 때도 있습니다. 이유는 모르겠지만, 시간이 좀 지나면 됩니다. 그리고, `conda install -c conda-forge ffmpeg`를 사용해서 설치하라는 말도 있던데, 저는 이걸 이용했더니 기존 라이브러리들에 싹 문제가 생겨서 다 지우고 다시 깔았습니다. 가급적이면, `brew`나 `apt-get`같은 것을 사용하는 게 좋을 것 같아요. 


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
    ## np.array 리스트를 넘기면, 알아서 gif를 만들어주는데, 
    ## 제가 이전에 figure를 np.array로 변환해서 진행했을때는 잘 안되더라고요...흠...
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

