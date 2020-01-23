---
title: python의 raw string
category: python
tags: python raw-string string json
---

## 배경

- 종종 웹에서 데이터를 긁어와야 할 때가 있습니다. 전문적으로 할 때는 다른 기법들도 있지만, 보통 쭉 긁어서 복사하는 걸 제일 많이 하죠. 
- 그런데, 이게 긁히지 않을 때는 **페이지 소스 보기**를 눌러서, 페이지 소스에서 제가 원하는 데이터가 있는 부분을 가져옵니다. 보통 json의 형태로 되어 있는 경우가 많죠. 
- 이걸 긁어서, python의 스트링으로 넣어주고, `json` 모듈로 변형하면 될것 같은데 종종 오류가 발생합니다. 
- 이는 python의 기본 string에서는 백슬래쉬를 포함한 문자들을 변형하기 때문이죠. 가령 다음의 차이가 있습니다. 

```python
In [1]: a_str = "aaaa\naaaa"

In [2]: b_raw_str = r"aaaa\naaaa"

In [3]: print(a_str)
aaaa
aaaa

In [4]: print(b_raw_str)
aaaa\naaaa

In [5]:
```

- raw_string에서는 백슬래시가 있는 부분을 줄바꿈, 탭 등으로 변환하지 않고, 그대로 넣어줍니다. 즉 훨신 편하게 처리됩니다.
- 그러니까, 아주 간단하게는 파이썬에서 json으로 변환이 잘 안되는 것 같으면, 그냥 스트링 앞에 `r`를 붙이면 됩니다. 

## reference

- <https://www.journaldev.com/23598/python-raw-string>