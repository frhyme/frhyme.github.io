---
title: pd.read_csv는 충분히 빠른가? 
category: python-libs
tags: python python-libs csv pandas 
---

## 1-line summary 

- `pd.read_csv`가 `csv.DictReader()`보다 더 빠른 것 같습니당.


## pd.read_csv is faster?

- 다른 라이브러리들도 있지만, csv를 읽을 때, `pd.read_csv`가 직관적이기도 하고 다른 관련 함수들도 많이 제공하기 때문에, 이 함수만 쓰고 있지만, 가끔, "충분히 빠른가?"라는 의심이 들 때가 있습니다. 특히, 여러 csv들을 다 읽어서 합치거나 해야 할때, 괜히 더 느리지 않나? 싶을 때가 있죠. 
- 그래서, `csv.DictReader()`와 간단히 비교해봤습니다. 


### Problem.

- 여러 개의 csv 파일을 한 번에 읽어서 하나의 `pd.DataFrame`으로 합칠 때 다음 2가지 방법 중에서 무엇이 더 빠른지 비교함
    1) pd.read_csv로 모든 csv를 읽고 이를 pd.concat로 합쳐줌.
    2) csv.DictReader로 읽고 이를 list에 넣어준다음 나중에 한번에 pd.DataFrame으로 합침.

```python
import pandas as pd 
import csv 
import time
import os 

path = './raw_data_csv/'
# required_column_sets: csv에서 필요한 column 이름들
# list로 비교하는 것보다, set로 projection하는 것이 훨씬 빠름.
required_column_sets = set(['col_a', 'col_b'])
####################################
# method 1: 
# pd.read_csv로 모든 csv를 읽고 이를 pd.concat로 합쳐줌.
start_time = time.time()
df_lst = []
for file_name in os.listdir(path):
    df = pd.read_csv(path+file_name, usecols=required_column_sets)
    df_lst.append(df)
df = pd.concat(df_lst).reset_index(drop=True)
print(f"pd.read_csv + pd.concat: {time.time() - start_time:.5f}")

####################################
# method 2:
# csv.DictReader로 읽고 리스트로 모드 넣은 다음 나중에 한번에 pd.DataFrame으로 합침.
start_time = time.time()
row_dict_lst = []
for file_name in os.listdir(path):
    with open(path+file_name, "r", encoding='utf-8-sig') as f:
        # python에서 file을 읽을 때 간혹 문자에 \ufeff 가 붙는 경우가 있는데 
        # 이는 encoding='utf-8-sig' 을 설정해주면 해결됨
        for row in csv.DictReader(f):
            row_dict_lst.append(
                {k: row[k] for k in row.keys() if k in required_column_sets})
csv_df = pd.DataFrame(row_dict_lst)
print(f"csv.DictReader + pd.DataFrame: {time.time() - start_time}")
assert len(csv_df)==len(df)
assert set(csv_df.columns)==set(df.columns)

```

- 결과를 보시면 그냥 pd.read_csv를 쓰는 것이 더 빠릅니다. 

```
pd.read_csv + pd.concat: 0.73001
csv.DictReader + pd.DataFrame: 0.8883731365203857
```

## wrap-up

- 일단 하나의 컴퓨터에서 돌릴 때는 `pandas.read_csv`로 그냥 써도 문제가 없을 것 같습니다만, 만약 훨씬 데이터가 커진다면 그때 발생하는 다른 문제점도 있겠죠.
- 또한, 명확하게 딱 그 지점만 비교한 것은 아닙니다만, 더 하려니까 귀찮아서 멈춥니다 호호호. 