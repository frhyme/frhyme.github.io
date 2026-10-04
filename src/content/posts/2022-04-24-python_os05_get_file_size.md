---
title: "python - os - get file size"
date: 2022-04-24
category: "python"
tags: ["python", "os", "file", "python_lib"]
permalink: "/python/python_os05_get_file_size/"
---

- python에서 file size 확인하는 방법은 다음과 같습니다.

```python
import os

file_name = 'aaa.svg'

file_size = os.path.getsize(file_name)
file_size = file_size / (1024.0 * 1024.0)
print(f'file_size = {file_size:6.2f} MB')
```