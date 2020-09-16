---
title: got multiple values for argument 
category: python-basic
tags: python python-libs 
---

## got multiple values for argument 

- 사소한 오류이기는 한데, 정리합니다. 
- 아래 코드에서 보는 것과 같이, func에 변수를 함께 넘길 경우에는 
  - 해당 함수가 선언되었을 때의 변수 순서에 맞춰서 넘기거나 
  - 아니면 위치와 상관없이, 변수 명을 분명하게 작성해서 넘겨야 합니다. 

```python
def temp_func(a=1, b=3):
    print(a, b)
temp_func(1, 3) #OK 
temp_func(b=5, a=3)#OK 
temp_func(1, a=3) #NOT OK
```

- 세번째처럼 그 순서를 마음대로 할 경우에는 아래와 같은 오류가 뜹니다.

```plaintext
TypeError: temp_func() got multiple values for argument 'a'
```

## reference

- [Stackoverflow - typeerror got multiple values for argument](https://stackoverflow.com/questions/21764770/typeerror-got-multiple-values-for-argument)
