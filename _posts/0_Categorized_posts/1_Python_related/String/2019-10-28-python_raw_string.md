---
title: python의 raw string
category: python
tags: python raw-string string json
---

## Raw String은 특수 문자를 무시한다

- 종종 웹에서 데이터를 긁어와야 할 때가 있습니다. 전문적으로 할 때는 다른 기법들도 있지만, 보통 쭉 긁어서 복사하는 걸 제일 많이 하죠. 
- 그런데, 이게 긁히지 않을 때는 **페이지 소스 보기**를 눌러서, 페이지 소스에서 제가 원하는 데이터가 있는 부분을 가져옵니다. 보통 json의 형태로 되어 있는 경우가 많죠. 
- 이걸 긁어서, python의 스트링으로 넣어주고, `json` 모듈로 변형하면 될것 같은데 종종 오류가 발생합니다. 
- 이는 python의 기본 string에서는 백슬래쉬를 포함한 문자들을 변형하기 때문이죠. 가령 다음의 차이가 있습니다. 

## String 

- 아래 코드는 기본적으로 그냥 String을 정의한 것이죠.
- 다만, 여기서는 `"\n"`을 줄바꿈으로 인식하게 됩니다. `"\n"`는 대부분의 프로그래밍 언어에서 "줄바꿈"으로 인식되는 특수문자니까요.

```python 
a_str = "aaaa\naaaa"
```

```plaintext
aaa
aaa
```

## Raw String

- 다만 아래는 위와 같은 것처럼 보이지만, `"` 앞에 "r"이 붙어 있죠. 즉, 이 아이는 raw string입니다.
- 이 아이는 특수 문자를 변경하지 않고, 모든 캐릭터를 그대로 보여줍니다.

```python
b_raw_str = r"aaaa\naaaa"
```

```plaintext
aaaa\naaaa
```

- 즉, json, html과 같은 문서에서 특수문자나 태그등을 변환하지 않고 그대로 사용할 목적이라면 스트링 앞에 `r`를 붙이면 됩니다. 

## reference

- [JournalDev - Raw String](https://www.journaldev.com/23598/python-raw-string)
