---
title: javascript에서 colormap 사용하기.
category: javascript
tags: javascript colormap 
---

## colormap

- 차트를 그릴 때 일일이 색깔을 지정하는 것은 매우 귀찮은 일입니다. 데이터의 칼럼의 수에 따라서 자동으로 색깔을 지정하고, 예쁘게 만들어주고 싶은데, 몇개가 들어올지 모르는데, 매번 색깔을 배정할 수는 없으니까요. 
- 아무튼 이럴 때 colormap을 씁니다. 

## colormap in javascript 

- 찾아보니 [javascript에서도 colormap을 지원하는 라이브러리](https://www.npmjs.com/package/colormap)가 있습니다.
    - 그런데, CDN을 통해서 설치하는 것이 아니라, `npm`을 사용해서 설치해야 하고, 
    - 설치한 다음에도 `requirejs`를 사용해서 돌려야 하는 것 같습니다. 
- 몇 번 시도 해봤는데 잘 안되고, 또 다른 colormap이 있는 것 같기는 한데 잘 모르겠어서, 그냥 python의 matplotlib의 colormap을 이용해서 RGB, HSL 의 형식으로 넘겨주기로 했습니다. 
- 혹시 잘 아시는 분이 있다면 알려주시면 감사하겠습니다. 

## colormap in matplotlib

- 순서는 대략 다음과 같습니다. 
    - maptlotlib의 칼라맵에서 필요한 수만큼의 색깔을 뽑고
    - 이를 RGBA의 형식으로 변환해서 리스트에 넣고 
    - 이를 Json으로 flask에 넘겨준다.

- 간단하게 다음처럼 함수를 작성하였습니다. 

```python
def extract_RGB_from_cmap(current_cmap=plt.cm.rainbow, color_num = 7, alpha=0.7):
    color_lst = [list(current_cmap(i)) for i in np.linspace(0, 1.0, color_num)]
    color_lst = [f"rgba{(c[0]*255, c[1]*255, c[2]*255, alpha)}"for c in color_lst]
    return color_lst
```

- 이렇게 만들고, 넘겨주면 알아서 잘 작동하네요 하하핫

## wrap-up

- 우선 왜, 자바스크립트에 이런 부분이 없는지 약간 의아하기는 합니다. 뭐 찾아보면 있지 않을까요?
- 물론 어차피 RGBA로 만드는 것이니까 알아서 값 세팅해서 넘겨도 될것 같기는 합니다만, 그래도 혹시나 해서 만들어봤습니다. 