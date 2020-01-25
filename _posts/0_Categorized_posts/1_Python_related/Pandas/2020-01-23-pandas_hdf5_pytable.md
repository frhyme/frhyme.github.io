---
title: python - pandas - save dataframe as hdf5.
category: others
tags: python python-libs pandas hdf5 pytable
---

## pd.dataframe을 hdf5의 형식으로 저장합시다. 

- 보통 우리는 `pd.DataFrame`을 그냥 무심코, `csv`의 형태로 저장하고는 합니다. 하지만, 슬프게도, csv로 저장하면 다음과 같은 문제들이 발생하죠. 
    - **비효율성**) string으로 저장하므로 데이터 용량을 많이 차지하며, 메모리에서도 과부하가 발생하여 읽고 쓸 때, 긴 시간이 소요되기 쉬움. 
    - **메타 데이터 저장못함**) `pd.DataFrame`은 각 칼럼별로 dtype들을 저장할 수 있는, 데이터 관리 툴입니다. 따라서 가능하면, 각 칼럼별로 지정해둔 dtype들이 유지되면서 옮겨지면 좋을텐데, 아쉽게도 csv로 저장할 경우 이 부분에 문제가 생기죠. 
- 물론, 그러함에도 불구하고, csv로 저장하면, excel등을 통해서 쉽게 파일을 볼 수 있다는 장점이 있습니다. 결국 어느 한 쪽을 선택했을 때 발생하는 트레이드오프 일 뿐이죠. 

## anyway. save it hdf5. 

- 따라서, 데이터를 빠르게 읽고 쓰기 위해서 다양한 형식들이 있습니다. python에서는 보통 pickle을 쓰는 것이 편하기는 한데, 오늘은 [hdf5(Hierarchical Data Format version 5)](https://www.hdfgroup.org/solutions/hdf5/)라는 형식에 따라서 `pd.DataFrame`을 저장해줄 거에요. csv, pickle에 비해서 hdf5는 일종의 Database와 같다고 생각해도 됩니다. 사실 
- 아무튼 간에, 우리는 그냥 저장만 할거니까요 호호. 다음의 간단한 python code를 만들고 실행하면 됩니다.

```python
import pandas as pd

df = pd.DataFrame() # 
df.to_hdf('df.h5', key='df', mode='w')
pd.read_hdf('df.h5', 'df')
```

- 하지만, 오류가 발생하네요. 그냥 `tables`라는 모듈을 설치해주면 될 것 같아요.

```
ImportError: HDFStore requires PyTables, "No module named 'tables'" problem importing
```

## install pytables. 

- [pytables](https://www.pytables.org/)는 아주 간단하게 hdf5의 형태로 데이터를 저장하기 위해 필요한 라이브러리입니다. documentation에 들어가면 내용이 길지만, 일단 그냥 설치해줍니다. 

```
pip install tables
```

- 그리고 이전에 해줬던, 코드를 다시 실행해주면 문제없이 되는 것을 알 수 있습니다.

## wrap-up

- csv는 string형식이니까 무시하고, pickle 또한, 보안상의 위험과 python에서만 돌아가므로 넘어간다고 해도, `hdf5, parquet, feather`과 같은 많은 다른 대안들이 남아 있습니다.
- 처음에는 "아니, 표준도 없고 뭐 이렇게 비슷한 것들이 많냐" 싶었는데, 다시 생각해보니, Database와 다를게 없죠. DB 시장에 셀수 없이 많은 vendor들이 있는 것과 기본적으로는 크게 다르지 않아요. 


## reference

- <https://datascienceschool.net/view-notebook/f1c286a1d5164975a9909bb7a341bf4c/>