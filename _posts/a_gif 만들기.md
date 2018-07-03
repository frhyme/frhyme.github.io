---
title: 마크다운에 animated gif를 넣어보기 
category: others
tags: gif 
---

## 우선 gif란 무엇인가? 

- Graphical Interchange Format(GIF)의 약자입니다. 초기에는 단순히 이미지 포맷에 가까웠지만, 지금은 '움짤'이 인기를 끌면서, 다시 부흥하고 있다고 하죠. 
- 여담이지만, 밞음이 "지프"인지, "기프"인지는 탕수육 부먹/찍먹 논란만큼 말이 많다고 합니다. GIF개발자가 "지프"가 맞다 라고 했지만, 여전히 변화는 없다고 하네요.
- 뭐, 어떻게 부르던 무슨 상관인가 싶지만, indentation에 대해서도 민감한 개발자들이 이런 요소에 민감하지 않을 리 없죠. 


## 

## 왜 갑자기 gif를 만들어보려고 하나요? 

- 마크다운으로 작업 중에, 움직이는 것들 좀 넣어보려고 하는데, 잘 되는지 모르겠어요. 한번 해보려고요 

### 웹 소스로부터 가져오는 경우 

- [giphy](https://giphy.com)라는 gif 리포지토리에서 가져왔습니다. 

```markdown
![](https://media.giphy.com/media/MWdOAxxPDEhNKyzXVK/giphy.gif){: width="50%" height="50%"}{: .center}
```

![](https://media.giphy.com/media/MWdOAxxPDEhNKyzXVK/giphy.gif){: width="50%" height="50%"}{: .center}

```html
<iframe src="https://giphy.com/embed/MWdOAxxPDEhNKyzXVK" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ionedigital-yellow-quotes-MWdOAxxPDEhNKyzXVK">via GIPHY</a></p>
```

<iframe src="https://giphy.com/embed/MWdOAxxPDEhNKyzXVK" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ionedigital-yellow-quotes-MWdOAxxPDEhNKyzXVK">via GIPHY</a></p>


- HTML5 video 


---

## 움직이는 이미지 두둠칫 두둠칫

- 파이썬에서 matplotlib

- 다음처럼 파이썬에서 움직이는 gif를 만들어보려고 했씁니다만, 장대하게 실패하여, 파이썬을 콘다로 아예 다시 설치했습니다. 
- 지금도 약간 빡치지만, 그래도 이후에 이걸 다시 볼 일이 있지 않을까? 싶어서, 일단 잘 정리해두려고 합니다. 
- 화가 나지만, 잘 정리해둬야, 지금 제가 빡치는 종류의 일이 다시 발생하지 않거든요. 





## issue

- [이 포스트](http://tiao.io/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/)에 있는 코드를 그대로 가져와서, 사용했던 것으로 기억합니다(오류가 나서 완전히 명확하지는 않고, 대략 85%의 정확도를 가질 것 같네요).
- 아무튼, 아래 코드를 보시면 `IPython.displyt.HTML`을 이용해서, 만들어진 이미지를 jupyter notebook에 뿌립니다. 그래서 쉽게 될줄 알았죠. 

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return (line,)

# animation function. This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return (line,)

# call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

HTML(anim.to_html5_video())
```

- 그래서 실행해보니, 다음과 같은 오류가 발생합니다. 

```
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-16-3dd9ec2777d7> in <module>()
     28 anim = animation.FuncAnimation(fig, animate, init_func=init,
     29                                frames=100, interval=20, blit=True)
---> 30 HTML(anim.to_html5_video())
     31 #rc('animation', html='html5')

~/anaconda3/lib/python3.6/site-packages/matplotlib/animation.py in to_html5_video(self)
   1203                 # We create a writer manually so that we can get the
   1204                 # appropriate size for the tag
-> 1205                 Writer = writers[rcParams['animation.writer']]
   1206                 writer = Writer(codec='h264',
   1207                                 bitrate=rcParams['animation.bitrate'],

~/anaconda3/lib/python3.6/site-packages/matplotlib/animation.py in __getitem__(self, name)
    157         self.ensure_not_dirty()
    158         if not self.avail:
--> 159             raise RuntimeError("No MovieWriters available!")
    160         return self.avail[name]
    161 

RuntimeError: No MovieWriters available!
```

- 뭐 잘 모르겠고, 오류니까 `RuntimeError: No MovieWriters available!`부분을 구글에서 검색해보니, 다음과 같은 [이미 질문한 포스트](https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available가 있더군요. 그래서 눌러서 들어가보니, 두번째 질문에 `conda install -c conda-forge ffmpeg`를 설치해야, 쥬피터 노트북 내에서 html을 비디오로 실행할 수 있다는 이야기가 있더군요. 
    - 여기서 조금 생각해보고 진행했었어야 했는데, 제가 솔직히 별생각없이 넘어가긴 했습니다. 
- 아무튼, 그래서 설치를 하고, 나니까. `matplotlib`에서 문제가 발생했습니다. 아마도 다음 오류였어요. 

```
KeyError: 'keymap.quit_all'
```

- 찾아봤는데 답이 없어서, 그냥 `conda update --all`을 실행했습니다.
- 이후에는 `matplotlib`도 제대로 되지 않음은 물론, jupyter notebook의 폰트까지 바뀌어 버렸어요. 
- 그래서 그냥 다 지우고 다시 하기로 했습니다 하하하하핫

## wrap-up

- jupyter notebook으로 모든 걸 작업하는데는 한계가 있다는 생각을 했습니다. 아마도, 파이썬 코드를 직접 짜서, 외부에서 돌렸으면, 애니메이션을 만드는 것이 문제가 없지 않았을까? 하는 생각이 조금 듭니다. 
- 흠. 그런데 애니메이션을 `Ipython`에서 혹은 영상을 띄우는 것이 그렇게 어려운 일이 아니었던 것으로 제가 기억하고 있긴 한데.....으아. 

## reference 

- <https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/>
- <http://tiao.io/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/>
- <https://stackoverflow.com/questions/48088932/library-not-loaded-rpath-libpng16-16-dylib>