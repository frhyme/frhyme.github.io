---
title: matplotlib에서 layer 순서 정하기 
category: python-lib
tags: python python-lib matplotlib zorder layer
---

## 파워포인트에서 '맨 앞으로 옮기기'같은 거요. 

- 파워포인트에서 폴리곤을 여러 개 그리고 뭐가 제일 앞에 나오는지, 뭐가 제일 뒤에 나오는지를 정하는 일이 있잖아요. 
- 그럴때 파워포인트에서는 단순하게 '맨 앞으로 옮기기'뭐 이런걸로 했는데, matplotlib에서는 어떻게 해야 하는지 모르겠어서 찾아봤씁니다. 

- 언제나 그렇듯이 스택오버플로우에 [제가 알고 싶은 부분](https://stackoverflow.com/questions/37246941/specifying-the-order-of-matplotlib-layers)이 이미 올라와있구요. 
- 그냥 그림을 그릴 때 `zorder`의 값을 지정해주면 그 값이 레이어의 위치라고 보시면 될 것 같아요. 
- 가장 바깥 쪽에 그려지는 그림일수록 `zorder`의 값이 커야 합니다 

- 그려봅니다. 

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
## 0, 1까지 사이의 값을 넘겨주면 colormap상에서 색 리스트를 리턴해줌 
colors = plt.cm.rainbow(np.linspace(0, 1, 7))

for i in range(0, 7):
    ## zorder가 layer의 위치 
    ## 클수록, 가장 위쪽에 보여진다고 생각하면 됨. 
    plt.scatter(0.2*i, 0, color=colors[i], s=50000, zorder=i)
xlim_min, xlim_max = plt.xlim()
plt.xlim(xlim_min-0.15, xlim_max+0.05)
plt.xticks([]), plt.yticks([])
plt.savefig('../../assets/images/markdown_img/180802_plt_zorder.svg')
plt.show()
```

![](assets/images/markdown_img/180802_plt_zorder.svg)