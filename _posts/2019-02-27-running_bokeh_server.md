---
title: running bokeh server 
category: python-libs
tags: python bokeh data-visualization python-libs 
---

## why do you wanna run bokeh server?

- 현재 구현중인 시스템에서 데이터를 시각화해서 보여줘야 합니다. 비교적 간단한 시뮬레이션 툴을 만드는 것인데, 이 과정에서 간단히 plot만 보내주는 것이 아니라, 애니메이션을 그려주면 좋을 것 같아요. 
- 즉, 시간이 지남에 따라서 그림을 연속해서 새로 그려주는....음 그런데 이걸 하려고 서버를 돌릴 필요성이 있나 싶은데..아무튼 간에요. 
- bokeh 라이브러리를 이용해서 애니메이션을 그려고보려고 하니, 아무래도 서버를 구축해서 돌려야 하는 것 같아요. 그래서 한번 공부해보기로 했습니다. 

## do it

- [Running a Bokeh Server](https://bokeh.pydata.org/en/latest/docs/user_guide/server.html#userguide-server)에 보면 다음처럼 작성되어 있습니다. 

> The architecture of Bokeh is such that high-level “model objects” (representing things like plots, ranges, axes, glyphs, etc.) are created in Python, and then converted to a JSON format that is consumed by the client library, BokehJS. 

- 이를 번역하면, bokeh의 아키텍쳐는 하이레벨의 model object를 python으로 구축하고, 이를 BokehJS가 해석할 수 있는 JSON으로 변환해서 보내주는 식으로 진행된다는 말입니다. 
    1. python으로 그림을 그리고 
    2. 이걸 json으로 변환해서 넘겨주고 
    3. 그러면 BokehJS가 이걸 해석해서 그림을 그려줌
- 그러나, 클라이언트에서의 변화(유저의 클릭 등의 interaction)로 인해서 그림이 변경될 경우들이 있을 수 있고, 이를 위해서는 클라이언트의 변화를 입력받아서 그림을 변경해서 json을 전달해주는 놈이 하나 있어야겠죠. 그 아이가 바로 bokeh에서 만들어지는 서버가 되겠죠. 

## stop it

- 음, 제가 원하는 방식으로 애니메이션이 만들어지는 것은 아직 잘 안되는 것 같아요.
- 제가 원하는 것은 웹 상에서 특정한 버튼을 눌렀을 때 그것에 해당하는 애니메이션이 수행될 수 있도록 처리하는 것인데, 그 애니메이션을 위해서 따로 서버를 또 추가로 세팅해야 하는 것은 제가 볼 때는 매우 비효율적인 것으로 생각됩니다.
- 아무튼 일단은 좀 멈추고, 다른 라이브러리들을 좀 더 뒤져본 다음에 다시 올게요 하하핫


## reference

- <https://bokeh.pydata.org/en/latest/docs/user_guide/server.html#userguide-server>