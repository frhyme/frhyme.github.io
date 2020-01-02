---
title: matplotlib legend 조절하기
category: python-lib
tags: python python-lib matplotlib legend
---

## legend를 잘 넣어야 글을 덜 적을 수 있습니다. 

- `matplotlib`로 그림을 열심히 그리고 나서, "이 색깔의 모양 저것은 무엇이고..." 하는 식으로 설명을 덧붙이면 매우 피곤해집니다. 이런 짓을 좀 덜 하려면 legend만 잘 넣어도 됩니다. 
- 포스트로 쓸 만큼, 뭐 대단한건 아닌데 뭐 그래도 일단 쓰겠습니다. 시작했으니까요. 

## label을 잘 넣읍시다. 

- 결과적으로 말하자면, 그냥 `plt.legend()`만 넣어주면 되긴 합니다. 물론, 이렇게 하려면 figure에 새로운 그림을 넣어줄 때마다(`scatter`, or `plot`, ...) label을 함께 넘겨줍니다. 잘 넣어주면, 나중에 `plt.legend()`를 해주면 알아서 잘 출력해줘요. 

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

plt.plot(np.arange(0, 10), np.random.normal(0, 1, 10), linestyle='--', c=plt.cm.rainbow(0.9), label='plot')
plt.scatter(np.random.normal(5, 2.5, 10), np.random.normal(0, 1, 10), 
            marker='o', c=plt.cm.rainbow(0.5), label='scatter')
plt.scatter(np.random.normal(5, 2.5, 10), np.random.normal(0, 1, 10), 
            marker='x', c=plt.cm.rainbow(0.1), label='scatter')
plt.legend(fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180601_legend_inside.svg')
plt.show()
```

- 아래처럼 legend가 표시되는 것을 알 수 있습니다. 단, legend의 위치는, 따로 값을 넣어주지 않으면 `matplotlib`가 알아서 최적이라고 생각하는 곳에 그려줍니다. 

![](/assets/images/markdown_img/180601_legend_inside.svg)

## legend 위치 조절

- 그런데, legend의 위치를 바꾸고 싶을 때가 있습니다. 특히, figure 안에 legend가 그려지는 것이 싫을 경우에는, 아래처럼, 해주면 됩니다. 
    - 다음처럼 넘겨주면, legend의 왼쪽 위를 bbox_to_anchor의 좌표로 고정합니다. 
    - 즉 아래의 뜻은 figure의 width, height 를 각각 0.0 - 1.0 사이로 봤을때, legend의 왼쪽 위를 figure의 1.0, 1.0 에 위치 시킨다는 의미이므로, figure의 바깥쪽에 legend가 표시되게 됩니다. 

```python
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0)
```

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

plt.plot(np.arange(0, 10), np.random.normal(0, 1, 10), linestyle='--', c=plt.cm.rainbow(0.9), label='plot')
plt.scatter(np.random.normal(5, 2.5, 10), np.random.normal(0, 1, 10), 
            marker='o', c=plt.cm.rainbow(0.5), label='scatter')
plt.scatter(np.random.normal(5, 2.5, 10), np.random.normal(0, 1, 10), 
            marker='x', c=plt.cm.rainbow(0.1), label='scatter')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180601_legend_outside.svg')
plt.show()
```

![](/assets/images/markdown_img/180601_legend_outside.svg)

## wrap-up 

- lable을 잘 입력합시다 매번!!