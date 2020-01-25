---
title: python - pandas - reading and writing feather
category: python-libs
tags: python python-libs pandas parquet
---

## what is feather? 

> Feather provides binary columnar serialization for data frames. It is designed to make reading and writing data frames efficient, and to make sharing data across data analysis languages easy. This initial version comes with bindings for python (written by Wes McKinney) and R (written by Hadley Wickham).
- [feather](https://github.com/wesm/feather)의 documentation 에 들어가시면, 무엇인지 대략 알 수 있습니다. 사실 다른 데이터 저장 형식들인 hdf5, parquet 등에도 비슷하게 작성되어 있는 내용들이어서, 가령 "효율적이고, 플랫폼구분없이 사용할 수 있고, 빠르고 데이터 분석에 적합하고"와 같은 표현들은 다른 저장형식에도 거의 동일하게 있어서, 굳이 더 말을 붙이지는 않았습니다. 
- 다만 [이 기사](https://blog.rstudio.com/2016/03/29/feather/)에서는 feather가 R과 python구분없이 동일하게 인식된다는 말이 붙어 있군요. 흐음...


## save dataframe as feather

- 아무튼, 일단 한번 사용해봅니다. 최소한 코드는 아주 간단하네요. 그리고, csv 등과는 비교할 수 없을 정도로 빠릅니다. 

```python
df.to_feather("df.feather")
pd.read_feather('df.feather')
```

## wrap-up

- 데이터를 중간에 저장할 때, 습관적으로 csv로 저장하곤 했습니다. 그런데, 이렇게 처리할 경우에는 데이터가 커질수록 읽고 쓰는데 너무 많은 시간이 소요된다는 문제가 있었죠. 
- 앞으로는 가능한 csv로 데이터를 읽고 쓰는 것을 지양하고, `feather`와 같이 간편한 데이터 저장형식을 사용하려고 합니다. 


## reference

- <https://pythontic.com/pandas/serialization/feather>
- <https://medium.com/@snehotosh.banerjee/feather-a-fast-on-disk-format-for-r-and-python-data-frames-de33d0516b03>