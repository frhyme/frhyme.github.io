---
title: tsne는 정말 얼마나 느린가요? pca보다 얼마나 느린가요?
category: python-lib
tags: python python-lib dimensionality-reductino tsne pca 

---

## tsne는 얼마나 느린가요. 

- 보통 차원이 너무 큰 데이터를 다루다 보니, 차원축소를 해야 할 때가 많은데, 그때 `pca`를 써야하나, `tsne`를 써야 하나 고민하게 됩니다. pca가 훨씬 빠르기는 한데, 굴곡이 진 부분, 즉 구부러진 부분을 무시하게 된다는 단점이 있습니다. 대신 tsne는 구부러진 부분도 펴서 잘 다려준다는 장점이 있스비다. 좋은 다리미질이다!!
- 아무튼, 평소에 별 생각없이 tsne를 쓰다가 계산이 끝나지 않는 일이 너무 많아서, 도대체 얼마나 느린가?를 미리 좀 가늠해야 할 것 같아서 시간 계산을 해봤습니다. 
    - 제가 계산하는 컴퓨터는 맥북에어..
        - MacBook Air (13-inch, Early 2015)
        - 프로세서: 1.6GHz intel Core i5
        - 메모리: 4GB 1600 MHz DDR3
        - 그래픽: Intel HD Graphics 6000 1536 MB
- 쓰고보니 이런 컴퓨터로 무슨 계산을 하는가...노인 학대가 아닌가...라는 생각도 들지만 그래도 일단 해보겠습니다....

## 랜덤하게 어레이를 만들어주는 함수를 생성

- dimension, sample size에 따라서 어레이를 만들어 리턴해주는 함수를 만들었습니다. 

```python
import nupmy as np 

def make_n_dim_norm_array(dim=2, sample_size=100, mu1=1, mu2=5):
    xy1 = np.array([np.random.normal(mu1, 1, sample_size)]*dim) # shape: 
    xy2 = np.array([np.random.normal(mu2, 1, sample_size)]*dim)
    xy = [xy1, xy2]
    """
    horizontally stack: 현재 xy는 2 by 10의 리스트가 row로 쌓여있는 형태임. 
    이를 hstack(horizontally stack)해주면, 수평선 방향으로 쌓아준다는 것이니까, 
    xy1 의 오른쪽에 xy2가 붙는다고 생각하면 됨. 따라서 2*10 + 2*10 이므로 2*20이 됨. 
    """
    xy = np.hstack(xy)# shape: 2*20 
    """
    그 다음 shape을 바꿔서 각 row에 xy가 있도록 변경
    """
    xy = xy.reshape(sample_size*2, dim) 
    return xy
```

## dim, sample size에 따라서 얼마나 달라지는가?? 

- dimension은 고정하고 sample size만 변경해가면서 TSNE, PCA의 계산 시간 비교를 해봅니다. 매 계산마다 3번하여 평균을 냅니다. 


### dimension matter?

- sample size를 고정하고 dimension을 변화해봤지만, 디멘션의 크기에 따라서는 계산시간이 별로 달라지지 않아요. 이는 tsne가 샘플 간의 거리를 재서 새로운 차원을 구축하는 테크닉이기 때문에, 차원을 늘린다고 해도, 결국 그 값들은 유클리디안 거리를 계산하는 정도로만 쓰일 뿐입니다. 
- 대신 sample size가 늘어날수록 계산해야 하는 edge가 늘어나기 때문에 시간이 오래 걸리겠죠. 
- 물론, 지금은 그냥 sample size가 200밖에 안되는데도 계산시간이 9초가 걸립니다. 흐음. 만약 계산시간이 리니어하게 움직인다고 해도, 20000개의 로우에 대해서 계산을 하려면 15분이 걸리네요. 만약 익스포넨셜하다면....으 끔찍하군요. 

```python
import time

for i in range(0, 5):
    dim = 3+3*i
    sample_size = 200
    xy = make_n_dim_norm_array(dim=dim, sample_size = sample_size, mu1=1, mu2 = 2+i)
    iter_num = 3
    
    TSNE_total = 0 
    for j in range(0, iter_num):
        TSNE_time = time.time()    
        TSNE(n_components=2).fit_transform(xy)
        TSNE_time = time.time() - TSNE_time
        TSNE_total+=TSNE_time
    PCA_total = 0 
    for j in range(0, iter_num):
        PCA_time = time.time()    
        PCA(n_components=2).fit_transform(xy)
        PCA_time = time.time() - PCA_time
        PCA_total+=PCA_time
    TSNE_total /=iter_num
    PCA_total /=iter_num
    print("TSNE_mean: {}, PCA_mean: {}".format(round(TSNE_total, 2), round(PCA_total, 2)))
    print("dim: {}, sample_size: {}, how faster? {}".format(dim, sample_size, round(TSNE_total/PCA_total,2)))
```

