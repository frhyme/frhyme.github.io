---
title: PyPDF2 - Merge pdf files
category: python
tags: python PyPDF2 pdf 
---

## PyPDF2 - Merge pdf files

- python을 이용해서 여러 pdf 파일을 하나로 합쳐보려고 합니다. 코딩이 아니라, 다른 방식으로 하려면 타 서비스를 사용해야 하는데, 이 서비스에서 pdf를 갈취하는 것은 아닌지 확신이 들지 않더라고요. 특히 pdf에는 민감한 자료들이 있는 경우들이 많아서, 그냥 다른 서비스에 함부로 넘기는 게 좀 그래요.
- 그래서 혹시 "python을 이용하면 할 수 있지 않을까?"싶어서 찾아보니 있어서 정리해보려고 합니다.

## PyPDF2

- [PyPDF2](https://pypi.org/project/PyPDF2/)는 대략 다음의 역할을 수행할 수 있습니다.
  - pdf에서 제목, 저자등 필요한 정보를 뽑기
  - page를 쪼개거나, page들을 합치기
  - 등등등
- 일단 `pip install PyPDF2`를 사용해서 설치부터 해보죠.

```plaintext
(base) seunghoonlee@seunghoonui-MacBookAir ~ % pip install PyPDF2
Collecting PyPDF2
  Downloading PyPDF2-1.26.0.tar.gz (77 kB)
     |████████████████████████████████| 77 kB 886 kB/s 
Building wheels for collected packages: PyPDF2
  Building wheel for PyPDF2 (setup.py) ... done
  Created wheel for PyPDF2: filename=PyPDF2-1.26.0-py3-none-any.whl size=61084 sha256=8b636aecf48a4f51261b3a87857a12994a0a1568ffddbbdd943a50809392f4bc
  Stored in directory: /Users/seunghoonlee/Library/Caches/pip/wheels/80/1a/24/648467ade3a77ed20f35cfd2badd32134e96dd25ca811e64b3
Successfully built PyPDF2
Installing collected packages: PyPDF2
Successfully installed PyPDF2-1.26.0
```

- 그리고 아래 코드를 실행해 주면 됩니다.

```python
from PyPDF2 import PdfFileMerger
import os

# current directory를 변경해주고.
folder_path = "/folder_name"
os.chdir(folder_path)

# PdfFilMerger를 생성하고
# 각 파일들을 추가해줍니다.
pdf_merger = PdfFileMerger()
for x in os.listdir():
    pdf_merger.append(x)

pdf_merger.write("result.pdf")
pdf_merger.close()
```
