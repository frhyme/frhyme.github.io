---
title: python - pandas - use it clever.
category: python-libs
tags: python python-libs pandas panquet feather csv hdf5 
---

## intro. 

- 2019년에 진행된 pycon 발표자료들을 다시 보면서, 제가 모르는 것들이 무엇이 있었는지를 정리하고 있습니다. 그러던 중에 [뚱뚱하고 굼뜬 판다스(Pandas)를 위한 효과적인 다이어트 전략](https://www.pycon.kr/program/talk-detail?id=73)이라는 자료를 보고, 제가 알던 내용과 모르던 내용들을 비교하기 위하여 다음과 같이 정리하였습니다. 
- 따라서, 만약 이 포스트의 내용이 도움이 된다면, 그것은 철저하게, 저 발표자료 덕분임을 밝힙니다. 


## Use pandas more efficient.

- 해당 자료는 발표자께서, "python에서 데이터 처리를 하려면 pandas를 쓰면 된다는데, 이것도 종종 너무 느리다. 왜 느릴까?"에서 시작된 것으로 보입니다. 어찌보면 결국 본질에 대한 이야기죠. 
- 특히, **시간**("데이터를 읽을 때, 간단히 분석해서 처리할때 너무 느리다")과 **가독성**("사람마다 표준화되어 있지 않은 코드")라는 두 가지 측면에서 해당 문제를 해결하죠. 그리고, pandas로 처리하는 것이 적합하지 않은 경우도 분명하게 서술하고 있습니다. 

### Don't save data as text.

- 우선, 컴퓨터라는 기계를 보면, 혹시, 엑셀을 쓰실 때, 엄청 많은 셀들을 선택하고 실수로 ctrl+c를 눌렀다가, 엑셀 자체가 뻗었던 경험이 있으신지 모르겠습니다. 컴퓨터에게 무언가를 시킬 때, 가장 많이 하게 되는 것은 값을 복사하는 것이죠. 
- 그리고, "텍스트"로 데이터를 저장하는 것이 제일 나쁩니다. 만약 이 값이 category라면(가령 "남성", "여성"이라면) 이를 각각, 0과 1로 바꾸어 저장하는 것이 훨씬 효율적입니다. 
- 혹시나 싶어서, 다음과 같이, `text`로 구성된 dataframe과 numeric data로 구성된 dataframe을 각각 csv로 저장하고, 다시 이를 읽어보니, 시간도 용량도 모두 numerical으로 처리할 때, 약 40% 가량 감소됨을 알 수 있엇습니다

```python
import pandas as pd 
import time

N = 10**7
# num_df : text "남성", "여성"으로 구성된 dataframe
text_df = pd.DataFrame({
    "col_A": ["남성" for i in range(0, N)] + ["여성" for i in range(0, N)]
})
# num_df : 0과 1로 구성된 dataframe
num_df = pd.DataFrame({
    "col_A": [0 for i in range(0, N)] + [1 for i in range(0, N)]
})

text_df.to_csv("text_csv.csv")
num_df.to_csv("num_df.csv")

start_time = time.time()
text_df = pd.read_csv("text_csv.csv")
print(time.time() - start_time)
start_time = time.time()
text_df = pd.read_csv("num_df.csv")
print(time.time() - start_time)

```

### Use Categorical dtype.

- 앞에서 말한 것처럼, 가능하면 numeric column으로 관리하는 것이 훨씬 효율적입니다. 텍스트 데이터를 관리할 경우(그리고, 카테고리 데이터가 아닐 경우)에는 `object`로 데이터 형식이 지정되어, 많은 메모리를 사용하게 되기는 하는데, 가능하면 이를 피할 수 있도록 데이터 전처리를 잘 해야겠죠. 아주 냉정히 말해서, text 데이터는 pandas에서 사용할 때 메모리 사용량의 대부분을 잡아먹게 됩니다. 
- 따라서, 만약, 경우에 따라서는 text data를 다른 dataframe에 구분해두고, 필요할 때만 가져오는 식으로 처리하는 것이 훨씬 효율적일 수 있습니다.
- 또한 범주가 아주 많은 text 데이터가 아니여서, category로 관리할 수 있을 경우에는 가급적 category로 dtype을 분명하게 처리해줍니다. memory뿐만 아니라, 시간 측면에서도 확연히 효율적으로 데이터를 처리해줍니다.

### Don't use csv format.

- csv는 아주 보편적인 file 형식입니다. 특히, string으로 저장되기 때문에, 데이터를 엑셀로 열기도 쉽고, vscode와 같은 IDE에서 열기도 쉽죠. 
- 다만, 여기서도 다시 발생하는 문제가 바로 csv라는 것이죠. 본 발표에서는 2가지 치명적인 문제점을 지적합니다. 
    - string이라서 읽고 쓰기가 더럽게 느림. 
    - 저장된 데이터 포맷에 관한 meta-date를 file format에 넣어서 관리할 수 없기 때문에, 매번 새롭게 지정해줘야 하는 번거로움이 발생함. 
- 정말 그럴까요? 한번 비교해보겠습니다.  `csv`, `pickle`, `hdf5`, `parquet`, `feather`에 대해서, 데이터의 수를 변경해가면서 읽고 쓰는 시간이 어떻게 달라지는지를 비교하였습니다. 

```python
import pandas as pd 
import numpy as np 
import time
import pickle


"""
같은 dataframe을 다른 형태의 format으로 저장하고 쓸 때, 
어느 정도의 시간 차이가 발생하는지 비교한다.
"""

# DataFrame Generated.
np.random.seed(0)

## text colum
result_dict = {}
for N in [10**n for n in [3, 5]]:
    text_lst = []
    for i in range(0, N):
        char_N = np.random.randint(10, 50, 1)[0]
        char_lst = np.random.choice(
            [chr(i) for i in range(ord('A'), ord('z')+1)], 
            char_N
        )
        text_lst.append("".join(char_lst))

    df = pd.DataFrame({
        'float_col1': np.random.normal(0, 1, N),  # float column
        'float_col2': np.random.normal(0, 1, N),  # float column
        'int_col1': np.random.randint(0, 100, N), # interger column
        'int_col2': np.random.randint(0, 100, N), # interger column
        'int_col3': np.random.randint(0, 100, N), # interger column
        'cat_col': np.random.randint(0, 5, N), # category column
        'str_col': text_lst
    })
    print("== df.dtypes")
    print(df.dtypes)
    #print(df.head())
    print(f"== dataframe {N} row generated")
    print("=="*30)

    result_dict[N] = {
        'csv':{}, 
        'pickle':{}, 
        'hdf5':{}, 
        'parquet':{}, 
        'feather':{}
    }
    ####################################
    # save and load it as csv
    print("== csv: save and load")
    write_start_time = time.time()
    df.to_csv("df.csv")
    csv_save_time = time.time() - write_start_time
    #print(f"save time : {}")
    load_start_time = time.time()
    pd.read_csv("df.csv")
    #print(f"load time : {time.time() - load_start_time:.3f}")
    csv_load_time = time.time() - load_start_time
    print("=="*30)

    # pickle
    print("== pickle: save and load")
    write_start_time = time.time()
    df.to_pickle("df.pickle")
    #print(f"save time : {time.time() - write_start_time:.3f}")
    pickle_save_time = time.time() - write_start_time
    load_start_time = time.time()
    pd.read_pickle('df.pickle')
    #print(f"load time : {time.time() - load_start_time:.3f}")
    pickle_load_time = time.time() - load_start_time
    print("=="*30)

    # hdf5 : N이 커질수록 빨리 읽고 쓰는 장점이 있음.
    print("== hdf5: save and load")
    write_start_time = time.time()
    df.to_hdf('df.h5', key='df', mode='w')
    #print(f"save time : {time.time() - write_start_time:.3f}")
    hdf5_save_time = time.time() - write_start_time

    load_start_time = time.time()
    pd.read_hdf('df.h5', 'df')
    #print(f"load time : {time.time() - load_start_time:.3f}")
    hdf5_load_time = time.time() - load_start_time
    print("=="*30)

    # parquet
    print("== parquet: save and load")
    write_start_time = time.time()
    df.to_parquet('df.parquet.gzip',compression='gzip')
    #print(f"save time : {time.time() - write_start_time:.3f}")
    parquet_save_time = time.time() - write_start_time

    load_start_time = time.time()
    pd.read_parquet('df.parquet.gzip')
    #print(f"load time : {time.time() - load_start_time:.3f}")
    parquet_load_time = time.time() - load_start_time
    print("=="*30)

    # feather 
    print("== feather: save and load")
    write_start_time = time.time()
    df.to_feather("df.feather")
    #print(f"save time : {time.time() - write_start_time:.3f}")
    feather_save_time = time.time() - write_start_time

    load_start_time = time.time()
    pd.read_feather('df.feather')
    #print(f"load time : {time.time() - load_start_time:.3f}")
    feather_load_time = time.time() - load_start_time
    print("=="*30)

    ###
    result_dict[N]['csv']['save_time']= csv_save_time
    result_dict[N]['csv']['load_time']= csv_load_time
    result_dict[N]['pickle']['save_time']= pickle_save_time
    result_dict[N]['pickle']['load_time']= pickle_load_time
    result_dict[N]['hdf5']['save_time']= hdf5_save_time
    result_dict[N]['hdf5']['load_time']= hdf5_load_time
    result_dict[N]['parquet']['save_time']= parquet_save_time
    result_dict[N]['parquet']['load_time']= parquet_load_time
    result_dict[N]['feather']['save_time']= feather_save_time
    result_dict[N]['feather']['load_time']= feather_load_time
    
#print(pd.DataFrame(result_dict))
for N, v_dict in result_dict.items():
    print(f"== N: {N}")    
    print(pd.DataFrame(v_dict))
    print("=="*30)
```

- 결과는 다음과 같습니다. N이 조금만 커져도, csv는 참혹할정도로 느려지구요, feather, pickle이 비교적 매우 빠른 편이네요.
- 즉, 혼자 사용한다면, pickle, feather를 사용하고 같이 쓴다면 가급적 parquet를 쓰는 것이 적합한 것 같네요. 

```
============================================================
== N: 1000
                csv    pickle      hdf5   parquet   feather
load_time  0.013443  0.003443  0.015921  0.011595  0.005634
save_time  0.093975  0.001949  0.886297  0.197345  0.007679
============================================================
== N: 100000
                csv    pickle      hdf5   parquet   feather
load_time  0.265626  0.032719  0.065878  0.115865  0.038448
save_time  1.163863  0.068440  0.108502  0.393810  0.063551
============================================================
```

### 기타 know-how.

- 그외로, 습관적으로 dataframe을 loop의 개념으로 접근하여, `iterrows`등의 메소드로 하나씩 처리하려는 경향이 있는데, 이는 데이터 처리 속도를 현저하게 떨어뜨리는 주범임. 최소한, `apply`를 사용하여 처리하거나, `vectorization`의 개념을 적용하는 것이 필요함. 
- 또한, rank 최상위 5개를 뽑는다와 같은 방법을 사용할 때, 전체 데이터를 정렬한 다음 순서대로 5번을 뽑는 것보다, `nlargest`를 사용하는 것이 속도 측면에서 훨씬 빠름. 즉, 습관적으로 선택하는 가장 쉬운 방법이라고 해도, 그것이 속도 측면에서 가장 효과적인지에 대해서는 고민해 봐야함. 즉, 가장 빠른 걸 선정하는 것이 목적이므로 전체를 정렬하는 것은 불필요한 작업이라는 말. 


## wrap-up

- 사실 `pandas`는 이미 python으로 코딩을 한다고 하면 모르는 사람이 없을 정도로 유명한 라이브러리입니다. 반대로 말하면, 모두가 자기가 쓰고 싶은 대로 쓰고 있다는 사실이죠. 또한, 이미 충분히 레드오션이고 모두가 익숙하다고 생각하기 때문에 이 라이브러리에 대해서 누군가 발표하리라고는 생각하지 못했습니다. 
- 결국 발표자께서는 "이거 더 잘 쓸 수 있고, 더 잘 쓰려면 어떻게 해야 한다"라는 아주 기본적인 내용을 정리하셨죠. 사실 발표 내용을 죽 읽어보면, 너무 간단하고 명쾌하죠. 
- 오히려, 발표 내용보다 제가 깨달은 것은 "내가 그것을 충분히 알고 있다고 자만하지마라"인 것 같습니다. 이 발표 내용을 보기 전까지, 저는 제가 `pandas`를 잘 안다고 생각했었으니까요.