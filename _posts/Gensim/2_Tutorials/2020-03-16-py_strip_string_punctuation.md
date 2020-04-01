---
title: python - strip string better with punctuation
category: python-basic
tags: python python-basic string punctuaion 
---

## 1-line summary 

- 보통 `strip()`이라고 쓰지만, 여기에 parameter를 넘겨주면 넘어간 리스트의 모든 원소를 지워준다.

## strip better

- 사소합니다만, 보통 문자열의 양쪽 공백을 지워줄 때 다음과 같이 처리하죠. 

```python
"  frhyme...  ".strip()
```

- 이게 다 인줄 알았는데, 이걸 이렇게 쓸 수도 있더군요. 아래와 같이 넘겨주면, ".", " "을 양쪽에서 모두 지워줍니다.

```python
"  frhyme...  ".strip(" .")
```

- 더 편하게 하려면 `string` 모듈에 있는 `punctuation`를 사용해서 처리할 수도 있죠.

```python
import string 

print("--"*20)
print(f"== string.punctuation")
print(f"{string.punctuation}")
print("--"*20)
```
```
----------------------------------------
== string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
----------------------------------------
```

- 다만, `string.punctuation`에는 스페이스(' ')가 없으므로 이를 채워서 다음처럼 변환해주는 것이 가장 좋습니다. 

```python
import string 
print("  ,#$%@#^frhyme...  ".strip(string.punctuation+" "))
```

## reference

- [w3schools - string strip](https://www.w3schools.com/python/ref_string_strip.asp)