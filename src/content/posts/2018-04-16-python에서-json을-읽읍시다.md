---
title: "python-basic) python에서 json을 읽어봅시다."
date: 2018-04-16
category: "python-libs"
tags: ["python", "python-libs", "json"]
permalink: "/python-lib/python에서-json을-읽읍시다/"
---

## intro

- 간단하게 파이썬에서 json 파일을 읽는 방법을 설명합니당
- json 파일은 파이썬에서 딕셔너리처럼 key-value pair로 구성되어 있어서, 간단하게 변환할 수 있을 것 같은데, 간단하게 변환해주지는 않습니당. 

## solution 

- 아래처럼 하시면, 됩니다. 

```python
import json
f = open("/test-9.json", "r").read()
d = json.loads(f)
```

- 만약 안되시면, 다음처럼 하시면 됩니다. 
  - 파일 초반에 특정 캐릭터가 문제가 되는데, 저는 그냥 무시했습니 하핫.

```python
import json
f = open("/test-9.json", "r").read()[1:]
d = json.loads(f)
```