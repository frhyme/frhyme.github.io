---
title: python에서 이미지 비디오로 변환하기. 
category: python-lib
tags: python python-lib jupyter-notebook HTML video image matplotlib

---

## 파이썬에서 이미지들을 비디오로 변환하기 

- 파이썬으로 그림을 그리다보면, 비디오를 만들고 싶을때가 있습니다. 
- 예를 들면, scatter 그림을 여러 개 찍어서 일종의 애니메이션처럼 만들고 싶을 때도 있고, 데이터가 추가되면서, optimum이 어디로 변해가는지도, 애니메이션으로 보여주면 좋겠다, 라는 생각들을 하게 되죠.
- 그래서, 다 좋은데 그걸 어떻게 해야 하는가? 를 이 포스트에서 다루어 보려고 합니다. 

## 우선, jupyter notebook에 비디오 표시하기 

- `from IPython.display import HTML`를 사용해서 다음으로 보여줍니다. 

```python
def show_video_in_jupyter_nb(width, height, video_url):
    from IPython.display import HTML
    return HTML("""<video width="{}" height="{}" controls>
    <source src={} type="video/mp4">
    </video>""".format(width, height, video_url))
#video_url = '../../assets/images/markdown_img/180628_test_video.mp4'
#show_video_in_jupyter_nb(200, 300,video_url)
```

## 비디오 만들기. 

- jpg파일들이 많이 있는 상황에서는 Pillow를 이용해서 만드는 방법도 있습니다만, 
- 저는 모든 이미지들이 np.array로 되어 있다고 가정하고, 여기서부터 비디오를 만들려고 합니다. 혹은 `plt.figure()`로부터 만들어 보려고 해요. 이 경우가 좀더 다양한 상황에 적용하기 쉬운것 같아요. 
- 저는 가능한, python 기본 라이브러리인 `matplotlib`를 이용해서 진행했습니다.

- 물론, 원래 `matplotlib.animation`를 사용할 때는, 데이터만 변형해가면서 그림을 그려주는 것이 일반적인데, 저는 그냥 이미지로 일괄적으로 변환해서 비디오로 만들어버렸습니다. 
- 이 편이, 제 기준에서는 좀 더 다양하게 활용할 수 있는 것 같아요. 

```python
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg # img read 
from IPython.display import HTML

def show_video_in_jupyter_nb(width, height, video_url):    
    return HTML("""<video width="{}" height="{}" controls>
    <source src={} type="video/mp4">
    </video>""".format(width, height, video_url))

def make_video(output_file_path):
    """
    - np.array로 넘기는 것은 문제가 없는데, np.array를 모두 0과 1사이의 float으로 변형해서 넘길 것 
    """
    ### read data 
    img1 = mpimg.imread("/Users/frhyme/Downloads/IMG_9715.JPG")
    img2 = img1*20
    img1, img2 = img1/256, img2/256
    height, width, layers = img1.shape
    ### make figure 
    fig, ax = plt.subplots(1, 1, figsize=(3, 4))
    ax.get_xaxis().set_visible(False), ax.get_yaxis().set_visible(False)
    plt.axis('off')
    im = ax.imshow(img1,interpolation='nearest')
    #plt.close()# 이미지 한장 뜨는걸 방지함. 
    ########################3
    ## update_img가 가장 중요함. 이 함수가 그림 그려지는 데이터를 조절해서 그림을 적당히 예쁘게 그려줌. 
    def update_img(f):#frame가 넘어옴
        tmp = img1 * f + img2* (1-f)
        im.set_data(tmp)# 데이터를 바꾸어주면서 그림을 그려야 함.
        return im
    """
    frames: If an integer, then equivalent to passing range(frames)
    interval: Delay between frames in milliseconds. Defaults to 200.
    """
    tight_layout()
    ani = animation.FuncAnimation(fig, func=update_img,
                                  frames=np.linspace(0, 1, 150),
                                  interval=500)
    ## ffmpeg가 깔려 있어야 할 수 있는데 brew install ffmpeg 를 사용하는 것이 좋음. 
    writer = animation.writers['ffmpeg'](fps=25)
    dpi = 256
    ani.save(output_file_path,writer=writer,dpi=dpi)
    return ani

video_url = '../../assets/images/markdown_img/180702_cat_blending.mp4'
make_video(video_url)
show_video_in_jupyter_nb(200, 300, video_url)
```

## wrap-up

- `ani.save`에서의 `dpi`는 가급적 256정도로 그대로 유지하고, 만약 비디오의 화질을 올리고 싶다면 넘기는 `np.array`의 화질을 올리는 것이 합당함. 

## reference

-<https://stackoverflow.com/questions/4092927/generating-movie-from-python-without-saving-individual-frames-to-files>