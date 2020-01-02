---
title: 데이터분석이고 나발이고 일단 수치들을 잘 표준화하는 것이 필요하지 않을까요? 
category: data-science
tags: data-science python python-lib scaling

---

## scaling is most important thing ever. 

- 엑셀을 열어보면 늘 칼럼의 데이터는 엉망진창입니다. missing data는 기본이고, 값이 있어도 지나치게 큰 데이터들(outlier)이 있거나, 칼럼 별로 range가 다르거나, 하는 이슈들이 있죠. 물론 robust한 clustering, classifier들이 있어서, 데이터 전처리를 무시해도 되는 경우들이 있기는 하지만, 별로 좋은 태도는 아니라고 생각됩니다. 
- 또한 개별 feature들은 모두 특정한 분포를 따를 것입니다. 그 분포를 중심으로 표준화를 해주는 것이 좋은데, 계산의 편의성을 위해서 그냥 모든 피쳐는 정규분포를 따른다고 가정하고(norm(0, 1)) 그 공간 내에서 어느 지점에 위치하는 지로 변환해줍니다. 
    - 예를 들어, 원래 피쳐에서 평균은 10이고 분산이 4라면, 12인 값은 1로 변환이 되겠죠. 
    - 또한 이렇게 변환을 하면, outlier는 무엇이고, 평균에서 얼마나 떨어져 있는지를 보다 명확하게 알 수 있습니다. 
    - 만약 지나치게 평균에서 떨어진 값들이 많다면 해당 분포는 정규분포가 아니다 라고 말할 수도 있겠네요. 

## 그래서 이상적인 scaling이란 무엇일까요? 

- 음 조금 애매하지만, 다음 조건을 만족하면 될 것 같아요. 
1. 해당 데이터 따르는 데이터 분포에 따라 값을 변환한 경우(보통 norm(0,1)로 가정)
2. 명백하게 아웃라이어 인 경우를 제외함(이건 사실 어느 정도 주관적이죠)
3. 모든 칼럼이 칼럼 별로 비슷한 range에 들어가 있을 것 
    - '비슷한'이라는 말이 좀 애매한데, 억지로 0과 1사이로 밀어넣는 것(normalization)이 필요한지 모르겠습니다. standardization만 하는 것이 정보를 더 유지하는 것 같아서 더 좋지 않을까? 하는 생각이 드는데, 이건 좀 더 공부가 필요할 것 같아요. 

## 아무튼 do it. 

1. 편하게 모든 피쳐 칼럼이 norm(0, 1)을 따른다고 가정하겠습니다(그리고 `sklearn.preprocessing.scale`에서 그게 디폴트 소근소근)
2. 아웃라이어는 2sigma를 넘어가는 경우를 아웃라이어라고 판단하겠습니다. 
3. `norm(0, 1)`로 가정했기 때문에 자연스럽게 모든 칼럼이 비슷한 range에 들어가게 됩니다.

- 랜덤하게 여러 가지의 분포를 만들어 주고, 아웃라이어를 임의로 넣어주고, 이를 `standardization`한 다음, 아웃라이어를 체크하는 코드입니다. 

```python
import numpy as np
import pandas as pd

sample_size = 100
"""분포별로 랜덤하게 값을 만들어줍니다. 
"""
test_dist_dict = {
    "uniform":np.random.randint(1, 100, sample_size),
    "norm_10_5":np.random.normal(10,5, sample_size),
    "norm_0_1":np.random.normal(0,1, sample_size),
    "exp":np.random.exponential(1, sample_size), 
    "poisson":np.random.poisson(10, sample_size)
}
"""append outlier in each columns: max*2
"""
for k in test_dist_dict.keys():
    l = list(test_dist_dict[k])
    l.append(max(l)*2)
    test_dist_dict[k] = np.array(l)
test_dist_df = pd.DataFrame(test_dist_dict)
print("not standardized yet")
print(test_dist_df.head())
print()

"""각 칼럼이 norm(0, 1)을 따른다고 가정하고 standardization해줍니다. 
"""
from sklearn import preprocessing
print("standardized")
new_X = pd.DataFrame(preprocessing.scale(test_dist_df, axis=0), 
                     index=test_dist_df.index,
                     columns=test_dist_df.columns
                    )
print(new_X.head())
print()

print("out of 2 sigma")
print(new_X[ 
    np.logical_or(np.any(new_X >= 2, axis=1), np.any(new_X <= -2, axis=1)) 
])
print()
print("inside of 2 sigma")
print(new_X[ 
    np.logical_and(np.all(new_X <= 2, axis=1), np.all(new_X >= -2, axis=1)) 
].head())
```

```
not standardized yet
        exp  norm_0_1  norm_10_5  poisson  uniform
0  3.097040  0.925267  11.764456        7       88
1  1.516744  1.312897  17.350357       11       80
2  1.067566 -0.166201  14.717949       13       82
3  0.209375  1.448831   3.403329       12       82
4  0.522443  0.841368  16.816397        7       82

standardized
        exp  norm_0_1  norm_10_5   poisson   uniform
0  1.735699  1.011912   0.189654 -0.811404  1.153538
1  0.411391  1.400518   1.214113  0.111997  0.885165
2  0.034973 -0.082302   0.731327  0.573697  0.952258
3 -0.684202  1.536793  -1.343784  0.342847  0.952258
4 -0.421846  0.927802   1.116184 -0.811404  0.952258

out of 2 sigma
          exp  norm_0_1  norm_10_5   poisson   uniform
43  -0.172024  0.483546  -0.730286 -2.196504 -1.664376
49   0.932857  2.069857   0.512488  0.342847  0.482606
56  -0.623548  1.154390  -2.714261 -0.118853 -1.765016
65  -0.833061 -0.457480  -2.021482 -0.349704  0.918712
84   3.037033 -0.459161  -0.033519 -0.811404  1.086445
100  6.933725  4.055396   5.882849  6.344948  4.172731

inside of 2 sigma
        exp  norm_0_1  norm_10_5   poisson   uniform
0  1.735699  1.011912   0.189654 -0.811404  1.153538
1  0.411391  1.400518   1.214113  0.111997  0.885165
2  0.034973 -0.082302   0.731327  0.573697  0.952258
3 -0.684202  1.536793  -1.343784  0.342847  0.952258
4 -0.421846  0.927802   1.116184 -0.811404  0.952258
```

- 저는 일단 norm(0, 1)을 기준으로 하고, 아웃라이어를 체크했습니다. 그리고 2sigma를 아웃라이어 라고 가정했구요. 이렇게 할 수 있기는 한데, 뭐 아웃라이어인지 아닌지, 해당 분포가 이게 맞는지 체크하는 일이 어려운 부분이 있어서. 아무튼 저도 그리고 여러분도 모두 우리인생 화이팅.

## 일반상식) standardization?? normalization?? 

- 한국말로 하면, 표준화와 일반화(정상화) 라고 할 수 있으려나요? 이 두 가지가 불분명하게 쓰이는 경우들이 꽤 있는 것 같은데, 각각의 개념은 다음과 같습니다. 웬만하면 그냥 `standardization`하는 것이 좋은것 같아요. 특히 아웃라이어 걸러내는 측면에서 유용합니다. 
- **standardization**: 해당 데이터들이 정규분포를 따른다고 가정하고, norm(0, 1)로 변환해줌
- **normalization**: MinMaxScaling과 유사한 개념. 데이터를 모두 0과 1 사이에 분포시킴

## reference

- <http://scikit-learn.org/stable/modules/preprocessing.html>
- <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler>