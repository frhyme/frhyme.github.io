---
title: os makedirs
category: python
tags: os python
---

## os - makedirs

- python 에서 디렉토리 생성이 필요할 경우 다음 두 가지 방식을 사용해서 생성할 수 있습니다.

```python
import os

# 현재 폴더에서 1개의 폴더만 생성하는 경우
os.mkdir('./new_folder')


# 깊이가 2 이상인 폴더를 생성하는 경우에 사용합니다.
# exist_ok=True : 기존에 폴더가 있을 경우에만 생성한다
# exist_ok=False: 기존에 폴더가 있을 경우 Error 발생
# default: exist_ok=False
os.makedirs('./upper_folder/folder', exist_ok=True)
```

