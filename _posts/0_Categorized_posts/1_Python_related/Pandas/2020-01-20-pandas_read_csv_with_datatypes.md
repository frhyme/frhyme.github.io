---
title: python - pandas - read csv with datatypes
category: python-libs
tags: python python-libs pandas datatype
---

## csv에서 특정 column을 string으로 읽고 싶을 때.

- `pd.DataFrame`은 사실 엑셀과 유사합니다. 엑셀처럼 각 칼럼의 데이터타입을 지정하고 관리할 수 있죠. 
- 아무튼, 가끔, csv에 저장된 값은 `1.60`이라는 문자열인데, 이를 그대로 `pd.read_csv`로 읽으면. `1.6`이라는 float으로 읽어버릴 때가 있습니다. `pd.read_csv`를 할때, 각 칼럼의 데이터 형식(dtype)을 지정해서 처리할 수 있으면 아주 좋을텐데, 이를 어떻게 하는지 이 글에서 설명합니다.

```python
import pandas as pd 
import numpy as np 

np.random.seed(0)

df_dict = {
    'col_A': [ f"{x:.2f}0" for x in np.random.normal(0, 1, 100)]
}

# 일부러 뒤에 0을 붙인 문자열을 저장한다. 
df = pd.DataFrame(df_dict)
# 저장될 때의 문자열은 object였지만, 
print("=="*20)
print(f"== df.dtypes : {df.dtypes}")
print(df.head(2))

# 저장은 제대로 되어 있지만, 이를 읽을 때, 문자열
df.to_csv('test.csv', index=False)
df = pd.read_csv('test.csv')
# 저장하고 다시 읽으면 float64를 읽는다.
print(f"== df.dtypes : {df.dtypes}")
print(df.head(2))
print("=="*20)
# 따라서, 다음처럼 읽을 때, dtype을 지정해주고 읽으면 된다.
df = pd.read_csv('test.csv', dtype={'col_A':object})
# 저장하고 다시 읽으면 float64를 읽는다.
print(f"== df.dtypes : {df.dtypes}")
print(df.head(2))
print("=="*20)
```

## reference

- <https://stackoverflow.com/questions/16988526/pandas-reading-csv-as-string-type>