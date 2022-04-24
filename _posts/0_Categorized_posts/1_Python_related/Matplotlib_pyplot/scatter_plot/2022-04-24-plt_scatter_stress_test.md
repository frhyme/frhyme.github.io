---
title: matplotlib - scatter 수에 따른 변화
category: matplotlib
tags: plt matplotlib scatter python figure
---

## matplotlib - scatter 수에 따른 변화

- scatter 에 point를 그릴 때, point의 수가 늘어남에 따라서 그리고 저장하는데 얼마나 시간이 걸리는지 간단하게 테스트 해봤습니다.
- '.svg' file로 처리했을 경우, 1,000,000 개를 그릴 때, file은 100MBd, 시간은 60초 이상 소요됩니다.
- 엄밀한 실험을 위해서는 현재 맥북의 리소스 가용도를 테스트 해야하지만, 귀찮으므로 하지 않겠습니다.

```platintext
scatter_size =      10, time =   0.06 sec, file_size =   0.02 MB
scatter_size =     100, time =   0.05 sec, file_size =   0.02 MB
scatter_size =    1000, time =   0.12 sec, file_size =   0.11 MB
scatter_size =   10000, time =   0.63 sec, file_size =   1.01 MB
scatter_size =  100000, time =   5.78 sec, file_size =   9.98 MB
scatter_size = 1000000, time =  64.28 sec, file_size =  99.69 MB
```

## Wrap-up

- 물론 filetype에 따라서 달라집니다. png나 다른 이미지로 처리하고, dpi를 조정하면 해결되는 문제이기는 하나, 원본을 그대로 유지하는 선에서 처리하는 것을 목적으로 하기 때문에 svg 파일로만 비교하였습니다.
- plotting은 여러 분야에서 필요로 하는 기능이지만 사실 꽤나 컴퓨팅 파워를 많이 사용하기도 하고 시간도 꽤 오래 걸리죠.
- [towardsdatascience - plotting in parallel with matplotlib and python](https://towardsdatascience.com/plotting-in-parallel-with-matplotlib-and-python-f7efb3d944de)를 보면, multiprocessing library를 이용해서 subplot간에 병렬처리하여 plotting 속도를 빠르게 한 경우는 보이는 것 같습니다.
- scatter의 경우 이미 독립적이기 때문에 multiprocessing module을 이용하여 각자 따로 그려 버릴 수도 있을 것 같습니다. 직접 코딩해볼 수 있을 것 같기는 한데, 늦었으므로 이 또한 다음에 해보겠습니다 하하.

## Code

```python
import numpy as np
import matplotlib.pyplot as plt
import time
import os


"""
2022.04.24 - sng_hn.lee - Init
- matplotlib에서 scatter를 처리하고 그림을 저장할 때, 소요되는 시간을 테스트 해봅니다.
---
scatter_size =      10, time =   0.06 sec, file_size =   0.02 MB
scatter_size =     100, time =   0.05 sec, file_size =   0.02 MB
scatter_size =    1000, time =   0.12 sec, file_size =   0.11 MB
scatter_size =   10000, time =   0.63 sec, file_size =   1.01 MB
scatter_size =  100000, time =   5.78 sec, file_size =   9.98 MB
scatter_size = 1000000, time =  64.28 sec, file_size =  99.69 MB
"""

file_type = '.svg'
for n in range(1, 7):
    scatter_size = 10**n
    file_name = f'n_{scatter_size}'
    file_name = file_name + file_type

    # draw figure
    plt.figure()

    xs = np.random.random(scatter_size)
    ys = np.random.random(scatter_size)

    start_time = time.time()
    plt.scatter(x=xs, y=ys)

    plt.savefig(file_name)
    end_time = time.time()
    time_duration = time.time() - start_time

    file_size = os.path.getsize(file_name)
    file_size = file_size / (1024.0 * 1024.0)
    print(f'scatter_size = {scatter_size:7d}, time = {time_duration:6.2f} sec, file_size = {file_size:6.2f} MB')
```
