---
title: dictionary를 pd.DataFrame으로 바꿀 때
category: python-libs
tags: python-libs python pandas dictionary dataframe
---

## 예제를 봅시다. 

- 매우 간단한 문제기 때문에 설명없이 바로 들어갑니다. 
- 다음처럼 간단한 딕셔너리가 있고, 이를 `pd.dataframe`의 contstructor를 이용해서 바로 변환해준다고 합시다. 
    - 우리의 마음같아서는 `year`가 index가 되고 `col_A`, `col_B`, `col_C`가 칼럼이 되기를 희망하지만, 마음처럼 그렇게 되지 않습니다. 


```python
import pandas as pd
import numpy as np 

test_df = {year:{'col_A': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                } for year in range(2008, 2012)}
test_df = pd.DataFrame(test_df)
print(test_df.columns)
print(test_df.index)
```

- 아래 에서 보시는 것처럼, columns에는 연도가 들어가고, index에는 칼럼이 들어갔네요 흠..

```
Int64Index([2008, 2009, 2010, 2011], dtype='int64')
Index(['col_A', 'col_B'], dtype='object')
```

## first way - transpose

- 사실 그냥 간단하게 transpose하면 되기는 합니다. 

```python
import pandas as pd
import numpy as np 

test_df = {year:{'col_A': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                } for year in range(2008, 2012)}
test_df = pd.DataFrame(test_df)
test_df = test_df.T
print(f"columsn: {test_df.columns}")
print(f"index: {test_df.index}")
```

```
columsn: Index(['col_A', 'col_B'], dtype='object')
index: Int64Index([2008, 2009, 2010, 2011], dtype='int64')
```

## second way: pd.DataFrame.from_dict

- 아래처럼, `pd.DataFrame.from_dict`를 사용해서 생성하고, `orient` argument에 `index`를 넣어주면 됩니다. 

```python
import pandas as pd
import numpy as np 

test_df = {year:{'col_A': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                 'col_B': np.random.randint(1, 100, size=10), 
                } for year in range(2008, 2012)}
test_df = pd.DataFrame.from_dict(test_df, orient='index')
print(f"columns: {test_df.columns}")
print(f"index: {test_df.index}")
```

## wrap-up

- 매우 간단한 내용이므로 더 추가해서 설명하지는 않겠습니다.
- 중요한 것은, 습관적으로 우리는 `pd.DataFrame()`으로 넘겨주는데, 이때 칼럼과 인덱스가 원하는 대로 되지 않을 때가 있고, 그걸 편하게 하려면, `Transpose`를 사용하거나, 처음에 변환할때 잘해주면 된다. 정도가 있겠네요. 