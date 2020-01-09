---
title: pandas - dataframe - sampling
category: pandas
tags: python python-libs dataframe sampling pandas
---

## dataframe sampling

- `pd.DataFrame`을 기본 데이터구조로 관리할 때, 종종 랜덤하게 데이터를 샘플링하고 싶을 때가 있습니다. 
- 가령, cross-validation처럼 처리를 하고 싶을 때 라거나, noise imbalance 문제로 인해서, 클래스별로 데이터의 수를 비슷하게 맞추기를 원한다거나 하는 등, 뭐 그런 경우들이 있죠. 
- 본문에서는 비교적 간략하게, `pd.DataFrame`로부터 데이터를 어떻게 샘플링할 수 있는지에 대해서 정리하였습니다. 

```python
import pandas as pd
import numpy as np 

N  = 100
df = pd.DataFrame({
    'col_a':np.random.random(N), 
    'col_b':np.random.randint(4, 100), 
    'col_c':np.random.randint(0, 10, N), 
})
print(df.head(5))
print("==")

# N sampling
print(
    df.sample(n=5, random_state=1)
)
# Fraction sampling
print("==")
print(
    df.sample(frac=0.05, random_state=1)
)
print("==")
# sampling by weight
# weight가 클수록 잘 나오도록 sampling 한다.
# column name을 넘기면 됨.
print(
    df.sample(
        frac=0.05, 
        weights='col_c', 
        random_state=1
    )
)
print("==")
```

```
      col_a  col_b  col_c
0  0.277943     21      8
1  0.318188     21      6
2  0.383598     21      6
3  0.383731     21      6
4  0.620893     21      8
==
       col_a  col_b  col_c
80  0.312053     21      3
84  0.605246     21      4
33  0.573956     21      3
81  0.971475     21      2
93  0.485356     21      3
==
       col_a  col_b  col_c
80  0.312053     21      3
84  0.605246     21      4
33  0.573956     21      3
81  0.971475     21      2
93  0.485356     21      3
==
       col_a  col_b  col_c
36  0.677911     21      5
65  0.285437     21      6
0   0.277943     21      8
25  0.280924     21      3
10  0.654636     21      2
==
```