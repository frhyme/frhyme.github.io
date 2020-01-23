---
title: 마크다운에 animated GIF를 넣어봅시다. 
category: others
tags: markdown gif 

---

## 우선 gif란 무엇인가? 

- Graphical Interchange Format(GIF)의 약자입니다. 초기에는 단순히 이미지 포맷에 가까웠지만, 지금은 '움짤'이 인기를 끌면서, 다시 부흥하고 있다고 하죠. 
- 여담이지만, 밞음이 "지프"인지, "기프"인지는 탕수육 부먹/찍먹 논란만큼 말이 많다고 합니다. GIF개발자가 "지프"가 맞다 라고 했지만, 여전히 변화는 없다고 하네요.
- 뭐, 어떻게 부르던 무슨 상관인가 싶지만, indentation에 대해서도 민감한 개발자들이 이런 요소에 민감하지 않을 리 없죠. 

## animated gif 란 무엇인가?

- 흔히들 말하는 '움짤'의 경우, 정확히는 **animated gif**를 말합니다.
- 앞서 말한 바와 같이, gif는 jpg, png 등처럼 이미지 교환형식으로 쓰였구요. 따라서 이미지가 한 장인 경우도, gif로 표현이 됩니다. 
- 웹에서 움직이는 파일(gif)를 저장했을 때, 저장하고 보니, 딱 한장만 담겨있는 경우들이 있잖아요? 움직이지 않고. 이런 경우들이 보통 animated gif에 담겨 있는 많은 이미지 중에서 한장만 담겨 있는 경우로 보면 됩니다. 

## 마크다운에 gif를 담을 때 

- 이미지랑 같은 방식으로 표현하면 됩니다. 


### local에서 가져오는 경우 

- 제가 임의로 만든 gif 파일입니다. 로컬에서도 똑같이 읽으면 되는데, 제가 지금 animated gif를 loop없이 만들었어요(어떻게 loop있는 상태로 만들어야 하는지 모르겠어요....)
- 일단 저는, `imagemagick`를 설치하고, 

> brew install imagemagick

- 다음 코드를 이용해서 만들었습니다. 

```python
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation
from IPython.display import HTML

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(figsize=(12, 3))

plt.xlim(( 0, 2)), plt.ylim((-2, 2))
line, = plt.plot([], [], lw=2)
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
                               frames=100, interval=20, blit=True, 
                               repeat=True
                              )
plt.close()
anim.save('../../assets/images/markdown_img/180703_sample_gif.gif', dpi=256, writer='imagemagick')
#anim.save('line.gif', dpi=80, writer='imagemagick')
#HTML(anim.to_html5_video())
print('complete')
```

- 아무튼, 이전에 같은 경로에 있는 `mp4`파일의 경우는 마크다운에 담는게 잘 안되었는데, gif는 문제없이 되는군요. 앞으로 가능하면, gif파일로부터 만들어서 처리하면 될것 같아요. 

![](/assets/images/markdown_img/180703_sample_gif.gif)


### 웹 소스로부터 가져오는 경우 

- [giphy](https://giphy.com)라는 gif 리포지토리에서 가져왔습니다. 
- 크기랑, 정렬을 조금수정하려고 값을 뒤에 넣었어요. 

```markdown
![](https://media.giphy.com/media/MWdOAxxPDEhNKyzXVK/giphy.gif){: width="50%" height="50%"}{: .center}
```

![](https://media.giphy.com/media/MWdOAxxPDEhNKyzXVK/giphy.gif){: width="50%" height="50%"}{: .center}

```html
<iframe src="https://giphy.com/embed/MWdOAxxPDEhNKyzXVK" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ionedigital-yellow-quotes-MWdOAxxPDEhNKyzXVK">via GIPHY</a></p>
```

<iframe src="https://giphy.com/embed/MWdOAxxPDEhNKyzXVK" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ionedigital-yellow-quotes-MWdOAxxPDEhNKyzXVK">via GIPHY</a></p>

## wrap-up

- gif를 루프있는 상태로 만드는 걸 정리해야할 것 같아요.


