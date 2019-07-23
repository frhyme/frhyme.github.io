---
title: npy, npz 데이터를 잘 저장핮. 
category: python-libs
tags: python python-libs numpy pickle hdfs5
---

## data를 잘 저장합시다. 

- 깔짝깔짝 파이썬 가지고 놀때는 몰랐지만, 점점 복잡한 알고리즘을 사용하게 되면서, 한번 계산할때의 계산량이 일정 이상을 넘어가는 일이 발생합니다. 
- 따라서, 매번 새롭게 계산하는 것이 아니라, 계산된 결과를 임시 파일로 저장해놓으면 좋겠죠. 
- 다양한 방식이 있습니다, 텍스트도 있을 수있고, json, pickle도 있을 수 있죠. 
- 아무튼, 여기서는 우선 `numpy`에 있는 npy, npz를 사용해보려고 합니다. 
- 아래처럼 처리하면 됩니다. 

## save data as npy or npz

```python
import numpy as np 

x_data = np.arange(5)
y_data = np.sin(x)

# npy는 하나의 데이터를 저장할 때, 
# np.save('aaa.npy', x_data) 
# npz는 복수의 파일을 key-value pair의 형태로 저장할 때, 
np.savez('aaa.npz', x=x_data, y=y_data)
data = np.load('aaa.npz')
new_x, new_y = data['x'], data['y']
print("=="*20)
print(x==new_x)
print(x)
print(new_x)
print("=="*20)
print(y==new_y)
print(y)
print(new_y)
print("=="*20)
```

```
========================================
[ True  True  True  True  True]
[0 1 2 3 4]
[0 1 2 3 4]
========================================
[ True  True  True  True  True]
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]
[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]
========================================
```

## why use npy or npz than pickle 

- pickle은 파이썬 네이티브구조입니다. 그래서 그냥, `pickle.dump`, `pickle.load`등으로 바이너리로 직접 저장하고 그대로 가져올 수있어서 매우 편하죠. 
- 그러니까, 그냥 pickle로 저장하면 되는데, 굳이 npy같은걸 쓸 필요가 있나요? 
- 있습니다. 속도가 아주 많이 차이가 나죠. 아래 그림에서 보는 것처럼, npy의 경우 pickle에 비해서 훨씬 적은 저장 공간을 차지하고, 더 빨리 읽어줍니다.

![](https://i.stack.imgur.com/4d6yo.png)

- 물론 그러함에도, pickle은 훨씬 많은 자료구조를 저장할 수 있는데 반하여, npy, npz의 경우 `numpy.array`에 대해서만 저장할 수 있다는 차이가 있죠. 

### hdf5

- 그외에도 [hdf5](https://datascienceschool.net/view-notebook/f1c286a1d5164975a9909bb7a341bf4c/)같은 것도 있다는데, 이건 다음과 같은 특징이 있습니다. 
    - "Hierarchical Data Format version 5"의 약자. 
    - hdf5는 일종의 데이터베이스임. 단, 데이터베이스시스템에서 매니지하는 것들을 빼고 쿼리와 저장 같은것만 쭉 넣었다고 볼 수 있음.
    - 속도는 빠르다고 하고, NASA에서 관리하고 있다고 하니까 알아서 잘해주겠지 뭐 하하하하 
    - 아무튼, 링크한걸 보면 빠르기는 존나 빠른데, 단지, 구졸ㄹ 변경했다고 해서, 이렇게 까지 빨라질 수 있는 것인지 잘 모르겠다 하하하.


## why npy is smaller and faster than pickle?

- 그렇다면, 왜 pickle보다 npy가 더 빠르고 더 적은 공간을 차지하는 걸까요? 

## wrap-up

- 자료를 저장한다는 것은, 다시 **machine-readable** 이냐, **human-readable**이냐로 구분됩니다. 
- 즉, 기계가 읽을 수 잇는 형태를 말하는 binary형태와, 사람이 읽을 수 있는 json의 형태이냐로 구분되죠. 당연하지만 binary의 형태가 훨씬 적은 용량을 차지합니다.

## reference