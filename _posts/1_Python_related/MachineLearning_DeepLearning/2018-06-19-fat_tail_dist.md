---
title: student-t dist를 알아보겠습니다. 
category: python-lib
tags: python python-lib probability student-t matplotlib numpy scipy
---

## solving fat-tail with student-t

- 예측 문제들에서는 사실 이 아이들이 student-t를 따르든지, normal dist를 따르든지 큰 상관이 없을 것 같습니다만(exp등을 따르면 예측률에 약간 차이가 발생할 수는 있지만), 시뮬레이션을 돌리거나, random-sampling을 하거나 할 때는 해당 변수가 어떤 분포를 따르는지 매우 정확하게 예측하는 것이 필요합니다. 
- 보통 간편하게 normal dist를 따른다고 가정하고 움직이기는 하는데, 현실 세계에서의 문제는 보통 양쪽 극단이 뚱뚱한 경우들이 있어요. normal dist보다 양쪽 극단의 probability density가 높아지는 경우죠. 
- 이를 해결하기 위해서, student-t dist를 활용합니다. 

## plot student-t dist

- `scipy.stats.t`를 이용하여, 
- x = `np.linspace(-4, 4, 100)`의 probability density function의 값을 계산해주고, 
- degree of freedom을 다르게 하여 plotting해줍니다.
- 아래 그림에서 보는 것처러, df가 작을수록 fat tail 이 되고, df가 커질수록 normal dist에 가까워집니다. 

```python
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 

x = np.linspace(-4, 4, 100)

plt.figure(figsize=(12, 6))
for df in [1, 2, 5, 10]:
    rv = sp.stats.t(df=df)
    plt.plot(x, rv.pdf(x), linestyle=':',
             label="student-t (dof={})".format(df) )
plt.plot(xx, sp.stats.norm().pdf(xx), label="Normal", lw=5, linestyle='--', alpha=0.9)
plt.legend()
plt.savefig('../../assets/images/markdown_img/180619_1444_student_t_dist.svg')
plt.show()
```

![](/assets/images/markdown_img/180619_1444_student_t_dist.svg)

## wrap-up 

- 일단 알겠는데, 현실 문제에서 이를 어떻게 적용해서 풀어야 하지? 나중에 여러 확률 변수를 활용해서 문제를 풀어야 할 일이 있을 때 사용할 수 있을 것 같음. 

## reference 

- <https://datascienceschool.net/view-notebook/8956e37db86c44b3b1b3a4c3357e590c/>