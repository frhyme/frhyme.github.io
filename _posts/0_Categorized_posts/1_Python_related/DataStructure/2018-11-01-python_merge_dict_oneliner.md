---
title: dictionary 한줄로 합치기. 
category: python-basic
tags: python python-basic python-libs dictionary
---

## dictionary 합치기

- 사실 언뜻 보면 별거 아닌데? 뭐 이런걸 포스트로 쓰나 라고 생각하실지 모릅니다. 네, 저도 처음에는 그렇다고 생각했어요. 
- 보통 파이썬에서 리스트를 사용할 때, 두 리스트를 합치고 싶을 때가 있습니다. 원래 리스트는 건드리지 않고요. 예를 들면 아래처럼 되죠. 

```python
a = [1,2,3]
b = [4,5,6]
c = a+b
```

- 그렇다면, 딕셔너리는 더하면 어떻게 될까요? 파이썬은 똑똑하니까, a와 b를 더해서 새로운 딕셔너리를 만들어줄까요? 

```python
a = {'a':1, 'b':2}
b = {'c':3}
a+b
```

- 에러가 뜹니다. 우리는 직관적으로 더해서 새로운 딕셔너리를 만들어줄 수 있다고 생각하지만, 컴퓨터는 다르게 생각하는것 같네요. 

```plaintext
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-7872ed753be7> in <module>()
      1 a = {'a':1, 'b':2}
      2 b = {'c':3}
----> 3 a+b

TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
```

- 아무튼 그렇다면 어떻게 딕셔너리를 합쳐줄 수 있을까요? 
- 아래처럼 해도 되는데 매우 더럽습니다. 

```python
a = {'a':1, 'b':2}
b = {'c':3}

c = {}
for k, v in a.items():
    c[k]=v
for k, v in b.items():
    c[k]=v
```

- 아래처럼 해도 되구요. 하지만, 미묘하게 조금 아쉽습니다. 저는 합쳐서 바로 리턴해주는 놈을 찾고 있거든요. 

```python
a = {'a':1, 'b':2}
b = {'c':3}

c = a.copy()
c.update(b) ## 이 라인의 실행결과는 None입니다. 
```

- 아래가 제일 좋은 방법입니다. 

```python
a = {'a':1, 'b':2}
b = {'c':3}
 
print({**a, **b})
```

```plaintext
{'a': 1, 'b': 2, 'c': 3}
```

## why 

- 별이 붙는것이 도대체 뭔가? 싶으신 분은 [제가 예전에 써둔 포스트](https://frhyme.github.io/python-basic/args_kwargs_python/)를 보시면 도움이 될것 같아용 홍홍

## wrap-up

- starred expression은 이전에도 썼지만, 이런 변종이 가능할지는 몰랐어요 헤헤헷

## reference 

- [stackoverflow - how to merge two dictionaries in a single expression](https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression)