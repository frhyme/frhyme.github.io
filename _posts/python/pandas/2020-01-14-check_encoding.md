---
title: python - pandas - check encoding.
category: python-libs
tags: python python-libs pandas csv encoding utf-8 numpy chardet 
---

## check your encoding file. 

- 보통 `pandas.csv`로 csv 파일들을 읽을 때 가장 흔히 발생하는 에러로 다음의 것이 있죠. 
- 길게 되어 있지만, 그저 "원래 파일이 utf-8로 인코딩되어 있지 않은데, utf-8로 인코딩하려고 해서 발생하는 문제"입니다. 

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

- 물론, `pandas.to_csv`를 실행할 때, `utf-8`이 기본값으로 되어 있어서, 그냥 별 다른 설정을 하지 않으면 상관없는데 아무튼, 저런 경우들이 종종 존재하죠. 사실, 이걸 해결하는 방법은 비교적, 매우 간단합니다. 


## solve it wrong.

- 틀린 방식입니다만, 많은 블로그들에서, 이 방식이 맞다고 지적하고 있어서 틀렸음을 명확히 보여줍니다. 몇몇 블로그에서는 다음과 같이 처리하면 해당 파일의 인코딩 방식을 알 수 있다고 합니다. 얼핏, 보면 맞는 것처럼 보이죠.

```python
with open('test_csv_190114.csv') as f:
    print(f)
```
```
<_io.TextIOWrapper name='test_csv_190114.csv' mode='r' encoding='UTF-8'>
```

- 한번 테스트를 해보겠습니다. 다음과 같이, python pandas에서 서로 다른 인코딩 방식(utf-8, utf-16)으로 csv를 각각 저장해주고, 파이썬 기본 방식으로 파일을 읽어서 출력해줍니다. 

```python
import pandas as pd 
import numpy as np 

# make dataframe and write it as csv file 
df = pd.DataFrame(
    {
        'col_a':np.random.random(10), 
        'col_b':np.random.random(10), 
    }
)
#print(df.head())
########################################
# utf-8로 인코딩했을 때 출력 결과가 utf8로 나오지만,
########################################
to_csv_param_dict = {
    'path_or_buf':"test_csv_190114.csv", 
    'sep': ',', 
    'encoding':'utf-8'
}
df.to_csv(**to_csv_param_dict)
print("=="*20)
print(f"== df csv file is encoded {to_csv_param_dict['encoding']}")
with open('test_csv_190114.csv') as f:
    print(f"file type is: {f}")
    print(f.readlines())
print("=="*20)
########################################
# utf-16으로 인코딩해도 utf-8로 결과가 나옴.
########################################
to_csv_param_dict = {
    'path_or_buf':"test_csv_190114.csv", 
    'sep': ',', 
    'encoding':'utf-16'
}
df.to_csv(**to_csv_param_dict)
print(f"== df csv file is encoded {to_csv_param_dict['encoding']}")
with open('test_csv_190114.csv') as f:
    print(f"file type is: {f}")
    print(f.readlines())
```

- 아래에서 보시는 것처럼 csv 파일을 `utf-8`로 저장하든, `utf-16`으로 저장하든 상관없이, 그냥 `encoding='UTF-8`으로 표시해줍니다. 
- 그리고 파일이 utf-8로 인코딩되어 있다고 생각하고 읽기 때문에, 이를 실제로 읽어서 출력하려고 하면, 다음과 같이 에러가 발생하죠.

