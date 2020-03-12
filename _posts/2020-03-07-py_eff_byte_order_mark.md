---
title: python에서 `\ufeff`가 읽힐 때 해결방법. 
category: python-basic
tags: python python-basic utf-8 string file 
---

## 1-line summary 

- `open(file_name, "r", encoding='utf-8-sig')`을 쓰면 해결 됩니다.

## python에서 `\ufeff`가 읽히는 문제. 

- 보통 csv를 읽을 때, `pandas`를 쓰긴 하지만 속도 문제로 인해 `csv`라는 모듈을 사용할 때가 있습니다(사실 요즘은 웬만하면 `pandas`가 더 빠르기는 하지만요). 이 때 csv를 읽어서 dictionary로 변환하는 다음과 같은 코드를 사용할 때, 첫번째 칼럼의 key에 `\ufeff`가 붙는 경우가 있습니다. 즉, 첫번째 칼럼의 이름이 "Author"라면 "feffAuthor"라는 식으로 표시되는 것이죠. 

```python 
with open(path+file_name, "r") as f:
    # python에서 file을 읽을 때 간혹 문자에 \ufeff 가 붙는 경우가 있음. 
    for row in csv.DictReader(f):
        row_dict = {k: row[k] for k in row.keys() if k in required_column_sets}
        row_dict_lst.append(row_dict)
```

## 일단 어떻게 해결할 수 있는가? 

- 물론 사소한 문제고 그냥 `str.replace("/ufeff", "")`로 처리해줘도 되는 문제이기는 합니다. 
- 다만 아래처럼 `encoding='utf-8-sig'`의 argument를 넘겨주는 것이 좀더 똑똑한 방법으로 보입니다.

```python 
# python에서 file을 읽을 때 간혹 문자에 \ufeff 가 붙는 경우가 있음. 
# 이 때는 encoding 방식을 변경해주면 됨 
################################################################
with open(path+file_name, "r", encoding='utf-8-sig') as f:
################################################################
    for row in csv.DictReader(f):
        row_dict = {k: row[k] for k in row.keys() if k in required_column_sets}
        row_dict_lst.append(row_dict)
```

## Byte Order Mark: 왜 이런일이 발생했는가?

- `/ufeff`는 해당 file이 어떤 문자열로 코딩되었는지를 의미하는 일종의 식별자입니다. "이 문서의 인코딩 방식은 뭐에요"라는 걸 알려주는 메타 정보인 것이죠. 보통 이러한 방식은 해당 파일의 맨 앞에 집어넣곤 합니다.
- 다만, `utf-8`의 경우는 BOM이 필요없습니다. 즉 default이기 때문에, 굳이 저 정보를 집어넣을 필요가 없는데, 가끔 파일들에서 저 `utf-8`로 인코딩되었다는 사실을 알려주는 것이죠. 
- 따라서, `utf-8-signature`이라는 인코딩 방식을 넘겨주면, 앞의 정보를 무시하게 됩니다. 이는 "이 아이는 확실하게 utf-8로 인코딩된 아이야"라는 것을 정확하게 전달하는 것이죠. 


## wrap-up

- 물론 그냥 `pandas.read_csv`를 쓰면 보통 문제없이 해결해줍니다. 
- 사람의 눈으로는 모든 것이 같은 데이터일지라도 사실은 내부의 byte 레벨에서는 다를 수 있는 것이죠. 



## reference

- [유니코드 BOM](https://brownbears.tistory.com/124)
- [u-ufeff-in-python-string in stackoverflow](https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string/17912811)