---
title: pd.concat이 df.append보다 빠릅니다.
category: python-libs
tags: python python-libs pandas pd.DataFrame
---

## 1-line summary 

- `pd.concat(list_of_pd.DataFrame)`이 `df.append(df)`보다 빠릅니다. 

## pd.concat vs df.append

- 쓰고보니 매우 간단한 내용입니다만, 정리합니다. 
- `pd.concat`는 dataframe으로 구성된 리스트들을 한번에 다 합쳐서 새로운 dataframe을 만들어주는 함수입니다. 
- 반면 `df.append`는 각 dataframe의 내부 method로 같은 column을 가진 dataframe을 끝에 붙여주는 것이죠.
- 당연히, 여러 dataframe을 합쳐야 할 때는 `pd.concat`가 더 빠른 것이 자명해보이지만, 저는 똥인지 된장인지 찍어먹어봐야 하는 사람이라서 직접 해봤습니다. 


```python
import pandas as pd 
import numpy as np 
import time

RG = np.random.RandomState(seed=0)

Row_N = 10
csv_N = 1000

def read_csv_as_dict_lst():
    """
    - csv를 dictionary_lst로 읽었다고 생각함.
    - row에 대한 정보를 {column_name: value}로 표현하여 모든 리스트에 넣어서 리턴. 
    """
    def random_string(str_len=20):
        return "".join(map(chr, RG.randint(ord('a'), ord('z'), str_len)))
    col_a = RG.randint(0, 100, Row_N)
    col_b = RG.random(Row_N)
    col_c = [random_string() for _ in range(0, Row_N)]
    return [{"col_A": a, "col_B": b, "col_C": c} for a, b, c in zip(col_a, col_b, col_c)] 

csv_lst = [read_csv_as_dict_lst() for _ in range(0, csv_N)]
##########################################################
# df_A.append(df_B)
# df_A에 df_B를 추가한 새로운 dataframe을 리턴함.
start_time = time.time()
df_append = pd.DataFrame(csv_lst[0])
for each_csv in csv_lst[1:]:
    df_append = df_append.append(pd.DataFrame(each_csv))
print(f"== df.append execution time: {time.time() - start_time:.5f}")
##########################################################
# pd.concat: 
# list of pd.DataFrame을 모두 합쳐서 하나의 DF로 리턴하는 함수
start_time = time.time() 
df_concat = pd.concat([pd.DataFrame(each_csv) for each_csv in csv_lst])
print(f"== pd.concat execution time: {time.time() - start_time:.5f}")
assert len(df_concat) == len(df_append)
```

- 결과를 보면 `pd.concat`이 `df.append`에 비해서 약 40% 정도의 시간만 소요합니다. 뭐 당연한 결과이긴 하죠.

```
== df.append execution time: 4.10729
== pd.concat execution time: 1.69913
```