---
title: SyntaxError - non-default argument follows default argument
category: python-basic
tags: python python-libs syntax error
---

## Intro: 초기값 있는 argument는 맨 뒤로!

- 아래 코드가 떴다는 이야기는, 함수의 argument의 순서로 볼 때, `a=10`처럼 초기 값을 정한 argument 앞에 `, b, ` 이렇게 온 경우를 말함.

```
SyntaxError: non-default argument follows default argument
```

- 아래를 보시면 좀 더 명확할 것 가텐요.

```python
# ERROR!!
def AAA(a=10, b):
    return 0
# RIGHT!!
def AAA(b, a=10):
    return 0
```

## Why?

- 왜 이런 에러가 발생되는걸까요? 별 차이가 없게 느껴지는데요. 사실, 이걸 이해하려면 "만약 에러가 발생하지 않는다면?"이라는 것을 가정하면 됩니다. 
- 즉, `default-argument`가 `non-default-argument`보다 앞에 와도 된다면, 아래와 같이 `AAA(3)`이 무엇을 의미하는지, 인터프리터가 혼동하게 됩니다.

```python
# IF this syntax is possible?
def AAA(a=10, b):
    return 10*a+b
# THEN
AAA(a=10, b=5) # Okay 
AAA(b=10, a=5) # Okay 
AAA(3) # Confused with AAA(a=3) and AAA(a=10, b=3)??
```

- 반대로, 현재 방식대로라면, 위에서 발생하는 해결되죠. 

```python
# CURRENTLY
def AAA(b, a=10):
    return 10*a+b
# THEN
AAA(a=10, b=5) # Okay 
AAA(b=5, a=10) # Okay 
AAA(5) # Okay b=5
```



## reference

[stackoverflow : why-cant-non-default-arguments-follow-default-arguments](https://stackoverflow.com/questions/16932825/why-cant-non-default-arguments-follow-default-arguments)