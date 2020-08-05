---
title: python - E712 - Comparison to true should be 'if cond is true:' 
category: python-basic
tags: python python-basic flake8 
---

## `True` 는 `is`를 사용해서 비교할 것

- python 코드 내에서 True를 비교할 때는 다음의 코드를 써야 합니다.

```python
x = True
if x is True:
    print(x)
```

- C에서는 True, False라는 것이 정확하게 존재하지 않고, 그냥 `0`이면 False, `1`이면 True로 생각해서 처리했죠. 
- 그렇게 해도 문제는 없습니다만, 사실 개념적으로 정수와 boolean은 다르기 때문에, 다르게 접근하는 것이 맞습니다.
- 실제로 "논리값"과 "정수값"은 다르고, 다른 사람의 코드에서 이게 혼재되어 있으면 읽다가 헷갈립니다. 
- 만약, python에서 `True`는 특정 메모리에 존재하는 하나의 상수 값입니다. 따라서, 어떤 경우에도 모두 같은 메모리 주소를 가지고 있죠. 
  
```python
id(1==1) # 4547562976
id(True) # 4547562976
```

- 따라서, identity testing을 하는 `is`를 사용하는 것이 적합합니다. 
- 가령, `==`의 경우는 다음과 같은 오류가 발생할 수 있는 여지가 있죠. 

```python
True == 1 # True
```

- 따라서, 항상, 무조건 True의 경우는 다음의 두 가지 중에서 선택하여 써야만 합니다.

```python
x = True 
if x:
    print(x)
```

```python
x = True 
if x is True:
    print(x)
```

## Reference

- [flake8rules - E712](https://www.flake8rules.com/rules/E712.html)
- [Flake8 error `E712 comparison to True should be 'if cond is True:' or 'if cond:'` in django](https://stackoverflow.com/questions/50836584/flake8-error-e712-comparison-to-true-should-be-if-cond-is-true-or-if-cond)