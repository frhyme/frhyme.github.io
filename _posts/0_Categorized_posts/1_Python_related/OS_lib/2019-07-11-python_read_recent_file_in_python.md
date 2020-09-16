---
title: python에서 가장 최근 파일 읽어오기. 
category: python-libs
tags: python python-libs python-basic
---

## python에서 가장 최근 파일을 불러옵시다

- 매우 간단하기 때문에, 그냥 바로 코드부터 작성하겠습니다. 
- 특정 폴더에 있는 파일들중에서 가장 최근에 만들어진 파일만 가져오도록 합니다. 

```python
import os

files_Path = "Output/" # 파일들이 들어있는 폴더
file_name_and_time_lst = []
# 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌. 
for f_name in os.listdir(f"{files_Path}"):
    written_time = os.path.getctime(f"{files_Path}{f_name}")
    file_name_and_time_lst.append((f_name, written_time))
# 생성시간 역순으로 정렬하고, 
sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
# 가장 앞에 이는 놈을 넣어준다.
recent_file = sorted_file_lst[0]
recent_file_name = recent_file[0]
```

## wrap-up

- 매우 간단합니다 하하하.
