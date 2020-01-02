---
title: handling missing value
category: data-science
tags: python-lib python pandas missing-value matplotlib sklearn numpy 

---

## missing value를 다뤄봅시다. 

- kaggle에서 데이터를 예측하다 보면, 에러가 아주 많이 발생합니다. 그 이유는, kaggle에서 제공되는 데이터들에 빈 공간이 너무 많기 때문이죠. 그냥 알아서! 빈 공간은 다 제외하고 주면 안됩니까! 라는 생각이 들지만, 몇 칸이 비어 있다고 해서, 나머지도 다 무시해서는 안되죠. 
- 아무튼, 여기서는 missing value를 처리하는 방법을 정리해봅니다. 

## fill numerical missing values

- numerical 값들에 대해서, missing value를 채울 때는 보통 전체 데이터에 대해서 평균을 넣어주는 경우가 제일 많습니다. 
- 하지만, 만약 categorical value별로 평균이 다르다면, 해당 instance가 속한 class를 고려해서 값을 추정해주는 것이 좋겠죠. 


```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.concat([
    pd.DataFrame({'v':np.random.normal(i*20, 2, num),'c':[chr(ord('A')+i) for j in range(0, num)]}) 
    for i, num in enumerate([500, 300, 200])]).reset_index(drop=True)

plt.figure(figsize=(12, 4))
plt.scatter(range(0, len(df)), df['v'], 
            c= df['c'].apply(lambda x: ord(x)), 
            cmap=plt.cm.rainbow, 
            alpha=0.5)
plt.title("none na value", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1731_missing_numeric_v_non_na_value.svg')
plt.show()

## drop somethings 
df_nan = df.copy()
df_nan['v'] =[ np.nan if abs(np.random.normal(0, 1)) > 1.0 else x for x in df['v']]

## 그냥 평균으로 일괄적으로 fillna를 해주면 아래 그림처럼 문제가 발생할 수 있음. 
df_nan_fillna_mean = df_nan.fillna(df_nan.mean())
plt.figure(figsize=(12, 4))
plt.scatter(range(0, len(df_nan)), df_nan_fillna_mean['v'], 
            c= df_nan_fillna_mean['c'].apply(lambda x: ord(x)), 
            cmap=plt.cm.rainbow, 
            alpha=0.5)
plt.title("fillna by all mean", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1731_missing_numeric_v_fillna_all_mean.svg')
plt.show()

"""
- 그래서 class를 고려해서 평균을 따로 내서 넣어주는 것이 좋다. 
- 아래처럼 그룹별로 평균을 낸 값으로 따로따로 그룹별로 dataframe을 계산 한 다음, 값을 넣어준다. 
"""

df_nan_with_group_mean = pd.concat(
    [g[1].fillna(g[1].mean()) for g in df_nan.groupby('c')]
)

plt.figure(figsize=(12, 4))
plt.scatter(range(0, len(df_nan_with_group_mean)), df_nan_with_group_mean['v'], 
            c=df_nan_with_group_mean['c'].apply(lambda x: ord(x)), 
            cmap=plt.cm.rainbow, 
            alpha=0.5)
plt.title("fillna by group mean", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1731_missing_numeric_v_fillna_group_mean.svg')
plt.show()
```

- 아래 그림에서처럼 전체 평균으로 채워 넣을 경우 슬픈 결과가 나올 수 있습니다. 

![](/assets/images/markdown_img/180605_1731_missing_numeric_v_non_na_value.svg)

![](/assets/images/markdown_img/180605_1731_missing_numeric_v_fillna_all_mean.svg)

![](/assets/images/markdown_img/180605_1731_missing_numeric_v_fillna_group_mean.svg)


## fillin categorical values

- 이 경우는 남아 있는 numericl value를 사용해서 거리를 비교하고, 가장 가까운 사람의 categorical value를 넣어주는 것이 제일 좋습니다. 
- 하지만 직접 코딩은 하지 않았습니다. 매우 귀찮아요. 

```python
"""
- 그럼 반대로, categorical value가 na일 경우 
"""

df = pd.concat([
    pd.DataFrame({'v':np.random.normal(i*20, 2, num),'c':[chr(ord('A')+i) for j in range(0, num)]}) 
    for i, num in enumerate([500, 300, 200])]).reset_index(drop=True)

plt.figure(figsize=(12, 4))
plt.scatter(range(0, len(df)), df['v'], 
            c= df['c'].apply(lambda x: ord(x)), 
            cmap=plt.cm.rainbow, 
            alpha=0.5)
plt.title("none na value", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1734_fill_categorical_v.svg')
plt.show()
## drop somethings 
df_nan = df.copy()
df_nan['c'] =[ np.nan if abs(np.random.normal(0, 1)) > 1.0 else x for x in df['c']]

"""
그냥 빈번한 것들을 random sampling해서 넣어줄경우? 
"""
df_nan_with_random = df_nan.copy()
df_nan_with_random['c'] = [ np.random.choice(df_nan['c'].dropna()) if pd.isnull(x) else x for x in df_nan['c']]
plt.figure(figsize=(12, 4))
plt.scatter(range(0, len(df)), df_nan_with_random['v'], 
            c= df_nan_with_random['c'].apply(lambda x: ord(x)), 
            cmap=plt.cm.rainbow, 
            alpha=0.5)
plt.title("random sampling", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1734_fill_categorical_v_fill_random.svg')
plt.show()
"""
- cluster 별로 평균을 내고, 그 중에서 가장 가까운 class를 이용해서 missing value를 채움
"""
```

![](/assets/images/markdown_img/180605_1734_fill_categorical_v.svg)

![](/assets/images/markdown_img/180605_1734_fill_categorical_v_fill_random.svg)


## wrap-up

- missing value는 나중에 채웁시다. 아 이거 너무 빡시고 귀찮은 일이에요. 
- 일단 dropna로 치워버리고, 나중에 한번에 처리하는게 훨씬 좋을 것 같아요. 극혐극혐