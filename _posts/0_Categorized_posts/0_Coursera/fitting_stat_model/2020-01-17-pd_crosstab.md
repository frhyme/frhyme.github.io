---
title: python - pandas - crosstab, pivot_table
category: python-libs
tags: python python-libs pandas crosstab DataFrame
---

## pandas - crosstab, pivot_table

- 우리가 이미 `panda.DataFrame`를 사용해서 필요한 데이터를 엑셀처럼 깔끔하게 구축해두었다고 합시다. 그런데, 이 데이터들을 혼합해서 간단한 [cross-table](https://docs.tibco.com/pub/spotfire/7.0.1/doc/html/cross/cross_what_is_a_cross_table.htm)을 만들고 싶을 때가 있죠. 
- cross-table은 가령, 우리에게 `year`, `fruit`, `consumption`이라는 세 가지의 칼럼이 있다고 할 때, row에는 `fruit`을 column에는 `year`를 그리고, `year`와 `fruit`의 교차 셀에는 `consumption`의 평균/최소/최대/합 등의 값을 배치함으로써, 대용량의 데이터들의 summary를 볼 수 있게 하는 것을 말합니다. 

## how to use it. 

- 그냥 다음과 같이 간단하게 사용하면 됩니다. 
- 우선, 테스트하기 위한 간단한 data를 만들어 봅니다. 

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
```

```
== toy example made
   year  season  fruit  value
0  2005  spring  apple    3.0
1  2005  spring  apple    3.0
2  2005  spring  apple    3.0
3  2005  spring  apple    3.0
4  2005  spring  apple    3.0
========================================
```

- 이제 만들어진 `pd.DataFrame`을 대상으로 cross_table을 만들어보겠습니다. 
- `pd.crosstab`를 선언하고, 필요한 parameter를 넘겨줍니다. 

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
# 리턴되는 값이 dataframe입니다. 
print(df_cross_table)
print("=="*20)
```

```
== pd.crosstab
col:year__        2005                                  2006
col:season__      fall spring    summer    winter       fall spring     summer     winter
row:fruit__
apple         3.218049    3.0  3.105181  2.855459  13.023536   13.0  12.841719  12.878402
banana        4.951872    5.0  4.763076  4.593588  15.444520   15.0  15.165840  15.395593
strawberry    3.884107    4.0  3.896715  3.107161  13.752699   14.0  14.235986  13.978936
```

- 사실 이 앞에서는 `pd.crosstab`를 사용했지만, 그냥 dataframe에서 바로 실행할 수도 있습니다. 

```python
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

```
========================================
== df.pivot
year            2005                                  2006
season          fall spring    summer    winter       fall spring     summer     winter
fruit
apple       3.218049    3.0  3.105181  2.855459  13.023536   13.0  12.841719  12.878402
banana      4.951872    5.0  4.763076  4.593588  15.444520   15.0  15.165840  15.395593
strawberry  3.884107    4.0  3.896715  3.107161  13.752699   14.0  14.235986  13.978936
========================================
```


## wrap-up

- cross-table, pivot-table 이라는 단어가 익숙하지는 않았는데, 그냥 이제 뭔지 정확하게 알게 된 것 같군요. 
- 다만, 아쉬운 것은 위의 표들을 보면 `season`부분이, fall, spring, summer winder 로 시간의 순서에 맞게 배열되어 있지 않습니다. 제가 데이터를 넣을 때는 위의 데이터들이 순서에 맞게 되어 있었음에도 불구하고 말이죠. 현재는 사전식, 즉 lexical order로 되어 있습니다. 
- 따라서, 순서를 유지하면서, crosstable을 만드는 방법에 대해서 다음에는 정리해보겠습니다. 



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