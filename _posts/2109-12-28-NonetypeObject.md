---
title: AttributeError - 'NoneType' object has no attribute
category: python-basic
tags: python-basic python 
---

## Nonetype은 그게 없어. 

- 이건 아주 기본적인 에러이기는 한데, 은근히 자주 발생합니다. 보통은 정규표현식을 사용할 때 많이 발생하기는 하죠. 
- 그래서 마치 이게 정규표현식에 관계된 에러라고 생각하기 쉬운데, 이건 그냥 ***'반환된 값이 없는데 당신이 그 객체로부터 어떤 메소드를 찾고 있어'***를 표현하는 겁니다.
- 매우 기본적인 파이썬 코드를 다음과 같이 작성했습니다.

```python
def test_func():
    print("This function does not return any")
None_var = test_func()
# type을 출력하는 것은 잘됨.
print(f"type(None_var) ==> {type(None_var)}")
# 이 값을 출력하는 것도 그냥 None을 출력하면 되니까, 잘됨.
print(f"None_var ==> {None_var}")
# 하지만, 반환되는 값이 없는데, 어떤 method를 리턴하려고 하면 안됨.
print(None_var.aa)
```

- 결과는 다음과 같이, 세번째 구문인 `print(None_var.aa)`을 실행할 때 문제가 발생하죠.
- 즉, 없는 값을 리턴하려고 할때, 발생하는 코드입니다.

```
This function does not return any
type(None_var) ==> <class 'NoneType'>
None_var ==> None
Traceback (most recent call last):
  File "test1.py", line 9, in <module>
    print(None_var.aa)
AttributeError: 'NoneType' object has no attribute 'aa'
```

## wrap-up

- 이 오류가 유독 정규표현식을 사용해서 처리할 때 많이 발생하는 이유는, 텍스트에서 필요한 값을 가져올 때, 아무 값도 거기에 없기 때문이죠. 즉, 원하는 형태의 표현의 텍스트가 없으면, 아무 값도 반환하지 못하는 것이 되고 이렇게 될 경우 지금 아무 값도 없는데, 거기서 메소드를 가져오려고 하면 에러가 납니다. 
- 아무튼, 이건 정규표현식 때문에 발생하는 에러가 아니에요. 그냥 코드를 잘못 처리했거나, 예외처리를 제대로 하지 않은 것이죠.