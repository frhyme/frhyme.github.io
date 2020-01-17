---
title: python - pandas - Ordered crosstab, pivot_table
category: python-libs
tags: python python-libs pandas crosstab DataFrame
---

## 순서를 유지한 채 crosstab을 만들기. 

- CrossTable은 복잡한 데이터세트로부터, 다양한 그룹별로 데이터들이 어떻게 분포되어 있는지 row, column으로 분리하여 봄으로써, 데이터의 특징에 대한 직관적인 해석을 지원합니다. 
- 그리고, 다음처럼 pandas의 dataframe으로부터 바로 생성해낼 수도 있죠(해당 데이터를 생성하는 부분은 맨 끝에 첨부하였습니다).

```python
# pd.crosstab
print("== pd.crosstab")
df_cross_table = pd.crosstab(
    # index, columns에는 series, list 등을 넣어줄 수 있는데, 
    # 아래처럼 multi-level로 들어갈 수 있음.
    index=df['fruit'], 
    columns=[df['year'], df['season']], 
    # 각 index, column에 맞춰서, 어떤 값을 그룹화할 것인지 선택하고, 
    values=df['value'], 
    # 그룹화된 값을 어떤 함수를 사용하여 summarize하여 처리할 것인지를 정리함.
    aggfunc=np.mean,  # np.sum, np.mean
    # rowname, colname에는 각 index, column_name이 어떤 의미를 가지는지에 대해서 표시해줍니다.
    rownames  = ['row:fruit__'], 
    colnames = ['col:year__', 'col:season__']
)
print(df_cross_table)
print("=="*20)
#
```

- 다음처럼 cross table이 나오죠. 

```
== pd.crosstab
col:year__        2005                                  2006
col:season__      fall spring    summer    winter       fall spring     summer     winter
row:fruit__
apple         3.218049    3.0  3.105181  2.855459  13.023536   13.0  12.841719  12.878402
banana        4.951872    5.0  4.763076  4.593588  15.444520   15.0  15.165840  15.395593
strawberry    3.884107    4.0  3.896715  3.107161  13.752699   14.0  14.235986  13.978936
```

## problem? 

- 다만, 자세히 보시면, season의 순서가 fall, spring, summer, winter의 순으로 되어 있음을 알 수 있습니다. 어찌 보면 큰 문제는 아니지만, 거슬리죠. 이걸 어떻게 고칠 수 있을까요? 

## solve it. 

- 아래와 같이 두 줄을 추가하면 됩니다. 즉, `dataframe`에게 "이 칼럼은 카테고리 데이터가 들어 있고, 순서가 있는 카테고리다"라는 정보를 전달하는 것이죠. 
- 이렇게 전달하고 나면 이후 `crosstab`, `pivot_table`이든 모두 알아서 잘 변경해줍니다. 

```python
#############################################
# column dtype => category
df['season'] = df['season'].astype('category')
# make it ordered category
df['season'] = df['season'].cat.set_categories(['spring', 'summer', 'fall', 'winter'], ordered=True)
#############################################
```

## wrap-up

- 처음에는 당연히, `pd.crosstab`의 parameter를 조정하여야 한다고 생각했는데 오히려 `dataframe`에서 수정하는 것이 방법이더군요. 
- 또한, 어찌보면, 이게 맞죠. dataframe은 해당 데이터에 대한 특성들을 관리해주는 툴인데, 이 아이가 알아서 이정도는 인지하고 처리하는 것이 너무 당위적인것 같습니다.


## raw code

```python
import pandas as pd 
import numpy as np 

# make toy example. 
N = 100 
data_lst = []
for year in range(2005, 2005+2):
    for s_i, season in enumerate(['spring', 'summer', 'fall', 'winter']):
        for i, fruit in enumerate(['apple', 'strawberry', 'banana']):
            for _ in range(0, N):
                v = np.random.normal(10*(year-2005)+i+3, s_i*2, 1)[0]
                d = (year, season, fruit, v)
                data_lst.append(d)
#print(data_lst)
df = pd.DataFrame(
    data_lst, columns=('year', 'season', 'fruit', 'value')
)
print("== toy example made")
print(df.head())
print("=="*20)

#############################################
# column dtype => category
df['season'] = df['season'].astype('category')
# make it ordered category
df['season'] = df['season'].cat.set_categories(['spring', 'summer', 'fall', 'winter'], ordered=True)
#############################################

# pd.crosstab
print("== pd.crosstab")
df_cross_table = pd.crosstab(
    # index, columns에는 series, list 등을 넣어줄 수 있는데, 
    # 아래처럼 multi-level로 들어갈 수 있음.
    index=df['fruit'], 
    columns=[df['year'], df['season']], 
    # 각 index, column에 맞춰서, 어떤 값을 그룹화할 것인지 선택하고, 
    values=df['value'], 
    # 그룹화된 값을 어떤 함수를 사용하여 summarize하여 처리할 것인지를 정리함.
    aggfunc=np.mean,  # np.sum, np.mean
    # rowname, colname에는 각 index, column_name이 어떤 의미를 가지는지에 대해서 표시해줍니다.
    rownames  = ['row:fruit__'], 
    colnames = ['col:year__', 'col:season__']
)
print(df_cross_table)
print("=="*20)
# 거의 같은 작업을 pd.DataFrame에서 바로 수행할 수도 있습니다. 
# 다만, 사소한 차이로는 df.pivot_table에는 row_names와 col_names 가 없다는 것이 있죠. 
print("== df.pivot")
df_pivot_table = df.pivot_table(
    index='fruit', 
    columns=['year', 'season'], 
    # 각 index, column에 맞춰서, 어떤 값을 그룹화할 것인지 선택하고, 
    values='value', 
    # 그룹화된 값을 어떤 함수를 사용하여 summarize하여 처리할 것인지를 정리함.
    aggfunc=np.mean,  # np.sum, np.mean
)

print(df_pivot_table)
print("=="*20)
```