---
title: python에서 특정 폴더 내에 가장 최근에 생성된 파일을 리턴하는 방법
category: python-basic
tags: python python-basic python-libs os 
---

## 1-line summary 

- `os.path.getctime(path)`을 사용하면 해당 파일의 생성 시간을 알 수 있음
- 이 값을 사용해서 "생성 시간" 기준으로 최대 값을 찾으면 됨.

## Get Latest file from path 

- 어떤 folder의 경로 `folder_path`가 있다고 합시다. 그리고 이 경로에는 코딩 과정에서 만들어지는 주요 산물들이 저장되죠.
- 코딩 중에 가장 최근에 업데이트된 파일을 알아서 읽고 싶을 때가 있죠. python library인 `os`에서는 이미 입력받은 경로에 대해서 "생성 시간"을 알아낼 수 있습니다. 
- 그렇다면 그냥 모든 파일들에 대해서 "생성 시간"을 읽고 정렬해주면 끝나는 문제죠. 
- 간단히 아래 코드를 사용하면 됩니다.

```python
import os  
"""
- 특정 folder 내에 있는 "가장 최근에 생성된" 파일을 리턴하는 방법 
"""
folder_path = 'social_entre_scopus_raw_data_csv/'

# each_file_path_and_gen_time: 각 file의 경로와, 생성 시간을 저장함
each_file_path_and_gen_time = []
for each_file_name in os.listdir(folder_path):
    # getctime: 입력받은 경로에 대한 생성 시간을 리턴
    each_file_path = folder_path + each_file_name
    each_file_gen_time = os.path.getctime(each_file_path)
    each_file_path_and_gen_time.append(
        (each_file_path, each_file_gen_time)
    )

# 가장 생성시각이 큰(가장 최근인) 파일을 리턴 
most_recent_file = max(each_file_path_and_gen_time, key=lambda x: x[1])[0]
```


## reference

- [stackoverflow: how-to-get-the-latest-file-in-a-folder-using-python](https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder-using-python)