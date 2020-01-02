---
title: pd.DataFrame를 function으로 그룹핑하기
category: python-lib
tags: python pandas dataframe groupby python-lib function
---

## dataframe을 function으로 그룹바이하기 

- `pandas.dataframe`을 사용하다보면 필요에 따라서 groupby를 사용할 일들이 있습니다. category로 구분된 칼럼이 존재한다면, 문제가 없지만 category로 된 칼럼이 없을때, 또 굳이 새로운 칼럼을 만들어서 칼럼명을 기억하고 싶지 않을때, 
- 그럴때는 그냥 dataframe의 값을 변형해서 그 값을 이용해서 그룹핑하고 싶을 때가 있습니당.

- 말이 중언부언 쓸데없는데, 결국 데이터프레임을 펑션으로 어떻게 그룹바이 하냐는 이야기입니다. 

## groupby by function

- 일단 매우 간단하게 다음처럼 row 10개짜리 데이터프레임을 만들었습니다. 

```python
import pandas as pd

temp_df = []
for i in range(0, 10):
    temp_df.append( (i, "{:0>5d}".format(i+10)) )
temp_df = pd.DataFrame(temp_df, columns=['col1', 'col2'])
print(temp_df.head())
```

```
   col1   col2
0     0  00010
1     1  00011
2     2  00012
3     3  00013
4     4  00014
```

- `col1`의 값들을 이용해서 짝수인 경우와 홀수인 경우를 구분하고 싶습니다. 
- 다음처럼 새로운 칼럼을 하나 만들어서 그 칼럼으로 그룹바이를 해도 되기는 하는데, 쓸데없는 칼럼이 하나 늘어나는 것이 마음에 들지 않아요. 

```python
temp_df['cat1'] = temp_df['col1']%2
for g_num, g in temp_df.groupby('cat1'):
    print("group number: {}".format(g_num))
    print(g)
    print("==============")
```

```
group number: 0
   col1   col2  cat1
0     0  00010     0
2     2  00012     0
4     4  00014     0
6     6  00016     0
8     8  00018     0
==============
group number: 1
   col1   col2  cat1
1     1  00011     1
3     3  00013     1
5     5  00015     1
7     7  00017     1
9     9  00019     1
==============
```

- 그래서 바로 함수를 사용해서 처리해주기로 합니다. 
- 아래처럼 간단하게 `index`를 input으로 받고, categorical value를 뱉어주는 함수를 집어넣으면 됩니다. 

```python
## index를 input으로 받아서 결과를 뱉어주는 함수를 만들면 됨
for g_num, g in temp_df.groupby(lambda idx: temp_df.iloc()[idx]['col1']%2):
    print("group number: {}".format(g_num))
    print(g)
    print("==============")
```

```
group number: 0
   col1   col2
0     0  00010
2     2  00012
4     4  00014
6     6  00016
8     8  00018
==============
group number: 1
   col1   col2
1     1  00011
3     3  00013
5     5  00015
7     7  00017
9     9  00019
==============
```