---
title: nx의 layout을 rescaling합니다. 
category: python-lib
tags: networkx python python-lib layout rescaling github issue 
---

## rescaling layout 

- networkx로 네트워크를 시각화할 때 다양한 layout을 씁니다. 보통 쓰는 spring, spectral, shell 등의 레이아웃에는 문제가 없는데, 아래와 같은 layout을 사용할때는 0.0과 1.0사이에 값이 분포하는 것이 아니라, 값이 훨씬 커지게 됩니다. 

```python
pos = nx.drawing.nx_agraph.graphviz_layout(R_net, prog='dot')
```

- 사실 보통 이게 큰 문제가 되지는 않지만, 이 값때문에 그림의 layout이 약간 무너지는 경우들이 있습니다. 예를 들면 그림이 title과 겹친다거나, 하는 일들이 있죠. 
- 그래서 가능하면 간단하게 layout을 변경해주는 것이 필요합니다. 
- [networkx.rescaled_layout](https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.rescale_layout.html)을 사용합니다. 

## issue 

- 그런데, 좀 이상하게 보통 nx에서의 포지션은 딕셔너리로 리턴이 됩니다. 예를 들면 아래와 같죠. 

```python
pos = nx.drawing.nx_agraph.graphviz_layout(R_net, prog='dot')
for k, v in pos.items():
    print("{}: {}".format(k, v))
```

```
R04: (423.0, 234.0)
R17: (207.0, 162.0)
R14: (423.0, 162.0)
R13: (639.0, 162.0)
R11: (279.0, 90.0)
R16: (117.0, 90.0)
R07: (351.0, 90.0)
R01: (423.0, 90.0)
R09: (639.0, 90.0)
R15: (495.0, 90.0)
R05: (711.0, 90.0)
R03: (207.0, 90.0)
R12: (567.0, 90.0)
R00: (387.0, 18.0)
R19: (27.0, 18.0)
R18: (243.0, 18.0)
R10: (99.0, 18.0)
R02: (171.0, 18.0)
R06: (567.0, 18.0)
R08: (315.0, 18.0)
```

- 그런데, [networkx.rescaled_layout](https://networkx.github.io/documentation/latest/reference/generated/networkx.drawing.layout.rescale_layout.html) 여기서는 input이 `np.array`가 되어야 합니다. 
- 결국 코드가 다음과 같아야 한다는 이야기죠. 
- 몇 줄만 추가하면 되는건데, 굳이 이렇게 할 필요가 있을까요? 의문이 듭니다 흠. 

```python
pos = nx.drawing.nx_agraph.graphviz_layout(R_net, prog='dot')
new_pos = nx.drawing.layout.rescale_layout(np.array([[v[0], v[1]] for v in pos.values()]), 1)
new_pos = {k: tuple(v) for k, v in zip(pos.keys(), new_pos)}
for k, v in new_pos.items():
    print("{}: {}".format(k, v))
```

```
R04: (0.16883116883116883, 0.43636363636363634)
R17: (-0.45454545454545453, 0.22857142857142859)
R14: (0.16883116883116883, 0.22857142857142859)
R13: (0.79220779220779225, 0.22857142857142859)
R11: (-0.24675324675324675, 0.020779220779220786)
R16: (-0.7142857142857143, 0.020779220779220786)
R07: (-0.03896103896103896, 0.020779220779220786)
R01: (0.16883116883116883, 0.020779220779220786)
R09: (0.79220779220779225, 0.020779220779220786)
R15: (0.37662337662337664, 0.020779220779220786)
R05: (1.0, 0.020779220779220786)
R03: (-0.45454545454545453, 0.020779220779220786)
R12: (0.58441558441558439, 0.020779220779220786)
R00: (0.064935064935064929, -0.18701298701298699)
R19: (-0.97402597402597402, -0.18701298701298699)
R18: (-0.35064935064935066, -0.18701298701298699)
R10: (-0.76623376623376627, -0.18701298701298699)
R02: (-0.55844155844155841, -0.18701298701298699)
R06: (0.58441558441558439, -0.18701298701298699)
R08: (-0.14285714285714285, -0.18701298701298699)
```

## 이슈를 날리자. 

- 제가 최근에 파이콘에 다녀왔습니다. 다녀오니까 처음에는 가볍게 파이썬을 시작한 사람들이 나중에는 오픈소스에 기여를 하기 시작하더군요. 아주 재밌다는 생각을 했어요. 그래서 돌아오면서 저도 가능하면 오픈소스 생태계에 기여해야겠다, 라고 생각을 했습니다. 
- 그래서 [networkx(github)](https://github.com/networkx)에 약간 무모하지만 이슈를 날려보기로 마음 먹었습니다. 


```
I am using `networkx.drawing.layout.rescale_layout`.

However, in this function, input is fixed to `np.array`.
In fact, other layouts (`nx.spring_layout`, `nx.spectral_layout`, etc.) return a dictionary (key: node label, value: pos tuple (x, y)).

So, for `networkx.drawing.layout.rescale_layout`, I think it would be useful to change the input to dictionary (key: node label, value: pos tuple (x, y)).

To change to the code:

I think this case is more versatile and I would like to ask you what you think.
```

```python
def rescale_layout(pos, scale=1):
    pos_v = np.array([[v[0], v[1]] for v in pos.values()])
    lim = 0  # max coordinate for all axes
    for i in range(pos_v.shape[1]):
        pos_v[:, i] -= pos_v[:, i].mean()
        lim = max(abs(pos_v[:, i]).max(), lim)
    # rescale to (-scale, scale) in all directions, preserves aspect
    if lim > 0:
        for i in range(pos_v.shape[1]):
            pos_v[:, i] *= scale / lim
    return {k: tuple(v) for k, v in zip(pos.keys(), pos_v)}
```

- 떨리는군요 흠...


## wrap-up

- 정작 코딩하는 것은 따로 있었는데 또 이렇게 말려서, 다른 길로 빠집니다 네 제 인생이 그렇져 뭐 하하핫