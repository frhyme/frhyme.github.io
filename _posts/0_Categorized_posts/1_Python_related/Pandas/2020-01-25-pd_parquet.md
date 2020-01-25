---
title: python - pandas - reading and writing parquet
category: python-libs
tags: python python-libs pandas parquet
---

## save pd.Dataframe as parquet.

- 우리는 dataframe을 습관적으로 `csv`로 저장합니다. 하지만, 이 아이는, 메타데이터를 저장할 수 없어 칼럼별로 dtype을 재지정해줘야 하는 일이 생길 수 있다는 것과, 읽고 쓸때 시간이 많이 걸린다는 단점이 있습니다. 
- 따라서, 이를 보완하기 위해 pickel, parquet, hdf5 와 같은 다양한 데이터 포맷이 있는데요 오늘은 `parquet`에 대해서 간략하게 정리합니다. 

### what is parquet?

> Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.

### Use it in pandas
- Hdoop ecosystem에서 돌아가는 프로젝트들에 맞게 설계된 저장형식이라고 되어있지만, 그냥 써도 됩니다. 다만, hadoop과 연계하여 쓸 경우에는 더 편한 부분들이 아마도 있겠죠. 
- 저는 python data library인 `pandas`에서 사용할 것입니다. 

```python
!pip install pyarrow
print("== parquet: save and load")
df.to_parquet(
    'df.parquet.gzip',
    compression='gzip'
)
pd.read_parquet(
    'df.parquet.gzip'
)
```
