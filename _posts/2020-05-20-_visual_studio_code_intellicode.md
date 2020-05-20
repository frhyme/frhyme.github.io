---
title: MS - IntelliCode 하지만 쓰지마세요
category: VS-CODE
tags: VS-CODE intellisense 
---

## Intro

- 이번에 [MS - IntelliCoce](https://go.microsoft.com/fwlink/?linkid=872679)라는 VS-code extension을 설치했습니다.
- 저는 vs-code에서 python을 개발하는데, 이유는 잘 모르겠지만, 제 vs-code 에서는 intellisense가 잘 작동하지 않습니다. 몇 가지 설정이 잘 안되어 있는 것이겠지만, 아무튼 그래요.
- 그외로도 좀 더 편하게 코딩할 수 있도록 도와주는 다른 기능들이 있을텐데, 이전의 맥북은 RAM이 4GB가 되지 않아서 설치할 엄두를 내지 못했죠.
- 하지만 지금은 16GB이므로 마구마구 설치하도록 합니다 호호호.

## About MS - IntelliCode

- "IntelliCode"라는 말에서 보는 것처럼, "똑똑하게 코딩하자"라는 말을 내포하고 있는 것이죠.
- Microsoft는 Github을 먹었고(인수했고), 마이크로소프트는 깃헙에 공개된 주요 프로젝트들의 코드들을 IntelliCode AI를 학습시켰다고 합니다. 여기서 "주요 프로젝트"라는 것은 결국 별(star)의 개수가 되겠죠.
- 어떻게 학습을 시켰는지는 몰라도, 아마, "보통 개발자가 이 코드를 쓰면 얘네를 쓸 확률이 높더라"라는 식으로 학습을 시켜서 개발을 빠르게 도와주는 것으로 예상됩니다.
- 다만, 개발자별로 자주 쓰는 형태는 판이하게 다를 수 있죠. 가령 저의 경우 주로 `networkX`를 사용하는데 그렇다면 제가 NetworkX를 많이 사용하면 이 라이브러리를 쓸때 더 편하도록, 혹은 제가 자주 쓰는 패턴을 추천해주는 방식으로 코딩이 되는 것인지, 그 부분은 명확하게 설명되어 있지 않습니다.

### For python user

- python 사용자들은 [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)대로 설치하면 됩니다.
- 딱히 어려운 부분이 있지는 않고, 그냥 python interpreter(혹은 vs-code python extension)을 잘 설치했다면 알아서 진행됩니다.
- 설치해서 사용해봤는데, 사실, 기존 intellisense 대비 무슨 차이가 있는지 잘 모르겠네요.

### 하지만 쓰지마세요

- 별로 좋은 확장이라고 생각되지 않습니다. 거창하게 나와 있지만, 그냥 기본 intellisence에 비해 전혀 강점이 있지 않습니다.
- 가령 다음의 코드가 있다고 해보겠습니다.

```python
import numpy as np

np.random.random()
```

- 그냥 기본 [python extension](https://code.visualstudio.com/docs/languages/python)을 설치하면, 여기에는 [jedi](https://jedi.readthedocs.io/en/latest/)를 사용하여 intellisense가 실행됩니다. jedi에서는 위와 같은 코드를 칠 때 `np.random()`이 타이핑되면 내부 메소드인 `.random()`가 나오게 되죠. 당연히 이렇게 돌아가야 합니다.
- 다만, IntelliCode의 경우는 `np.random`을 치고 나면 내부 메소드인 `.random()`이 제시되지 않습니다. 왜 그런지, 이유를 모르겠네요. 그리고, IntelliCode를 설치하게 되면 jedi는 자동으로 enable가 아닌 것으로 설정에서 변경됩니다.
- 이런 식으로 할 거면 왜 만들었는지, 저는 당최 이해할 수가 없네요. 최악이라고 생각합니다.
- 그러함에도, 제가 잘못 써서 그럴 수 있으니, 잘 사용하고 계신 분들은 어떻게 사용하시는지 알려주시면 감사하겠네요.

## wrap-up

- 알파고가 등장한 지도 매우 오래되었고, 따라서 어느 정도는 더 똑똑한 알고리즘이 코딩을 편하게 해준다고 생각했지만, 제가 보기에는 아직 갈길이 먼 것 같아요.
- 사실, 그냥 "이 사람이 많이 쓰는 메소드"만 빈도로 정렬해서 처리하는 것을 벤치마크로만 설정하고 진행해도 이기기 어려울 겁니다. 아주 냉정하게 말해도 그래요.
