---
title: python에서 json을 "한글을 읽을수 있게" 저장하는 방법
category: python-libs
tags: python python-basic json python-libs
---

## JSON: JavaScript Object Notation

- 우선 JSON은 JavaScript Object Notation의 줄임말이며, python의 dictionary와 유사하게, (key, value)의 형태로 값을 저장하는 것을 말합니다. 요즘에는 그냥 dictionary와 약간 동의어로 이해하는 경우가 많기는 하지만요. 
- 다만, JSON은 텍스트 파일이 아닙니다. 물론, 단순하게 값을 저장할 때는 이렇게 생각해도 될수 있지만, 정확하게는 바이너리 데이터로 이해하고 있는 것이 좀 더 올바르죠. 

## ensure_ascii

- 아래에서는 딕셔너리를 json string으로 변환해주는 `json.dumps`를 사용합니다. 
- 그리고 `ensure_ascii=True`인 경우와 아닌 경우를 비교하여 봅니다.

```python
import json 

# 아래와 같이 간단한 딕녀서리를 만들고 이를 저장한다고 합시다.
simple_dict = {
    'abcadf1': '이승훈asfsdbc'
}

# ensure_ascii가 True이면, ascii가 아닌, 다른 문자들은 모두 이스케이프 문자로 표현됩니다. 
# 이스케이프 문자: 이스케이프 시퀀스를 따르며, 백슬래시로부터 시작하는 문자.
print(json.dumps(simple_dict, indent=4, ensure_ascii=True))
print("==")
# 반면, ensure_ascii를 False로 하면, 아스키에 포함되지 않는 문자들도 모두 출력되죠.
print(json.dumps(simple_dict, indent=4, ensure_ascii=False))
```

- 아래에서 보시는 것처럼, `ensure_ascii=False`를 설정하면, 이스케이프 문자로 표시하는 것이 아니라, 한글의 경우에도 잘 출력해주는 것을 알 수 있습니다.

```plaintext
{
    "abcadf1": "\uc774\uc2b9\ud6c8asfsdbc"
}
==
{
    "abcadf1": "이승훈asfsdbc"
}
Leeseunghoonui-MacBoo
```

## reference

- [python에서 JSON을 사용하는 방법](https://soooprmx.com/archives/6788)