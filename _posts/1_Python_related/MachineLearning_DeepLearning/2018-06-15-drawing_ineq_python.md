---
title: matplotlib로 부등식 그려보기 
category: python-lib
tags: python python-lib matplotlib 
---

## inequality 를 matplotlib에 표현하기

- 요즘 다시 python으로 LP 푸는 법을 다시 정리해보고 있는데, 그리다보니 부등식을 2차원에 그려보는 일이 필요한 것 같아요. 손으로 그리는게 훨씬 빠른데...아무튼. 
- 가능하면 좀 generic한 function을 만들어보는 것도 괜찮겠지만, 그건 좀 어려운 일인것 같아서 제외하였습니다. 그냥 이미 교점을 아는 상태에서, 혹은 함수를 아는 상태에서 어떻게 그려줄 수 있는지만 간단하게 정리할게요. 

## fill and fill_between

- matplotlib에 있는 두 가지 function, `fill`, `fill_between`을 활용합니다. 
- `fill(x, y)`: x sequence와 y sequence를 연속으로 이어지고 그 내면을 모두 채워줍니다. 
- `fill_between(x, y1, y2)`: y1과 y1의 교차점을 채워줍니다 

### can you fill it ~~~

- 채웁니다. 간단합니다. 

```python
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))
x = [0, 1, 1, 0.5, 0] + [0]
y = [0, 0, 3, 2, 4] + [0]

plt.plot(x, y, 'red', linestyle=':')
plt.scatter(x, y, s=100) # 꼭지점 그리기
plt.fill(x, y, 'g', alpha=0.5) 
# 만약 그림이 잘 안 그려진다면, polygon이 선형의 형태가 아닌지 체크해보는 것이 좋습니다. 

xs = np.linspace(2, 5, 100)
#왼쪽 그림
plt.plot(xs, xs, color='blue')
plt.fill_between(xs, y1=xs, y2=np.log(xs))
# 오른쪽 그림 
plt.plot(xs, np.log(xs), color='blue')
plt.savefig('../../assets/images/markdown_img/180615_1909_plt_fill.svg')
plt.show()
```

![](/assets/images/markdown_img/180615_1909_plt_fill.svg)

## wrap-up

- 비교적 간단해 보이기는 하는데, 다양한 경우를 모두 맞춰서 적합하게 그려주는 것은 어려운 것 같아요. 

## reference 

- <https://stackoverflow.com/questions/17576508/python-matplotlib-drawing-linear-inequality-functions?rq=1>
- <https://stackoverflow.com/questions/17576508/python-matplotlib-drawing-linear-inequality-functions>