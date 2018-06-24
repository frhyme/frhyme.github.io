---
title: dot language로 nn 그려서 보기 
category: machine-learning
tags: python dot python-lib machine-learning neural-network
---

## 뉴럴넷이 복잡해서 지금 제대로 그리고 있는지 모르겠을때. 

- 그럴 때, neural network를 그려보면 좋겠다는 생각을 합니다. `tensorflow`에 `tensorboard`가 있는데, 이건 좀 다르고, 그냥 간단하게 어떤 node에서 어떤 node로 흘러가는가? 만 보고 싶다는 생각을 해요. 
- 특히, 지금 input_space, output_space 가 맞게 설계된거야? 라는 생각이 들 때가 있는데, 그럴때 아주 유용한 것 같아요. 

## do it. 

- 아래처럼 하면 됩니다 하하핫. 다행히도 keras에서 이미 관련 함수를 제공하고 있어요. 아마도 `pydot`이 이미 깔려 있어야 할 것 같기는 한데. 
- keras model을 dot language로 변환하고, 
- dot language를 svg 파일로 저장합니다 끗. 

```python
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense, Input

from IPython.display import SVG #jupyter notebook에서 보려고 
from keras.utils.vis_utils import model_to_dot # keras model을 dot language로 변환

model1 = Sequential([
    # 원래는 Input layer도 있으면 좋지만, 없어도 알아서 자동으로 만들어줍니다. 
    SimpleRNN(units=1, input_shape=(3, 1), name='name1'),
    Dense(10, activation='linear', name='name2'), 
    Dense(1, activation='linear'), 
    ])
model_dot = model_to_dot(model1, show_shapes=True)
# 파일로 저장하기 
from keras.utils import plot_model
plot_model(model1, to_file='../../assets/images/markdown_img/180620_nn_to_dot.svg')
# jupyter notebook에서 보기 위함
SVG(model_to_dot(model1, show_shapes=True).create(prog='dot', format='svg'))
```

![](/assets/images/markdown_img/180620_nn_to_dot.svg)


## wrap-up 

- 아마도 pydot, pygraphviz와 충돌 문제가 발생할 수 있습니다. 이 라이브러리들은 안정성이 매우 역같은데, 잘 되길 기도합니다... 

## reference 

- <https://keras.io/visualization/>