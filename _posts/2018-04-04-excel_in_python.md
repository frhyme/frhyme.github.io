---
title: Excel + python(in Pandas)
category: python-lib
tags: python python-lib excel pandas OrderedDict 

---

## Intro

- `Markdown`을 알기 전에는 공부하다가 공유하면 좋을 것이라고 생각되는 자료들을 ppt로 만드는 일이 많았습니다. 그래서 slideshare를 이용하곤 했는데, 그때 올리던 자료 중에서 유독, 조회수가 높은 자료가 있었는데 ***파이썬에서 엑셀 파일을 어떻게 읽을 수 있느냐***에 대한 내용이었습니다. 
	- [Python+excel in slideshare](https://www.slideshare.net/frhyme/python-excel)
- 이제는 깃헙블로그에 내용을 올리기로 했기 때문에, 해당 내용을 여기로 옮기고 보완해서 정리해보기로 했습니다.

## python vs. vba

- 과거에 증권가에서도 그렇고, `excel+vba` 만 잘 써도 할 수 있는 것들이 많았던 시절이 있었다고 생각합니다만(학부 시절에도 C를 한참 배우다가 vba로 시뮬레이션 돌리는 것을 배우기도 했고), 이제는 vba만으로는 한계가 있다고 생각합니다(물론 개인적인 생각일수 있구요).
	- (제가 가진 좁은 세계 안에서) vba는 python처럼 (다른 사람들이 잘 만들어놓은) 라이브러리를 활용하는 것도 매우 어려울 뿐만 아니라, 문법 자체도 낯섭니다. 배우면 좋지만, 확장성이 떨어지는 vba를 굳이 배워야 하나? 라는 생각이 드는 것도 사실입니다. 
- 아무튼, 저는 과거 vba로 처리했던 부분들을 python을 활용해서 처리할 수 있다고 생각합니다. 또한 훨씬 편하고, 다양한 분석이나 처리를 할 수 있다고 생각하고, 사실이기도 하고요. 

## which package??

- 슬라이드쉐어에서 제가 작성할 때는 `xlrd`, `xlwt`, `openpyxl` 등을 언급했는데(대략 1년 반전이네요), 지금은 그냥 `pandas`만으로 충분하지 않나 생각합니다. 
	- `pandas`의 경우 현재는 거의 데이터 사이언스의 표준 라이브러리에 가깝다고 여겨지는 상태입니다(다른 라이브러리들은 쓰는 사람들이 줄어드는 것 같아요(제 생각입니다)

## how to read and write excel in python

- 이 자료에서는 `pandas`에 대해서는 자세하게 설명드리지 않습니다. 특히 `dataframe`에 대해서는 자세하게 설명드리지 않는데, 정말 간단하게는 그냥 테이블 혹은 극단적으로는 엑셀 시트라고 생각하셔도 상관없습니다. 

### how to read excel

#### code 

- 우선 데이터 프레임을 두 개 만듭니다. 
	- 각각 엑셀의 시트별로 들어갑니다.

```python
import pandas as pd

df1 = pd.DataFrame({"A":range(0, 10), "B":range(10, 20)})
df2 = pd.DataFrame({"C":range(0, 20), "D":range(10, 30)})
```

- 해당 데이터 프레임들을 `test_excel.xlsx` 파일에 넣어줍니다. 
	- 우선 원하는 엑셀 파일명을 가지고 `ExcelWriter`을 만들어주고
	- 개별 데이터프레임을 시트명과 함께 엑셀에 넣어주고
	- 세이브를 하면 끝납니다. 
- 해당 경로에 가 보시면, 파일이 생성되어 있고, 값도 잘 정리되어 있는 것을 알 수 있습니다. 

```python
writer = pd.ExcelWriter('test_excel.xlsx')
df1.to_excel(writer, 'sheet1')
df2.to_excel(writer, 'sheet2')
writer.save()
```

### how to write excel 

- 이제 만든 엑셀 파일을 한번 읽어봅시다. 읽는 건 훨씬 간단합니다.

```python
new_df2 = pd.read_excel('test_excel.xlsx')
print(type(new_df2))
print(new_df2.head())
```

- 그러나, 저희는 두 개의 시트를 만들었는데, 하나밖에 읽지 못합니다. 
	- pd.read_excel은 기본적으로는 첫번째 시트만 읽어들입니다 

```
<class 'pandas.core.frame.DataFrame'>
   A   B
0  0  10
1  1  11
2  2  12
3  3  13
4  4  14
```

- 따라서 여러 시트를 한번에 읽어들이도록 해보겠습니다. 
	- `arguement`의 이름이 sheetname(older version)일 수도있고, sheet_name(recent version)일 수도 있습니다. 

- 여러 시트를 동시에 읽는 경우, `OrderDict`라는 자료 구조가 리턴되는 것을 알 수 있습니다.
	- 조금 낯설지만, 해당 자료구조는 Dictionary와 똑같은데, 순서가 지켜지는 Dictionary라고 생각하시면 됩니다.
	- 아무튼 아래처럼 접근하면 됩니다. 

```python
df_dict = pd.read_excel('test_excel.xlsx', sheetname=None)
print(type(df_dict))
for k in df_dict.keys():
    print(df_dict[k].head())
    print()
```

```
<class 'collections.OrderedDict'>
   A   B
0  0  10
1  1  11
2  2  12
3  3  13
4  4  14

   C   D
0  0  10
1  1  11
2  2  12
3  3  13
4  4  14
```


## wrap-up

- 사실 pandas 말고도, win32.com을 이용하면 훨씬 다양한 짓(그래프 생성)들을 할 수 있지만, 이 부분은 추후에 다시 정리하겠습니다. 
- 엑셀 뿐만 아니라, ppt 작업을 좀 편하게 할 수 있는 방법이 없을까를 고민하고 있습니다. 
	- 예를 들어 {제목: 내용} 딕셔너리로부터 자동으로 매 슬라이드를 만들어주는 코드? 같은 걸 생각해봅니다. 
