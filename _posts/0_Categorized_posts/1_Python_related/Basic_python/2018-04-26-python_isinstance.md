---
title: python에서 객체 isinstance 체크하기 
category: python-basic
tags: python python-basic object-oriented-programming type-checking

---

## Intro 

- 파이썬을 활용하다보면 객체의 타입을 활용해서 조건을 걸어주는 일들이 생긴다. 객체의 타입에 따라서 제어해주고 싶을 때 다음 코드를 쓰면 유용할 수 있다. 

## Code

```python
class aa(object):
    aa=5
class bb(aa):
    bb=6
A = aa()
B = bb()

print("Is A instance of aa?: {}".format(isinstance(A, aa)))
print("Is B instance of aa?: {}".format(isinstance(B, aa)))
print("Is A instance of bb?: {}".format(isinstance(A, bb)))
print("Is aa is subclass of bb?: {}".format(issubclass(aa, bb)))
print("Is bb is subclass of aa?: {}".format(issubclass(bb, aa)))
```

- 코드의 실행 결과는 다음과 같다. 해당 instance가 해당 class의 instance일 경우 True, 아닐 경우 False를 리턴한다.

```plaintext
    Is A instance of aa?: True
    Is B instance of aa?: True
    Is A instance of bb?: False
    Is aa is subclass of bb?: False
    Is bb is subclass of aa?: True
```