```
TSNE_mean: 9.16, PCA_mean: 0.0
dim: 3, sample_size: 200, how faster? 7494.0
TSNE_mean: 9.49, PCA_mean: 0.0
dim: 6, sample_size: 200, how faster? 18506.24
TSNE_mean: 9.06, PCA_mean: 0.0
dim: 9, sample_size: 200, how faster? 9407.07
TSNE_mean: 8.93, PCA_mean: 0.0
dim: 12, sample_size: 200, how faster? 1894.6
TSNE_mean: 8.45, PCA_mean: 0.01
dim: 15, sample_size: 200, how faster? 1650.62
```

### sample size matter? and plotting 

- dimension은 큰 영향을 주지 않고요, 그렇다면, sample size에 얼마나 민감하게 움직일까요? 
- sample size를 늘려가면서 값을 확인해보고, sample size에 따른 변화를 플로팅해보겠습니다. 
- 저는 좀 당연하게 익스포넨셜하겠지? 라고 생각했는데, sample size( 100 부터 4100까지)에서는 아직 익스포넨셜하다고 하기는 조금 애매합니다. 물론 제가 너무 sample size를 적게 잡았는데, 제 컴퓨터가 구려서 이거 하는데도 너무 많은 시간이 소요되었어요...
- 아무튼 tsne는 샘플 사이즈가 1000개만 되어도 1분이 걸립니다.... 끔찍. 

![](/assets/images/markdown_img/tsne_time_plotting_20180517.svg)

```python
import time
import matplotlib.pyplot as plt

plt_lst = []
for i in range(0, 5):
    dim = 3
    sample_size = 100+i*1000
    xy = make_n_dim_norm_array(dim=dim, sample_size = sample_size, mu1=1, mu2 = 2+i)
    iter_num = 1
    
    TSNE_total = 0 
    for j in range(0, iter_num):
        TSNE_time = time.time()    
        TSNE(n_components=2).fit_transform(xy)
        TSNE_time = time.time() - TSNE_time
        TSNE_total+=TSNE_time
    PCA_total = 0 
    for j in range(0, iter_num):
        PCA_time = time.time()    
        PCA(n_components=2).fit_transform(xy)
        PCA_time = time.time() - PCA_time
        PCA_total+=PCA_time
    TSNE_total /=iter_num
    PCA_total /=iter_num
    plt_lst.append((sample_size, TSNE_total))
    print("TSNE_mean: {}, PCA_mean: {}".format(round(TSNE_total, 2), round(PCA_total, 2)))
    print("dim: {}, sample_size: {}, how faster? {}".format(dim, sample_size, round(TSNE_total/PCA_total,2)))

plt.figure(figsize=(12, 4))
x_lst = [x[0] for x in plt_lst]
y_lst = [x[1] for x in plt_lst]
plt.plot(x_lst, y_lst, marker='o')
plt.plot([x_lst[0], x_lst[-1]], [y_lst[0], y_lst[-1]])
plt.savefig("../../assets/images/markdown_img/tsne_time_plotting_20180517.svg")
plt.show()
```

```
TSNE_mean: 3.71, PCA_mean: 0.0
dim: 3, sample_size: 100, how faster? 6250.78
TSNE_mean: 62.17, PCA_mean: 0.01
dim: 3, sample_size: 1100, how faster? 5315.78
TSNE_mean: 131.66, PCA_mean: 0.04
dim: 3, sample_size: 2100, how faster? 3086.22
TSNE_mean: 195.78, PCA_mean: 0.02
dim: 3, sample_size: 3100, how faster? 9979.7
TSNE_mean: 279.01, PCA_mean: 0.02
dim: 3, sample_size: 4100, how faster? 12288.78
```


## pca는 언제 느려지는가??

- pca는 tsne에 비해서 압도적으로 빠른 모습을 보이는데 언제 느려지는지 한번 혹사해보려고 합니다 하하핫. 
- 대략 샘플 사이즈가 10000개를 넘어가면 1초를 넘기기 시작하는군요. 그래도 나름 리니어하게 증가하는 편인 것 같습니다. 


```python
import time

plt_lst = []
for i in range(0, 10):
    dim = 100
    sample_size = 10000*(i+1)
    xy = make_n_dim_norm_array(dim=dim, sample_size = sample_size, mu1=1, mu2 = 2+i)
    iter_num = 3
    for j in range(0, iter_num):
        PCA_time = time.time()    
        PCA(n_components=2).fit_transform(xy)
        PCA_time = time.time() - PCA_time
        PCA_total+=PCA_time
    PCA_total /=iter_num
    plt_lst.append((sample_size, PCA_total))
    print("dim: {}, sample_size: {}, PCA_mean? {}".format(dim, sample_size, round(PCA_total,2)))
```

```
dim: 100, sample_size: 10000, PCA_mean? 1.59
dim: 100, sample_size: 20000, PCA_mean? 0.98
dim: 100, sample_size: 30000, PCA_mean? 0.89
dim: 100, sample_size: 40000, PCA_mean? 1.04
dim: 100, sample_size: 50000, PCA_mean? 1.24
dim: 100, sample_size: 60000, PCA_mean? 1.48
dim: 100, sample_size: 70000, PCA_mean? 1.96
dim: 100, sample_size: 80000, PCA_mean? 3.08
dim: 100, sample_size: 90000, PCA_mean? 3.08
dim: 100, sample_size: 100000, PCA_mean? 3.67
```