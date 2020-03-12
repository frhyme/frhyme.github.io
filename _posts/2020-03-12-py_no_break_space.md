---
title: python에서 string 내 space 가 없어지지 않을때(non-breaking-space)
category: python-basic
tags: python python-basic string space
---

## 왜 `str.replace(" ", "")`했는데 공백이 남아있지? 

- 요즘 일이 있어서 간단하게 string을 처리하고 있습니다. 특히, 오늘은 pdf로부터 텍스트 데이터를 읽어서, 텍스트를 전처리해야 하는 일이 있었죠. 
- 일단 아주 간단하게, `strip()`을 사용해서 공백을 삭제했는데, 공백이 안 없어지는 겁니다. 아니, 왜 이러나 하고 한참 이유를 찾다보니, **non-breaking-space(줄바꿈방지공백)** 이라는 것이 있더군요. 

## NBSP: Non-Breaking SPace

- NBSP는 이를 포함하는 문자열이 맨 끝에 오지만, 길이가 길어서 줄 끝에 맞추기가 어려울 경우에는, 해당 문자열을 포함한 모든 단어를 그대로 다음 줄로 넘기는 것을 말합니다. 사실, 일반적인 문서 에디터를 쓰다 보면, 한 줄의 마지막에 있는 단어는 잘리지 않고 전체가 아래로 내려가는 경우가 있죠. 이런 것을 NBSP라고 합니다. 
- 그림으로 보면 이해가 더 빠를 수 있죠.

![](https://intelligentediting.com/media/60844/nonbreaking.jpg)

## remove NBSP in python

- python에서 보면 다음과 같습니다(정확히는 ISO/IEC 8859 표준에 따른 것이지만 그냥 넘어갑니다). NBSP는 `\xa0`로 표현되죠. 

```python
# 아래처럼 그냥 출력할 때는 이 아이가 space인지 non-break space인지 모릅니다. 
test_str = "aa\xa0\xa0\xa0\xa0bb"
print(test_str)
# 따라서, 그냥 space인줄 알고 변경해도 바뀌지 않죠. 
print(test_str.replace(" ", ""))
# 이런 경우는 보통 non-breaking-space가 있는 것이므로 이 아이를 삭제해주면 됩니다.
print(test_str.replace("\xa0", ""))
```

```
aa    bb
aa    bb
aabb
```

