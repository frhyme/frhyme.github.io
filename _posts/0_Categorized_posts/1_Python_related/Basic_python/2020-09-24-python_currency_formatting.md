---
title: python - 통화를 표현하기 위해서 3칸마다 쉼표 넣기.
category: python-basic
tags: python python-basic f-string string currency
---

## Intro - python에서 통화 형식 출력하기

- python에서 통화를 출력하는 간단한 방법을 정리합니다. 매우 쉽죠. 
- 저는 f-string을 사용해서 통화로 출력해줍니다. 다음처럼 하면 되죠.

```python
a = 123456
print(f"{a}")  # 123456
print(f"{a:,}")  # 123,456
```
