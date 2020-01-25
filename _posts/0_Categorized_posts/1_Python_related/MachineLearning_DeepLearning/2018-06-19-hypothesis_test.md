---
title: 데이터의 분포를 검정해봅시다. 
category: python-lib
tags: python python-lib data-sceienc hypothesis-test scipy 
---

## 데이터의 분포를 검정해봅시다. 

- 데이터를 분석하기 전에 개별 데이터 칼럼들에 대해서 데이터 정리를 해줍니다. skewness가 있는지, qqplot상 normality를 가지는지를 체크해보죠. 
- 그런데, 이건 어느 정도 그냥 그림으로 때려 보는 거고, 엄밀하게 'normality'를 가진다, 가지지 않는다 를 명확하게 검정해주는 방법이 있을 것 같아요. 그래서 찾아보니, 방법이 당연히 있습니다. 
- 또한, 단순히 normality test뿐만 아니라, 해당 데이터의 분포의 분산이 무엇인지, 평균이 어느정도인지, 를 확인해보는 것도 가능합니다. 

## hypothesis test

- 유사공대생으로서, 수식없이 설명합니다 하하하핫. 
    - 일단 맞는지 보려면, 가정을 해야 합니다. 예를 들면 '이 아이의 평균은 0이다'처럼요. 
    - 그 가정(평균은 0이다) 하에서, 현재 가지고 있는 데이터 sample이 나올 수 있는 확률을 계산합니다. 
    - 그 확률값이 바로 p-value가 되죠. 
    - 만약 p-value가 0.4-0.7 정도 라고 합시다. 이럼 약간 애매하죠? 가정이 아니라고 하기 애매하죠? 
    - 만약 p-value가 0.05라고 합시다. 이 때는 가정이 맞지 않다고 할 수 있을 것 같아요. '확률적으로 충분히 작으니까요'
- 이게 다에요. 현재 우리가 가정한 상황/세계 속에서 해당 결과가 나올 법하냐, 나올법하지 않은가를 검정하는 것을 hypothesis test라고 합니다. 
- 흐름은 대략 이래요. 그리고 우리가 밑의 코드에서 할 것들은 그냥 두 데이터 분포를 넣어주고 `p-value`가 어떻게 나오는지 보는 것이 다입니다. 

## do it.

- 아래에서는 평균이 같은지, 분산이 같은지 등을 체크합니다. 만약, Maximal Likelihood Estimation 처럼 추정을 하고 싶다면, 적합한 분포를 넣어주고 비교하면 되겠죠. 

```python
# 두 독립표본의 평균이 같은지 체크하는 검정 
from scipy.stats import ttest_ind

n = 5000
x = np.random.normal(1, 4, n)
ys = [np.random.uniform(-4, 5, n), 
      np.random.exponential(1, n), 
      np.random.normal(1, 50, n),
      np.random.normal(1, 100, n)
     ]
for y in ys:
    print("평균이 같은지 확인, p-value: {:.3f}".format(ttest_ind(x, y).pvalue))
print("------------")
# 등분산 검정: 두 분포의 분산이 같은지 체크하는 검정 
from scipy.stats import bartlett
n = 5000
x = np.random.normal(0, 4, n)
ys = [np.random.normal(1, 4, n), 
      np.random.normal(1, 3.5, n), 
      np.random.normal(1, 4.1, n)
     ]
for y in ys:
    print("등분산 검정, p-value: {:.3f}".format(bartlett(x, y).pvalue))

# normality test 
# 사실, 아래 검정은, normality test뿐만 아니라, 두 dist가 같은 dist인지를 확인하는 검정방법이다. 
print("------------")
from scipy.stats import ks_2samp
n = 5000
x = np.random.normal(0, 1, n)
ys = [np.random.normal(0, 1.5, n), 
      np.random.standard_t(8, n),
      np.random.standard_t(10, n),
      np.random.standard_t(50, n)
     ]
for y in ys:
    print("같은 분포인지를 확인하는 검정, p-value: {:.3f}".format(ks_2samp(x, y).pvalue))
```

```
평균이 같은지 확인, p-value: 0.000
평균이 같은지 확인, p-value: 0.131
평균이 같은지 확인, p-value: 0.393
평균이 같은지 확인, p-value: 0.154
------------
등분산 검정, p-value: 0.274
등분산 검정, p-value: 0.000
등분산 검정, p-value: 0.134
------------
같은 분포인지를 확인하는 검정, p-value: 0.000
같은 분포인지를 확인하는 검정, p-value: 0.176
같은 분포인지를 확인하는 검정, p-value: 0.607
같은 분포인지를 확인하는 검정, p-value: 0.418
```

## wrap-up

- 흐음. 쓸말이 없다. 

## reference 

- <https://datascienceschool.net/view-notebook/14bde0cc05514b2cae2088805ef9ed52/>