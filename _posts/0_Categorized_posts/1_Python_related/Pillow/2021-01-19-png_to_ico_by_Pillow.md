---
title: Pillow - png를 ico로 변환
category: python-lib
tags: python pillow png ico image
---

## Pillow - png를 ico로 변환

- 일단 [Pillow](https://pillow.readthedocs.io/en/stable/)를 설치합니다.

```plaintext
(pythonProject) seunghoonlee@seunghoonui-MacBookAir pythonProject % pip install Pillow
Collecting Pillow
  Downloading Pillow-8.1.0-cp38-cp38-macosx_10_10_x86_64.whl (2.2 MB)
     |████████████████████████████████| 2.2 MB 1.6 MB/s 
Installing collected packages: Pillow
Successfully installed Pillow-8.1.0
```

- 그리고 다음 코드를 실행하면, 변환해줍니다. 
- pip를 통해 설치한 건 `Pillow`이지만, import할때는 `PIL`을 사용합니다.

```python
from PIL import Image

filename = "favicon.png"
img = Image.open(filename)
img.save("logo.ico")
```