```
========================================
== df csv file is encoded utf-8
file type is: <_io.TextIOWrapper name='test_csv_190114.csv' mode='r' encoding='UTF-8'>
[',col_a,col_b\n', '0,0.013845954945651995,0.9711504967882624\n', '1,0.22623236002583202,0.8325203572048832\n', '2,0.624492205639335,0.08927496566336979\n', '3,0.8551070031229804,0.6534901938649194\n', '4,0.5739514150486329,0.47376986796101206\n', '5,0.8231597457095641,0.7995586032801442\n', '6,0.9593301357288136,0.8635370988998786\n', '7,0.1966328421358593,0.7588163653359546\n', '8,0.1577009039418904,0.7749176617999953\n', '9,0.2998450716697477,0.5567583140954053\n']
========================================
== df csv file is encoded utf-16
file type is: <_io.TextIOWrapper name='test_csv_190114.csv' mode='r' encoding='UTF-8'>
Traceback (most recent call last):
  File "pd_csv.py", line 41, in <module>
    print(f.readlines())
  File "/Users/frhyme/anaconda3/lib/python3.6/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

## solve it right.

- 자, 그래서 저렇게 해서는 안되고, 다음과 같이 `chardet`라는 라이브러리를 이용합니다. 


```python
import pandas as pd
import numpy as np 

import chardet


# 무작위의 dataframe을 만들어줍니다. 
# 이 값을 가지고, 다양한 인코딩 방식으로 저장하고 읽고 할 것입니다 
np.random.seed(0)
N = 10 
df = pd.DataFrame({
        'col_a': np.random.random(N), 
        'col_b': np.random.random(N), 
        'col_c': ['a' for i  in range(0, N)]
    })

# 다음과 같은 다양한 인코딩 방식으로 저장하고 이 값을 추정합니다.
encoding_ways = [
    'utf-8', 
    'utf-16', 
    'utf-32-le',
    'ISO 8859-1', 
    'windows-1251', 
    'euc-kr'
]
print("=="*30)
for encoding_w in encoding_ways:
    # 각 encoding_w에 맞게 인코딩해주고, 
    file_name = f"temp_csv_190114_{encoding_w}.csv"
    df.to_csv(file_name, encoding=encoding_w)
    print(f"== encoded  as {encoding_w}")
    # binary로 파일을 읽어서, chardet.detect 를 사용하여 추정합니다.
    with open(file_name, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        # check what the character encoding might be
    #print("--"*30)
    # 추정된 결과를 표시하고, 
    detected_encoding_way = result['encoding']
    print(f"== detected as {detected_encoding_way} ::: {result}")
    # 추정된 방식으로 파일을 읽어봅ㅂ니다.
    df_read = pd.read_csv(file_name, encoding=detected_encoding_way) 
    print(f"== decoded  as {detected_encoding_way}")
    print(df.head(2))
    print("=="*30)
```

- 결과는 다음과 같습니다. 대부분 그냥 애매하면 ascii로 처리해주기는 하지만, 그건 그렇게 읽어서 처리해도 데이터의 결과에 문제가 없기 때문이죠. 

```
============================================================
== encoded  as utf-8
== detected as ascii ::: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
== decoded  as ascii
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
== encoded  as utf-16
== detected as UTF-16 ::: {'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}
== decoded  as UTF-16
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
== encoded  as utf-32-le
== detected as ascii ::: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
== decoded  as ascii
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
== encoded  as ISO 8859-1
== detected as ascii ::: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
== decoded  as ascii
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
== encoded  as windows-1251
== detected as ascii ::: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
== decoded  as ascii
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
== encoded  as euc-kr
== detected as ascii ::: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
== decoded  as ascii
      col_a     col_b col_c
0  0.548814  0.791725     a
1  0.715189  0.528895     a
============================================================
```

## wrap-up

- 테스트에서, 저 복잡한 문자열을 인코딩해서 얼마나 정확하게 결과를 보여주는지 파악했으면 좋았겠지만, 다른 문자들을 랜덤하게 만드는게 좀 번거롭고 어려워서 제외하였습니다. 
- 또한, `chardet`는 확정적인 방식이 아니라, 해당 파일에 대한 "가장 가능성 높은 인코딩 방식"을 유추해주는 것에 가까워요. 그래서 confidence가 존재하는 것이죠. 


## reference

- <https://krinkere.github.io/krinkersite/encoding_csv_file_python.html>